# NameSilo Abuse Investigation — Case File

Generated UTC: 2026-06-03T07:21:17+00:00

This is the compact sanitized entry point for agents and reporting. It uses aggregate outputs only and omits raw contact fields, server access details, keys, tokens, and passwords.

## Source Of Truth

- Raw input: `1479_full.csv`.
- Input profile: `csv_profile_1479.json`.
- Current scan aggregates: `report_stats.json`.
- Evidence manifest and hashes: `evidence_manifest.json` / `evidence_manifest.txt`.
- Historical report: `report_clean.txt` is useful for timeline context, but its totals predate the rescan and conflict with the current aggregate set.

## Dataset

- CSV rows counted: 5,269,356.
- Domains with IP/DNS candidate: 3,397,413 (64.5% of CSV rows).
- Domains without IP/DNS candidate: 1,871,943 (35.5% of CSV rows).
- Rows with email field: 221,862. Do not publish raw values.
- Rows with phone field: 119,819. Do not publish raw values.

## Current Scan Summary

- Total NameSilo domains in scan stats: 5,269,357.
- Domains queued/scanned with DNS: 3,397,413.
- Dead or no HTTP response: 2,255,310 (66.4% of scanned).
- Active/responded: 1,129,114 (33.2% of scanned).
- Cloudflare-fronted domains: 429,079 (complete merged scan; initial scan reported 363,185).

## Key Findings

- brand_phishing_domains: 3,726
- indonesian_gambling_domains: 24,349
- chinese_adult_piracy_domains: 10,571
- namesilo_self_parked_domains: 8,684 (complete merged scan; initial scan reported 7,438)
- namesilo_self_parked_gambling_adult: 185
- single_server_fingerprint_domains: 328,230
- cloudflare_flagged_phishing_on_that_server: 2,062

## Source Consistency

- Needs review: CSV row count vs report total. csv_profile=5,269,356, report_stats=5,269,357; delta=-1.
- Needs review: CSV no-IP count vs manifest no-DNS count. csv_profile=1,871,943, manifest=1,871,944; delta=-1.
- Resolved: gambling delta. manifest=24,349 (heuristic/keyword), evidence_data=19,198 (favicon-confirmed cluster match). Both figures are correct; the report uses both with explicit labels.
- Explained: final_report scanned (2,503,213) vs report_stats (3,397,413). Delta of ~894K is the rescan batch (all_missing_results.jsonl). Current baseline is report_stats.json.
- Explained: report_clean dead count (3,242,664) predates rescan. Use report_stats.json dead=2,255,310 as the current figure.

## Next Reporting Improvements

- Treat `report_stats.json` plus `evidence_manifest.json` as the current aggregate baseline until a newer manifest is generated.
- Regenerate the manifest after each merge/rescan so the evidence counts and hashes move together.
- Keep public reports on aggregate counts and IOC examples; keep raw CSV contact fields private.
- Move obsolete reports into an archive folder only after confirming no workflow depends on their current paths.

## Key Deliverables

- `NameSilo Report.html` — full visual investigation report (public).
- `clusters.html` — favicon & server fingerprint cluster page (public).
- `domains.html` — 107,252 IOC domains, searchable/filterable (public).
- `namesilo-post.jpg` — satirical summary image.
- `evidence/criminal_domains.json` — 107,252 IOC records with category, country, title.
- `evidence/evidence_manifest.json` — master integrity anchor with SHA-256 hashes.
- `case_metrics.json` — sanitized machine-readable aggregate summary.
- `CASE_FILE.md` — this entry point.
