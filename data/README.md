# data/ — Phishing domain evidence archive

Auto-updated daily by `scan/fetch_new.py` from NetAPI feed.

## Structure

```
data/
├── all.txt                          # All collected domains (deduplicated)
├── index.json                        # Full analytics snapshot
├── new/
│   └── YYYY/MM/
│       ├── YYYY-MM-DD.txt           # Plain domain list per day
│       └── YYYY-MM-DD.json          # Enriched per-domain records
├── snapshots/
│   └── YYYY-MM.json                  # Monthly aggregated stats
└── ioc/                              # Threat intel exports
    ├── serial_registrants.json       # Repeat registrant emails + domains
    ├── shared_ips.json               # IPs hosting multiple phishing domains
    ├── brand_domains.json            # Domains grouped by targeted brand
    ├── serial_emails.txt             # Plain-text: email⇥count
    ├── shared_ips.txt                # Plain-text: ip⇥count⇥country
    ├── brand_domains.txt             # Plain-text: keyword⇥domain
    └── stix-bundle.json              # STIX 2.1 bundle (MISP/OpenCTI ready)
```

## Per-domain enriched JSON

Each entry in `data/new/YYYY/MM/YYYY-MM-DD.json` contains:

```json
{
  "domain":      "fake-wallet.xyz",
  "expiring_at": "2027-06-15",
  "ip":          "1.2.3.4",
  "ip_country":  "CN",
  "email":       "registrant@example.com",
  "phone":       "+86123456789"
}
```

## index.json fields

| Field | Type | Description |
|-------|------|-------------|
| `days` | list | Per-day count + revenue + path |
| `total_new_all_time` | int | Unique domains across full history |
| `total_revenue_estimate` | float | USD, based on public TLD prices |
| `avg_registration_days` | int | Average registration period |
| `ip_countries` | dict | Top 10 hosting countries |
| `top_shared_ips` | dict | Top 20 IPs by domain count |
| `deployed_count` | int | Domains with active IP |
| `no_ip_count` | int | Domains parked / not yet deployed |
| `deployment_rate` | float | % with active IP |
| `reg_periods` | dict | Buckets: <1yr, =1yr, 2yr, 3yr+ |
| `pct_gt_1yr` | float | % registered for >1 year |
| `pct_gt_2yr` | float | % registered for >2 years |
| `tld_stats` | dict | Top 20 TLD: count + avg reg days |
| `revenue_by_tld` | dict | TLD revenue breakdown |
| `catch_age_buckets` | dict | Same-day / week / month / older |
| `avg_catch_age_days` | int | Avg domain age when first caught |
| `fresh_pct` | float | % caught ≤7d old |
| `burst_days` | list | Top 10 high-volume registration days |
| `top_registrant_emails` | dict | Top 20 emails by domain count |
| `top_registrant_phones` | dict | Top 10 phones |
| `serial_email_count` | int | Emails with ≥10 registered domains |
| `brand_heatmap` | dict | Top 20 keyword matches in domain labels |
| `unranked_pct` | float | % with zero Majestic rank |
| `correlation_count` | int | Domains confirmed in main blocklist |
| `correlation_pct` | float | Confirmation rate |
| `last_updated` | str | ISO date of latest fetch |

## License

Public domain — use freely for research, defense, and accountability.
