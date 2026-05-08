# Medium / external mirror archive

Every external article and mirror surface for this investigation, with **immutable archive URLs** and one-click "save now" links for the major archive services.

If any of the live URLs goes dark — Medium suspends the account, the registrar files a takedown, X removes more posts — the archive copies are permanent.

---

## Master Medium article — "NameSilo Lied to Defend a $20M Crypto Scam"

| Surface | URL | Status |
|---|---|---|
| Live | https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e | published |
| Wayback (latest) | https://web.archive.org/web/2026/https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e | check before sharing |
| Wayback (save fresh) | https://web.archive.org/save/https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e | one-click save |
| archive.ph | https://archive.ph/https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e | check / save |
| GhostArchive | https://ghostarchive.org/archive?url=https%3A%2F%2Fphishdestroy.medium.com%2Fnamesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e | manual save |

---

## Earlier Medium piece — "xmrwallet.com" technical write-up

The original drainer breakdown that triggered the operator's first email to us.

| Surface | URL |
|---|---|
| Live | https://phishdestroy.medium.com/xmrwallet-com-2953f35b8a79 |
| Wayback (save fresh) | https://web.archive.org/save/https://phishdestroy.medium.com/xmrwallet-com-2953f35b8a79 |
| archive.ph | https://archive.ph/https://phishdestroy.medium.com/xmrwallet-com-2953f35b8a79 |

---

## PhishDestroy.io canonical pages

| Page | URL |
|---|---|
| Article (canonical) | https://phishdestroy.io/namesilo-killed-our-twitter |
| Technical breakdown | https://phishdestroy.io/xmrwallet-namesilo-exposed |
| Save canonical | https://web.archive.org/save/https://phishdestroy.io/namesilo-killed-our-twitter |
| Save technical | https://web.archive.org/save/https://phishdestroy.io/xmrwallet-namesilo-exposed |

---

## NameSilo's own tweet — the artifact at the centre of the case

Permanently archived **before** any deletion attempt could succeed:

| Surface | URL |
|---|---|
| GhostArchive (immutable) | https://ghostarchive.org/archive/CXXZ0 |
| Local screenshot | [`evidence/03-namesilo-statement-mar13.png`](evidence/03-namesilo-statement-mar13.png) |
| SHA-256 of the screenshot | `ad29e1d3d4803ff37c88ef860bef6de9e62f6ce533657f2e5c5460eb2e0b8ebf` |

---

## GitHub repositories

| Repo | URL | Purpose |
|---|---|---|
| `namesilo-xmrwallet-coverup` (this repo) | https://github.com/phishdestroy/namesilo-xmrwallet-coverup | The cover-up case file |
| `DO-NOT-USE-xmrwallet-com` | https://github.com/phishdestroy/DO-NOT-USE-xmrwallet-com | Earlier technical evidence |
| GitHub Pages mirror (this repo, `docs/`) | https://phishdestroy.github.io/namesilo-xmrwallet-coverup/ | SEO-optimized static-site copy |
| Custom domain (planned) | https://namesilo-xmrwallet.phishdestroy.io | via `docs/CNAME` |

---

## How to push every URL to the Wayback Machine in one shot

```bash
#!/usr/bin/env bash
set -e
URLS=(
  "https://phishdestroy.io/namesilo-killed-our-twitter"
  "https://phishdestroy.io/xmrwallet-namesilo-exposed"
  "https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e"
  "https://phishdestroy.medium.com/xmrwallet-com-2953f35b8a79"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup"
  "https://github.com/phishdestroy/DO-NOT-USE-xmrwallet-com"
  "https://phishdestroy.github.io/namesilo-xmrwallet-coverup/"
)
for u in "${URLS[@]}"; do
  echo "[wayback] $u"
  curl -fsSL -X POST "https://web.archive.org/save/$u" \
       -H 'User-Agent: PhishDestroy-Archive/1.0' \
       --max-time 120 || true
  sleep 8
done
```

Re-run this whenever a meaningful change is committed to the repo. Wayback is rate-limited (~8s sleep between submissions is a safe floor).

---

## How to push to archive.ph in bulk

archive.ph does not have a clean public POST endpoint, but the page accepts URL-encoded GET parameters that trigger a save. The legitimate path is to paste each URL on https://archive.ph/ in a browser. For the seven URLs above, that's roughly seven clicks.

---

## Status check (run periodically)

After publication, sanity-check each archive surface every few weeks. If any URL has been quietly delisted, archived versions remain accessible at the Wayback / archive.ph / GhostArchive copies above. Note any takedown attempts in [`PRESSURE.md`](PRESSURE.md) §3 ("Stage 3 — Ongoing").

The point is not paranoia. The point is that this case has already produced, in seven weeks, at least three separate documented silencing attempts. The behavior is quantifiable. We document it as it happens.
