# Documented Victims & Full Scam Timeline

> This document collects all publicly documented victim reports of the XMRWallet cryptocurrency drainer and provides a comprehensive timeline of the scam operation and the investigation that exposed it.

---

## Documented Victim Reports

The following reports were collected from public review platforms. Each represents a real person who trusted XMRWallet with their funds and had them stolen.

| Amount | Source | Statement |
|--------|--------|-----------|
| 590 XMR (~$177,000) | Sitejabber | "deposited 590 monero — 2 days gone" |
| 17.44 XMR | Trustpilot | TxID and TX Key fully documented by victim |
| 20 XMR | Sitejabber | "put 20 xmr — next day 0 xmr" |
| $200 | Trustpilot | "stole $200, leaving me high and dry" |
| Unknown | Trustpilot | "transferred to some other wallet instead of mine" |
| Unknown | Trustpilot | "cannot verify transaction using private viewing key" |

### Scale Assessment

- **15+ individually documented victims** across Trustpilot, Sitejabber, and Reddit.
- **Conservative estimate:** 10,000 to 50,000+ wallets compromised over 8 years of operation.
- **Total stolen (conservative):** 5,000 to 50,000+ XMR ($1.5M to $15M+ at historical prices).

### On the Disappearance of Reviews

Many victim reviews were mass-reported and removed by the operator or associates. Trustpilot and Sitejabber both showed patterns of legitimate negative reviews vanishing while suspiciously detailed 5-star reviews appeared in clusters. The actual victim count is significantly higher than what remains visible today.

---

## The Operator's Standard Response to Victims

When victims contact XMRWallet support about missing funds, they receive the same deflection:

**"Sync problem."**

This is the standard script. By the time a victim notices their balance is zero and contacts support, the funds have already been exfiltrated to the operator's wallet. The "sync problem" buys time and discourages victims from immediately filing complaints. Some victims were told to "try again later" or "re-import your wallet" — advice designed to make the victim believe the issue is temporary and technical rather than theft.

---

## Full Timeline

### 2016 — The Scam Begins

- **2016-08-29:** `xmrwallet.com` domain registered. The scam operation launches, presenting itself as a free, open-source Monero web wallet.

### 2016-2025 — Years of Silent Theft

- **2016-2025:** Thousands of wallets created. Private spend keys exfiltrated server-side on every wallet creation and login. Victims appear on Trustpilot, Sitejabber, and Reddit over the years. Each report is isolated — no one connects the dots yet.
- **2018:** Operator's Reddit account `u/WiseSolution` banned from r/Monero. First wave of victim reports surfaces.
- **2018-11-06:** Last commit to the XMRWallet GitHub repository before a 5.3-year gap in development activity. The code was never truly open-source in any meaningful sense — the server-side theft mechanism was never in the public repo.

### 2024 — The Return

- **2024-03-15:** First GitHub commit after the 5.3-year gap. The operator resurfaces, likely prompted by renewed scrutiny or the need to update infrastructure.

### 2026 — Exposure, Retaliation, and Takedowns

