"""
Local scan without Lambda/SQS.
Reads domains_to_scan.jsonl, writes results_local/*.jsonl
Resume: skips domains already present in output files.

Usage: python local_scan.py
       python local_scan.py --concurrency 300  # if connections drop
"""
import asyncio
import json
import os
import sys
import time
import argparse
from datetime import datetime
from pathlib import Path

# Import scan logic from lambda/
sys.path.insert(0, str(Path(__file__).parent / "lambda"))
import handler as lh
import fingerprint as fp

from config import DOMAINS_FILE

OUTPUT_DIR = Path("E:/namesilo-scanner/results_local")
OUTPUT_DIR.mkdir(exist_ok=True)

CHUNK_SIZE  = 5_000    # domains per output file
REPORT_EVERY = 10_000  # progress report every N domains


def load_done() -> set:
    done = set()
    for f in OUTPUT_DIR.glob("*.jsonl"):
        with open(f, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                try:
                    d = json.loads(line).get("domain")
                    if d:
                        done.add(d)
                except Exception:
                    pass
    return done


async def scan_chunk(items: list, concurrency: int) -> list:
    lh.CONCUR_PER_INV = concurrency
    connector = __import__("aiohttp").TCPConnector(
        limit=concurrency, ssl=False, enable_cleanup_closed=True
    )
    import aiohttp
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 Chrome/124.0 Safari/537.36"),
        "Accept": "text/html,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        tasks = [lh._scan_item(session, item) for item in items]
        return await asyncio.gather(*tasks, return_exceptions=False)


def write_chunk(records: list, chunk_idx: int):
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out = OUTPUT_DIR / f"scan_{ts}_{chunk_idx:05d}.jsonl"
    with open(out, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def run(concurrency: int = 500):
    print(f"Loading done domains...")
    done = load_done()
    print(f"  Already scanned: {len(done):,}")

    total = written = skipped = errors = 0
    chunk_buf = []
    chunk_idx = 0
    t0 = time.time()
    t_chunk = t0

    with open(DOMAINS_FILE, encoding="utf-8") as f:
        lines = f.readlines()

    items_all = []
    for line in lines:
        try:
            item = json.loads(line)
        except Exception:
            continue
        if item["domain"] in done:
            skipped += 1
            continue
        items_all.append(item)

    total_todo = len(items_all)
    print(f"  To scan: {total_todo:,}  (skipped already done: {skipped:,})\n")

    # Process in batches of CHUNK_SIZE
    for i in range(0, total_todo, CHUNK_SIZE):
        batch = items_all[i : i + CHUNK_SIZE]
        results = asyncio.run(scan_chunk(batch, concurrency))

        chunk_buf.extend(results)
        written += len(results)
        errs = sum(1 for r in results if r.get("error"))
        errors += errs

        write_chunk(results, chunk_idx)
        chunk_idx += 1

        elapsed = time.time() - t0
        rate = written / elapsed if elapsed > 0 else 0
        eta_s = (total_todo - written) / rate if rate > 0 else 0
        eta_m = eta_s / 60

        print(
            f"  {written:>8,}/{total_todo:,}  "
            f"err={errs}  "
            f"{rate:.0f} dom/s  "
            f"ETA {eta_m:.0f} min",
            flush=True
        )

    elapsed = time.time() - t0
    print(f"\n✓ Done: {written:,} scanned, {errors:,} errors, {elapsed/60:.1f} min")
    print(f"  Results: {OUTPUT_DIR}")
    print(f"\n  Next step: python analyze.py {OUTPUT_DIR}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--concurrency", type=int, default=500,
                   help="Concurrent HTTP connections (default: 500)")
    args = p.parse_args()
    run(args.concurrency)
