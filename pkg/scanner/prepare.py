"""
Step 1: Filter CSV → JSONL keeping only entries with an IP.
Output: domains_to_scan.jsonl (one line = one domain + metadata)
"""
import csv
import json
import sys
from config import SOURCE_CSV, DOMAINS_FILE

def run():
    written = skipped = 0
    with open(SOURCE_CSV, encoding="utf-8", errors="replace") as src, \
         open(DOMAINS_FILE, "w", encoding="utf-8") as dst:

        reader = csv.DictReader(src)
        for row in reader:
            ip = row.get("ip", "").strip()
            if not ip:
                skipped += 1
                continue

            domain = row.get("url", "").strip().lower()
            if not domain:
                skipped += 1
                continue

            obj = {
                "domain": domain,
                "ip": ip,
                "ip_country": row.get("ip_country", "").strip(),
                "registered_at": row.get("registered_at", ""),
                "expiring_at": row.get("expiring_at", ""),
                "majestic_rank": row.get("majestic_rank", ""),
            }
            dst.write(json.dumps(obj) + "\n")
            written += 1

            if written % 100_000 == 0:
                print(f"  written {written:,} | skipped {skipped:,}", flush=True)

    print(f"\nDone. Written: {written:,} | Skipped (no IP): {skipped:,}")
    print(f"Output: {DOMAINS_FILE}")

if __name__ == "__main__":
    run()
