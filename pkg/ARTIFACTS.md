# Evidence Artifacts — NameSilo Registrar Abuse Investigation

**Case:** NameSilo mass-abuse registrar investigation  
**Scan period:** 2026-06-02 → 2026-06-03 UTC  
**Investigator:** PhishDestroy  
**Manifest SHA-256:** `af7f81f859e1f7a3a0a8fa19a4ab92d94c1be7750e6b63e1e46ea0020c0f624b`

---

## Dataset at a Glance

| Metric | Value |
|---|---|
| Total NameSilo domains (complete zone) | 5,269,357 |
| Domains with DNS / scanned | 3,397,413 |
| Dead / no HTTP response | 2,255,310 (66.4%) |
| Active / responded | 1,129,114 (33.2%) |
| Cloudflare-fronted | 429,079 |

### Key Findings

| Category | Count |
|---|---|
| Brand phishing domains | **3,726** |
| Indonesian gambling domains (heuristic) | **24,349** |
| Indonesian gambling domains (favicon-confirmed) | **19,198** |
| Chinese adult and piracy domains | **10,571** |
| NameSilo self-parked domains | 8,684 |
| NameSilo self-parked + gambling/adult | 185 |
| Single-server fingerprint cluster | 328,230 |
| Cloudflare-flagged phishing on that server | 2,062 |
| Total criminal/abuse domains (evidence_data.json) | 107,252 |

---

## Artifacts

### PUBLIC — verifiable via GitHub

#### `NameSilo Report.html`
Full visual investigation report with methodology, charts, IOC examples, and findings.  
**Visibility:** Public

#### `clusters.html`
Favicon fingerprint clusters and server fingerprint analysis — 12 operator clusters, visual grid.  
**Visibility:** Public

#### `domains.html`
Full IOC domain list — 107,252 criminal/abuse domains with category, country, page type, title.  
**Visibility:** Public

#### `namesilo-post.jpg`
Satirical summary image — "WE SCANNED ALL 5,269,357 OF THEIR DOMAINS. 87.3% IS JUNK."  
**Visibility:** Public

#### `evidence/evidence_manifest.json`
Master evidence manifest — links all artifacts, timestamps, and methodology notes.  
**Visibility:** Public · `github.com/PhishDestroy/namesilo-scanner`  
**SHA-256:** `af7f81f859e1f7a3a0a8fa19a4ab92d94c1be7750e6b63e1e46ea0020c0f624b`

#### `CASE_FILE.md`
Compact sanitized case narrative — entry point for agents and reporting.  
**Visibility:** Public

---

### PRIVATE — SHA-256 via manifest

#### `1479_full.csv`
Complete NameSilo zone export — 5,269,356 rows, 9 columns  
(`registrar, url, registered_at, expiring_at, majestic_rank, emails, phones, ip, ip_country`).  
349 MB. Contains PII (emails, phones) — **do not publish raw values.**  
**Visibility:** Private  
**SHA-256:** `dd533dfa46077ba6c5bf204cd984f53fd4308f395d293a3e7ac561c596990907`

#### `all_active_domains.csv`
All 1,129,115 domains that returned an HTTP response — page_type, title, language, cloudflare flag, parking_service, favicon_hash.  
84 MB.  
**Visibility:** Private

#### `cloudflare_domains.csv`
429,080 Cloudflare-fronted domains — page_type, title, parking_service, final_url, server_fp, word_count.  
45 MB.  
**Visibility:** Private

#### `namesilo_parked_domains.csv`
8,684 NameSilo self-parked domains with full scan record.  
942 KB.  
**Visibility:** Private

#### `garbage_domains.jsonl`
Full scan output — 3,376,188 records including dead/empty/low-content domains.  
407 MB.  
**Visibility:** Private

#### `domains_to_scan.jsonl`
Input domain list — 3,397,413 NameSilo domains with DNS resolution. 499 MB.  
**Visibility:** Private  
**SHA-256:** `70782d6b6312f27533267fc34977a971b90c5ab394e075d76ba25d22bd866f23`