- **2026-02-04:** `xmrwallet.cc` registered secretly (prepaid for 8 years). An escape domain, ready in case the primary `.com` is taken down.
- **2026-02-09:** `xmrwallet.biz` registered secretly (prepaid for 5 years). A second escape domain.
- **2026-02-13:** GitHub Issue #35 filed — transaction hijacking mechanism publicly exposed with technical proof.
- **2026-02-16:** Operator emails PhishDestroy: *"no phishing going on."*
- **2026-02-17:** Operator emails PhishDestroy: *"This is the data we need"* — directly contradicting his previous denial by acknowledging the evidence.
- **2026-02-17:** Operator emails PhishDestroy: *"Feel free to subpoena the domain registrar"* — a taunt that assumes no one will follow through.
- **2026-02-18:** GitHub Issue #36 filed — live network capture published showing real-time exfiltration of wallet keys.
- **2026-02-22:** @ImCryptOpus tweets: XMRWallet shutdown confirmed, $10M+ stolen.
- **2026-02-23:** `xmrwallet.cc` **SUSPENDED** by PDR Ltd (registrar).
- **2026-02-23:** `xmrwallet.biz` **SUSPENDED** by WebNic.
- **2026-02-23:** Operator deletes GitHub Issues #35 and #36 — destroying public evidence.
- **2026-02-23:** Operator emails PhishDestroy claiming to have *"hired a lawyer and PI."* Neither ever appeared.
- **2026-02-26:** `xmrwallet.net` registered (prepaid for 10 years, same IP as `.biz`). Third escape domain.
- **2026-02-26:** `xmrwallet.me` registered (prepaid for 10 years, same IP as `.cc`). Fourth escape domain.
- **2026-03-04:** NameSilo, LLC (IANA #1479) (registrar for `.com`) responds to abuse reports: *"The registrant is the victim"* — siding with the scam operator.
- **2026-03-08:** `xmrwallet.net` DNS goes **DEAD**.
- **2026-03-12:** @Phish_Destroy confronts NameSilo, LLC (IANA #1479) publicly: *"9 reports is no joke."*
- **2026-03-13:** NameSilo, LLC (IANA #1479) publishes a statement containing four demonstrable lies.
- **2026-03-14:** @Phish_Destroy responds: *"New service from NameSilo, LLC (IANA #1479): helping scammers clear VT"* — documenting NameSilo's assistance in removing VirusTotal flags.
- **2026-03-16:** Full rebuttal thread published, dismantling each of NameSilo's four lies with evidence.
- **2026-03-18:** Case formally forwarded to ICANN Compliance and law enforcement.
- **2026-03 (late):** @Phish_Destroy account **permanently locked** on X (Twitter). No violation cited at time of lock.
- **2026-04-15:** X Support responds: *"no violation, restored"* — but the lock remains in place. Account still inaccessible.
- **Ongoing:** Bing search delisting of evidence pages, DDoS attacks against investigation infrastructure, coordinated mass-reporting of social media accounts and review posts.

---

## Scoreboard

| Domain | Status | Registration Wasted |
|--------|--------|---------------------|
| `xmrwallet.cc` | **SUSPENDED** (PDR) | 8 years prepaid |
| `xmrwallet.biz` | **SUSPENDED** (WebNic) | 5 years prepaid |
| `xmrwallet.net` | **DNS DEAD** | 10 years prepaid |
| `xmrwallet.me` | ACTIVE | Key-Systems — next target |
| `xmrwallet.com` | ACTIVE | NameSilo, LLC (IANA #1479) protecting operator |

**Escape domains neutralized: 3 of 4.**
**Years of prepaid registration wasted by the operator: 23 years.**

---

## How to Report XMRWallet

If you are a victim or have evidence, file reports with the following agencies and contacts:

- **FBI Internet Crime Complaint Center (IC3):** [https://ic3.gov](https://ic3.gov)
- **FTC Fraud Reporting:** [https://reportfraud.ftc.gov](https://reportfraud.ftc.gov)
- **ICANN Compliance (against NameSilo):** [https://icann.org/compliance](https://icann.org/compliance)
- **Key-Systems Abuse (xmrwallet.me registrar):** [abuse@key-systems.net](mailto:abuse@key-systems.net)
- **Direct victim intake — PhishDestroy:** [report@phishdestroy.io](mailto:report@phishdestroy.io)

If you have a GitHub account, you can also file an issue using the evidence template in this repository's `.github/ISSUE_TEMPLATE/` directory.

---

## Safe Alternatives to XMRWallet

Do not use web wallets for Monero. Use one of the following trusted, open-source options:

- **Monero Official Wallet:** [https://getmonero.org](https://getmonero.org) — the reference GUI and CLI wallets maintained by the Monero Project.
- **Cake Wallet:** [https://cakewallet.com](https://cakewallet.com) — open-source mobile wallet for Monero, Bitcoin, and Litecoin.
- **Feather Wallet:** [https://featherwallet.org](https://featherwallet.org) — lightweight, privacy-focused Monero desktop wallet.
- **Hardware wallets:** Ledger and Trezor both support Monero. Your keys never leave the device.

**The only wallet you can trust is one where you control the keys on your own device.**
