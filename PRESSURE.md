# The Pressure Campaign — Documented Attempts to Erase This Story

> **NameSilo, LLC (IANA #1479) and the operator of `xmrwallet[.]com` have an identical playbook when caught: silence the witness. They are still doing this, right now, while you are reading.**

This document collects every documented attempt — by either party — to suppress, delete, or delist the evidence presented in this repository.

---

## The pattern

Both the operator and his registrar share the same response when confronted:

1. **Deny the substance.** Refuse to engage with the technical evidence.
2. **Reframe the dispute as personal harassment.** "You are killing my domains" / "We are the victim."
3. **Locate the platform-level "report" button on whatever surface the critic uses.** Twitter, GitHub, Trustpilot, BitcoinTalk, YouTube, Bing, search engines — pick the one that allows automated suppression of the source.
4. **Push the report through paid or privileged access channels** if available, to bypass automated review.
5. **Continue normal operations under the assumption the critic will give up after the surface goes dark.**

The operator pioneered this pattern over ten years on his own behalf. NameSilo, LLC (IANA #1479) replicated it on a corporate scale within three weeks of being publicly criticised.

---

## Timeline — confirmed events

### Stage 1 — The operator's own track record (pre-2026)

The operator of `xmrwallet[.]com`, when criticised on third-party platforms, has historically:

- Filed false DMCA takedowns against GitHub repositories documenting the drainer.
- Mass-reported negative Trustpilot reviews until they were removed.
- Engaged in coordinated reporting against BitcoinTalk threads warning users.
- Reported YouTube videos that walked through the technical analysis.
- Targeted Twitter/X researchers with the "report" button via puppet accounts.

This pattern was documented years before our investigation began. Other researchers, including the CryptOpus thread of February 22, 2026, had already published parts of it. Local copy: [`evidence/04-tweet-cryptopus-quote.png`](evidence/04-tweet-cryptopus-quote.png).

We knew, going in, that this was the operator's behavior. We did not initially expect it from his registrar.

---

### Stage 2 — The registrar joins the campaign (March 2026)

#### 2026-03-13 — NameSilo, LLC (IANA #1479) publishes the public defense

NameSilo's official corporate Twitter account publishes a four-claim public statement under the PhishDestroy investigation thread, calling the operator "the victim" of an alleged compromise, denying any prior abuse reports, and committing to help him scrub his VirusTotal detections.

→ [`evidence/03-namesilo-statement-mar13.png`](evidence/03-namesilo-statement-mar13.png)
→ [GhostArchive permanent copy](https://ghostarchive.org/archive/CXXZ0)

#### 2026-03-16 — We post the receipts

@Phish_Destroy (paid X Gold Checkmark account, ~6.5K followers, never warned, never restricted, never reported anything fake) publishes three direct rebuttals citing the operator's own emails, the technical breakdown, and the contradiction with three other registrars' actions:

- *"@NameSilo is lying"* — [`evidence/04-tweet-namesilo-is-lying.png`](evidence/04-tweet-namesilo-is-lying.png)
- *"@NameSilo is acting as press secretary for a $2M+ Monero theft operation."* — [`evidence/04-tweet-press-secretary.png`](evidence/04-tweet-press-secretary.png)
- *"Honest question for @NameSilo: Who is this operator to you?"* — [`evidence/04-tweet-honest-question.png`](evidence/04-tweet-honest-question.png)

We also begin tagging NameSilo, LLC (IANA #1479) under **older threads from other researchers** documenting `xmrwallet` going back to 2022. This pulls archived third-party evidence directly into the registrar's mentions, defeating their "we received no abuse reports" claim with material they cannot dispute the authorship of.

#### 2026-03-18 — We forward the case to ICANN

In writing, on Twitter, with delivery confirmation:

> *"Because no response or action has been provided, and due to what appears to be deliberately false statements made to protect a fraud operator, we have forwarded the full investigation materials to @ICANN Contractual Compliance, relevant regulatory authorities, and law enforcement…"*

This is the post that, on our reading, tipped the registrar from "argue back on Twitter" into "use platform-level access to silence."

#### 2026-03-?? — @Phish_Destroy is locked

Within days of the ICANN escalation post, @Phish_Destroy is permanently locked. Email #1 from X Support reads:

> *"Our support team has determined that a violation against inauthentic behaviors [occurred]. We will not overturn our decision."*

No tweet quoted. No specific rule cited. No example. **No automated rule trigger fingerprint.** This is the signature of a human-agent decision following an inbound complaint, not the signature of policy automation.

#### 2026-04-15 — X's own automation contradicts the lock

On appeal, X Support sends a new email:

- Subject line: **"[4] Your account has been restored."**
- Body: *"Hello, We have reviewed your appeal request for account, @Phish_Destroy. **Our automated systems have determined there was no violation and have restored your account to full functionality.** Thanks, X Support."*

→ [`evidence/06-x-support-no-violation.png`](evidence/06-x-support-no-violation.png)
→ [`evidence/06-x-support-subject-restored.png`](evidence/06-x-support-subject-restored.png)

**The account is still locked.** The subscription is still being billed. Email #2 has not been retracted. We cannot pull down our own posts; the content @Phish_Destroy published rebutting NameSilo, LLC (IANA #1479) is invisible from the account that authored it.

This is the smoking gun: **X's own automation reviewed the case and cleared the account in writing**. The lock is being maintained against that automated determination. The mechanism that overrode the automation is the **Gold Checkmark live human-support channel** — a paid corporate access tier whose declared perk is direct contact with X moderators.

> *Concierge censorship that you can buy.*

---

### Stage 3 — Ongoing, beyond X (April 2026 onward)

#### Bing search delisting attempts

We are tracking ongoing attempts to remove `phishdestroy.io` content related to the NameSilo, LLC (IANA #1479) / xmrwallet investigation from Bing search results. Webmaster Tools indicates inbound complaints. Detailed evidence is being collected for a separate publication; the Twitter lock above is the documented case in this repository.

If you are a Bing trust-and-safety reviewer reading this: the delisting requests are being filed against legitimate threat-intelligence research that has been forwarded to ICANN Contractual Compliance and federal law-enforcement channels. The original publication is a US-hosted security-research operation with a documented two-year track record of reporting through proper channels. Treat with appropriate scepticism.

#### DDoS traffic against `phishdestroy.io`

Source-IP analysis of recent DDoS traffic against `phishdestroy.io` shows correlation with hosting infrastructure tied to NameSilo's largest historical abuse-tolerant reseller, **"njan la"**. This analysis is being formalised for separate publication.

#### Content scrubbing on third-party platforms

Coordinated reporting against:
- The PhishDestroy GitHub Issue that originally triggered the operator's first email
- Public mirrors of the `xmrwallet[.]com` technical breakdown
- The earlier Medium write-up: [phishdestroy.medium.com/xmrwallet-com-2953f35b8a79](https://phishdestroy.medium.com/xmrwallet-com-2953f35b8a79)

…is being monitored. Any takedown action that succeeds will be documented in a follow-up commit to this repository.

---

## What this all proves

**The pressure campaign is itself the strongest evidence of the underlying connection.**

Registrars whose customers are independently caught running scams **do not behave this way**. The normal response is silence — quietly act on the report, quietly do nothing, ride out the news cycle. NameSilo, LLC (IANA #1479) did not do that. NameSilo, LLC (IANA #1479):

- Published a public defense.
- Committed to scrubbing security detections.
- When proven wrong, paid for and used platform-level access to silence the witness.
- Has continued the pressure campaign across multiple surfaces beyond X.

A registrar that goes this far, this publicly, this consistently, on behalf of a single operator, **has reasons that cannot be explained by ordinary commercial relationships.** That is the position this repository asserts, and that the pressure campaign confirms.

---

## What we are doing in response

**Nothing dramatic. Just keeping the receipts.**

- **Hydra principle:** every surface they take down, we publish on five more. This repository is one of those surfaces. So is [phishdestroy.io](https://phishdestroy.io). So are the Medium articles. So are the GhostArchive snapshots. So are the GitHub Pages mirrors. The cost of suppression scales linearly; the cost of mirroring is logarithmic.
- **Public abuse ledger:** every NameSilo-related abuse report we file from this point forward is published live, with a delivery timestamp, on phishdestroy.io. NameSilo's *"prior to that, we had received no abuse reports"* claim cannot be made twice.
- **Permanent archives:** every external reference in this repository has at least one immutable archive URL — Wayback, GhostArchive, archive.today. See [`SOURCES.md`](SOURCES.md).
- **Court-ready format:** every screenshot is SHA-256 fingerprinted in [`EVIDENCE_HASHES.txt`](EVIDENCE_HASHES.txt). Every claim has a citation. The license file ([`LICENSE`](LICENSE)) is **explicit written consent** for any victim, prosecutor, regulator, or court to use this material as-is.
- **No retaliation. No campaigns. No petitions. No "demand action" buttons.** We do not need a movement. We need the file to remain visible. The file remains visible by being mirrored, fingerprinted, and impossible to silently modify.

---

## A direct note to NameSilo, LLC (IANA #1479) and the operator

You can keep clicking the report button. It changes nothing.

Every takedown attempt only adds another timestamp to the file — another data point on the pressure campaign, another signal to ICANN and to the watching public that the registrar's behavior here is not normal.

You are losing this loudly. Stop.

---

*Continue:* [The connection &rarr;](CONNECTION.md) · [Line-by-line debunking of the lies &rarr;](THE-LIES.md) · [Evidence index &rarr;](EVIDENCE_INDEX.md)
