<img src="https://capsule-render.vercel.app/api?type=waving&color=0:030810,100:da3633&height=120&fontColor=ffffff&animation=fadeIn&text=Live%20Stats%20%C2%B7%20NameSilo&fontSize=32&desc=IANA%20%231479%20%C2%B7%20Auto-updated%20daily&descAlignY=62&descSize=14" width="100%"/>

# Live Stats — NameSilo, LLC Investigation

Auto-updated daily by [GitHub Actions](../.github/workflows/daily_fetch.yml) at **06:00 UTC**.


<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

Badge Endpoints

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


<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

Update Schedule

| What | When | Output |
|:---|:---|:---|
| New domain fetch | Daily 06:00 UTC |  |
| Monthly rollup | Daily 06:00 UTC |  |
| All-time list | Daily 06:00 UTC |  |
| Feed index | Daily 06:00 UTC |  |
| These badges | Daily 06:00 UTC |  |

Source: [scan/fetch_new.py](../scan/fetch_new.py) · Requires  secret

---


<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

PhishDestroy Registrar Investigations

| Registrar | IANA | Domains scanned | Malicious | Daily feed | Live report |
|:---|:---:|---:|---:|:---:|:---|
| **NICENIC INTERNATIONAL GROUP** | #3765 | 343,107 | 18,927 | ✅ | [nicenic-evidence →](https://phishdestroy.github.io/nicenic-evidence/) |
| **Trustname.com / Fewmoretaps OÜ** | #4318 | 9,109 | 1,114 | ✅ | [trustname-evidence →](https://phishdestroy.github.io/trustname-evidence/) |
| **NameSilo, LLC** | #1479 | 5,269,357 | 183,419 | ✅ | [namesilo-evidence →](https://phishdestroy.github.io/namesilo-evidence/) |

[PhishDestroy](https://phishdestroy.io) · [GitHub](https://github.com/phishdestroy) · TLP:CLEAR

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:da3633,100:030810&height=60&section=footer" width="100%"/>
