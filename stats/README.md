# stats/ — shields.io endpoint badges

Each `.json` here is a [shields.io endpoint](https://shields.io/badges/endpoint-badge) badge file.
Auto-regenerated daily by `scan/fetch_new.py` after the NetAPI fetch.

| File | Badge content | Color |
|------|---------------|-------|
| `today.json` | New domains registered today | `red` |
| `total.json` | Total domains all time | `red` |
| `last_fetch.json` | Date of last successful fetch | `blue` |
| `revenue.json` | Estimated registrar revenue from these domains | `gold` |
| `lifetime.json` | Average registration period (days) | `purple` |
| `hosting.json` | Top 3 hosting countries | `blue` |
| `top_ip.json` | Most popular shared IP (domain count) | `purple` |
| `no_ip.json` | Domains with no DNS at registration (%) | `gold` |
| `deployed.json` | Domains with active IP (%) | `green` |
| `longreg.json` | % registered >1yr / >2yr | `purple` |
| `tld_top.json` | Top 3 TLD zones | `purple` |
| `top_tld_rev.json` | TLD generating most revenue | `gold` |
| `freshness.json` | % caught ≤7d after registration | `green` |
| `serial_regs.json` | Serial registrant emails (≥10 domains) | `red` |
| `brands.json` | Top 3 targeted brand keywords | `purple` |
| `unranked.json` | % with zero Majestic rank | `purple` |
| `correlation.json` | % confirmed in main Destroylist blocklist | `green` |

**Usage in markdown:**
```markdown
![Total](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/<owner>/<repo>/<branch>/stats/total.json)
```