#### `final_garbage.jsonl`
Complete scan results — active records (1,129,114 domains). 468 MB.  
**Visibility:** Private  
**SHA-256:** `b0d6cc1c80b2964593b310029fde4b7f4aeac6c702baaecae78359beab84b0f6`

#### `all_missing_results.jsonl`
Rescan results — previously unscanned ~894K domains. 304 MB.  
**Visibility:** Private  
**SHA-256:** `e8224d3fd4928de67a5ba995a727c11fa28e6cbdb2e5a1cf4a8f78b1387181aa`

#### `garbage_5s.jsonl`
Initial scan results — 911,188 non-dead records (pre-rescan). 246 MB.  
**Visibility:** Private  
**SHA-256:** `3f3d36ebc97fb97ef6ac492f66ff8301f80a98a161f28e726850863a8ac76f8e`

#### `reports/report_stats.json`
Scan statistics — `total_namesilo, scanned, dead, active, cloudflare, page_types` breakdown.  
Generated at scan completion.  
**Visibility:** Private  
**SHA-256:** see `evidence_manifest.json` → `sources.scan_stats.sha256`

#### `evidence/evidence_data.json`
Full domain lists per abuse category (brand phishing, Indonesian gambling, Chinese adult/piracy).  
Contains complete IOC sets for law enforcement / brand-rights holders.  
**Visibility:** Private — share only with authorized recipients  
**SHA-256:** see `evidence_manifest.json` → `sources.evidence_data.sha256`

#### `evidence/criminal_domains.json`
107,252 criminal/abuse domains with category, page_type, country, title, favicon hash.  
Source data for `domains.html`. 16 MB.  
**Visibility:** Private

---

## Methodology

| Parameter | Value |
|---|---|
| Scanner | aiohttp + asyncio (Python 3.11) |
| HTTP timeout | 5 seconds |
| Concurrency | 400–600 async connections per node |
| Favicon clustering | MurmurHash3 — identical hash = same operator |
| Server fingerprint | SHA-256 of (Server + X-Powered-By + ETag), truncated to 12 hex chars |
| Coverage | Complete zone file — no sampling |

**Infrastructure used:**
- AWS Lambda: `namesilo-scanner`, us-east-1, up to 400 concurrent executions
- GCP Cloud Run: `domain-scanner-job`, us-central1

---

## File Structure (this package)

```
pkg/
├── NameSilo Report.html        ← main investigation report (public)
├── clusters.html               ← favicon & server fingerprint clusters (public)
├── domains.html                ← 107,252 IOC domain list (public)
├── namesilo-post.jpg           ← satirical summary image
├── CASE_FILE.md                ← case narrative
├── ARTIFACTS.md                ← this file
├── README.md
├── 1479_full.csv               (private — 349MB, full zone + WHOIS data)
├── all_active_domains.csv      (private — 84MB, 1,129,115 active domains)
├── cloudflare_domains.csv      (private — 45MB, 429,080 CF-fronted domains)
├── namesilo_parked_domains.csv (private — 942KB, NameSilo self-parked)
├── garbage_domains.jsonl       (private — 407MB, full scan output)
├── final_garbage.jsonl         (private — 468MB, active scan results)
├── all_missing_results.jsonl   (private — 304MB, rescan results)
├── garbage_5s.jsonl            (private — 246MB, initial scan results)
├── domains_to_scan.jsonl       (private — 499MB, scan input list)
├── reports/
│   ├── report_stats.json       (private — aggregate scan metrics)
│   └── report_clean.txt        (human-readable scan summary)
├── evidence/
│   ├── evidence_manifest.json  (public — master integrity anchor)
│   ├── evidence_manifest.txt
│   ├── criminal_domains.json   (private — 107,252 IOC records)
│   ├── evidence_data.json      (private — full IOC sets by category)
│   ├── case_metrics.json
│   └── csv_profile_1479.json
└── scanner/                    ← scan pipeline source code
    ├── analyze.py
    ├── enqueue.py
    ├── local_scan.py
    ├── prepare.py
    ├── scan_missing.py
    ├── lambda/
    └── cloudrun/
```
