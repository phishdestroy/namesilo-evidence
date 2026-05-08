# Security & Reporting

This repository documents an active fraud operation (`xmrwallet[.]com`) and the registrar response to it (`NameSilo`). It is a public evidence package, not a software project. The "security policy" below applies accordingly.

## If you are a victim of `xmrwallet[.]com`

Please contact **[report@phishdestroy.io](mailto:report@phishdestroy.io)** with:

1. The dates of any transactions you sent through `xmrwallet[.]com`.
2. The originating wallet address(es) you used.
3. The amount of Monero (XMR) lost.
4. Any direct correspondence you have with `xmrwallet[.]com` operators.

Do **not** post wallet addresses, transaction IDs, or personal contact information in a public Issue. Use email.

You can also open a confidential GitHub Issue using the [Victim Report template](.github/ISSUE_TEMPLATE/victim-report.yml) — Issues marked "victim" will be triaged privately and will not be made publicly visible until you confirm consent.

## If you have additional evidence about NameSilo / xmrwallet

Use the [Additional Evidence template](.github/ISSUE_TEMPLATE/additional-evidence.yml).

We particularly value:

- Screenshots of NameSilo abuse-report submissions that were ignored or returned with "no violation" — especially with delivery receipts / ticket IDs.
- Direct correspondence with `xmrwallet[.]com` operators.
- Documentation of takedown attempts (DMCA, platform reports, search-engine delisting requests) that target legitimate research on this case.
- Information about the "njan la" reseller's relationship to NameSilo.

## If you are an ICANN compliance officer, regulator, journalist, or law-enforcement contact

The full case file was forwarded to **ICANN Contractual Compliance on March 18, 2026**. This repository is the public mirror of that filing. For raw materials (full email headers, server-side captures, the 20+ historical abuse-report delivery receipts), contact **[abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)** with a subject line that identifies your role.

## If you find a tampered screenshot

If `sha256sum -c EVIDENCE_HASHES.txt` fails on your local clone, do **not** trust the modified file. Open an Issue with:

1. The output of `sha256sum -c EVIDENCE_HASHES.txt` showing the failed file.
2. The exact commit you cloned (`git rev-parse HEAD`).
3. Your clone source URL.

We will investigate. Tampering with this evidence package is itself an indicator worth recording.

## For takedown notices

This repository contains:

- Public corporate statements (NameSilo's tweet) — already permanently archived at GhostArchive.
- Direct correspondence sent **to** `abuse@phishdestroy.io` by the operator of `xmrwallet[.]com` — published under fair-use / public-interest doctrine, with the operator clearly informed at the time of writing that escalation, including public documentation, would follow continued misrepresentation.
- Screenshots of @Phish_Destroy's own published posts on X.
- Screenshots of automated email correspondence between PhishDestroy and X Support.

If you wish to dispute the publication of any specific item, use **[abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)** with a clear identification of the item, your legal basis, and your contact information. We do not act on takedown requests filed through GitHub's content-removal channels for the materials in this repository, because every item here has been forwarded to ICANN Contractual Compliance and is part of an ongoing regulatory matter.

## Encryption

For sensitive submissions, request a PGP key by emailing `abuse@phishdestroy.io` with subject line `pgp request`.
