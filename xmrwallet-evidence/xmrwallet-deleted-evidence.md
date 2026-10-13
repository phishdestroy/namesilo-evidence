# xmrwallet.com — Deleted Evidence (Full Archive)

> **The operator of xmrwallet.com deleted GitHub Issues #35 and #36 after being exposed. All evidence was archived before deletion.**

## What was deleted

On approximately 2026-02-23, after both escape domains (xmrwallet.biz and xmrwallet.cc) were suspended by registrars, the operator **nathroy** (Nathalie Roy) deleted:

- **Issue #35** — "xmrwallet.com: Fake Monero Wallet (Server-Side TX Hijacking)"
  - Full code analysis of `raw_tx_and_hash.raw = 0`
  - `session_key` decoded to reveal Base64-encoded view key
  - Production PHP endpoints not present in GitHub
  - 5.3-year commit gap documentation
  - Operator identity and infrastructure mapping

- **Issue #36** — "xmrwallet.com steals your Monero view key — proof from live network capture"
  - 109 HTTP requests captured via Firefox webRequest API
  - 43 instances of view key transmission in single session
  - 2 wallets compromised (existing + newly created)
  - Backdoor session `8de50123dab32` (10 requests, not user-initiated)
  - Verification signature analysis (spend key proof)

## Why deletion proves guilt

In 8 years of operation, the operator has **never once** provided:

| What we asked | What we got |
|---------------|-------------|
| Network capture proving viewkey is NOT sent to server | Nothing |
| Code proving signed TX IS broadcast (not `raw = 0`) | Nothing |
| Explanation for `session_key` containing `base64(viewkey)` | Nothing |
| Explanation for backdoor session `8de50123dab32` | Nothing |
| Explanation for `swept` TX type (not in Monero protocol) | Nothing |
| Any technical counter-argument of any kind | **Nothing. Ever.** |

You don't delete evidence you can technically rebut.

## Archived copies

| Archive | Link |
|---------|------|
| Full archived page (all evidence) | [deleted.html](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/deleted.html) |
| Issue #35 — full cached HTML | [cache-issue35](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/cache-issue35/) |
| Issue #36 — full cached HTML | [cache-issue36](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/cache-issue36/) |

## Timeline of destruction

```
2026-02-13  Issue #35 published — TX hijacking exposed
2026-02-18  Issue #36 published — live network capture with 43 viewkey transmissions
2026-02-??  xmrwallet.biz SUSPENDED by registrar
2026-02-??  xmrwallet.cc SUSPENDED by registrar
2026-02-23  Operator DELETES Issues #35 + #36. Wipes repo content.
2026-02-23  PhishDestroy publishes full archive. You're reading it now.
```

## Report

- [Full Investigation](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/)
- Report xmrwallet.com: abuse@namesilo.com
- FBI IC3: https://ic3.gov

---

*Investigation by [PhishDestroy Research](https://github.com/phishdestroy)*
