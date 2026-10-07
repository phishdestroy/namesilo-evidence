"""
scan_missing.py — finds missing domains and launches scans on srv-1 and srv-2.

Steps:
1. SSH to dump-srv, count all scanned domains across lambda/, gcs/, rescan_srv1/, rescan_srv2/
2. Find original domain list (local or on dump-srv)
3. Compute missing = original - scanned
4. Write missing_domains.jsonl to dump-srv:/root/missing_domains.jsonl
5. Split 50/50 → upload chunk_missing_srv1.jsonl to srv-1, chunk_missing_srv2.jsonl to srv-2
6. Upload scanner files (handler.py, fingerprint.py, local_scan.py) to both servers
7. Launch scan in tmux session "rescan" on each server
8. Report summary
"""

import paramiko
import io
import json
import os
import sys
import time
import tempfile
import threading
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────

LOCAL_DOMAINS_FILE = "E:/namesilo-scanner/domains_to_scan.jsonl"
LAMBDA_HANDLER     = "E:/namesilo-scanner/lambda/handler.py"
LAMBDA_FINGERPRINT = "E:/namesilo-scanner/lambda/fingerprint.py"

DUMP_SRV = {
    "name": "dump-srv",
    "ip": "[redacted]",
    "password": "[redacted]",
    "port": 22,
}

SCAN_SERVERS = [
    {
        "name": "srv-1",
        "ip": "[redacted]",
        "password": "[redacted]",
        "port": 22,
        "concurrency": 400,
    },
    {
        "name": "srv-2",
        "ip": "[redacted]",
        "password": "[redacted]",
        "port": 22,
        "concurrency": 500,
    },
]

SCAN_BASE_DIR = "/mnt/HC_Volume_105301587/namesilo_scan"

# ── Scanner script to deploy on remote servers ────────────────────────────────

REMOTE_SCAN_PY = r'''
import asyncio, json, os, sys, time, argparse
from pathlib import Path
from datetime import datetime

# Stub env vars needed by handler.py before import
os.environ.setdefault("S3_BUCKET", "local")
os.environ.setdefault("HTTP_TIMEOUT", "5")
os.environ.setdefault("MAX_REDIRECTS", "3")

# Stub boto3 so handler.py imports cleanly without AWS
import types
boto3_stub = types.ModuleType("boto3")
boto3_stub.client = lambda *a, **kw: None
sys.modules.setdefault("boto3", boto3_stub)

sys.path.insert(0, str(Path.home() / "scanner"))
import handler as lh

OUTPUT_DIR = Path.home() / "results_missing"
OUTPUT_DIR.mkdir(exist_ok=True)
CHUNK_SIZE   = 5000
REPORT_EVERY = 10000


def load_done():
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


async def scan_chunk(items, concurrency):
    lh.CONCUR_PER_INV = concurrency
    import aiohttp
    connector = aiohttp.TCPConnector(limit=concurrency, ssl=False, enable_cleanup_closed=True)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36",
        "Accept": "text/html,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        tasks = [lh._scan_item(session, item) for item in items]
        return await asyncio.gather(*tasks, return_exceptions=False)


def run(concurrency=400):
    done = load_done()
    print(f"Already done: {len(done):,}", flush=True)

    chunk_file = Path.home() / "chunk_missing.jsonl"
    if not chunk_file.exists():
        print(f"ERROR: {chunk_file} not found!", flush=True)
        sys.exit(1)

    with open(chunk_file, encoding="utf-8") as f:
        lines = f.readlines()

    items = []
    for line in lines:
        try:
            item = json.loads(line)
            if item["domain"] not in done:
                items.append(item)
        except Exception:
            pass

    total = len(items)
    print(f"To scan: {total:,}", flush=True)

    written = errors = 0
    t0 = time.time()
    chunk_idx = 0

    for i in range(0, total, CHUNK_SIZE):
        batch = items[i : i + CHUNK_SIZE]
        results = asyncio.run(scan_chunk(batch, concurrency))

        ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        out = OUTPUT_DIR / f"scan_{ts}_{chunk_idx:05d}.jsonl"
        with open(out, "w", encoding="utf-8") as f:
            for r in results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        chunk_idx += 1
        written += len(results)
        errors += sum(1 for r in results if r.get("error"))

        if written % REPORT_EVERY < CHUNK_SIZE or i + CHUNK_SIZE >= total:
            elapsed = time.time() - t0
            rate = written / elapsed if elapsed > 0 else 0
            eta = (total - written) / rate / 60 if rate > 0 else 0
            print(
                f"{written:>8,}/{total:,}  err={errors}  "
                f"{rate:.0f}/s  ETA {eta:.0f}min",
                flush=True,
            )

    elapsed = time.time() - t0
    print(
        f"DONE: {written:,} scanned, {errors:,} errors, {elapsed/60:.1f}min",
        flush=True,
    )


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--concurrency", type=int, default=400)
    args = p.parse_args()
    run(args.concurrency)
'''


