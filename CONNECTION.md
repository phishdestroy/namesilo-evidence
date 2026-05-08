# The Connection — How NameSilo Outed Itself

> **NameSilo did not get caught accidentally protecting a scammer. They put the relationship in public themselves, in their own corporate voice, on March 13, 2026.**

This document collects every piece of evidence that links the registrar **NameSilo, LLC** to the operator of `xmrwallet[.]com` — referred to in our correspondence as **N.R.** — and demonstrates that the connection is not inferred. It is **stated**, in writing, by both sides.

---

## 1. The scammer named the registrar as a safe haven, three weeks before the registrar acted

On **February 17, 2026**, in an email to `abuse@phishdestroy.io`, the operator of `xmrwallet[.]com` wrote:

> *"Feel free to subpoena the domain registrar for my information."*

**This sentence is the entire story compressed.**

Read literally: the operator of a ten-year crypto-drainer, sitting on $550-a-month Belize bulletproof hosting, behind Russian DDoS-Guard, calmly invited a security-research organization to issue a subpoena to his own domain registrar. He named NameSilo without naming them. He pointed at them as the place that *protects* his identity, not the place that *threatens* it.

**Nobody behaves like that with a registrar that might shut them down.**

Nobody behaves like that unless they already know how the registrar will react.

The email is preserved in raw form in the PhishDestroy mail-server logs, with full SMTP headers, DKIM signatures from the originating MTA, and timestamps independently verifiable from the receiving side. The relevant excerpt is also reproduced in:

- [`evidence/01-operator-email-feb16.png`](evidence/01-operator-email-feb16.png) (first email, Feb 16, asking for report removal)
- [`evidence/01-phishdestroy-reply-feb16.png`](evidence/01-phishdestroy-reply-feb16.png) (our reply, technical breakdown)

The "subpoena the registrar" line came in his **third** email (Feb 17), which we are preserving for direct ICANN/court submission rather than public release until any pending proceedings allow.

---

## 2. Twenty-four days later, NameSilo confirmed his confidence was justified

On **March 13, 2026**, NameSilo's official Twitter account ([@NameSilo](https://twitter.com/NameSilo)) published an unsolicited public defense of `xmrwallet[.]com` directly under the PhishDestroy investigation thread.

