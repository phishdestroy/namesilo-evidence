# Sources & Permanent Archives

Every external claim referenced in this repository, with at least one immutable archive URL.

## Primary article (canonical)

- **PhishDestroy.io:** https://phishdestroy.io/namesilo-killed-our-twitter
- **Medium:** https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e
- **Earlier scam write-up:** https://phishdestroy.medium.com/xmrwallet-com-2953f35b8a79
- **dev.to:** see `article.devto.md` in upstream working tree (pending publication)
- **GitHub repo (this one):** https://github.com/phishdestroy/namesilo-xmrwallet-coverup
- **GitHub Pages mirror:** https://phishdestroy.github.io/namesilo-xmrwallet-coverup/

## NameSilo's public statement of March 13, 2026

- **GhostArchive (immutable):** https://ghostarchive.org/archive/CXXZ0
- **Local immutable copy:** [`evidence/03-namesilo-statement-mar13.png`](evidence/03-namesilo-statement-mar13.png)
- **SHA-256:** `ad29e1d3d4803ff37c88ef860bef6de9e62f6ce533657f2e5c5460eb2e0b8ebf`

## `xmrwallet[.]com` technical investigation

- **Full breakdown (public):** https://phishdestroy.io/xmrwallet-namesilo-exposed
- **GitHub evidence repo (technical):** https://github.com/phishdestroy/DO-NOT-USE-xmrwallet-com

## @Phish_Destroy public posts (March 16-18, 2026)

The X/Twitter account is currently locked. The local screenshots in [`evidence/`](evidence/) are the canonical copies.

- *"@NameSilo is lying"* — [`evidence/04-tweet-namesilo-is-lying.png`](evidence/04-tweet-namesilo-is-lying.png)
- *"Acting as press secretary for a $2M+ Monero theft operation"* — [`evidence/04-tweet-press-secretary.png`](evidence/04-tweet-press-secretary.png)
- *"Honest question for @NameSilo: Who is this operator to you?"* — [`evidence/04-tweet-honest-question.png`](evidence/04-tweet-honest-question.png)
- Quote of CryptOpus thread (Feb 22, 2026) — [`evidence/04-tweet-cryptopus-quote.png`](evidence/04-tweet-cryptopus-quote.png)
- Original Wayback / archive.today / GhostArchive snapshots are listed in the parent working tree's [`backup/`](../backup/) directory (Wayback CDX dumps, archive.today HTML, DDG SERP harvests for `@Phish_Destroy`).

## X Support correspondence (April 15, 2026)

- Email body — [`evidence/06-x-support-no-violation.png`](evidence/06-x-support-no-violation.png)
- Subject line — [`evidence/06-x-support-subject-restored.png`](evidence/06-x-support-subject-restored.png)

## Operator (N.R.) emails to `abuse@phishdestroy.io`

- **2026-02-16** — first email asking for report removal — [`evidence/01-operator-email-feb16.png`](evidence/01-operator-email-feb16.png)
- **2026-02-16** — PhishDestroy's technical reply — [`evidence/01-phishdestroy-reply-feb16.png`](evidence/01-phishdestroy-reply-feb16.png)
- **2026-02-17** — *"Feel free to subpoena the domain registrar for my information"* — preserved in raw mail-log form, available to ICANN Compliance and law enforcement on request

## ICANN Contractual Compliance escalation

- **Filed:** March 18, 2026
- **Reference materials:**
  - The full operator email thread
  - 20+ historical abuse-report delivery receipts to NameSilo, LLC (IANA #1479) (2023-2026)
  - NameSilo's public tweet of March 13, 2026
  - Technical breakdown of `xmrwallet[.]com`
- **Public statement of forwarding:** original tweet now invisible (account locked); reproduced verbatim in [`PRESSURE.md`](PRESSURE.md) §2 (2026-03-18).

## Other registrars (for comparison)

`xmrwallet[.]com` was simultaneously hosted across several registrar accounts. Three suspended on identical evidence:

| Registrar | Status |
|---|---|
| PublicDomainRegistry (PDR) | Suspended |
| WebNic | Suspended |
| NICENIC | Suspended |
| **NameSilo, LLC (IANA #1479)** | **Public defense + offer to scrub VirusTotal** |

## Chain of custody

- All screenshots were captured on the PhishDestroy researcher workstation at the times stated in [`evidence/EVIDENCE.md`](evidence/EVIDENCE.md).
- Files were copied verbatim into this repository on 2026-05-07 and SHA-256 fingerprinted at the same commit.
- No screenshot has been edited, cropped, redacted, or recompressed.
- The canonical copies are in this Git repository. Modification history visible in `git log -p evidence/`.

## Verification

To verify the integrity of every screenshot in this repository:

```bash
git clone https://github.com/phishdestroy/namesilo-xmrwallet-coverup.git
cd namesilo-xmrwallet-coverup/evidence
sha256sum -c ../EVIDENCE_HASHES.txt
```

All ten files must report `OK`.
