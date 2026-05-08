# Security & Reporting

This repository documents an active fraud operation (`xmrwallet[.]com`) and the conduct of its registrar, NameSilo, LLC (IANA #1479). It is a public evidence package, not a software project. The "security policy" below applies accordingly.

---

## Notice to GitHub Trust & Safety, Bing, and all platform reviewers

**The operator of `xmrwallet[.]com` and NameSilo, LLC (IANA #1479) are actively filing fraudulent takedown requests against this repository and related research.** This is not speculation — it is a documented, eight-year pattern. Here is what they have already done:

| Platform | What they did |
|---|---|
| **Twitter/X** | Used the Gold Checkmark corporate support channel to lock @Phish_Destroy. X's own automation reviewed the appeal and wrote: *"no violation, restored to full functionality."* The account is **still locked.** ([evidence](evidence/06-x-support-no-violation.png)) |
| **Bing** | Filed delisting requests against `phishdestroy.io` content related to this investigation. Webmaster Tools shows inbound complaints. |
| **GitHub** | The operator has previously filed **false DMCA takedowns** against repositories documenting the scam. He also deleted his own GitHub Issues #35 and #36 containing victim reports and technical analysis. |
| **Trustpilot** | Mass-reported negative reviews from real victims until they were removed by automated moderation. |
| **BitcoinTalk** | Coordinated reporting against warning threads to trigger removal. |
| **YouTube** | Reported technical analysis videos demonstrating the theft mechanism. |
| **Google Search** | Published **50+ paid SEO articles** to bury victim complaints and negative coverage. |

**The pattern is always the same:** never address the technical evidence. Never produce a rebuttal. Just find the "report" button on whatever platform the evidence appears on, and press it.

**If you are reviewing a takedown request against this repository:** the materials here have been forwarded to **ICANN Contractual Compliance** (March 18, 2026) and to **federal law enforcement**. The filer of the takedown request is aware of this — we stated it publicly before our account was locked. They are filing anyway, because suppression is the only response they have. The technical evidence has never been disputed.

---

## What this repository actually contains (for reviewers)

Every item in this repository is one of the following:

1. **Public corporate statements** — NameSilo, LLC (IANA #1479)'s own tweet, published on their own verified corporate account. Already permanently archived at [GhostArchive](https://ghostarchive.org/archive/CXXZ0).

2. **Correspondence sent to us** — The operator of `xmrwallet[.]com` emailed `abuse@phishdestroy.io` voluntarily. He was explicitly warned in our same-day reply that escalation, including public documentation, would follow continued misrepresentation. He continued. Published under fair-use and public-interest doctrine.

3. **Our own published posts** — Screenshots of @Phish_Destroy's tweets, authored by us, on our own account. We hold full copyright.

4. **Automated platform correspondence** — X Support emails sent to us. We are the recipient and hold the right to publish.

5. **Original technical research** — Server-side analysis of `xmrwallet[.]com`'s theft mechanism, performed independently by PhishDestroy. This is original work, not copied from anyone.

6. **Third-party public reporting** — Quotes from @ImCryptOpus and other public accounts, clearly attributed. Fair use for commentary and criticism.

**None of this is copyrighted by NameSilo, LLC (IANA #1479) or the operator.** A DMCA takedown against this repository would be a fraudulent filing under 17 U.S.C. 512(f), carrying liability for damages and attorney's fees.

---

## If you are a victim of `xmrwallet[.]com`

Contact **[report@phishdestroy.io](mailto:report@phishdestroy.io)** with:

1. The dates of any transactions you sent through `xmrwallet[.]com`.
2. The originating wallet address(es) you used.
3. The amount of Monero (XMR) lost.
4. Any direct correspondence you have with `xmrwallet[.]com` operators.

Do **not** post wallet addresses, transaction IDs, or personal contact information in a public Issue. Use email.

You can also open a confidential GitHub Issue using the [Victim Report template](.github/ISSUE_TEMPLATE/victim-report.yml) — Issues marked "victim" will be triaged privately and will not be made publicly visible until you confirm consent.

Full victim documentation and the complete 2016-2026 timeline: [`VICTIMS.md`](VICTIMS.md)

---

## If you have additional evidence about NameSilo, LLC (IANA #1479) or xmrwallet

Use the [Additional Evidence template](.github/ISSUE_TEMPLATE/additional-evidence.yml).

We particularly value:

- Screenshots of NameSilo, LLC (IANA #1479) abuse-report submissions that were ignored or returned with "no violation" — especially with delivery receipts / ticket IDs.
- Direct correspondence with `xmrwallet[.]com` operators.
- **Documentation of takedown attempts** (DMCA, platform reports, search-engine delisting requests) that target legitimate research on this case — every one of these is itself evidence of the suppression campaign.
- Information about the "njan la" reseller's relationship to NameSilo, LLC (IANA #1479).

---

## If you are an ICANN compliance officer, regulator, journalist, or law-enforcement contact

The full case file was forwarded to **ICANN Contractual Compliance on March 18, 2026**. This repository is the public mirror of that filing. For raw materials (full email headers, server-side captures, the 20+ historical abuse-report delivery receipts), contact **[abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)** with a subject line that identifies your role.

---

## If you find a tampered screenshot

If `sha256sum -c EVIDENCE_HASHES.txt` fails on your local clone, do **not** trust the modified file. Open an Issue with:

1. The output of `sha256sum -c EVIDENCE_HASHES.txt` showing the failed file.
2. The exact commit you cloned (`git rev-parse HEAD`).
3. Your clone source URL.

We will investigate. Tampering with this evidence package is itself an indicator worth recording.

---

## For takedown notices

If you believe you have a legitimate legal basis to dispute the publication of any specific item in this repository, email **[abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)** with:

- Clear identification of the specific item
- Your legal basis
- Your contact information

We will review in good faith.

**However:** we do not act on takedown requests filed through GitHub's automated content-removal channels for the materials in this repository. Every item here has been forwarded to ICANN Contractual Compliance and federal law enforcement, and is part of an ongoing regulatory and legal matter.

Filing a false DMCA claim against documented security research that has been submitted to federal authorities is not a content-moderation action. It is obstruction. And it will be documented in [`PRESSURE.md`](PRESSURE.md) alongside every other attempt.

---

## Encryption

For sensitive submissions, request a PGP key by emailing `abuse@phishdestroy.io` with subject line `pgp request`.