# ── SSH helpers ───────────────────────────────────────────────────────────────

def ssh_connect(srv: dict) -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        srv["ip"],
        port=srv["port"],
        username="root",
        password=srv["password"],
        timeout=20,
        allow_agent=False,
        look_for_keys=False,
    )
    return c


def run_cmd(c: paramiko.SSHClient, cmd: str, timeout: int = 120) -> tuple[str, str]:
    _, o, e = c.exec_command(cmd, timeout=timeout)
    out = o.read().decode(errors="replace").strip()
    err = e.read().decode(errors="replace").strip()
    return out, err


# ── Step 1: Count scanned domains on dump-srv ─────────────────────────────────

def count_scanned_on_dump() -> int:
    """SSH to dump-srv and count unique domains across all result folders."""
    print("\n[dump-srv] Counting scanned domains...", flush=True)
    c = ssh_connect(DUMP_SRV)

    # List folders
    out, _ = run_cmd(c, f"ls {SCAN_BASE_DIR}/")
    print(f"  Folders: {out}", flush=True)

    # Count with Python on remote — faster than shell loops
    count_script = f"""
import json, os, glob
base = "{SCAN_BASE_DIR}"
folders = ["lambda", "gcs", "rescan_srv1", "rescan_srv2"]
seen = set()
for folder in folders:
    pattern = os.path.join(base, folder, "*.json*")
    files = glob.glob(pattern)
    for fpath in files:
        try:
            with open(fpath, encoding="utf-8", errors="replace") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        d = json.loads(line).get("domain")
                        if d:
                            seen.add(d)
                    except Exception:
                        pass
        except Exception as ex:
            pass
print(len(seen))
"""
    # Write script to remote
    sftp = c.open_sftp()
    with sftp.open("/root/_count_scanned.py", "w") as rf:
        rf.write(count_script)
    sftp.close()

    print("  Running count script on dump-srv (may take a few minutes)...", flush=True)
    out, err = run_cmd(c, "python3 /root/_count_scanned.py", timeout=600)
    if err:
        print(f"  stderr: {err[:300]}", flush=True)

    c.close()
    try:
        count = int(out.strip())
        print(f"  Scanned domains: {count:,}", flush=True)
        return count
    except ValueError:
        print(f"  Could not parse count: '{out}'", flush=True)
        return 0


# ── Step 2: Find original domain list ────────────────────────────────────────

def check_original_list() -> int:
    """Check that local domains_to_scan.jsonl exists and count lines."""
    p = Path(LOCAL_DOMAINS_FILE)
    if not p.exists():
        print(f"ERROR: {LOCAL_DOMAINS_FILE} not found locally!", flush=True)
        sys.exit(1)
    with open(p, encoding="utf-8") as f:
        count = sum(1 for _ in f)
    print(f"[local] Original domain list: {count:,} lines", flush=True)
    return count


# ── Step 3: Build missing_domains.jsonl on dump-srv ──────────────────────────

