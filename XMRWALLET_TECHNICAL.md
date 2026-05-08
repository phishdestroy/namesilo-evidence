# Technical Breakdown — `xmrwallet[.]com` is a Server-Side Key Drainer

> **The "compromised a few months ago" framing in NameSilo's March 13 statement is impossible. The theft mechanism is built into the production site itself, has been there for ~10 years, and is the entire reason the site exists.**

This document captures the technical observations PhishDestroy delivered to the operator (N.R.) on **February 16, 2026** — the same observations that triggered the operator's three-email pushback, and that NameSilo later attempted to dismiss without addressing.

The full reproducible breakdown lives at:
**→ [phishdestroy.io/xmrwallet-namesilo-exposed](https://phishdestroy.io/xmrwallet-namesilo-exposed)**

This document is the case-file summary. Use it for ICANN compliance filings, IC3 reports, civil claims, and journalist briefings.

---

## TL;DR — eight indicators that don't survive the "compromise" theory

A web wallet that is genuinely non-custodial — *as `xmrwallet[.]com` claims to be in its homepage copy, in the operator's GitHub repo, and in the operator's emails to PhishDestroy* — must satisfy a small list of structural properties:

1. The signed transaction the user authorises **is the transaction that gets broadcast**.
2. The private spend key, view key, and seed never leave the user's device.
3. The frontend code visible in the page **is** the code performing the cryptography.
4. There is no production endpoint that the published source code does not document.

`xmrwallet[.]com` violates **all four**, and has done so for approximately a decade.

| # | Observable in production | What it implies |
|---|---|---|
| 1 | `raw_tx_and_hash.raw = 0` — the client-generated transaction is constructed and **immediately discarded** | The site is performing a "ceremony" transaction in the browser purely for UX; the real transaction is built elsewhere. |
| 2 | The **backend** constructs and broadcasts a separate transaction, independently of whatever the client signed | The user is not signing the transaction that moves their funds. |
| 3 | A `session_key` parameter is present in production HTTP requests **and absent** from the operator's public GitHub repository | The production site is materially different from the "open source" code the operator points to. |
| 4 | The `session_key` payload contains the **full wallet address** and the **base64-encoded private view key** | These are exactly the materials needed for a server to scan and sweep an account. |
| 5 | A non-standard transaction `type == 'swept'` is observed | This is not a normal Monero transaction type. It is the operator's internal label for funds being lifted from a victim wallet. |
| 6 | These `swept` transactions pair with `Unknown transaction id` on the legitimate Monero network | Server-side initiated transactions, broadcast through operator infrastructure, not visible via standard tooling. |
| 7 | A `verification` parameter and a separate **encrypted payload** are sent to the backend on every transaction; neither is documented in the public repo | Unauthenticated client-side code accepts these on faith because the user has no path to inspect them. |
| 8 | The HTTP API to the backend has **8 distinct PHP endpoints** dedicated to this exfiltration plumbing | A non-custodial wallet should have, at most, a relay endpoint and an explorer-proxy endpoint. Eight is the signature of a stack designed to extract, not to relay. |

Each of these indicators is independently reproducible from a clean machine, against the live `xmrwallet[.]com` infrastructure, with no privileged access required.

---

## What "compromised" would have looked like, if it were real

NameSilo's March 13 statement claims the domain was *"compromised a few months ago (during which a copy of the webpage was replaced with a crypto-drainer)."*

A genuine compromise of an open-source wallet would leave a forensic trail:

| Forensic indicator | Status on `xmrwallet[.]com` |
|---|---|
| Diff between the operator's GitHub repo at commit X and the deployed code, showing the moment of modification | **No such diff exists.** The production code has carried the `session_key` exfiltration parameters for years before "a few months ago." |
| DNS / hosting / TLS-cert changes around the alleged compromise window | **None visible** in passive DNS or in CT-log timeline. |
| Incident-response statement from the registrant naming the compromise vector | **Never issued.** The operator's own emails to PhishDestroy in February 2026 defend the site as his own work — never claim a hack. |
| A clear before/after delta in the production behavior | **None visible.** The eight endpoints have been stable for years. |
| Backup of the legitimate version anywhere | **None offered.** If a clean copy of `xmrwallet[.]com` ever existed, the operator and registrar have made no effort to restore it. |

The "compromise" framing is incompatible with **every** technical indicator. It is also incompatible with the operator's own email correspondence, where he never makes the claim.

The framing first appears in NameSilo's tweet of March 13, 2026, **introduced to the public record by the registrar**, not by the registrant.

---

## What the eight PHP endpoints do

We will not publish the endpoint URLs in this public document, because their exact form is useful for forensic confirmation and we would prefer to preserve that confirmation channel for ICANN compliance officers, security vendors, and any prosecutor who reaches out via [`abuse@phishdestroy.io`](mailto:abuse@phishdestroy.io).

In summary, the endpoints implement, between them:

1. **Session establishment.** A handshake that issues the `session_key` cookie and binds it to the wallet's public address.
2. **Private-view-key registration.** The browser is induced to send the user's view key, base64-encoded inside `session_key`, on the pretense of "syncing" wallet history. This alone is enough to track every incoming transaction to the wallet.
3. **Transaction "ceremony" relay.** Accepts the client-built transaction, returns success, then discards it. Used purely for UX so the user sees a "broadcast" confirmation.
4. **Server-side transaction construction.** Builds the actual fund-moving transaction on operator infrastructure, using the registered view key and the operator's own outputs.
5. **Sweep dispatch.** The "type == 'swept'" path — the operator's internal name for the lift.
6. **Encrypted payload exchange.** A bidirectional channel for parameters the operator does not want visible in cleartext to a passive observer or to the user's browser dev-tools.
7. **Backend "verification" RPC.** A check that the client is authenticated to the session before any of the above happens — used to filter out passive scanners and bots.
8. **Telemetry / logging.** Operational endpoint reporting victim browser fingerprints back to operator infrastructure.

None of these endpoints exist in the operator's public GitHub repository. **All of them are live in production right now.**

---

## What three other registrars saw, and what they did about it

`xmrwallet[.]com` was not unique to NameSilo. Operator-controlled mirrors of the same drainer were registered across multiple registrars during the same window. The evidence package distributed to all of them was identical.

| Registrar | Action on identical evidence | Time to action |
|---|---|---|
| **PublicDomainRegistry (PDR)** | Suspended | Days |
| **WebNic** | Suspended | Days |
| **NICENIC** | Suspended | Days |
| **NameSilo** | **Public defense + offer to scrub VirusTotal** | — |

Three independent registrar abuse teams — including NICENIC, which we have publicly documented for years as one of the slowest abuse handlers in the industry — reached the same conclusion: **suspend the domain.** Only NameSilo reached a different one.

---

## What we sent the operator, on February 16, 2026

The exchange was civil, technical, and explicit. It is preserved in [`evidence/01-operator-email-feb16.png`](evidence/01-operator-email-feb16.png) and [`evidence/01-phishdestroy-reply-feb16.png`](evidence/01-phishdestroy-reply-feb16.png). The operative paragraph from our reply:

> "The current assessment stands and is technically grounded. The behavior aligns with known high-risk transaction handling patterns. Dismissing findings without addressing these mechanics does not change the conclusion.
>
> If this remains a technical discussion, it stays at this level.
>
> If it escalates — through continued denial or misrepresentation — it may justify a complete end-to-end audit with full documentation, reproducible evidence, and formal submission to relevant security and infrastructure channels.
>
> **Nothing here is based on assumptions — only on observable system behavior and verifiable logic. What happens next depends entirely on how you choose to proceed.**"

The operator chose to escalate. So did his registrar.

---

## What this means for victims

If you sent any amount of Monero through `xmrwallet[.]com`, the technical realities above mean two things:

1. **The operator already has your private view key.** From the moment you imported your seed into the site, the `session_key` parameter transmitted that view key to operator infrastructure. The operator can monitor, in real time, every incoming transaction to the wallet.
2. **The operator may not have your spend key, depending on which UI flow you used.** The view key alone is enough to track funds. The spend key is what authorises sweeps. If the spend key was extracted, the funds are gone. If only the view key was, the funds are *trackable but not yet swept* — and **moving them out of that wallet, to a fresh seed, on a clean machine, immediately, is the right action**.

**Do not contact `xmrwallet[.]com` support.** Do not paste anything into a "recovery" form. Use a different wallet client (recommended: the official Monero GUI, or Monero CLI tools) on a clean machine, generate a new seed, sweep your funds out before the operator notices.

For complaint channels, see [`README.md` §11](README.md#11-victim-resources--legal-use).

---

## What this means for security vendors

NameSilo's commitment to *"removing the website from VT reports"* is, in plain terms, a registrar lobbying on behalf of a confirmed scammer to have their detections lifted.

Detections of `xmrwallet[.]com` should be **strengthened**, not relaxed, on the basis of:

- The reproducible technical indicators above
- The fact that three registrars suspended on identical evidence
- The pattern of the operator and the registrar attempting to silence external researchers
- The presence of the `session_key`/private-view-key exfiltration in production code that is not visible in the operator's public repo

If your firm has a formal disagreement process with NameSilo about specific detections on this domain, please contact **[abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)** before adjusting them. We will provide raw HTTP traces, source-port pairs, and `session_key` payloads under NDA where appropriate.

---

## Pointers to the deeper material

- **Full public technical breakdown:** [phishdestroy.io/xmrwallet-namesilo-exposed](https://phishdestroy.io/xmrwallet-namesilo-exposed)
- **Earlier Medium write-up of the scam itself:** [phishdestroy.medium.com/xmrwallet-com-2953f35b8a79](https://phishdestroy.medium.com/xmrwallet-com-2953f35b8a79)
- **Earlier GitHub evidence repository:** [github.com/phishdestroy/DO-NOT-USE-xmrwallet-com](https://github.com/phishdestroy/DO-NOT-USE-xmrwallet-com)
- **Operator's first email (the "we are not phishing" denial):** [`evidence/01-operator-email-feb16.png`](evidence/01-operator-email-feb16.png)
- **PhishDestroy's reply (technical breakdown + escalation warning):** [`evidence/01-phishdestroy-reply-feb16.png`](evidence/01-phishdestroy-reply-feb16.png)

---

*Continue:* [The connection →](CONNECTION.md) · [The lies →](THE-LIES.md) · [Pressure campaign →](PRESSURE.md) · [Master proof index →](PROOFS.md)
