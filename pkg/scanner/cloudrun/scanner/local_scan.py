"""
Cloud Run Job scanner.
Reads a domains chunk from GCS (CHUNK_URL) or a local file,
scans them concurrently, writes results back to GCS (OUTPUT_BUCKET).

Env vars:
  CHUNK_URL      - gs://bucket/path/to/chunk.jsonl  (required)
  OUTPUT_BUCKET  - gs://bucket or bucket name       (required)
  TASK_INDEX     - Cloud Run task index (0-based)   (default: 0)
  CONCURRENCY    - parallel HTTP connections        (default: 400)
  HTTP_TIMEOUT   - seconds per request              (default: 5)
  CHUNK_SIZE     - domains per output file          (default: 2000)
"""
import asyncio
import json
import os
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

# ── GCS helpers ────────────────────────────────────────────────────────────

def _parse_gs(url: str):
    """Return (bucket, blob_name) from gs://bucket/path or bucket/path."""
    url = url.strip()
    if url.startswith("gs://"):
        url = url[5:]
    parts = url.split("/", 1)
    bucket = parts[0]
    blob = parts[1] if len(parts) > 1 else ""
    return bucket, blob


def gcs_download_bytes(gs_url: str) -> bytes:
    from google.cloud import storage
    bucket_name, blob_name = _parse_gs(gs_url)
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    return blob.download_as_bytes()


def gcs_upload_bytes(data: bytes, gs_bucket: str, blob_name: str) -> str:
    from google.cloud import storage
    bucket_name, _ = _parse_gs(gs_bucket)
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(data, content_type="application/x-ndjson")
    return f"gs://{bucket_name}/{blob_name}"


# ── Scanner ────────────────────────────────────────────────────────────────

# Patch env before importing handler
os.environ.setdefault("HTTP_TIMEOUT", "5")
os.environ.setdefault("MAX_REDIRECTS", "3")
os.environ.setdefault("CONCUR_PER_INV", "400")

sys.path.insert(0, str(Path(__file__).parent))
import handler as lh


async def scan_chunk(items: list, concurrency: int) -> list:
    import aiohttp
    lh.CONCUR_PER_INV = concurrency
    connector = aiohttp.TCPConnector(
        limit=concurrency,
        ssl=False,
        enable_cleanup_closed=True,
    )
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
        ),
        "Accept": "text/html,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        tasks = [lh._scan_item(session, item) for item in items]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    # Normalise exceptions
    out = []
    for i, r in enumerate(results):
        if isinstance(r, Exception):
            domain = items[i].get("domain", "?") if i < len(items) else "?"
            out.append({"domain": domain, "error": str(r)[:120], "page_type": "dead"})
        else:
            out.append(r)
    return out


def run():
    chunk_url    = os.environ.get("CHUNK_URL", "").strip()
    output_bucket = os.environ.get("OUTPUT_BUCKET", "").strip()
    # CLOUD_RUN_TASK_INDEX is auto-injected by Cloud Run Jobs; TASK_INDEX is the fallback
    task_index   = int(os.environ.get("CLOUD_RUN_TASK_INDEX",
                       os.environ.get("TASK_INDEX", "0")))
    concurrency  = int(os.environ.get("CONCURRENCY", "400"))
    chunk_size   = int(os.environ.get("CHUNK_SIZE", "2000"))
    http_timeout = int(os.environ.get("HTTP_TIMEOUT", "5"))

    # Apply HTTP_TIMEOUT to handler
    lh.HTTP_TIMEOUT = http_timeout

    print(f"[task={task_index}] CHUNK_URL={chunk_url}", flush=True)
    print(f"[task={task_index}] OUTPUT_BUCKET={output_bucket}", flush=True)
    print(f"[task={task_index}] concurrency={concurrency} http_timeout={http_timeout}", flush=True)

    if not chunk_url:
        print("ERROR: CHUNK_URL not set", flush=True)
        sys.exit(1)
    if not output_bucket:
        print("ERROR: OUTPUT_BUCKET not set", flush=True)
        sys.exit(1)

    # Download chunk
    print(f"[task={task_index}] Downloading chunk from {chunk_url}...", flush=True)
    raw = gcs_download_bytes(chunk_url)
    lines = raw.decode("utf-8", errors="replace").splitlines()

    items = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            item = json.loads(line)
            items.append(item)
        except Exception:
            pass

    total = len(items)
    print(f"[task={task_index}] Loaded {total:,} domains", flush=True)

    if total == 0:
        print(f"[task={task_index}] No domains to scan — exiting.", flush=True)
        return

    written = errors = 0
    t0 = time.time()
    file_idx = 0

    for i in range(0, total, chunk_size):
        batch = items[i : i + chunk_size]
        try:
            results = asyncio.run(scan_chunk(batch, concurrency))
        except Exception as e:
            print(f"[task={task_index}] CHUNK ERROR at offset {i}: {e}", flush=True)
            traceback.print_exc()
            continue

        # Serialize
        jsonl_bytes = "\n".join(
            json.dumps(r, ensure_ascii=False) for r in results
        ).encode("utf-8")

        # Upload to GCS
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        blob_name = f"results/task_{task_index:04d}/scan_{ts}_{file_idx:04d}.jsonl"
        dest = gcs_upload_bytes(jsonl_bytes, output_bucket, blob_name)

        written += len(results)
        errs = sum(1 for r in results if r.get("error"))
        errors += errs
        file_idx += 1

        elapsed = time.time() - t0
        rate = written / elapsed if elapsed > 0 else 0
        eta_s = (total - written) / rate if rate > 0 else 0
        print(
            f"[task={task_index}] {written:>7,}/{total:,}  "
            f"err={errs}  {rate:.0f}/s  ETA {eta_s/60:.0f}min  -> {dest}",
            flush=True,
        )

    elapsed = time.time() - t0
    print(
        f"[task={task_index}] DONE: {written:,} scanned, {errors:,} errors, "
        f"{elapsed/60:.1f} min",
        flush=True,
    )


if __name__ == "__main__":
    run()
