#!/usr/bin/env python3
"""Build docs/feed-ioc.json for the Feed IOC browser page.

Reads ioc/indicators.csv and normalises it into the shape the page expects.
The CSV schema differs per evidence repo, so columns are detected rather than
hardcoded. Empty fields are omitted to keep the payload small; the page caps
at the highest-severity MAX_ENTRIES rows and reports the full total.
"""

import csv, json, sys
from pathlib import Path

CSV_PATH = Path("ioc/indicators.csv")
OUT_PATH = Path("docs/feed-ioc.json")
MAX_ENTRIES = 120_000

csv.field_size_limit(10_000_000)

DOMAIN_COLS = ("domain", "indicator", "host", "hostname")
FEED_COLS   = ("threat_sources", "source", "sources", "feeds")
DATE_COLS   = ("registered_at", "registered", "date", "first_seen")
SEV_RANK    = {"HIGH": 3, "MEDIUM": 2, "MED": 2, "LOW": 1, "INFO": 0}


def pick(row, names):
    for n in names:
        v = row.get(n)
        if v:
            return str(v).strip()
    return ""


def norm_sev(row):
    """Normalise numeric or textual severity to HIGH / MEDIUM / LOW."""
    label = (row.get("severity_label") or "").strip().upper()
    if label in SEV_RANK:
        return label
    raw = (row.get("severity") or "").strip().upper()
    if raw in SEV_RANK:
        return "MEDIUM" if raw == "MED" else raw
    try:
        n = int(float(raw))
    except (TypeError, ValueError):
        return "LOW"
    return "HIGH" if n >= 3 else "MEDIUM" if n == 2 else "LOW"


def split_feeds(value):
    out = []
    for part in value.replace(";", ",").replace("|", ",").split(","):
        part = part.strip()
        if part and part.lower() not in ("none", "n/a", "-"):
            out.append(part)
    return out


def main():
    if not CSV_PATH.exists():
        print(f"[!] {CSV_PATH} not found", file=sys.stderr)
        return 1

    entries, seen = [], set()
    with CSV_PATH.open(encoding="utf-8-sig", errors="replace", newline="") as fh:
        for row in csv.DictReader(fh):
            domain = pick(row, DOMAIN_COLS).lower().strip(".")
            if not domain or domain in seen:
                continue
            seen.add(domain)
            e = {"domain": domain, "severity": norm_sev(row)}
            tld = (row.get("tld") or "").strip().lstrip(".")
            if not tld and "." in domain:
                tld = domain.rsplit(".", 1)[-1]
            if tld:
                e["tld"] = tld
            for key, src in (("category", ("category", "type")),
                             ("ip", ("ip",)),
                             ("ip_country", ("ip_country", "country")),
                             ("date", DATE_COLS)):
                v = pick(row, src)
                if v:
                    e[key] = v
            feeds = split_feeds(pick(row, FEED_COLS))
            if feeds:
                e["feeds"] = feeds
            entries.append(e)

    # The published blocklists are the source of truth for coverage: some repos
    # have a partial or malformed indicators.csv, so anything listed in ioc/
    # still has to show up on the page.
    for path, sev in ((Path("ioc/domains_high.txt"), "HIGH"),
                      (Path("ioc/domains_all_malicious.txt"), "MEDIUM")):
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            d = line.strip().lower().strip(".")
            if not d or d.startswith("#") or d in seen:
                continue
            seen.add(d)
            e = {"domain": d, "severity": sev}
            if "." in d:
                e["tld"] = d.rsplit(".", 1)[-1]
            e["category"] = "PHISHING" if sev == "HIGH" else "SUSPICIOUS"
            entries.append(e)

    total = len(entries)
    entries.sort(key=lambda e: (-SEV_RANK.get(e["severity"], 0), e["domain"]))
    shown = entries[:MAX_ENTRIES]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(
        json.dumps({"total": total, "included": len(shown), "domains": shown},
                   ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8")

    if len(shown) < total:
        print(f"[!] capped: {len(shown):,} of {total:,} written "
              f"(highest severity first); raise MAX_ENTRIES to include all")
    print(f"[+] {OUT_PATH}: {len(shown):,} entries, {total:,} total IOC")
    return 0


if __name__ == "__main__":
    sys.exit(main())
