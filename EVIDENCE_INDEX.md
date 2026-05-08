# Evidence Index

Every piece of evidence in this repository, indexed. Each row links to the file, gives the date and origin, states what it proves, and is independently verifiable via SHA-256.

To verify integrity:

```bash
cd evidence && sha256sum -c ../EVIDENCE_HASHES.txt
```

All ten files must report `OK`. If any fail, the local copy has been tampered with — open an Issue and we will investigate.

---

## §1 — How it started

| File | Date | Source | What it proves |
|---|---|---|---|
| [`evidence/01-operator-email-feb16.png`](evidence/01-operator-email-feb16.png) | 2026-02-16 | Operator (N.R.) → `abuse@phishdestroy.io` | The operator wrote to PhishDestroy first, defending his code as his own work, asking for the report to be removed. He never claimed a hack. This contradicts NameSilo's later "compromised" framing. |
| [`evidence/01-phishdestroy-reply-feb16.png`](evidence/01-phishdestroy-reply-feb16.png) | 2026-02-16 | PhishDestroy → operator | Same-day technical reply, documenting the eight-PHP-endpoint key exfiltration and the explicit warning: *"What happens next depends entirely on how you choose to proceed."* Establishes that PhishDestroy gave the operator a clean exit before any escalation. |

---

## §3 — NameSilo's statement

| File | Date | Source | What it proves |
|---|---|---|---|
| [`evidence/03-namesilo-statement-mar13.png`](evidence/03-namesilo-statement-mar13.png) | 2026-03-13 | [@NameSilo official] | The four-claim public defense of `xmrwallet[.]com`. Permanently archived: [ghostarchive.org/archive/CXXZ0](https://ghostarchive.org/archive/CXXZ0). Each claim is debunked in detail in [`THE-LIES.md`](THE-LIES.md). |

---

## §4 — Public rebuttal (now invisible from locked account)

| File | Date | Source | What it proves |
|---|---|---|---|
| [`evidence/04-tweet-namesilo-is-lying.png`](evidence/04-tweet-namesilo-is-lying.png) | 2026-03-16 | @Phish_Destroy | Direct accusation, citing the operator's own emails as proof the "compromised" framing was fabricated. |
| [`evidence/04-tweet-press-secretary.png`](evidence/04-tweet-press-secretary.png) | 2026-03-16 | @Phish_Destroy | Thread headline: *"NameSilo is acting as press secretary for a $2M+ Monero theft operation."* |
| [`evidence/04-tweet-honest-question.png`](evidence/04-tweet-honest-question.png) | 2026-03-16 | @Phish_Destroy | The relationship question put to NameSilo directly: *"Who is this operator to you? Employee? Contractor? Friend of support staff? Relative?"* — never answered. |
| [`evidence/04-tweet-cryptopus-quote.png`](evidence/04-tweet-cryptopus-quote.png) | 2026-03-16 (quoting 2026-02-22) | @Phish_Destroy quoting [@ImCryptOpus](https://twitter.com/ImCryptOpus) | Third-party reporting from Feb 22, 2026: XMRWallet shutdown, $10M+ stolen. Establishes that public reporting on this domain predates PhishDestroy's investigation by months and contradicts NameSilo's "no abuse reports received" claim with externally authored material. |

---

## §6 — The smoking gun (X cleared us, the lock didn't move)

| File | Date | Source | What it proves |
|---|---|---|---|
| [`evidence/06-x-support-no-violation.png`](evidence/06-x-support-no-violation.png) | 2026-04-15 | X Support → @Phish_Destroy | *"Our automated systems have determined there was no violation and have restored your account to full functionality."* The lock is still in place anyway. |
| [`evidence/06-x-support-subject-restored.png`](evidence/06-x-support-subject-restored.png) | 2026-04-15 | X Support → @Phish_Destroy | Subject line: *"[4] Your account has been restored."* — confirming the body of the message, in X's own metadata. |

These two together prove that a human agent at X manually overrode an automated determination of "no violation" — the only known mechanism for which is the **Gold Checkmark live-support channel**, the paid corporate access tier NameSilo holds.

---

## §9 — What NameSilo tried to silence

| File | Date | Source | What it proves |
|---|---|---|---|
| [`evidence/09-phishdestroy-platform.png`](evidence/09-phishdestroy-platform.png) | snapshot | PhishDestroy production dashboard | The actual operation NameSilo's takedown was aimed at: 350,000+ malicious domains scanned, 54+ trusted partners. Not a hobbyist account. A professional anti-phishing platform whose research the registrar attempted to suppress. |

---

## SHA-256 fingerprints

```
919b5ee4c0f3a889381c644b557736d35625c69abaddd0ec7a8251eb514b0111  01-operator-email-feb16.png
ecced35149dbf19dff7399cd86708d28aff7b8ab044e132c4c92cafbe222a753  01-phishdestroy-reply-feb16.png
ad29e1d3d4803ff37c88ef860bef6de9e62f6ce533657f2e5c5460eb2e0b8ebf  03-namesilo-statement-mar13.png
6ffd3020793e9d850f0f10f7b4406b165e7d266d692a647ecb24eab9840e7f7f  04-tweet-cryptopus-quote.png
bbb0ecd0b7164bf91ace59bc0de01ae953a828a34765b36b89e07479e76ee674  04-tweet-honest-question.png
c556e13ff0e4265cbba76b6a518f0862dee67467c1b264181e27eef8046eda6a  04-tweet-namesilo-is-lying.png
c9007cb4acf1a264fb82e36a57708a1c35e4b6824eb2734a6a7dff095588bd84  04-tweet-press-secretary.png
2753d02ffeb1b2853bdc33ddec888e3652d9d3829b265e1228c8f28b53b86efa  06-x-support-no-violation.png
482d0ebba1656c3b338957e40cda0abc7a0017eb6ad08f2a0d639468298ccaf3  06-x-support-subject-restored.png
de5b430bb4cad5a422ddf1bb6a8c348fffdf0673e7ea8bfface4fb312f46b087  09-phishdestroy-platform.png
```

Canonical, machine-readable form: [`EVIDENCE_HASHES.txt`](EVIDENCE_HASHES.txt).

---

## Materials not in this repository (available on request)

The following items are referenced in the case file but not published here, generally because they are operational, contain sensitive headers, or are being preserved for direct ICANN / regulatory / court submission:

- **The full email thread with the operator (Feb 16-Feb 17, 2026)**, including the *"Feel free to subpoena the domain registrar for my information"* line of February 17. Available to ICANN Compliance and law enforcement on request.
- **Full server-side capture of the eight `xmrwallet[.]com` PHP endpoints**, with raw HTTP traces showing the `session_key` exfiltration. Excerpted in the public technical breakdown at [phishdestroy.io/xmrwallet-namesilo-exposed](https://phishdestroy.io/xmrwallet-namesilo-exposed).
- **The 20+ historical abuse-report delivery receipts to NameSilo (2023-2026)**. Available on request to anyone testing the *"prior to that, we had received no abuse reports"* claim.
- **Internal mail-server logs** corroborating the dates and SMTP headers of the operator emails.
- **Source-IP DDoS analysis** linking inbound attack traffic to NameSilo reseller infrastructure. Pending separate publication.

For access, contact **[abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)** with a subject line that identifies your role and the specific materials you need.

---

*Continue:* [The connection &rarr;](CONNECTION.md) · [The lies &rarr;](THE-LIES.md) · [The pressure campaign &rarr;](PRESSURE.md)
