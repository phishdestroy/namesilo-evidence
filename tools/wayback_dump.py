"""
Wayback Machine dump for @Phish_Destroy
- queries CDX API for every snapshot of x.com/twitter.com URLs containing the handle
- downloads each snapshot HTML
- saves to ./snapshots/ with timestamp filename
"""
import json
import os
import time
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

HANDLE = "Phish_Destroy"
OUT = Path(__file__).parent / "snapshots"
OUT.mkdir(exist_ok=True)

CDX_TARGETS = [
    f"twitter.com/{HANDLE}",
    f"twitter.com/{HANDLE}/*",
    f"x.com/{HANDLE}",
    f"x.com/{HANDLE}/*",
    f"mobile.twitter.com/{HANDLE}/*",
    f"nitter.net/{HANDLE}/*",
]

UA = {"User-Agent": "Mozilla/5.0 (research; phishdestroy backup)"}

def cdx_query(target):
    url = (
        "https://web.archive.org/cdx/search/cdx?"
        f"url={quote(target)}"
        "&output=json&fl=timestamp,original,statuscode,mimetype"
        "&filter=statuscode:200&filter=mimetype:text/html"
        "&collapse=digest"
    )
    print(f"[cdx] {target}")
    req = Request(url, headers=UA)
    with urlopen(req, timeout=60) as r:
        rows = json.load(r)
    if not rows:
        return []
    return rows[1:]

def fetch_snapshot(timestamp, original):
    snap_url = f"https://web.archive.org/web/{timestamp}id_/{original}"
    safe_orig = original.replace("/", "_").replace(":", "_").replace("?", "_")[:120]
    out_file = OUT / f"{timestamp}__{safe_orig}.html"
    if out_file.exists():
        return False
    try:
        req = Request(snap_url, headers=UA)
        with urlopen(req, timeout=90) as r:
            data = r.read()
        out_file.write_bytes(data)
        print(f"  saved {out_file.name} ({len(data)} bytes)")
        return True
    except Exception as e:
        print(f"  fail {snap_url} :: {e}")
        return False

def main():
    seen = set()
    total = 0
    for tgt in CDX_TARGETS:
        try:
            rows = cdx_query(tgt)
        except Exception as e:
            print(f"[cdx-fail] {tgt} :: {e}")
            continue
        for ts, original, status, mime in rows:
            key = (ts, original)
            if key in seen:
                continue
            seen.add(key)
            fetch_snapshot(ts, original)
            total += 1
            time.sleep(0.4)  # polite
    print(f"\n[done] {total} snapshots queued")

if __name__ == "__main__":
    main()