def build_missing_on_dump(local_domains_file: str) -> int:
    """
    Upload the original domain list to dump-srv if needed, then compute
    missing domains and write /root/missing_domains.jsonl.
    Returns number of missing domains.
    """
    print("\n[dump-srv] Building missing_domains.jsonl...", flush=True)
    c = ssh_connect(DUMP_SRV)
    sftp = c.open_sftp()

    # Check if domains list already on dump-srv
    out, _ = run_cmd(c, "wc -l /root/domains_to_scan.jsonl 2>/dev/null || echo 0")
    remote_count = 0
    try:
        remote_count = int(out.split()[0])
    except Exception:
        pass

    if remote_count < 3_000_000:
        print(f"  Uploading domains_to_scan.jsonl to dump-srv ({Path(local_domains_file).stat().st_size / 1e6:.0f} MB)...", flush=True)
        sftp.put(local_domains_file, "/root/domains_to_scan.jsonl")
        print("  Upload complete.", flush=True)
    else:
        print(f"  domains_to_scan.jsonl already on dump-srv ({remote_count:,} lines)", flush=True)

    # Build missing script
    missing_script = f"""
import json, os, glob
base = "{SCAN_BASE_DIR}"
folders = ["lambda", "gcs", "rescan_srv1", "rescan_srv2"]
print("Reading scanned domains...", flush=True)
seen = set()
for folder in folders:
    pattern = os.path.join(base, folder, "*.json*")
    files = glob.glob(pattern)
    for fpath in files:
        try:
            with open(fpath, encoding="utf-8", errors="replace") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        d = json.loads(line).get("domain")
                        if d:
                            seen.add(d)
                    except Exception:
                        pass
        except Exception:
            pass
print(f"Scanned: {{len(seen):,}}", flush=True)

print("Reading original list...", flush=True)
missing = []
with open("/root/domains_to_scan.jsonl", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            d = obj.get("domain")
            if d and d not in seen:
                missing.append(obj)
        except Exception:
            pass

print(f"Missing: {{len(missing):,}}", flush=True)
with open("/root/missing_domains.jsonl", "w", encoding="utf-8") as f:
    for obj in missing:
        f.write(json.dumps({{"domain": obj["domain"]}}) + "\\n")
print(f"Written: /root/missing_domains.jsonl", flush=True)
"""

    with sftp.open("/root/_build_missing.py", "w") as rf:
        rf.write(missing_script)

    print("  Running missing-domains script (may take several minutes)...", flush=True)
    out, err = run_cmd(c, "python3 /root/_build_missing.py", timeout=900)
    print(f"  Output:\n{out}", flush=True)
    if err:
        print(f"  stderr: {err[:500]}", flush=True)

    # Get count
    out2, _ = run_cmd(c, "wc -l /root/missing_domains.jsonl")
    sftp.close()
    c.close()

    try:
        missing_count = int(out2.split()[0])
        print(f"\n  Missing domains: {missing_count:,}", flush=True)
        return missing_count
    except Exception:
        print(f"  wc output: '{out2}'", flush=True)
        return 0


# ── Step 4: Split and deploy to scan servers ──────────────────────────────────

def download_missing_from_dump() -> list[str]:
    """Download /root/missing_domains.jsonl from dump-srv into memory."""
    print("\n[dump-srv] Downloading missing_domains.jsonl...", flush=True)
    c = ssh_connect(DUMP_SRV)
    sftp = c.open_sftp()
    buf = io.BytesIO()
    sftp.getfo("/root/missing_domains.jsonl", buf)
    sftp.close()
    c.close()
    lines = buf.getvalue().decode("utf-8", errors="replace").splitlines(keepends=True)
    print(f"  Downloaded {len(lines):,} lines", flush=True)
    return lines


def install_deps_and_deploy(srv: dict, chunk_lines: list[str]):
    """Deploy scanner to a single server and launch in tmux."""
    name = srv["name"]
    conc = srv["concurrency"]
    print(f"\n[{name}] Connecting...", flush=True)

    try:
        c = ssh_connect(srv)
        sftp = c.open_sftp()

        # Install dependencies
        print(f"[{name}] Installing Python deps...", flush=True)
        install_cmd = (
            "export DEBIAN_FRONTEND=noninteractive && "
            "apt-get install -y -qq python3-pip python3-dev 2>/dev/null; "
            "pip3 install --quiet aiohttp 2>&1 | tail -2"
        )
        out, _ = run_cmd(c, install_cmd, timeout=180)
        print(f"[{name}] Deps: {out[-100:]}", flush=True)

        # Create dirs
        run_cmd(c, "mkdir -p ~/scanner ~/results_missing")

        # Upload handler.py and fingerprint.py
        sftp.put(LAMBDA_HANDLER, "/root/scanner/handler.py")
        sftp.put(LAMBDA_FINGERPRINT, "/root/scanner/fingerprint.py")
        print(f"[{name}] Scanner files uploaded", flush=True)

        # Upload remote local_scan.py
        with sftp.open("/root/scanner/local_scan.py", "w") as rf:
            rf.write(REMOTE_SCAN_PY)
        print(f"[{name}] local_scan.py uploaded", flush=True)

        # Upload chunk
        chunk_data = "".join(chunk_lines).encode("utf-8")
        print(f"[{name}] Uploading chunk ({len(chunk_lines):,} domains, {len(chunk_data)/1e6:.1f} MB)...", flush=True)
        with sftp.open("/root/chunk_missing.jsonl", "wb") as rf:
            rf.write(chunk_data)
        print(f"[{name}] Chunk uploaded", flush=True)

        sftp.close()

        # Kill any existing rescan session and start fresh
        run_cmd(c, "tmux kill-session -t rescan 2>/dev/null; sleep 0.5")
        start_cmd = (
            f"tmux new-session -d -s rescan "
            f"'python3 /root/scanner/local_scan.py --concurrency {conc} "
            f"2>&1 | tee /root/scan_missing.log'"
        )
        out, err = run_cmd(c, start_cmd)
        time.sleep(2)

        # Verify it started
        out2, _ = run_cmd(c, "tmux list-sessions 2>/dev/null")
        ps_out, _ = run_cmd(c, "ps aux | grep local_scan | grep -v grep | head -2")
        print(f"[{name}] tmux sessions: {out2}", flush=True)
        print(f"[{name}] process: {ps_out or '(not yet visible)'}", flush=True)

        c.close()
        print(f"[{name}] LAUNCHED (concurrency={conc}) ✓", flush=True)

    except Exception as ex:
        print(f"[{name}] ERROR: {ex}", flush=True)
        import traceback
        traceback.print_exc()


