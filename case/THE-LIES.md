# The Lies — NameSilo's March 13, 2026 Statement, Sentence by Sentence

> **Four sentences. Four falsehoods. Each one independently provable. Not "differently interpreted." Not "out of date." Not "a misunderstanding." False.**

The original tweet, by NameSilo's official corporate Twitter account ([@NameSilo](https://twitter.com/NameSilo)), is permanently archived at:

**→ [ghostarchive.org/archive/CXXZ0](https://ghostarchive.org/archive/CXXZ0)**

Local immutable copy: [`evidence/03-namesilo-statement-mar13.png`](evidence/03-namesilo-statement-mar13.png) (SHA-256: `ad29e1d3d4803ff37c88ef860bef6de9e62f6ce533657f2e5c5460eb2e0b8ebf`)

The full text, transcribed:

> *"Our Abuse team conducted an in-depth review into this case and it seems that domain was compromised a few months ago (during which a copy of the webpage was replaced with a crypto-drainer). Prior to that, we had received no abuse reports related to this domain. After an extensive review… [working with the registrant to remove the website from VT reports]."*

---

## Lie #1 — "Domain was compromised a few months ago."

### The claim

`xmrwallet[.]com` was a legitimate Monero wallet whose code was secretly replaced with a crypto-drainer "a few months ago" by some unspecified third-party attacker.

### The reality

The theft code **is** the website. It has been the website from day one, for approximately a decade.

Server-side analysis of the live `xmrwallet[.]com` infrastructure, performed independently from the operator's public GitHub repository, demonstrates:

- **Eight PHP endpoints** specifically dedicated to private-key exfiltration.
- **Server-side construction of the actual transaction**, parallel to and independent of the client-side transaction the user thinks they are signing.
- **Production-only parameters** — `session_key`, `verification`, encrypted payload — that have no presence in the public GitHub repository the operator points to as "the source code."
- The `session_key` parameter carrying **the full wallet address and the private view key**, base64-encoded, transmitted to operator infrastructure on every transaction.
- Non-standard transaction `type == 'swept'` paired with "Unknown transaction id" on the legitimate Monero network — the signature of a server-initiated key-exfiltration sweep, not a user-initiated transaction.

The full reproducible technical breakdown is at:
**→ [phishdestroy.io/xmrwallet-namesilo-exposed](https://phishdestroy.io/xmrwallet-namesilo-exposed)**

### What "compromise" would look like, if it were real

A genuine compromise of an open-source wallet would leave a forensic trail:

- A diff between the GitHub repo at commit X and the deployed code, showing the moment of modification.
- DNS / hosting / TLS-cert changes around the supposed compromise window.
- An incident-response statement from the registrant naming the compromise vector.
- A clear before/after in the production behavior of the site.

NameSilo, LLC (IANA #1479) provided **none of this**. The operator provided **none of this** in his direct emails to us. Asked the question repeatedly, both refused to specify when, how, or by whom. Because the answer is: never, no, nobody. The site was not compromised. The site was built to steal.

### Verdict

**False on its face.** A registrar's abuse team had no technical basis to claim "compromise" without being able to identify a single forensic indicator of one. Either NameSilo, LLC (IANA #1479) did no review at all and asserted the operator's framing as fact, or they did a review and chose to publish a known-false summary. Both readings are disqualifying.

---

## Lie #2 — "Prior to that, we had received no abuse reports related to this domain."

### The claim

NameSilo, LLC (IANA #1479) had no record of any prior abuse complaint against `xmrwallet[.]com` before the alleged "compromise."

### The reality

PhishDestroy alone has submitted **20+ abuse reports** through NameSilo's own abuse portal between **2023 and 2026**, on `xmrwallet[.]com` and operator-linked mirrors. We hold the **delivery receipts** — confirmation pages, ticket IDs, automated acknowledgements from NameSilo's own intake system — for each of them.

Beyond PhishDestroy, public threads from independent researchers (including the CryptOpus thread of February 22, 2026, see [`evidence/04-tweet-cryptopus-quote.png`](evidence/04-tweet-cryptopus-quote.png)) document third-party reporting going back years.

### Two possible readings of NameSilo's claim

1. **NameSilo's abuse team genuinely does not know what reports it has received.** Their intake system is so broken that 20+ delivery-receipted submissions over three years can be erased from internal memory. This is, by itself, an ICANN-compliance failure.
2. **NameSilo's abuse team knows, and lied anyway.** The public statement was crafted to deny the existence of any prior accountability for the domain.

### Verdict

**False under either reading.** PhishDestroy is in possession of every delivery receipt and is willing to produce them, in full, to any ICANN compliance officer, regulator, or court. The materials were forwarded to ICANN Contractual Compliance on March 18, 2026.

---

## Lie #3 — "After an extensive review… not involving the registrant."

### The claim

NameSilo, LLC (IANA #1479) concluded their review independently and the registrant was not party to its conclusions.

### The reality

The operator wrote to us **first**, on February 16, 2026, defending his code as his own work, asking us to remove our report:

> *"Hi, You are incorrect with your report. There is no phishing going on with xmrwallet.com, this is the official domain name for xmrwallet. We are an open source crypto wallet that is non-custodial, we don't store seeds or keys, everything is done in your browser locally. Please remove your report on us, thank you. N.R."*

— [`evidence/01-operator-email-feb16.png`](evidence/01-operator-email-feb16.png)

He did not, in this email or any other, claim he had been hacked. He claimed the site was operating normally and PhishDestroy was wrong. He demanded the report be retracted. He continued this position through subsequent emails over the following days.

NameSilo's tweet of March 13 then claimed a "compromise" narrative the operator himself had never advanced. **The registrant could not have been the source of that framing**, because the registrant did not believe it.

### Verdict

**False.** Either NameSilo's "extensive review" never asked the registrant — in which case it cannot be called extensive — or it did ask and adopted a narrative the registrant did not support. Both readings are nonsensical without a third-party silently providing the framing. NameSilo, LLC (IANA #1479) has not named that third party.

---

## Lie #4 — "Working with the registrant to remove the website from VT reports."

### The claim

NameSilo, LLC (IANA #1479) committed publicly to assisting the operator in getting `xmrwallet[.]com` removed from VirusTotal's threat detections.

### The reality

This is the single most damning sentence in the tweet, and it is also the only one that NameSilo, LLC (IANA #1479) did not technically lie about — because they actually said it, and they meant it.

Consider what is being committed to:

- A registrar's small in-house abuse team,
- Looking at a phishing site flagged by **multiple authoritative security vendors**,
- Including Fortune-500-grade telemetry providers whose threat feeds are downstream of major commercial security products,
- Has decided, **on its own technical judgment**, that all of those vendors are wrong,
- And is going to **advocate publicly to those vendors to remove their detections**.

There is no legitimate framework in which a domain registrar takes on this role. Registrars are not security vendors. They have no original threat-research capacity. Their abuse teams handle ticket triage, registrant verification, and at most a basic content review. A registrar that announces it is going to **dispute the threat-intelligence findings of every authoritative vendor on a confirmed drainer** is not doing abuse handling. It is doing **public-facing reputation laundering for a fraud operator**.

This commitment was made on a public channel, in NameSilo's official corporate voice, with full awareness that the audience would include other registrars, security vendors, and ICANN compliance.

### Verdict

**Stated as written. Damning as written.** NameSilo's only protection here is the absence of mass attention. This document removes that protection.

---

## What the four claims have in common

Each of the four sentences in NameSilo's statement has the same defect: **none of them survives contact with documents NameSilo, LLC (IANA #1479) itself does not control.**

- Claim #1 falls apart against the public technical breakdown.
- Claim #2 falls apart against the delivery receipts in PhishDestroy's portal logs.
- Claim #3 falls apart against the operator's own emails to PhishDestroy.
- Claim #4 falls apart against any reasonable definition of registrar abuse handling.

A statement that fails on every sentence, in a context that should never have produced a statement at all (registrars do not normally tweet defenses of suspected operators), is not a "review." It is a position.

The position is: **NameSilo, LLC (IANA #1479) is on the operator's side.**

That is the position they put on the public record themselves.

This document, and the rest of this repository, is the receipt.

---

*Continue:* [The connection &rarr;](CONNECTION.md) · [The pressure campaign &rarr;](PRESSURE.md) · [Evidence index &rarr;](EVIDENCE_INDEX.md)