![NameSilo's official tweet — March 13, 2026](evidence/03-namesilo-statement-mar13.png)

> *"Our Abuse team conducted an in-depth review into this case and it seems that domain was compromised a few months ago (during which a copy of the webpage was replaced with a crypto-drainer). Prior to that, we had received no abuse reports related to this domain. After an extensive review…"*

— and the tweet went on to commit to **"working with the registrant to remove the website from VirusTotal reports."**

Permanently archived: [ghostarchive.org/archive/CXXZ0](https://ghostarchive.org/archive/CXXZ0)

This is the moment NameSilo voluntarily entered the case file. **Nothing in our investigation ever required NameSilo to comment publicly.** They published this tweet on their own initiative, in their own corporate voice. It is on the record forever.

---

## 3. Three other registrars looked at identical evidence and acted the opposite way

`xmrwallet[.]com` was not unique to NameSilo. Operator-controlled mirrors of the same drainer were registered across multiple registrars during the same window. The evidence package distributed to all of them was identical.

| Registrar | Action on identical evidence | Time to action |
|---|---|---|
| **PublicDomainRegistry (PDR)** | Suspended | Days |
| **WebNic** | Suspended | Days |
| **NICENIC** | Suspended | Days |
| **NameSilo** | **Public defense + offer to scrub VirusTotal** | — |

Three independent registrar abuse teams — including NICENIC, which we have publicly documented for years as one of the slowest and laziest abuse handlers on the internet — reached the same conclusion: **suspend the domain.** Only NameSilo reached a different one.

That divergence cannot be explained by "varying review standards." NICENIC's review standards are essentially nonexistent. NICENIC still suspended. The variable is not the evidence; the variable is NameSilo.

---

## 4. NameSilo's defense is structurally identical to the scammer's

Set the operator's emails (Feb 16-17) and NameSilo's tweet (Mar 13) side by side and the rhetorical fingerprints match.

| Operator (N.R.) | NameSilo (official) |
|---|---|
| "There is no phishing going on with xmrwallet.com." | "Our Abuse team conducted an in-depth review… domain was compromised." |
| "We are an open source crypto wallet that is non-custodial." | "(during which a copy of the webpage was replaced with a crypto-drainer)" |
| "Please remove your report on us." | "We had received no abuse reports related to this domain." |
| Accuses PhishDestroy of "killing three of his domains." | Implies PhishDestroy's reports were never received. |
| Treats the analysis as personal harassment, not technical work. | Frames the operator as a victim of a third-party hack. |

Same posture. Same framing. Same dismissal of reproducible technical evidence in favor of a "trust me, this is fine" rebuttal. **They speak with one voice on this domain.**

---

## 5. NameSilo helped the scammer attempt to scrub his security record

The fourth claim of NameSilo's tweet is the most consequential, and the one most observers under-weight:

> *"Working with the registrant to remove the website from VT reports."*

A registrar's small in-house abuse team, looking at a confirmed phishing site that:

- Has been live for ~10 years,
- Steals private keys via server-side `session_key` exfiltration,
- Is flagged by **6+ authoritative security vendors** (including Fortune-500-grade telemetry providers),
- Has been suspended at **3 other registrars** on the same evidence,

…publicly announces that it is going to **help the registrant get those vendors' detections removed**.

This is not abuse handling. This is **active obstruction of consumer-protection telemetry on behalf of a confirmed thief**. There is no legitimate read of this commitment. A registrar has no business advocating to security vendors that detections of their customer's drainer site be lifted, and certainly not in public, and certainly not before any reasonable review of the underlying technical evidence.

NameSilo committed to this in writing. They have not retracted it.

---

## 6. The "njan la" reseller pattern — long-running infrastructure overlap

`xmrwallet[.]com` is one domain in a much wider pattern. NameSilo's largest historical abuse-tolerant reseller, **"njan la"**, was the dominant supplier of bulletproof crypto-scam domains during 2022-2024 — the peak of the crypto-drainer and pig-butchering epidemics.

Among the patterns we are currently formalising for publication on [phishdestroy.io](https://phishdestroy.io):

- "njan la" charged 2x-5x premium pricing for domains visibly used in active fraud.
- "njan la" suspended its public API around the time aggregate abuse reporting began to surface the volume.
- A non-trivial fraction of NameSilo-registered domains in our 2022-2024 abuse logs trace back through this reseller.
- DDoS traffic targeting `phishdestroy.io` in the weeks following our investigation publication has source-IP correlation with infrastructure tied to this reseller ecosystem.

The full reseller analysis is being prepared for separate publication. **What is in this repository is the part of the connection that is already on the record, in NameSilo's own published voice.**

---

## 7. Conclusion

The connection between NameSilo and the operator of `xmrwallet[.]com` is not theoretical. It is not a guess. It is not "circumstantial." It is composed of:

- The operator publicly inviting a subpoena to his own registrar (Feb 17);
- The same registrar publicly defending him 24 days later (Mar 13);
- A four-sentence public statement that contradicts the operator's own emails, the technical evidence, and the action of three other registrars on identical material;
- A written commitment from the registrar to help the operator scrub his security detections;
- A pressure campaign against the researchers, executed via the registrar's paid X Gold Checkmark support channel, in the days after the receipts were posted (see [`PRESSURE.md`](PRESSURE.md)).

A connection of this density, between a registrar and a long-running fraud operator, is a matter for ICANN Contractual Compliance, for the relevant US consumer-protection authorities, and — given the cross-border nature of the harm — for international cooperation channels.

The case has been forwarded to all of the above. This repository is the public copy.

---

*Continue:* [Line-by-line breakdown of the lies &rarr;](THE-LIES.md) · [The pressure campaign &rarr;](PRESSURE.md) · [Evidence index &rarr;](EVIDENCE_INDEX.md)
