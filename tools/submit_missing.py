"""
For every tweet ID listed in out/missing.txt, submit the URL to:
  - Wayback Machine "Save Page Now"
  - archive.ph (HTML form submit)

This forces fresh captures of tweets that don't yet have any archive copy.
Re-run inventory.py afterwards to download the new captures.
"""
import time
import urllib.parse
from pathlib import Path
from urllib.request import Request, urlopen

OUT = Path(__file__).parent / "out"
MISSING = OUT / "missing.txt"
HANDLE = "Phish_Destroy"

UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) PhishDestroyArchiver/1.0",
}

def submit_wayback(url: str):
    save = f"https://web.archive.org/save/{url}"
    try:
        req = Request(save, headers=UA)
        with urlopen(req, timeout=120) as r:
            print(f"[wayback] {url} -> {r.status}")
    except Exception as e:
        print(f"[wayback] {url} -> ERR {e}")

def submit_archive_ph(url: str):
    form = "https://archive.ph/submit/"
    data = urllib.parse.urlencode({"url": url, "anyway": "1"}).encode()
    try:
        req = Request(form, data=data, headers=UA, method="POST")
        with urlopen(req, timeout=120) as r:
            print(f"[archive.ph] {url} -> {r.status}")
    except Exception as e:
        print(f"[archive.ph] {url} -> ERR {e}")

def main():
    if not MISSING.exists():
        print(f"no missing.txt at {MISSING} — run inventory.py first")
        return
    ids = [x.strip() for x in MISSING.read_text().splitlines() if x.strip()]
    print(f"submitting {len(ids)} tweets to both archives...")
    for i, tid in enumerate(ids, 1):
        url = f"https://x.com/{HANDLE}/status/{tid}"
        print(f"\n[{i}/{len(ids)}] {url}")
        submit_wayback(url)
        time.sleep(8)
        submit_archive_ph(url)
        time.sleep(8)

if __name__ == "__main__":
    main()
