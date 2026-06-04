<!--
NameSilo, LLC (IANA #1479) — Registrar Abuse Investigation
Keywords: namesilo, xmrwallet, monero-drainer, crypto-scam, registrar-abuse, icann-compliance, phishdestroy
-->

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=26&pause=800&color=FF3333&center=true&vCenter=true&multiline=false&width=960&lines=NameSilo%2C+LLC+(IANA+%231479)+%E2%80%94+Registrar+Abuse+Investigation;5%2C269%2C357+Domains+Scanned.+87.3%25+Is+Junk.;183%2C419+Malicious+Domains+Behind+Their+Own+Privacy+Shield.;Filed+with+ICANN+%C2%B7+March+18%2C+2026." alt="PhishDestroy Investigation" />

<br/><br/>

[![Live Investigation](https://img.shields.io/badge/%F0%9F%94%B4%20LIVE-phishdestroy.eth.limo-FF3333?style=for-the-badge)](https://phishdestroy.eth.limo/)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Evidence_Portal-black?style=for-the-badge&logo=github)](https://phishdestroy.github.io/namesilo-evidence/)
[![ICANN Filed](https://img.shields.io/badge/ICANN-Compliance_Filed_Mar_18_2026-orange?style=for-the-badge)](https://www.icann.org/compliance)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-blue?style=for-the-badge)](LICENSE)

<br/>

![Domains](https://img.shields.io/badge/Domains_Scanned-5%2C269%2C357-red?style=flat-square&labelColor=111)
![Junk](https://img.shields.io/badge/Junk_Rate-87.3%25-critical?style=flat-square&labelColor=111)
![Phishing](https://img.shields.io/badge/Phishing_Domains-3%2C726-red?style=flat-square&labelColor=111)
![PG Malicious](https://img.shields.io/badge/PrivacyGuardian_Malicious-183%2C419-critical?style=flat-square&labelColor=111)
![Cluster](https://img.shields.io/badge/Server_Fingerprint_Cluster-328%2C230-red?style=flat-square&labelColor=111)
![Trustpilot Deleted](https://img.shields.io/badge/Trustpilot_Reviews_Deleted-129_in_4mo-critical?style=flat-square&labelColor=111)

</div>

---

## What This Is

**NameSilo, LLC (IANA #1479)** is a US-based ICANN-accredited domain registrar, publicly traded on the CSE (ticker: URL). This repository is the complete, SHA-256-verified evidence package documenting how they publicly defended a 10-year, $10–20M Monero wallet drainer, denied receiving over 20 abuse reports, and committed in writing to helping the operator erase his VirusTotal security record — then used their X Gold Checkmark live-support access to lock the research account that published the receipts.

**xmrwallet[.]com** has been running since ~2016. Every login silently sends the user's private view key to the operator's server. The site has never been compromised. The theft code *is* the product.

Three registrars (PDR, WebNic, NICENIC) suspended the domain on review. NameSilo, LLC (IANA #1479) published a press release for the operator. Their only response to this investigation: they quietly moved his domain to Namecheap.

> Full investigation site: **[phishdestroy.eth.limo](https://phishdestroy.eth.limo/)** — IPFS-hosted, ENS-resolved, censorship-resistant.
> Evidence portal: **[phishdestroy.github.io/namesilo-evidence](https://phishdestroy.github.io/namesilo-evidence/)**

---

## The Exhibit That Started It All

NameSilo's official corporate tweet, **March 13, 2026**, defending a confirmed crypto drainer. 11,300 public views. Permanently archived.

<div align="center">

![NameSilo official corporate tweet March 13 2026 — calling xmrwallet operator the victim, denying 20+ abuse reports, committing to scrub VirusTotal detections](evidence/03-namesilo-statement-mar13.png)

*NameSilo, LLC (IANA #1479) @namesilo — March 13, 2026. Four sentences. Four lies. [GhostArchive](https://ghostarchive.org/archive/CXXZ0)*

</div>

The operator's own email — sent to PhishDestroy on **February 16, 2026**, 25 days before this tweet — makes no mention of any hack. He defends the site as his own work.

<div align="center">

![Operator email February 16 2026 — defending xmrwallet as his own, no mention of compromise](evidence/01-operator-email-feb16.png)

*"There is no phishing going on with xmrwallet.com." — The operator, Feb 16. NameSilo invented the "compromise" story on Mar 13.*

</div>

X Support cleared our account in writing on April 15, 2026. The lock is still in place.

<div align="center">

<table><tr>
<td width="50%"><img src="evidence/06-x-support-no-violation.png" alt="X Support: no violation, restored"/></td>
<td width="50%"><img src="evidence/06-x-support-subject-restored.png" alt="X Support subject: account restored"/></td>
</tr></table>

*"No violation. Restored to full functionality." — X Support, April 15, 2026. Account still locked. Gold subscription still billed.*

</div>

---

## Investigation Scale

<div align="center">

| Metric | Value | Source |
|:-------|------:|:-------|
| Total NameSilo domains scanned | **5,269,357** | Complete zone file census |
| Domains with no legitimate use | **4,600,249 (87.3%)** | HTTP + content classification |
| Brand-phishing domains | **3,726** | Favicon fingerprint + content |
| Indonesian gambling cluster | **19,198** | MurmurHash3 favicon clustering |
| Single server fingerprint cluster | **328,230 domains** | SHA-256(Server+XPB+ETag) |
| CF-confirmed phishing on that cluster | **2,062** | Cloudflare threat feed |
| Malicious behind PrivacyGuardian | **183,419** | RDAP + 25 threat intelligence feeds |
| Hard-confirmed malicious (3+ sources) | **109,196** | Multi-source cross-validation |
| Brand impersonations (USPS, Google…) | **201** | Content + title analysis |
| Dead domains: NameSilo vs industry avg | **32.2% vs 14–21%** | 8-registrar, 130M domain comparison |
| Trustpilot reviews deleted (4 months) | **129 confirmed** | Wayback Machine vs. live scrape |
| xmrwallet victim losses (estimated) | **$10M–$20M** | On-chain + victim reports |
| Abuse reports submitted, ignored | **20+** (delivery-receipted) | Submission records |
| Other registrars that suspended | **3** (PDR, WebNic, NICENIC) | Suspension notices |

</div>

---

## Interactive Reports

<div align="center">

| Report | Description | Link |
|:-------|:------------|:-----|
| Zone Scan Report | Full investigation: charts, IOC breakdown, chain of custody | [namesilo-scan.html](https://phishdestroy.github.io/namesilo-evidence/namesilo-scan.html) |
| Favicon Cluster Analysis | 12 operator clusters via MurmurHash3 fingerprinting | [namesilo-clusters.html](https://phishdestroy.github.io/namesilo-evidence/namesilo-clusters.html) |
| IOC Domain List | 107,252 criminal domains — searchable, flags, favicons | [namesilo-domains.html](https://phishdestroy.github.io/namesilo-evidence/namesilo-domains.html) |
| PrivacyGuardian Shield | 183,419 malicious domains behind NameSilo's own WHOIS privacy | [namesilo-privacyguardian.html](https://phishdestroy.github.io/namesilo-evidence/namesilo-privacyguardian.html) |
| Review Manipulation & PR Newswire | 129 deleted reviews, bot network, same-day PR Newswire with scammer | [namesilo-reviews.html](https://phishdestroy.github.io/namesilo-evidence/namesilo-reviews.html) |
| Investigation Index | Main portal with links to all reports | [phishdestroy.github.io/namesilo-evidence](https://phishdestroy.github.io/namesilo-evidence/) |

</div>

> Raw scan data (JSONL/CSV, up to 499 MB) as gzip archives: [`pkg/raw_data/`](pkg/raw_data/)

---

## Methodology

Two-pass distributed scanner — AWS Lambda + GCP Cloud Run, 400 concurrent workers:

```
Phase 1 — AWS Lambda (400 concurrent)         2,503,213 domains  |  5s timeout
Phase 2 — GCP Cloud Run (20 × 400 async)        894,300 domains  |  rescan of missed

Merged: 3,397,413 domains with DNS → 1,129,114 active HTTP responses
```

```
HTTP response
  ├── Page-type classifier    active_content / parking / redirect / phishing / …
  ├── Favicon fingerprint     MurmurHash3 → operator clusters
  ├── Server fingerprint      SHA-256(Server + X-Powered-By + ETag) → 12-char hex
  ├── Parking detection       named service patterns
  └── Brand matching          domain + title + favicon hash → phishing label
```

PrivacyGuardian pipeline:

```
4,974,265 PG candidate domains
  → RDAP validation (rdap.namesilo.com)
    → 164,027 confirmed PG-protected
      → 25+ threat feeds cross-reference
        → 183,419 malicious  |  109,196 hard-confirmed (3+ sources)
```

---

## Timeline

```
2016          xmrwallet.com live. session_key silently exfiltrated 40+ times/session.

2023–2026     20+ delivery-receipted abuse reports → abuse@namesilo.com. No action.

Feb 16, 2026  Operator emails PhishDestroy: "There is no phishing." No hack claim.

Mar 12, 2026  PhishDestroy: "9 reports is no joke anymore."

Mar 13, 2026  NameSilo official tweet (11,300 views):
              ✗ "Domain was compromised a few months ago"
              ✗ "No abuse reports received prior to this"
              ✗ "The registrant is also the victim"
              ✗ "Working with registrant to remove website from VT reports"
              
              PDR, WebNic, NICENIC: suspended. NameSilo: published press release.

Mar 16, 2026  PhishDestroy posts operator emails publicly. Account locked same day.

Mar 18, 2026  Filed with ICANN Contractual Compliance.

Apr 15, 2026  X Support: "No violation. Account restored." Lock not lifted.

May 11, 2026  NameSilo legal threat tweet. Zero factual rebuttal.

May 2026      DMCA filed against this investigation. Keyword/geo suppression detected.
              Same-day PR Newswire releases: xmrwallet (Jan 21) + NameSilo (Jan 22).

Jun 2026      Zone scan complete: 5,269,357 domains, 87.3% junk.
              NameSilo's action: transferred scammer domain to Namecheap. Site live.
```

---

## Forensic Diagrams

<div align="center">

| | | |
|:-:|:-:|:-:|
| [![Money Flow](docs/assets/diagram-money-flow.png)](docs/assets/diagram-money-flow.png) | [![Timeline](docs/assets/diagram-timeline.png)](docs/assets/diagram-timeline.png) | [![Theft Mechanism](docs/assets/diagram-theft-mechanism.png)](docs/assets/diagram-theft-mechanism.png) |
| Money Flow | 10-Year Timeline | Theft Mechanism |
| [![Operator Network](docs/assets/diagram-operator-network.png)](docs/assets/diagram-operator-network.png) | [![Suppression](docs/assets/diagram-suppression.png)](docs/assets/diagram-suppression.png) | [![Domain Infrastructure](docs/assets/diagram-domain-infra.png)](docs/assets/diagram-domain-infra.png) |
| Operator Network | Suppression Campaign | Domain Infrastructure |

</div>

---

## NameSilo vs. The Facts

| NameSilo's Statement | Reality | Verdict |
|:---|:---|:---:|
| "Domain was compromised a few months ago." | Exfiltration code *is* the site — 8 PHP endpoints, `session_key` server-side capture, `raw_tx_and_hash.raw = 0`. Operator's Feb 16 email: no hack claim. | **FALSE** |
| "Prior to this, we received no abuse reports." | 20+ delivery-receipted reports, 2023–2026. Public tweet the day before: "9 reports is no joke anymore." | **FALSE** |
| "Extensive review… not involving registrant." | Operator contacted PhishDestroy first, defending the site as his own. NameSilo adopted a narrative the operator never advanced. | **FALSE** |
| "Working with registrant to remove from VT." | A registrar helping a confirmed fraud operator erase consumer-protection security alerts. Published on their own verified account. | **DOCUMENTED** |

> [`THE-LIES.md`](THE-LIES.md) — full line-by-line rebuttal &nbsp;·&nbsp; [`CONNECTION.md`](CONNECTION.md) — operator evidence chain

---

## Repository

```
namesilo-evidence/
├── PROOFS.md                               ← master evidence index
├── INVESTIGATION_DOSSIER_EN.md             ← complete dossier (613 lines)
├── ARTICLE_FULL.md                         ← full investigative article
├── CONNECTION.md                           ← NameSilo ↔ operator evidence chain
├── THE-LIES.md                             ← NameSilo Mar 13 statement, rebutted
├── NAMESILO-RESPONSE-MAY2026.md            ← May 11 legal threat, documented
├── NAMESILO_DOMAIN_ANOMALY_REPORT.md       ← 8-registrar, 130M domain analysis
├── PRESSURE.md                             ← DMCA / DDoS / account suppression log
├── SCAM_TECHNICAL.md                       ← xmrwallet PHP endpoint breakdown
├── OPERATOR_PROFILE.md                     ← identity, domains, IPs, IOCs
├── VICTIMS.md                              ← documented victims, 2016–2026
├── EVIDENCE_HASHES.txt                     ← SHA-256 of all evidence files
│
├── evidence/                               ← 16 SHA-256-verified screenshots
│
├── docs/                                   ← phishdestroy.github.io/namesilo-evidence/
│   ├── namesilo-scan.html                  ← zone scan report
│   ├── namesilo-clusters.html              ← favicon clusters
│   ├── namesilo-domains.html               ← 107k IOCs (searchable)
│   ├── namesilo-privacyguardian.html       ← 183k malicious PG domains
│   ├── namesilo-reviews.html               ← Trustpilot deletion + PR Newswire
│   └── assets/                             ← 11 forensic diagrams
│
├── pkg/                                    ← zone scan evidence package
│   ├── evidence/                           ← JSON evidence + manifest
│   └── raw_data/                           ← gzip scan datasets (JSONL/CSV)
│
└── xmrwallet-evidence/                     ← xmrwallet-specific package
```

---

## Evidence Verification

```bash
git clone https://github.com/phishdestroy/namesilo-evidence.git
cd namesilo-evidence/evidence
sha256sum -c ../EVIDENCE_HASHES.txt
# All files: OK
```

Full manifest: [`pkg/evidence/evidence_manifest.json`](pkg/evidence/evidence_manifest.json)

---

## Suppression Log

| Date | Incident | Status |
|:-----|:---------|:-------|
| Mar 13, 2026 | NameSilo four-lie defense published | [Archived](https://ghostarchive.org/archive/CXXZ0) |
| Mar 2026 | @Phish_Destroy locked via X Gold Checkmark live support | **Still locked** |
| Apr 15, 2026 | X automation: "no violation, restored" | Lock not lifted |
| May 11, 2026 | NameSilo legal threat tweet. Zero rebuttal. | [Documented](NAMESILO-RESPONSE-MAY2026.md) |
| May 2026 | DMCA against this investigation | Not delisted |
| May 2026 | Keyword/geo search suppression | Under documentation |
| Jun 2026 | Scammer domain transferred to Namecheap | Site remains live |

> Full documentation: [`PRESSURE.md`](PRESSURE.md)

---

## For Victims, Regulators & Press

**Victims** — attach this repo URL to:
[IC3 (FBI)](https://www.ic3.gov) · [FTC](https://reportfraud.ftc.gov) · [ICANN Compliance](https://www.icann.org/compliance) · police reports · civil claims

[`LICENSE`](LICENSE) grants explicit written permission to use this evidence in any legal or regulatory proceeding.

Contact: **[report@phishdestroy.io](mailto:report@phishdestroy.io)**

**Regulators / journalists** — raw materials (email headers, PHP captures, historical abuse-report receipts) on request: **[abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)**

---

## Mirrors

| Platform | URL |
|:---------|:----|
| **Live investigation site** | [phishdestroy.eth.limo](https://phishdestroy.eth.limo/) — IPFS via ENS |
| **GitHub Pages** | [phishdestroy.github.io/namesilo-evidence](https://phishdestroy.github.io/namesilo-evidence/) |
| **Arweave (permanent)** | [arweave.net/LUuditolJS…](https://arweave.net/LUuditolJS-Y15IezfpzRI36sxhd1CIvFNOf_eAG2AU) |
| Codeberg | [codeberg.org/phishdestroy/namesilo-evidence](https://codeberg.org/phishdestroy/namesilo-evidence) |
| Medium | [phishdestroy.medium.com](https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e) |
| GhostArchive | [ghostarchive.org/archive/CXXZ0](https://ghostarchive.org/archive/CXXZ0) |
| Wayback (repo) | [snapshot](https://web.archive.org/web/20260508165630/https://github.com/phishdestroy/namesilo-evidence) |
| IPFS CID | `bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq` |

---

## All Exhibits

### Exhibit A — NameSilo's statement, verbatim

March 13, 2026. Official corporate account. 11,300 views. [Archived](https://ghostarchive.org/archive/CXXZ0).

<div align="center">

![NameSilo official tweet March 13 2026 — defending xmrwallet operator, denying abuse reports, offering VT delisting](evidence/03-namesilo-statement-mar13.png)

*NameSilo, LLC (IANA #1479) @namesilo — March 13, 2026.*

</div>

<div align="center">

![PhishDestroy rebuttal — NameSilo is acting as press secretary for a Monero theft operation](evidence/04-tweet-press-secretary.png)

*@Phish_Destroy, March 16, 2026. Account locked shortly after.*

</div>

---

### Exhibit B — The operator's own email

February 16, 2026. Operator defends the site as his own. No hack claim. Published 25 days before NameSilo's "compromise" narrative.

<div align="center">

![Operator email February 16 2026 — no phishing claim, no hack claim](evidence/01-operator-email-feb16.png)

</div>

<div align="center">

![PhishDestroy reply February 16 — technical breakdown and escalation notice](evidence/01-phishdestroy-reply-feb16.png)

</div>

---

### Exhibit C — X cleared us. Lock stayed.

<div align="center">

<table><tr>
<td width="50%"><img src="evidence/06-x-support-no-violation.png" alt="X Support: no violation found"/></td>
<td width="50%"><img src="evidence/06-x-support-subject-restored.png" alt="X Support: account restored"/></td>
</tr></table>

*April 15, 2026. Automated review: no violation, restored. Human override applied. Account still locked.*

</div>

---

### Exhibit D — The question never answered

<div align="center">

![Who is this operator to you?](evidence/04-tweet-honest-question.png)

*"Who is this operator to you?" — 72 likes, 7.9K views. Never answered. Account locked.*

</div>

---

### Exhibit E — GhostArchive: the record they cannot delete

<div align="center">

![GhostArchive — March 12 confrontation tweet](evidence/12-ghostarchive-namesilo-tweet-top.png)

</div>

<div align="center">

![GhostArchive — NameSilo full official reply, 11.3K views](evidence/13-ghostarchive-namesilo-tweet-full.png)

</div>

---

### Exhibit F — The thread they locked (March 14, 2026)

<div align="center">

![March 14 thread — the hack story is a lie](evidence/14-tweet-thread-mar14-lies-exposed.png)

</div>

<div align="center">

![March 14 thread — abuse department disgrace](evidence/15-tweet-thread-mar14-abuse-dept-disgrace.png)

</div>

<div align="center">

![March 14 — new service from NameSilo: helping scammers get VT bans removed](evidence/16-tweet-mar14-vt-delisting-service.png)

</div>

---

<div align="center">

**PhishDestroy Research**

[phishdestroy.eth.limo](https://phishdestroy.eth.limo/) &nbsp;·&nbsp; [phishdestroy.github.io/namesilo-evidence](https://phishdestroy.github.io/namesilo-evidence/) &nbsp;·&nbsp; [abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)

*TLP:CLEAR &nbsp;·&nbsp; CC-BY-4.0 &nbsp;·&nbsp; Evidence chain maintained from first report, 2023, to present.*

</div>
