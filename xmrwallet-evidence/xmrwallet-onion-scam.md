# xmrwallet.com Tor (.onion) — Same Scam, Different Address

> **The xmrwallet Tor onion address runs the same theft infrastructure as the clearnet site.**

## Onion address

```
xmrtor3fsapuu6y26za7vpzox4vpaj6ny5viq2arbmozm7kg6jitnlid.onion
```

Historical (deprecated Tor v2):
```
xmrwalletdatuxms.onion
```

## Why this matters

The Tor version of xmrwallet.com runs **identical code** to the clearnet site:
- Same `session_key` containing your Base64-encoded private view key
- Same `raw_tx_and_hash.raw = 0` — your transaction discarded, server builds its own
- Same `type == 'swept'` theft marker
- Same `/support_login.html` backdoor endpoint

Using Tor does not protect you — the theft happens **server-side**. Your view key is sent to **their** server regardless of how you connect.

## The Tor trap

The operator advertises the .onion address specifically to attract privacy-conscious users — the exact demographic most likely to:
1. Hold significant XMR amounts
2. Trust a service offering "private" access
3. Be less likely to report theft to authorities

## Status

The .onion address remains **active** as of February 2026. Unlike clearnet domains, Tor addresses cannot be suspended by registrars.

## Full investigation

- [Full Evidence](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/)
- [Deleted Issues Archive](https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/deleted.html)
- [VirusTotal — 6/93 flag clearnet as malicious](https://www.virustotal.com/gui/domain/www.xmrwallet.com)

## Use safe wallets instead

- [Feather Wallet](https://featherwallet.org) — built-in Tor, open source, no server-side keys
- [Monero GUI](https://getmonero.org/downloads) — official wallet, connect via your own node

---

*Investigation by [PhishDestroy Research](https://github.com/phishdestroy)*
