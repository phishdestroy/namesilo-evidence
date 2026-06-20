# Live Stats — NameSilo, LLC Investigation

Auto-updated daily by [GitHub Actions](../.github/workflows/daily_fetch.yml) at **06:00 UTC**.

## Badge Endpoints

These JSON files power the live shields.io badges in the README.  
Fetch them directly or embed in any dashboard.

| File | Label | Current value | Use |
|:---|:---|:---|:---|
| [today.json](today.json) |  | domains registered in last 24h | daily activity |
| [total.json](total.json) |  | all-time new domains tracked | running total |
| [last_fetch.json](last_fetch.json) |  | ISO date of last successful run | health check |

**Embed a badge:**
```
https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/phishdestroy/namesilo-evidence/main/stats/today.json
```

## Update Schedule

| What | When | Output |
|:---|:---|:---|
| New domain fetch | Daily 06:00 UTC |  |
| Monthly rollup | Daily 06:00 UTC |  |
| All-time list | Daily 06:00 UTC |  |
| Feed index | Daily 06:00 UTC |  |
| These badges | Daily 06:00 UTC |  |

Source: [scan/fetch_new.py](../scan/fetch_new.py) · Requires  secret

---

## PhishDestroy Registrar Investigations

| Registrar | IANA | Domains scanned | Malicious | Daily feed | Live report |
|:---|:---:|---:|---:|:---:|:---|
| **NICENIC INTERNATIONAL GROUP** | #3765 | 343,107 | 18,927 | ✅ | [nicenic-evidence →](https://phishdestroy.github.io/nicenic-evidence/) |
| **Trustname.com / Fewmoretaps OÜ** | #4318 | 9,109 | 1,114 | ✅ | [trustname-evidence →](https://phishdestroy.github.io/trustname-evidence/) |
| **NameSilo, LLC** | #1479 | 5,269,357 | 183,419 | ✅ | [namesilo-evidence →](https://phishdestroy.github.io/namesilo-evidence/) |

[PhishDestroy](https://phishdestroy.io) · [GitHub](https://github.com/phishdestroy) · TLP:CLEAR
