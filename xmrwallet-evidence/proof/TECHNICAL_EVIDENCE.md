# 🔬 Technical Proof

Raw network capture evidence from a live session on www.xmrwallet.com.
Captured using Firefox WebExtension (webRequest API).

## What was captured

- 105 HTTP requests to xmrwallet.com
- 3 POST requests to `/auth.php` with wallet credentials
- 40 POST requests where `session_key` contains Base64-encoded private view key
- 1 automatic call to `/support_login.html` with a different session_id (backdoor indicator)

## Wallets exposed during the test session

**Wallet A (existing wallet, isnew=0):**
```
address: 46EkQdF7iQ4i4Ah935SipgXbDSryh5yv76UnhsPXTaUYegCMJPqDN88UKCuraauhmbYBK2YzDX76E46KQHAKYV9a63vokJb
viewkey: efba13ecb8b360660a3dcaafaf7cf99149713d064b9d64997b2454d58ee67800
```

**Wallet B (created on the site, isnew=1):**
```
address: 49uroty7nZtKkendSiLWv5avrtJvRqhXTG6t4Xy2ByDzhwxxKimTz7C3m1WwHTJiUcBZspQi3FygQXP55wQfKBHKB8U8pYT
viewkey: 7c6e0a46172809792b524466e4a86b58db3b48e5d3441dead24416d79bbc9909
```

## How session_key works (the damning part)

The server issues a `session_key` after login. Format:
```
[encrypted_blob]:[base64(address)]:[base64(viewkey)]
```

Every subsequent API call sends this token back to the server.
The server therefore receives the view key on **every single request**.

Verify yourself:
```python
import base64

# Part 1 of session_key (colon-separated)
addr_b64 = "NDZFa1FkRjdpUTRpNEFoOTM1U2lwZ1hiRFNyeWg1eXY3NlVuaHNQWFRhVVllZ0NNSlBxRE44OFVLQ3VyYWF1aG1iWUJLMll6RFg3NkU0NktRSEFLWVY5YTYzdm9rSmI="
print(base64.b64decode(addr_b64).decode())
# → 46EkQdF7iQ4i4Ah935SipgXbDSryh5yv76UnhsPXTaUYegCMJPqDN88UKCuraauhmbYBK2YzDX76E46KQHAKYV9a63vokJb

# Part 2 of session_key
vk_b64 = "ZWZiYTEzZWNiOGIzNjA2NjBhM2RjYWFmYWY3Y2Y5OTE0OTcxM2QwNjRiOWQ2NDk5N2IyNDU0ZDU4ZWU2NzgwMA=="
print(base64.b64decode(vk_b64).decode())
# → efba13ecb8b360660a3dcaafaf7cf99149713d064b9d64997b2454d58ee67800
```

## Endpoints that received the view key

| Endpoint | Count |
|----------|-------|
| /getheightsync.php | 12 |
| /gettransactions.php | 10 |
| /getbalance.php | 6 |
| /dashboard.html | 4 |
| /send.html | 3 |
| /receive.html | 3 |
| /getsubaddresses.php | 1 |
| /getoutputs.php | 1 |
| **Total** | **40** |

## GitHub Issues (deleted by operator — archived)

- Archive: https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/deleted.html
- Issue #35 cached copy (full HTML): https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/cache-issue35/
- Issue #36 cached copy (full HTML): https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/cache-issue36/
- Full local archive with screenshots and code: https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/deleted.html
