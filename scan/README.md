# Scan Pipeline

| Script | Purpose |
|---|---|
| `fetch_new.py` | Daily: fetch new registrations from NetAPI → `data/new/` |

Run via [GitHub Actions](../../.github/workflows/daily_fetch.yml) daily at 06:00 UTC.
Requires `NETAPI_TOKEN` secret in repository settings.
