# Is xmrwallet.com safe? — NO.

> **xmrwallet.com is not safe. It is a confirmed Monero theft service operating since 2016.**

## Short answer

**No. Do not use xmrwallet.com under any circumstances.**

Your private view key is stolen on every login. Your transactions are hijacked server-side. 15+ victims documented. $2M+ estimated stolen.

## What happens when you use xmrwallet.com

1. You enter your wallet credentials
2. Your **private view key** is Base64-encoded into `session_key` and sent to their server
3. This key is retransmitted on **every API request** — 40+ times per session
4. When you send XMR, the client builds a transaction — then **discards it** (`raw_tx_and_hash.raw = 0`)
5. The server builds **its own transaction** and can redirect your funds to any address
6. You see a fake confirmation. Your XMR is gone.

## Is xmrwallet.com open source?

**No.** The GitHub repository is a facade:
- 5.3-year commit gap (2018-2024) — zero updates while production code evolved
- Production code contains `session_key`, `verification`, encrypted `data` — none in GitHub
- `/support_login.html` backdoor endpoint — not in GitHub
- Auditing the GitHub repo is useless

## Is xmrwallet.com a scam?

**Yes.** Confirmed by:
- 6/93 VirusTotal vendors flag as malicious (including Fortinet: Phishing)
- 15+ victim reports on Trustpilot, Sitejabber, Reddit
- Operator banned from r/Monero
- 21+ GitHub issues deleted by operator
- 2 escape domains (xmrwallet.cc, xmrwallet.biz) registered and suspended
- Operator deleted evidence after exposure instead of providing rebuttal

## Who runs xmrwallet.com?

**Nathalie Roy** (Canada)
- GitHub: nathroy (ID: 39167759)
- Reddit: u/WiseSolution (banned from r/Monero)
- Self-identified on support.html

## What should I use instead?

| Wallet | Type | Link |
|--------|------|------|
| **Monero GUI / CLI** | Official desktop | [getmonero.org](https://getmonero.org/downloads) |
| **Feather Wallet** | Desktop + Tor | [featherwallet.org](https://featherwallet.org) |
| **Cake Wallet** | Mobile (iOS/Android) | [cakewallet.com](https://cakewallet.com) |
| **Monerujo** | Android | [monerujo.app](https://monerujo.app) |
| **Ledger / Trezor** | Hardware | [ledger.com](https://ledger.com) / [trezor.io](https://trezor.io) |

**Rule: Any website that asks for your private spend key or seed phrase = scam.**

## I already used xmrwallet.com — what do I do?

1. **Move any remaining funds immediately** using a safe wallet (Feather, Monero GUI)
2. Create a new wallet on a safe platform — your old keys are compromised
3. Report to law enforcement: [ic3.gov](https://ic3.gov)
4. Report the site: [Google Safe Browsing](https://safebrowsing.google.com/safebrowsing/report_phish/)
5. See full victim guide: [LOST_FUNDS.md](../LOST_FUNDS.md)

## Full evidence

- [Complete Technical Analysis](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/)
- [Deleted Issues Archive](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/deleted.html)

---

*Investigation by [PhishDestroy Research](https://github.com/phishdestroy)*
