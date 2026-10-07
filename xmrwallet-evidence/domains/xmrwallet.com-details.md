# xmrwallet.com — Primary Scam Domain

| | |
|---|---|
| **Status** | Active |
| **Registered** | 2016-08-29 |
| **Expires** | 2031-08-29 |
| **Registrar** | NameSilo LLC |
| **IP** | 186.2.165.49 |
| **ASN** | AS59692 — IQWeb FZ-LLC (Belize) |
| **NS** | ns1/ns2.ddos-guard.net |
| **MX** | mx1/mx2.privateemail.com |
| **CDN** | DDoS-Guard |

## Confirmed Malicious Behavior

- View key exfiltration via `session_key` (Base64) — 40+ times per session
- Transaction hijacking: `raw_tx_and_hash.raw = 0`
- Server-side `type='swept'` theft marker
- 4 Google trackers (GTM, GA, GA4, DoubleClick)
- `/support_login.html` backdoor (`session_id=8de50123dab32`)
- 5.3-year GitHub commit gap (2018-2024)

## DNS Map

See [DNSDumpster map](../../docs/img/dnsmap-xmrwallet-com.png)

## Escape Domains

- [xmrwallet.cc](../xmrwallet.cc/) — SUSPENDED
- [xmrwallet.biz](../xmrwallet.biz/) — SUSPENDED
- [xmrwallet.net](../xmrwallet.net/) — ACTIVE
- [xmrwallet.me](../xmrwallet.me/) — ACTIVE

## NameSilo Cover-Up

NameSilo received the same evidence that led 3 other registrars to suspend. NameSilo called the operator "the victim," claimed the site was "compromised," and helped remove VirusTotal warnings. The operator's own emails contradict NameSilo's "hack" story.

## Report

- **ICANN complaint (recommended):** https://www.icann.org/compliance/complaint
- abuse@namesilo.com (warning: NameSilo sided with operator)
- abuse@ddos-guard.net
- https://safebrowsing.google.com/safebrowsing/report_phish/
- https://phish.report/
