#!/usr/bin/env python3
import os, sys, datetime, pathlib, urllib.request, urllib.parse

REGISTRAR_ID = os.environ["REGISTRAR_ID"]
TOKEN        = os.environ["NETAPI_TOKEN"]
TODAY        = datetime.date.today().isoformat()
YEAR         = TODAY[:4]
MONTH_DIR    = TODAY[5:7]
MONTH        = TODAY[:7]

BASE       = pathlib.Path("data/new")
day_file   = BASE / YEAR / MONTH_DIR / f"{TODAY}.txt"
month_file = BASE / YEAR / f"{MONTH}.txt"
all_file   = pathlib.Path("data/all.txt")

params = urllib.parse.urlencode({
    "method":       "download-whois",
    "registrar_id": REGISTRAR_ID,
    "filter_type":  "new",
    "token":        TOKEN,
})
req = urllib.request.Request(
    f"https://netapi.com/api/?{params}",
    headers={"User-Agent": "PhishDestroy-Research/1.0"}
)
with urllib.request.urlopen(req, timeout=120) as r:
    raw = r.read().decode("utf-8", errors="replace")

domains = []
for line in raw.splitlines():
    line = line.strip().lower()
    if not line or line.startswith(("#", ";", "%")):
        continue
    if ":" in line:
        key, _, val = line.partition(":")
        if key.strip() in ("domain", "domain name", "name"):
            line = val.strip()
        else:
            continue
    if "." in line and " " not in line:
        domains.append(line)

if not domains:
    print(f"[{TODAY}] No new domains.")
    sys.exit(0)

domains = sorted(set(domains))
print(f"[{TODAY}] {len(domains)} new domains (registrar {REGISTRAR_ID})")

day_file.parent.mkdir(parents=True, exist_ok=True)
day_file.write_text("\n".join(domains) + "\n", encoding="utf-8")

month_file.parent.mkdir(parents=True, exist_ok=True)
existing = set(month_file.read_text(encoding="utf-8").splitlines()) if month_file.exists() else set()
month_file.write_text("\n".join(sorted(existing | set(domains))) + "\n", encoding="utf-8")

all_file.parent.mkdir(parents=True, exist_ok=True)
existing_all = set(all_file.read_text(encoding="utf-8").splitlines()) if all_file.exists() else set()
all_file.write_text("\n".join(sorted(existing_all | set(domains))) + "\n", encoding="utf-8")

print(f"  {day_file}: {len(domains)}")
print(f"  {month_file}: {len(existing | set(domains))}")
print(f"  {all_file}: {len(existing_all | set(domains))}")
