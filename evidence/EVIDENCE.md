# Evidence manifest

Every screenshot here is a verbatim, unedited capture of correspondence,
public posts, or platform UI. Pixel-for-pixel integrity is asserted via
SHA-256 in [`../EVIDENCE_HASHES.txt`](../EVIDENCE_HASHES.txt).

Verify with:

```bash
cd evidence && sha256sum -c ../EVIDENCE_HASHES.txt
```

| File | Section | Date | What it shows |
|---|---|---|---|
| `01-operator-email-feb16.png` | §1 | 2026-02-16 | First email from N.R., the `xmrwallet[.]com` operator, asking PhishDestroy to remove the abuse report. Sent to `abuse@phishdestroy.io` after a GitHub Issue was opened on the operator's repo. |
| `01-phishdestroy-reply-feb16.png` | §1 | 2026-02-16 | PhishDestroy's same-day technical reply. Documents the eight-PHP-endpoint key exfiltration and the `session_key`/`raw_tx_and_hash.raw=0` divergence between the operator's GitHub code and his production site. Closes with the explicit warning: *"What happens next depends entirely on how you choose to proceed."* |
| `03-namesilo-statement-mar13.png` | §3 | 2026-03-13 | NameSilo's official tweet under the PhishDestroy investigation thread. The four-claim defense of `xmrwallet[.]com`, including the public commitment to "remove the website from VT reports." Permanently archived: https://ghostarchive.org/archive/CXXZ0 |
| `04-tweet-namesilo-is-lying.png` | §4 | 2026-03-16 | @Phish_Destroy: *"Let's be direct. @NameSilo is lying."* Account is now locked; this is the canonical copy. |
| `04-tweet-press-secretary.png` | §4 | 2026-03-16 | @Phish_Destroy thread headline: *"@NameSilo is acting as press secretary for a $2M+ Monero theft operation."* |
| `04-tweet-honest-question.png` | §4 | 2026-03-16 | @Phish_Destroy: *"Honest question for @NameSilo: Who is this operator to you? Employee? Contractor? Friend of support staff? Relative?"* |
| `04-tweet-cryptopus-quote.png` | §4 | 2026-03-16 (quoting 2026-02-22) | Third-party reporting (CryptOpus, @ImCryptOpus): *"XMRWallet was reportedly shut down after allegedly operating for more than a decade as a fraudulent #Monero wallet, with estimates suggesting over $10M in user funds were stolen."* The thread @Phish_Destroy was tagging NameSilo under in the days before the lock. |
| `06-x-support-no-violation.png` | §6 | 2026-04-15 | X Support response to the @Phish_Destroy appeal: *"Our automated systems have determined there was no violation and have restored your account to full functionality."* The account is **still locked** despite this. |
| `06-x-support-subject-restored.png` | §6 | 2026-04-15 | Subject line of the same email: *"[4] Your account has been restored."* |
| `09-phishdestroy-platform.png` | §9 | snapshot | PhishDestroy Threat Intelligence Platform — 350,000+ malicious domains scanned, 54+ trusted partners. The actual operation NameSilo's takedown was aimed at. |

## What's NOT in this manifest

Several screenshots in the original working tree contain operational details
of PhishDestroy infrastructure (server credentials, internal dashboards) that
have nothing to do with the NameSilo / xmrwallet case and are deliberately
omitted from this public package. If a court order or ICANN compliance
inquiry requires them, contact `abuse@phishdestroy.io` directly.

## Chain of custody

- All screenshots were captured on the PhishDestroy researcher workstation at the times stated above.
- Files were copied verbatim into this repository on 2026-05-07 and SHA-256-fingerprinted at the same commit.
- No screenshot has been edited, cropped, redacted, or recompressed for this package.
- The canonical copies are in this Git repository. Modification history is visible in `git log -p evidence/`.

## Reuse for legal proceedings

See [`../LICENSE`](../LICENSE) for the explicit evidentiary-use grant. No
further authorization from PhishDestroy is required to attach these
screenshots to any complaint, filing, or proceeding.
