<img src="https://capsule-render.vercel.app/api?type=waving&color=0:030810,100:da3633&height=120&fontColor=ffffff&animation=fadeIn&text=Scan%20Pipeline&fontSize=32&desc=NameSilo%20Investigation%20Tools&descAlignY=62&descSize=14" width="100%"/>

# Scan Pipeline

| Script | Purpose |
|---|---|
| `fetch_new.py` | Daily: fetch new registrations from NetAPI → `data/new/` |

Run via [GitHub Actions](../../.github/workflows/daily_fetch.yml) daily at 06:00 UTC.
Requires `NETAPI_TOKEN` secret in repository settings.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:da3633,100:030810&height=60&section=footer" width="100%"/>
