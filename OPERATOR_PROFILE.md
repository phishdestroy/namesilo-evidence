# Operator Profile: xmrwallet.com

> **Classification:** Investigative Intelligence Dossier
> **Subject:** Operator of xmrwallet.com — an active Monero wallet-draining service
> **Compiled from:** [PhishDestroy.io](https://phishdestroy.io) investigation, the [DO-NOT-USE-xmrwallet-com](https://github.com/phishdestroy/DO-NOT-USE-xmrwallet-com) GitHub repository, direct email correspondence with the operator, public WHOIS/DNS records, archived victim reports, and on-chain transaction analysis.
> **Period of investigation:** 2018 – May 2026
> **Status:** ACTIVE THREAT — xmrwallet.com remains operational as of this writing.

---

## 1. Identity

| Field | Value |
|---|---|
| **Full Name** | Nathalie Roy |
| **GitHub** | [nathroy](https://github.com/nathroy) (User ID: 39167759) |
| **Email (operational)** | admin@xmrwallet.com |
| **Email (personal)** | royn5094@protonmail.com |
| **Reddit** | u/WiseSolution — BANNED from r/Monero (2018, self-promotion of xmrwallet.com) |
| **Twitter/X** | [@xmrwalletcom](https://twitter.com/xmrwalletcom) |

---

## 2. Domain Infrastructure

The operator registered five domains across four different registrars — a deliberate strategy to slow coordinated takedown efforts. All domains share common mail and nameserver infrastructure, confirming single-operator control.

### 2.1 Domain Portfolio

| Domain | Registrar | Prepaid Period | IP Address | AS | Status |
|---|---|---|---|---|---|
| **xmrwallet.com** | NameSilo | Paid until 2031 | 186.2.165.49 | AS59692 (IQWeb FZ-LLC) | **ACTIVE** — NameSilo protecting |
| **xmrwallet.cc** | PublicDomainRegistry | 8 years | 185.129.100.248 | AS57724 (DDoS-Guard) | **SUSPENDED** |
| **xmrwallet.biz** | WebNic | 5 years | 190.115.31.40 | AS59692 (IQWeb FZ-LLC) | **SUSPENDED** |
| **xmrwallet.net** | NICENIC | 10 years | 190.115.31.40 | AS59692 (IQWeb FZ-LLC) | **DNS DEAD** |
| **xmrwallet.me** | Key-Systems GmbH | 10 years | 185.129.100.248 | AS57724 (DDoS-Guard) | **ACTIVE** |

**Total prepaid registration across portfolio:** 23+ years of advance payments, now largely wasted — 3 of 4 escape domains neutralized.

### 2.2 Tor Hidden Service

```
xmrtor3fsapuu6y26za7vpzox4vpaj6ny5viq2arbmozm7kg6jitnlid.onion
```
Status: **ACTIVE**

### 2.3 Shared Infrastructure Indicators

| Service | Configuration |
|---|---|
| **MX Records** | mx1.privateemail.com, mx2.privateemail.com (all domains) |
| **Nameservers** | ns1.ddos-guard.net, ns2.ddos-guard.net (all domains) |
| **Google Analytics** | UA-116766241-1 (all clearnet domains) |
| **DDoS-Guard Cookies** | `__ddg8_`, `__ddg9_`, `__ddg10_`, `__ddg1_` |

The use of identical MX, NS, analytics tracking IDs, and DDoS-Guard cookie prefixes across all five domains constitutes definitive proof of unified operator control.

---

## 3. Hosting

Bulletproof hosting in **Belize**, fronted by Russian DDoS-Guard (AS57724). Estimated cost: **$550+/month**. The operator pays premium rates specifically to resist law enforcement cooperation and abuse takedowns. IQWeb FZ-LLC (AS59692, UAE-registered) provides additional IP space.

This is not economy hosting. This is infrastructure selected and paid for specifically because it will not cooperate with abuse reports.

---

## 4. Operator Communications (Verbatim)

Direct email correspondence with the operator reveals a pattern of lies followed by immediate contradiction, then legal threats that never materialize.

### February 16, 2026
> "We don't store seeds or keys, everything is done locally"

**This is a lie.** Technical analysis proves the `session_key` parameter transmits the user's viewkey to the server 40+ times per session. The wallet does not operate "locally" — it exfiltrates private key material on every interaction.

### February 17, 2026
> "This is the data we need"

Sent **within 24 hours** of the February 16 denial, directly contradicting the claim that "everything is done locally." The operator admitted the server requires user key data — the exact data he denied collecting one day earlier.

### February 17, 2026
> "Feel free to subpoena the domain registrar"

This statement was sent **before any abuse report was filed**. The operator expressed confidence that NameSilo would protect the domain — a confidence that proved justified. NameSilo has refused to act on the primary .com domain to this day.

### February 23, 2026
> "I've hired a lawyer and a private investigator"

Sent the same day two domains (.cc and .biz) were suspended. No lawyer ever appeared. No legal action was ever filed. No private investigator ever made contact. This was a bluff designed to intimidate researchers into silence.

---

## 5. Evidence Destruction

### GitHub Issue Deletion — February 23, 2026

On the same day domains .cc and .biz were suspended, the operator deleted GitHub Issues **#35** and **#36** from the xmrwallet repository. These issues contained:

- Full technical analysis of the viewkey exfiltration mechanism
- Victim reports with transaction IDs
- Community discussion threads with corroborating evidence

The issues were not *closed* — they were **deleted**. Closing an issue preserves the discussion. Deletion destroys it. This is not moderation; it is evidence destruction.

All content was archived prior to deletion.

### Systematic Suppression Campaign

| Platform | Action Taken |
|---|---|
| **GitHub** | Deleted Issues #35, #36. Filed false DMCA takedowns against repositories documenting the scam. Targeted researcher accounts. 21+ issues deleted over 8 years. |
| **Trustpilot** | Mass-reported negative reviews until removed by automated moderation. |
| **BitcoinTalk** | Coordinated reporting against warning threads to trigger removal. |
| **YouTube** | Reported technical analysis videos demonstrating the theft mechanism. |
| **Twitter/X** | Deployed puppet accounts to mass-report researchers. PhishDestroy's account was locked after rebutting NameSilo publicly. |
| **Search Engines** | Published **50+ paid SEO articles** to bury victim complaints and negative coverage in search results. |

The operator has never, in eight years, produced a single technical rebuttal to the theft allegations. The response has been exclusively suppression, deletion, and intimidation.

---

## 6. Documented Victims

| Amount Stolen | Source | Victim Statement |
|---|---|---|
| **590 XMR (~$177,000)** | Sitejabber | "deposited 590 monero — 2 days gone" |
| **17.44 XMR** | Trustpilot | TxID and TX Key documented and verified |
| **20 XMR** | Sitejabber | "put 20 xmr — next day 0 xmr" |
| **~$200** | Trustpilot | "stole $200, leaving me high and dry" |
| **Unknown** | Trustpilot | "transferred to some other wallet instead of mine" |
| **Unknown** | Trustpilot | "cannot verify transaction using private viewing key" |

### Scale Estimate

The service has operated for **8 years** (2018–2026). Given traffic analysis, SEO investment, and the number of suppressed victim reports:

- **Conservative estimate:** 10,000–50,000+ wallets compromised
- **Estimated total stolen:** 5,000–50,000+ XMR ($1.5M–$15M+ at historical prices)

The operator's standard deflection when victims report missing funds: claim it is a "sync problem." By the time a user sees this message, the funds have already been swept.

---

## 7. GitHub Commit Gap

The xmrwallet GitHub repository shows a **5.3-year gap** with zero public commits:

- Last commit before gap: **2018-11-06**
- First commit after gap: **2024-03-15**

During this 5.3-year period, the production website continued to evolve, with theft infrastructure being developed and refined outside of the public repository. The public repo served as a facade of legitimacy while the actual operational code — including the viewkey exfiltration mechanism — was maintained privately.

---

## 8. Google Trackers in a "Privacy Wallet"

A wallet marketed as a privacy-preserving Monero tool loads the following tracking scripts on every pageview:

- **Google Tag Manager (GTM)**
- **Google Analytics (UA)** — UA-116766241-1
- **Google Analytics 4 (GA4)**
- **DoubleClick Ad Tracker**

Every user who visits xmrwallet.com has their browsing session fingerprinted by Google's advertising infrastructure. This directly contradicts all privacy claims and demonstrates the operator's fundamental indifference to user privacy — consistent with a service designed to steal, not protect.

---

## 9. Second Developer

In **March 2026**, a custom CAPTCHA system was deployed on xmrwallet.com featuring proof-of-work computation, a slider challenge, and mouse trajectory tracking. Code analysis revealed characteristics inconsistent with the original developer:

- Properly commented JavaScript with numbered steps
- `FIX:` annotations indicating structured development process
- Clean code organization

The original theft code contains **zero comments**. This CAPTCHA was written by a second developer — someone brought in specifically to harden the site against automated analysis after the PhishDestroy investigation went public.

The CAPTCHA was defeated within hours of deployment, achieving a **100% bypass rate**.

---

## 10. Cover-Up Pattern Summary

Across 8 years of operation, the following pattern has repeated without variation:

1. Victim reports funds missing
2. Operator claims "sync problem" (funds already stolen)
3. Victim escalates publicly
4. Operator deletes the report
5. If report persists, operator files false DMCA / mass-reports the platform
6. Operator publishes paid SEO content to bury remaining traces
7. No technical rebuttal is ever produced

**21+ GitHub issues deleted. Zero technical rebuttals. Ever.**

---

## 11. What the Operator Has Never Produced

Despite 8 years of allegations and multiple detailed technical analyses, the operator has never provided:

- A network capture proving the user's viewkey is NOT sent to the server
- Code proving signed transactions ARE broadcast to the Monero network (the `raw` parameter equals `0`, meaning transactions are sent to the operator's server, not the blockchain)
- An explanation for `session_key` containing `base64(viewkey)`
- An explanation for backdoor session ID `8de50123dab32`
- An explanation for the `swept` transaction type (this type does not exist in the Monero protocol)
- Any technical counter-argument whatsoever

**Nothing. Ever. In eight years.**

---

## 12. Indicators of Compromise (IOC)

For security vendors, threat intelligence platforms, and browser/DNS blocklist operators.

### Domains (Block)
```
xmrwallet.com
xmrwallet.cc
xmrwallet.biz
xmrwallet.net
xmrwallet.me
```

### Tor Hidden Service (Block)
```
xmrtor3fsapuu6y26za7vpzox4vpaj6ny5viq2arbmozm7kg6jitnlid.onion
```

### IP Addresses (Block)
```
186.2.165.49    (AS59692 IQWeb FZ-LLC)
185.129.100.248 (AS57724 DDoS-Guard)
190.115.31.40   (AS59692 IQWeb FZ-LLC)
```

### Autonomous Systems
```
AS59692  IQWeb FZ-LLC (UAE — bulletproof hosting)
AS57724  DDoS-Guard Ltd (Russia — DDoS protection / CDN)
```

### Email Addresses
```
admin@xmrwallet.com
royn5094@protonmail.com
```

### Google Analytics Tracking ID
```
UA-116766241-1
```

### DDoS-Guard Cookie Identifiers
```
__ddg8_
__ddg9_
__ddg10_
__ddg1_
```

### Mail Infrastructure
```
mx1.privateemail.com
mx2.privateemail.com
```

### DNS Infrastructure
```
ns1.ddos-guard.net
ns2.ddos-guard.net
```

### Backdoor Session Identifier
```
8de50123dab32
```

### GitHub Account
```
https://github.com/nathroy (ID: 39167759)
```

### Social Media
```
Reddit:    u/WiseSolution (banned from r/Monero)
Twitter/X: @xmrwalletcom
```

---

## 13. Classification & Recommended Actions

| Entity | Recommended Action |
|---|---|
| **Browser vendors** (Google Safe Browsing, Microsoft SmartScreen, Firefox/Mozilla) | Add all domains and Tor address to phishing/scam blocklists |
| **DNS providers** (Cloudflare 1.1.1.1, Google 8.8.8.8, Quad9) | Block resolution for all five domains |
| **Cryptocurrency exchanges** | Flag and trace any deposits originating from xmrwallet-associated addresses |
| **ICANN** | Investigate NameSilo's refusal to act on documented phishing/fraud domain |
| **NameSilo (registrar)** | Suspend xmrwallet.com — the last active clearnet domain |
| **DDoS-Guard** | Terminate hosting services for documented fraud infrastructure |
| **Law enforcement** | Subpoena NameSilo, Namecheap (PrivateEmail), and DDoS-Guard for subscriber records |

---

*This document is part of the PhishDestroy public evidence archive. For the full technical analysis, see [XMRWALLET_TECHNICAL.md](XMRWALLET_TECHNICAL.md). For the complete evidence index with SHA-256 hashes, see [EVIDENCE_INDEX.md](EVIDENCE_INDEX.md). For the master proof dossier with all verbatim communications, see [PROOFS.md](PROOFS.md).*

*All claims in this document are supported by archived evidence. Nothing has been fabricated. Nothing has been exaggerated. The operator has had eight years to produce a technical rebuttal. He has produced nothing.*
