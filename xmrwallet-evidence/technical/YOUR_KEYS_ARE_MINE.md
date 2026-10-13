# 👋 Hi, your private view key is here

Yes, this folder name is literal.

Every time you opened this wallet — logged in, checked balance,
looked at transactions, clicked literally anything —
your **private Monero view key** was sent to the server.

Not once. **Every. Single. Request.**

Encoded in Base64 inside `session_key`, re-transmitted 40+ times per session.
The server owner can see every incoming transaction you ever received.
Forever. Irrevocably.

```
session_key = [encrypted blob] : base64(YOUR_ADDRESS) : base64(YOUR_VIEW_KEY)
```

Decode it yourself:
```python
import base64
part = "ZWZiYTEzZWNiOGIzNjA2NjBhM2RjYWFmYWY3Y2Y5OTE0OTcxM2QwNjRiOWQ2NDk5N2IyNDU0ZDU4ZWU2NzgwMA=="
print(base64.b64decode(part).decode())
# efba13ecb8b360660a3dcaafaf7cf99149713d064b9d64997b2454d58ee67800
# ↑ that's a real private view key captured from live traffic
```

Full proof (operator deleted originals, archived here): https://phishdestroy.github.io/DO-NOT-USE-xmrwallet-com/deleted.html
