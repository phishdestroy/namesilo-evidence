# xmrwallet.com — Confirmed Scam

> **xmrwallet.com steals your Monero. Private view key exfiltrated. Transactions hijacked server-side.**

## What xmrwallet.com does

1. **Steals your private view key** — encoded in `session_key` and transmitted to their server 40+ times per session
2. **Hijacks your transactions** — client builds TX then discards it (`raw_tx_and_hash.raw = 0`), server constructs its own TX and redirects your funds
3. **Hides behind fake open source** — 5.3 year commit gap (2018-2024), production code differs fundamentally from GitHub
4. **Tracks you with Google** — 4 Google trackers (GTM, UA, GA4, DoubleClick) inside a "privacy" Monero wallet
5. **Deletes evidence** — 21+ GitHub issues deleted, escape domains registered after exposure

## Quick Facts

| Fact | Detail |
|------|--------|
| Domain | xmrwallet.com (NameSilo, paid until 2031) |
| Operator | Nathalie Roy (Canada), GitHub: nathroy |
| Victims | 15+ documented, $2M+ estimated stolen |
| Operating since | 2016 |
| Escape domains | xmrwallet.cc (SUSPENDED), xmrwallet.biz (SUSPENDED) |
| Tor | xmrtor3fsapuu6y26za7vpzox4vpaj6ny5viq2arbmozm7kg6jitnlid.onion |
| Hosting | IQWeb AS59692 / DDoS-Guard (offshore) |
| VirusTotal | 6/93 vendors flag as malicious |

## Evidence

- [Full Technical Analysis](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/)
- [Deleted Issues Archive](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/deleted.html)
- [Issue #35 — TX Hijacking (cached)](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/cache-issue35/)
- [Issue #36 — View Key Theft (cached)](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/cache-issue36/)
- [VirusTotal](https://www.virustotal.com/gui/domain/www.xmrwallet.com)

## The operator deleted GitHub Issues #35 and #36

After PhishDestroy published proof of server-side TX hijacking and view key theft, and after both escape domains were suspended by registrars, the operator silently deleted all evidence from GitHub.

**No technical rebuttal was ever provided. Not once in 8 years.**

Instead of proving innocence — the operator destroyed evidence. Classic fraud behavior.

## Report

- Google Safe Browsing: https://safebrowsing.google.com/safebrowsing/report_phish/
- Registrar: abuse@namesilo.com
- Hosting: abuse@ddos-guard.net
- FBI IC3: https://ic3.gov

## Use safe wallets instead

- [Monero GUI](https://getmonero.org/downloads) — official
- [Feather Wallet](https://featherwallet.org) — lightweight, Tor built-in
- [Cake Wallet](https://cakewallet.com) — iOS/Android
- [Monerujo](https://monerujo.app) — Android

---

*Investigation by [PhishDestroy Research](https://github.com/phishdestroy)*
