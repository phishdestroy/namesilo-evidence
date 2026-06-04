<!--
NameSilo, LLC (IANA #1479) / xmrwallet — public evidence repository
Canonical: https://phishdestroy.io/namesilo-evidence
SEO topics: namesilo, xmrwallet, monero-drainer, crypto-scam, registrar-abuse, icann-compliance, phishdestroy
-->

<div align="center">

# NameSilo, LLC (IANA #1479) — Registrar Abuse Investigation

### Public evidence repository · Filed with ICANN Contractual Compliance, March 18, 2026

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-blue.svg)](LICENSE)
[![Evidence: SHA-256 verified](https://img.shields.io/badge/evidence-SHA--256_verified-green.svg)](EVIDENCE_HASHES.txt)
[![Mirror: GitHub Pages](https://img.shields.io/badge/mirror-GitHub_Pages-black.svg)](docs/)
[![Canonical: phishdestroy.io](https://img.shields.io/badge/canonical-phishdestroy.io-red.svg)](https://phishdestroy.io)
[![Domains scanned](https://img.shields.io/badge/domains_scanned-5%2C269%2C357-red.svg)](https://phishdestroy.github.io/namesilo-evidence/namesilo-scan.html)
[![Junk rate](https://img.shields.io/badge/junk_rate-87.3%25-critical.svg)](https://phishdestroy.github.io/namesilo-evidence/namesilo-scan.html)

</div>

---

## Key Findings

| Finding | Value | Source |
|---------|-------|--------|
| NameSilo domains — complete zone census | **5,269,357** | Zone file, June 2026 |
| Domains classified as junk/abuse | **87.3%** | Full zone scan |
| Brand-phishing domains | **3,726** | Favicon + content analysis |
| Indonesian gambling networks | **24,349** heuristic · **19,198** favicon-confirmed | Cluster analysis |
| Single server fingerprint cluster | **328,230** domains | SHA-256 server fingerprint |
| Cloudflare-confirmed phishing on that cluster | **2,062** | CF threat feed |
| Malicious domains behind PrivacyGuardian (NameSilo's own WHOIS privacy) | **183,419** | 25+ threat feeds, RDAP-validated |
| Hard-confirmed malicious PG-protected domains | **109,196** | Multi-source verification |
| Dead domains: NameSilo vs industry average | **32.2%** vs **14–21%** | 8-registrar comparison |
| xmrwallet.com — estimated funds drained | **$10M–$20M** | On-chain analysis, victim reports |
| xmrwallet.com — years of operation | **~10 years** (2016–2026) | Domain history, archived content |
| Abuse reports submitted to NameSilo — ignored | **20+** delivery-receipted | Email records |
| Other registrars that suspended on sight | **3** (PDR, WebNic, NICENIC) | Suspension notices |

---

## What Happened

On **March 13, 2026**, NameSilo, LLC (IANA #1479) — a US-based ICANN-accredited registrar — published an official corporate statement on Twitter/X defending `xmrwallet[.]com`, a confirmed Monero wallet drainer that had been operating for approximately 10 years.

In that statement NameSilo: (1) claimed the domain "was compromised" — a narrative the operator himself never advanced; (2) denied receiving any prior abuse reports — contradicted by 20+ delivery-receipted submissions; (3) committed **in writing** to helping the operator remove the domain from VirusTotal detection lists; (4) called the operator "the victim."

Three other registrars (PDR, WebNic, NICENIC) reviewed identical evidence and suspended the domain within days. NameSilo published a defense.

On **March 16, 2026**, our research account on X/Twitter was locked via NameSilo's paid Gold Checkmark live-support channel — hours after we published the receipts. X's automated review confirmed no violation and restored the account; a human agent overrode the restoration. The account remains locked.

On **March 18, 2026**, this case was filed with **ICANN Contractual Compliance**.

> Evidence chain: [CONNECTION.md](CONNECTION.md) · Lies rebutted: [THE-LIES.md](THE-LIES.md) · Suppression log: [PRESSURE.md](PRESSURE.md)

**[Master proof index →](PROOFS.md)** · **[Full article →](ARTICLE_FULL.md)** · **[The Connection →](CONNECTION.md)** · **[The Lies →](THE-LIES.md)** · **[Pressure Campaign →](PRESSURE.md)** · **[Technical breakdown →](SCAM_TECHNICAL.md)** · **[Operator dossier →](OPERATOR_PROFILE.md)** · **[Victims →](VICTIMS.md)** · **[Full Dossier →](INVESTIGATION_DOSSIER_EN.md)**</div>

---

## 📂 Repository Index

| Document | Description |
|----------|-------------|
| [PROOFS.md](PROOFS.md) | Master evidence index — all exhibits with SHA-256 hashes |
| [ARTICLE_FULL.md](ARTICLE_FULL.md) | Full investigative article |
| [INVESTIGATION_DOSSIER_EN.md](INVESTIGATION_DOSSIER_EN.md) | Complete investigation dossier — victims, timeline, technical proof |
| [CONNECTION.md](CONNECTION.md) | How NameSilo is connected to the xmrwallet operator |
| [THE-LIES.md](THE-LIES.md) | Point-by-point rebuttal of NameSilo's March 13 public statement |
| [NAMESILO-RESPONSE-MAY2026.md](NAMESILO-RESPONSE-MAY2026.md) | NameSilo's May 11 legal threat tweet — documented and archived |
| [NAMESILO_DOMAIN_ANOMALY_REPORT.md](NAMESILO_DOMAIN_ANOMALY_REPORT.md) | Statistical analysis: NameSilo is an outlier across 8 registrars |
| [PRESSURE.md](PRESSURE.md) | Suppression campaign — Twitter lock, DMCA abuse, Trustpilot removals |
| [SCAM_TECHNICAL.md](SCAM_TECHNICAL.md) | Technical breakdown of the xmrwallet drainer mechanism |
| [OPERATOR_PROFILE.md](OPERATOR_PROFILE.md) | Operator dossier — 10-year history |
| [VICTIMS.md](VICTIMS.md) | Victim accounts and confirmed losses |
| [SOURCES.md](SOURCES.md) | All primary sources |

---

## 📊 Zone Scan — All 5,269,357 NameSilo Domains

We obtained and processed NameSilo's **complete zone file** — every active domain, without sampling.  
**87.3% is junk.** 3,726 brand-phishing domains. 24,349 Indonesian gambling domains. 328,230 domains sharing one server fingerprint.

| Report | Description |
|--------|-------------|
| **[Full Investigation Report →](https://phishdestroy.github.io/namesilo-evidence/namesilo-scan.html)** | Visual report with charts, methodology, IOC breakdown |
| **[Favicon Cluster Analysis →](https://phishdestroy.github.io/namesilo-evidence/namesilo-clusters.html)** | 12 operator clusters identified via MurmurHash3 fingerprinting |
| **[107,252 IOC Domains →](https://phishdestroy.github.io/namesilo-evidence/namesilo-domains.html)** | Full searchable list of criminal/abuse domains |
| **[Evidence Manifest →](docs/evidence/evidence_manifest.json)** | SHA-256 integrity anchors for all data files |
| **[Artifacts Index →](pkg/ARTIFACTS.md)** | Complete list of scan datasets and methodology |

> Raw scan data (JSONL/CSV, up to 499MB) available in [`pkg/raw_data/`](pkg/raw_data/) as gzip archives.

| Report | Description |
|--------|-------------|
| **[PrivacyGuardian Shield →](https://phishdestroy.github.io/namesilo-evidence/namesilo-privacyguardian.html)** | 183,419 malicious domains behind NameSilo's own WHOIS privacy service |

---

## 🖼️ Evidence Diagrams

Visual forensic diagrams available in [`docs/assets/`](docs/assets/):

| Diagram | Description |
|---------|-------------|
| [Money Flow](docs/assets/diagram-money-flow.png) | How funds move through the xmrwallet operation |
| [Operator Network](docs/assets/diagram-operator-network.png) | Infrastructure and actor connections |
| [Timeline](docs/assets/diagram-timeline.png) | 10-year operation timeline |
| [Theft Mechanism](docs/assets/diagram-theft-mechanism.png) | Technical theft flow — private view key exfiltration |
| [Suppression Campaign](docs/assets/diagram-suppression.png) | Platform abuse and evidence erasure tactics |
| [Domain Infrastructure](docs/assets/diagram-domain-infra.png) | Domain registration and hosting patterns |



---


### Latest Developments

- **May 11, 2026** — NameSilo published a second public statement threatening legal action against investigators. No factual rebuttal was provided. Full documentation: [NAMESILO-RESPONSE-MAY2026.md](NAMESILO-RESPONSE-MAY2026.md)
- **June 2026** — Complete zone scan of all 5,269,357 NameSilo domains completed. 87.3% classified as junk or abuse. Full dataset and methodology: [Zone Scan Report](https://phishdestroy.github.io/namesilo-evidence/namesilo-scan.html)
- **June 2026** — PrivacyGuardian investigation completed: 183,419 malicious domains confirmed behind NameSilo's own WHOIS privacy service. [PrivacyGuardian Shield](https://phishdestroy.github.io/namesilo-evidence/namesilo-privacyguardian.html)
- **Ongoing** — xmrwallet.com domain transferred from NameSilo to Namecheap. The site remains operational. Investigation continues.
---

## What this repository is

This is the immutable, court-usable case file for what NameSilo, LLC (IANA #1479) did when caught defending a Monero theft operation that has been live for roughly **ten years** and stolen an estimated **$10M-$20M** in user funds.

NameSilo, LLC (IANA #1479) did not ignore our reports — that would be ordinary registrar negligence. NameSilo, LLC (IANA #1479) went **publicly on the record** to call the operator "the victim," to deny ever receiving any of our 20+ delivery-receipted abuse reports, and to commit — in writing, on Twitter — to **helping the operator scrub his security detections from VirusTotal**.

When we proved every sentence of that statement was false, the takedown started.

> **Our research account was locked. Our domain has been targeted with Bing delisting attempts. They are still lying. They are still trying to erase this story.**
>
> So this repository exists. Mirrored. Hashed. Permanently archived. Not deletable.

---

## Exhibit A — NameSilo's lie, in their own words

This is NameSilo's official corporate tweet of **March 13, 2026** — published under our investigation thread, defending a confirmed $20M crypto drainer. Four sentences. Four lies. Permanently archived: [ghostarchive.org/archive/CXXZ0](https://ghostarchive.org/archive/CXXZ0)

<div align="center">

![NameSilo's official corporate tweet of March 13 2026 — calling the xmrwallet operator the victim, denying 20+ abuse reports, and committing to help scrub VirusTotal detections](evidence/03-namesilo-statement-mar13.png)

*NameSilo, LLC (IANA #1479) (@namesilo), replying to @Phish_Destroy — March 13, 2026. 11K views. They chose to put this in public. It stays in public.*

</div>

We confronted them **the day before** this tweet: *"9 reports is no joke anymore."* Their response was not to act on the reports — it was to publicly defend the scammer. Two days later, we called it what it was:

<div align="center">

![PhishDestroy rebuttal thread — NameSilo, LLC (IANA #1479) is acting as press secretary for a 2M+ Monero theft operation. 6 security vendors flag it. 3 registrars suspended it.](evidence/04-tweet-press-secretary.png)

*@Phish_Destroy, March 16, 2026 — "NameSilo, LLC (IANA #1479) is acting as press secretary for a $2M+ Monero theft operation." These tweets are now invisible because the account was locked.*

</div>

---

## Exhibit B — The operator's own email, proving NameSilo, LLC (IANA #1479) lied

The operator wrote to us **first** — February 16, 2026, from `royn5094@protonmail.com`. He defended the site as his own work. He never claimed a hack. This email alone destroys NameSilo's "domain was compromised" narrative.

<div align="center">

![Email from the xmrwallet operator nathroy, February 16 2026 — defending the site, claiming no phishing, asking PhishDestroy to remove the report. He never claims a hack.](evidence/01-operator-email-feb16.png)

*The operator, in his own words: "There is no phishing going on with xmrwallet.com." He never claimed a hack. NameSilo, LLC (IANA #1479) invented the "compromise" story 25 days later.*

</div>

We replied the same day with a complete technical breakdown — 8 PHP endpoints, `session_key` exfiltration, `raw_tx_and_hash.raw = 0` — and an explicit warning:

<div align="center">

![PhishDestroy technical reply to the operator, February 16 2026 — documenting session_key viewkey exfiltration, production-only parameters, and the warning: What happens next depends entirely on how you choose to proceed.](evidence/01-phishdestroy-reply-feb16.png)

*"What happens next depends entirely on how you choose to proceed." — PhishDestroy, Feb 16. He chose to keep lying. His registrar chose to help.*

</div>

---

## Exhibit C — They silenced us. X cleared us. The lock stayed.

After we posted the receipts publicly and escalated to ICANN, our account was permanently locked. X's own automation reviewed the appeal and wrote back **in writing**:

<div align="center">

<table><tr>
<td width="50%">

![X Support email, April 15 2026: Our automated systems have determined there was no violation and have restored your account to full functionality.](evidence/06-x-support-no-violation.png)

</td>
<td width="50%">

![X Support email subject line: Your account has been restored, April 15 2026](evidence/06-x-support-subject-restored.png)

</td>
</tr></table>

*X Support, April 15, 2026: "No violation. Restored to full functionality." The account is **still locked.** The Gold subscription is **still being billed.** A human agent at X — accessible via NameSilo's paid Gold Checkmark support channel — overrode the machine.*

</div>

**Concierge censorship that you can buy.** Full breakdown: [`PRESSURE.md`](PRESSURE.md)

---

## Exhibit D — The question they never answered

<div align="center">

![PhishDestroy tweet: Honest question for NameSilo, LLC (IANA #1479) — Who is this operator to you? Employee? Contractor? Friend of support staff? Relative? Because he told us subpoena the registrar like a man who already had your answer.](evidence/04-tweet-honest-question.png)

*"Who is this operator to you?" — @Phish_Destroy, March 16. 72 likes, 7.9K views. Never answered. Then our account was locked.*

</div>

---

## Exhibit E — The GhostArchive receipts (they can't delete these)

These are from the [GhostArchive snapshot](https://ghostarchive.org/archive/CXXZ0) taken **before** they started deleting. The full tweet thread, archived March 16, 2026. NameSilo's official reply is visible. Our responses are visible. The timestamps are visible. Everything they tried to make disappear is right here.

<div align="center">

![GhostArchive snapshot — @Phish_Destroy confronting @namesilo on March 12: 9 reports is no joke anymore. Stop letting this old man scam people. NiceNIC, WebNic, Key-Systems, PDR all banned his domains. NameSilo protects him. XMRWallet.com SCAM banner visible.](evidence/12-ghostarchive-namesilo-tweet-top.png)

*GhostArchive — our original tweet confronting NameSilo, March 12. "9 reports is no joke anymore. Stop letting this old man scam people." Below it: NameSilo's official reply with the four lies. Archived before they could touch it.*

</div>

<div align="center">

![GhostArchive snapshot — NameSilo's full official reply: Our Abuse team conducted an in-depth review... domain was compromised... no abuse reports received... working to get website delisted from VT reports. 8:08 PM March 12, 2026. 11.3K views.](evidence/13-ghostarchive-namesilo-tweet-full.png)

*The full NameSilo, LLC (IANA #1479) tweet — every word. "The registrant is also working to get the website delisted from VT reports." A registrar helping a scammer erase security warnings. They said this. Out loud. 11.3K people saw it.*

</div>

## Exhibit F — The thread they killed (archived copies)

These tweets were published on @Phish_Destroy on **March 14, 2026** — two days before the account was locked. They confronted NameSilo directly, called out the lies, and documented everything. NameSilo's response was not to answer — it was to get the account locked.

<div align="center">

![Tweet thread March 14 — I am not going to prove anything further to the registrar. Google exists, the public record exists. The hack story is a lie and the claim that there were no earlier reports is also a lie. Reports from PhishDestroy existed. Good luck to you and your Russian scammer.](evidence/14-tweet-thread-mar14-lies-exposed.png)

*@Phish_Destroy, March 14: "The 'hack' story is a lie, and the claim that there were no earlier reports is also a lie. Reports from PhishDestroy existed, and this can be verified even through public tweets. So good luck to you and your Russian scammer."*

</div>

<div align="center">

![Tweet thread March 14 — Your abuse department is a disgrace. For 10 years you have been protecting a scammer. Do you not have enough evidence? What is happening here is illegal. This old lying Russian fraudster and his fake website are not some mystery.](evidence/15-tweet-thread-mar14-abuse-dept-disgrace.png)

*@Phish_Destroy, March 14: "Your abuse department is a disgrace. For 10 years you have been protecting a scammer, and even now you have done absolutely nothing. What is happening here is illegal." Plus: the GitHub PR screenshot — "We believe that truth is better than your profit."*

</div>

<div align="center">

![Tweet March 14 — New service from NameSilo: their abuse team is helping scammers get VirusTotal bans removed. I honestly thought that after NICENIC nothing could surprise me anymore — but you still managed to surprise me. Abuse Report Complaint Filed, Abuse Report Ignored infographic.](evidence/16-tweet-mar14-vt-delisting-service.png)

*@Phish_Destroy, March 14: "New service from NameSilo: helping scammers get VirusTotal bans removed." The infographic shows the cycle: Abuse Report filed → Complaint Filed → Abuse Report Ignored → NameSilo: "the domain was compromised" → "working to get delisted from VT." All while archived snapshots from 2021-2022 prove the malicious activity was always there.*

</div>

---

## The connection — in one paragraph

A scammer running a ten-year crypto drainer, on $550-a-month bulletproof hosting in Belize, behind Russian DDoS-Guard, wrote to us on **February 17, 2026**: *"Feel free to subpoena the domain registrar for my information."* Twenty-four days later, on **March 13, 2026**, that same registrar — **NameSilo, LLC (IANA #1479)** — published an official tweet calling him **"the victim"** of a hypothetical hack, denying our 20+ abuse reports ever arrived, and announcing a public commitment to **clean up his VirusTotal detections**. Three other registrars (PDR, WebNic, NICENIC) holding the same domain looked at the same evidence and **suspended in days**. NameSilo, LLC (IANA #1479) wrote a press release for him. **They put the connection in public themselves.** This repository is the receipts.

> Full evidence chain: [`CONNECTION.md`](CONNECTION.md)

---

## The lies — in one table

| NameSilo's claim | Reality | Verdict |
|---|---|---|
| "Domain was compromised a few months ago." | The theft code *is* the website. 8 PHP endpoints, server-side `session_key` exfiltration, `raw_tx_and_hash.raw = 0`. Built to steal from day one, ~10 years. The operator **never claimed a hack** in his own emails. | **FALSE** |
| "Prior to that, we had received no abuse reports." | **20+ delivery-receipted abuse reports** through their own portal, 2023-2026. Our tweet from **one day before** their statement says "9 reports is no joke anymore." | **FALSE** |
| "After an extensive review... not involving the registrant." | The operator wrote to **us** defending his code as his own. NameSilo, LLC (IANA #1479) adopted a "compromise" framing the operator himself never advanced. | **FALSE** |
| "Working with the registrant to remove the website from VT reports." | A registrar helping a confirmed scammer erase his security warnings from 6+ authoritative vendors. Not abuse handling. **Active obstruction of consumer-protection telemetry.** | **DAMNING** |

> Full line-by-line breakdown: [`THE-LIES.md`](THE-LIES.md)

---

## The pressure campaign — what they're still doing right now

The moment we replied with the operator's own emails, the silencing started. **They have not stopped.**

| Date | What happened | Status |
|---|---|---|
| 2026-03-13 | NameSilo, LLC (IANA #1479) publishes the four-lie defense | [Archived forever](https://ghostarchive.org/archive/CXXZ0) |
| 2026-03-16 | We post the receipts — "@NameSilo is lying" | Tweets now invisible (account locked) |
| 2026-03-18 | We escalate to ICANN + law enforcement | On record |
| 2026-03-?? | **@Phish_Destroy permanently locked** via Gold Checkmark live-support | **Still locked** |
| 2026-04-15 | X automation: *"no violation, restored"* | **Lock not lifted. Gold still billed.** |
| Ongoing | **Bing search delisting** of `phishdestroy.io` | Tracking |
| Ongoing | **DDoS** from "njan la" reseller infrastructure | Mitigated |
| 8 years | Operator: fake DMCA, mass-report reviews, delete GitHub issues, 50+ paid SEO articles to bury victims | [Documented](OPERATOR_PROFILE.md) |

> Full timeline: [`PRESSURE.md`](PRESSURE.md) &middot; Operator's 8-year suppression history: [`OPERATOR_PROFILE.md`](OPERATOR_PROFILE.md)

---

## What's in this repository

```
.
├── README.md                              ← you are here
├── PROOFS.md                              ← master evidence index, every exhibit SHA-256 verified
├── INVESTIGATION_DOSSIER_EN.md            ← complete investigation dossier (613 lines)
├── ARTICLE_FULL.md                        ← full investigative article
├── CONNECTION.md                          ← NameSilo ↔ xmrwallet operator evidence chain
├── THE-LIES.md                            ← line-by-line rebuttal of NameSilo's March 13 statement
├── NAMESILO-RESPONSE-MAY2026.md           ← NameSilo's May 11 legal threat, documented
├── NAMESILO_DOMAIN_ANOMALY_REPORT.md      ← statistical analysis: 8 registrars, 130M domains
├── PRESSURE.md                            ← suppression campaign log
├── SCAM_TECHNICAL.md                      ← xmrwallet technical breakdown (8 PHP endpoints)
├── XMRWALLET_TECHNICAL.md                 ← server-side key drainer case file
├── OPERATOR_PROFILE.md                    ← operator dossier: identity, domains, IPs, IOCs
├── VICTIMS.md                             ← documented victims, 2016–2026 timeline
├── EVIDENCE_INDEX.md                      ← every screenshot indexed with SHA-256
├── SOURCES.md                             ← permanent archive URLs for all external claims
├── EVIDENCE_HASHES.txt                    ← SHA-256 of every screenshot
├── CITATION.cff                           ← machine-readable citation for legal/academic use
├── LICENSE                                ← CC-BY-4.0, explicit grant for legal/regulatory use
├── evidence/                              ← 10 SHA-256 verified screenshots
├── tools/                                 ← archive tooling (Wayback, archive.ph)
├── xmrwallet-evidence/                    ← xmrwallet-specific evidence package
├── pkg/                                   ← zone scan evidence package (5.27M domains)
│   ├── report.html                        ← main investigation report
│   ├── clusters.html                      ← favicon cluster analysis
│   ├── domains.html                       ← 107,252 IOC domains
│   ├── evidence/                          ← JSON evidence files + manifest
│   └── raw_data/                          ← gzip scan datasets (JSONL/CSV)
└── docs/                                  ← GitHub Pages
    ├── namesilo-scan.html                 ← zone scan report
    ├── namesilo-clusters.html             ← favicon clusters
    ├── namesilo-domains.html              ← 107,252 IOC domains (searchable)
    ├── namesilo-privacyguardian.html      ← 183,419 PG-shielded malicious domains
    ├── behavioral-patterns.html           ← behavioral analysis
    ├── assets/                            ← 11 forensic diagrams (PNG)
    └── evidence/                          ← SHA-256 manifests
```

> **Where do I start?** Open [`PROOFS.md`](PROOFS.md) — every piece of evidence and every mirror in one place. That is the file to share if you only have one URL.

---

## Verify the evidence yourself

Every screenshot in `evidence/` has a SHA-256 fingerprint in [`EVIDENCE_HASHES.txt`](EVIDENCE_HASHES.txt). To check that nothing has been tampered with:

```bash
git clone https://github.com/phishdestroy/namesilo-evidence.git
cd namesilo-evidence/evidence
sha256sum -c ../EVIDENCE_HASHES.txt
```

All 10 files should report `OK`. If any fails, do not trust the modified copy — open an Issue and we will investigate.

---

## For victims of `xmrwallet[.]com`

If you have lost funds to `xmrwallet[.]com`, this repository is a **ready-made evidence package** you can attach to:

- A police report (in any jurisdiction)
- An IC3 (FBI) cybercrime complaint — https://www.ic3.gov
- A FTC complaint — https://reportfraud.ftc.gov
- An ICANN Contractual Compliance complaint against NameSilo, LLC (IANA #1479) — https://www.icann.org/compliance
- A civil claim against NameSilo, LLC (IANA #1479) and/or the operator
- A chargeback / insurance filing

The license file in this repo ([`LICENSE`](LICENSE)) is **explicit, written consent** to use this evidence as-is in any of the above. No further authorization required from PhishDestroy.

Direct contact for victims: **[report@phishdestroy.io](mailto:report@phishdestroy.io)**

> Open an Issue using the [Victim Report template](.github/ISSUE_TEMPLATE/victim-report.yml) if you want your case added to the public ledger.
>
> Documented victims and the full 2016-2026 timeline: [`VICTIMS.md`](VICTIMS.md)

---

## For ICANN compliance officers, regulators, journalists

The full case file was forwarded to **ICANN Contractual Compliance on March 18, 2026**. This repository is the public mirror of that filing, with the same screenshots, the same hashes, and the same explicit consent for republication.

If you need additional materials (raw email headers, server-side capture of the eight `xmrwallet[.]com` PHP endpoints, the 20+ historical abuse-report delivery receipts to NameSilo, LLC (IANA #1479) dating back to 2023), contact **[abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)** with a subject line that identifies your role.

---

## Why this matters beyond one domain

NameSilo, LLC (IANA #1479) is tied — in our records — to **hundreds of active crypto-scam domains targeting US users**. Across two years of work we have submitted thousands of abuse reports through their portal. The pattern, consistently, is silence.

`xmrwallet[.]com` is the case where they broke their silence. They went on the record. They put a defense of a confirmed scammer in their own corporate voice, on a public channel, with an offer to help him erase his security record.

This is not a single registrar making a single review error. **This is a registrar publishing a corporate policy of protecting a specific operator** — and using paid platform-level access (X Gold Checkmark live support) to silence the people who proved them wrong.

If a registrar can do this once, in public, and walk it off — every other registrar learns the lesson.

So this case is not going to walk off.

---

## Mirrors & Permanent Copies

This story is being kept alive in multiple places, intentionally. Every link below is a separate surface that would require a separate legal action to remove. Good luck.

### IPFS — Permanent, Decentralized, No "Report" Button

- **ENS + IPFS:** [`phishdestroy.eth.limo`](https://phishdestroy.eth.limo/) — Ethereum Name Service → IPFS. No server, no host, no takedown mechanism.
- **IPFS CID:** `bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq`
- **Evidence page:** [`phishdestroy.eth.limo/evidence.html`](https://phishdestroy.eth.limo/evidence.html) — all 16 screenshots, articles, Medium mirror, Wayback links
- **4EVERLAND hosting:** [`ipfs-archive-nsdim0vd-phishdestroy.ipfs.4everland.app`](https://ipfs-archive-nsdim0vd-phishdestroy.ipfs.4everland.app/)
- **IPFS Gateways (all serve the same CID):**
  - [`dweb.link/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq`](https://dweb.link/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq/)
  - [`4everland.io/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq`](https://4everland.io/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq/)
  - [`w3s.link/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq`](https://w3s.link/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq/)
  - [`nftstorage.link/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq`](https://nftstorage.link/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq/)
  - [`gateway.ipfs.io/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq`](https://gateway.ipfs.io/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq/)

### Web — Traditional Hosting

- **Canonical:** [phishdestroy.io/namesilo-killed-our-twitter](https://phishdestroy.io/namesilo-killed-our-twitter)
- **Medium:** [phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam](https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e)
- **GitHub Pages mirror:** [`docs/index.html`](docs/index.html)
- **GitHub evidence repo (this one):** the file you are reading right now
- **Codeberg mirror:** [codeberg.org/phishdestroy/namesilo-evidence](https://codeberg.org/phishdestroy/namesilo-evidence)

### Third-Party Archives (we don't control these)

- **GhostArchive (NameSilo's tweet):** [ghostarchive.org/archive/CXXZ0](https://ghostarchive.org/archive/CXXZ0)
- **Wayback — PhishDestroy GitHub:** [web.archive.org snapshot](https://web.archive.org/web/20260508165746/https://github.com/phishdestroy)
- **Wayback — This repo:** [web.archive.org snapshot](https://web.archive.org/web/20260508165630/https://github.com/phishdestroy/namesilo-evidence)
- **Wayback — xmrwallet.com (live scam):** [web.archive.org snapshot](https://web.archive.org/web/20260411223411/https://www.xmrwallet.com/)
- **Wayback — xmrwallet.cc (clone, taken down):** [web.archive.org snapshot](https://web.archive.org/web/20260223024911/https://www.xmrwallet.cc/)
- **Wayback — xmrwallet.biz (clone, taken down):** [web.archive.org snapshot](https://web.archive.org/web/20260220194352/https://www.xmrwallet.biz/)
- **Wayback — xmrwallet.me (clone, taken down):** [web.archive.org snapshot](https://web.archive.org/web/20260312042503/https://www.xmrwallet.me/)
- **Wayback — xmrwallet investigation:** [web.archive.org snapshot](https://web.archive.org/web/20260508085233/https://github.com/phishdestroy/DO-NOT-USE-xmrwallet-com)
- **Wayback — xmrwallet GitHub Pages:** [web.archive.org snapshot](https://web.archive.org/web/20260508085233/https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/)

> Cut down one link. Five more grow back. We run on the **Hydra principle**.

---

<div align="center">

### *Scammers delete evidence. NameSilo, LLC (IANA #1479) defended one. X locked our account. Bing is delisting us. The archive remains. The truth remains. We remain.*

**PhishDestroy Research** · [phishdestroy.io](https://phishdestroy.io) · [abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)

</div>