# ── Step 5: Check tmux status ─────────────────────────────────────────────────

def check_srv_status(srv: dict):
    name = srv["name"]
    try:
        c = ssh_connect(srv)
        out, _ = run_cmd(c, "tail -5 /root/scan_missing.log 2>/dev/null")
        sessions, _ = run_cmd(c, "tmux list-sessions 2>/dev/null")
        files, _ = run_cmd(c, "ls ~/results_missing/*.jsonl 2>/dev/null | wc -l")
        c.close()
        print(f"\n[{name}] tmux: {sessions}")
        print(f"[{name}] output files: {files}")
        print(f"[{name}] last log lines:\n{out}")
    except Exception as ex:
        print(f"[{name}] status check error: {ex}", flush=True)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Namesilo Missing Domains Scanner")
    print("=" * 60)

    # Step 1: Count scanned
    scanned_count = count_scanned_on_dump()

    # Step 2: Check original list locally
    original_count = check_original_list()

    # Step 3: Build missing list on dump-srv
    missing_count = build_missing_on_dump(LOCAL_DOMAINS_FILE)

    if missing_count == 0:
        print("\nNo missing domains found. Exiting.")
        return

    # Step 4: Download missing list and split
    print(f"\nSplitting {missing_count:,} missing domains 50/50...")
    all_lines = download_missing_from_dump()
    mid = len(all_lines) // 2
    chunks = {
        "srv-1": all_lines[:mid],
        "srv-2": all_lines[mid:],
    }
    for name, chunk in chunks.items():
        print(f"  {name}: {len(chunk):,} domains")

    # Step 5: Deploy and launch in parallel
    print("\nDeploying and launching scans...")
    threads = []
    for srv in SCAN_SERVERS:
        chunk = chunks[srv["name"]]
        t = threading.Thread(target=install_deps_and_deploy, args=(srv, chunk))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Step 6: Status check after a few seconds
    print("\n" + "=" * 60)
    print("Checking status after 5 seconds...")
    time.sleep(5)
    for srv in SCAN_SERVERS:
        check_srv_status(srv)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print(f"  Original domains:  {original_count:,}")
    print(f"  Already scanned:   {scanned_count:,}")
    print(f"  Missing (to scan): {missing_count:,}")
    print(f"  srv-1 chunk:       {len(chunks['srv-1']):,} (concurrency={SCAN_SERVERS[0]['concurrency']})")
    print(f"  srv-2 chunk:       {len(chunks['srv-2']):,} (concurrency={SCAN_SERVERS[1]['concurrency']})")
    print()
    print("Monitor progress:")
    print("  python check_missing_progress.py")
    print()
    print("Check tmux directly:")
    print("  ssh root@[srv-1]  → tmux attach -t rescan")
    print("  ssh root@[srv-2]  → tmux attach -t rescan")
    print()
    print("Results will be in ~/results_missing/ on each server.")
    print("After scanning, collect with collect_missing_results.py")


if __name__ == "__main__":
    main()
