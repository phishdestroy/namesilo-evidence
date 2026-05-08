# How xmrwallet.com Steals Your Monero — Complete Technical Breakdown

> **Mirrored from [phishdestroy.io](https://phishdestroy.io/xmrwallet-namesilo-exposed) and [github.com/phishdestroy/DO-NOT-USE-xmrwallet-com](https://github.com/phishdestroy/DO-NOT-USE-xmrwallet-com) so it cannot be deleted.**

This document is a full technical dissection of the theft architecture embedded in xmrwallet.com's production code. Every claim below is backed by network captures, source-level analysis, and archived evidence. The site has operated for over 10 years under the protection of its registrar, NameSilo LLC.

---

## 1. View Key Theft

Every login to xmrwallet.com transmits the user's **private view key** to the server, encoded in Base64. This is not incidental — it is the core exfiltration mechanism.

**Authentication payload structure:**

```
POST /auth.php HTTP/1.1
Host: xmrwallet.com
Content-Type: application/x-www-form-urlencoded

session_key = [blob]:[base64(address)]:[base64(viewkey)]
```

The private view key is concatenated into a composite `session_key` parameter alongside the wallet address and a server-generated token. This three-part structure does not exist in the public GitHub repository (see Section 5).

Once captured, the view key is **retransmitted 40+ times per session** across 8 distinct PHP endpoints. There is no legitimate reason to transmit a private view key to a server at all — let alone repeatedly across multiple endpoints. The view key gives the operator full visibility into every incoming transaction, balance, and subaddress associated with the wallet.

---

## 2. Transaction Hijacking

When a user initiates a send transaction, the following JavaScript executes in production:

```javascript
raw_tx_and_hash.raw = 0  // user's signed TX — silently discarded
if (type == 'swept') {   // internal theft marker
  txid = 'Unknown transaction id'
}
```

**What this does:**

1. The user's legitimately signed transaction (`raw`) is zeroed out — it is never broadcast to the Monero network.
2. The server substitutes its own transaction, sweeping the wallet balance to an operator-controlled address.
3. The `'swept'` type flag is an internal marker for theft operations.
4. The user sees `"Unknown transaction id"` — a dead-end string that cannot be looked up on any block explorer.

The user believes their transaction was sent. In reality, their entire wallet balance has been swept to the attacker. The fake transaction ID ensures they cannot immediately verify the theft on-chain.

---

## 3. The 8 PHP Endpoints — View Key Transmission Counts

Every authenticated session floods the user's private view key across the following endpoints:

| Endpoint | Method | View Key Transmissions | Notes |
|---|---|---|---|
| `/auth.php` | POST | 1 (initial) | Login — session_key contains base64(viewkey) |
| `/getheightsync.php` | POST | 12 | Block height sync — viewkey sent every poll cycle |
| `/gettransactions.php` | POST | 10 | Transaction history fetch |
| `/getbalance.php` | POST | 6 | Balance check |
| `/getsubaddresses.php` | POST | 4 | Subaddress enumeration |
| `/support_login.html` | POST | 1 | Viewkey + session_id — **backdoor endpoint** |
| Additional endpoints | POST | ~6+ | Miscellaneous polling and state sync |

**Total: 40+ private view key transmissions per session.**

The `/support_login.html` endpoint is particularly notable: it transmits both the view key and a session identifier, functioning as a secondary exfiltration channel and operator backdoor. This endpoint has no user-facing purpose.

---

## 4. Why This Cannot Be Accidental

A legitimate client-side Monero wallet:

- **Never** transmits the private view key to any server.
- **Never** zeros out signed transactions.
- **Never** uses internal type markers like `'swept'`.
- **Never** returns fake transaction IDs.

The architecture is purpose-built for theft. The view key provides surveillance (know when funds arrive), and the transaction hijacking provides extraction (steal the funds when the user tries to move them — or sweep them proactively).

---

## 5. Production vs. GitHub Repository Divergence

xmrwallet.com maintains a public GitHub repository to project legitimacy. The production code diverges from it in critical ways:

| Aspect | GitHub (Public) | Production (Live) |
|---|---|---|
| Authentication | 2-part (address + key) | **3-part**: `session_key = token : base64(address) : base64(viewkey)` |
| Parameters | Standard | `session_key`, `verification`, `data` — **completely absent from public repo** |
| View key handling | Client-side only | Transmitted to server 40+ times per session |
| Commit history | **5.3-year gap** (2018–2024) | Code evolved continuously during gap |
| Transaction signing | Normal flow | `raw_tx_and_hash.raw = 0` — TX discarded |

**The 5.3-year commit gap (2018–2024)** is the smoking gun for intent. The production site was actively maintained, updated, and operated throughout this period — but no commits were pushed to GitHub. The theft architecture was developed and deployed off-repository, deliberately hidden from public review.

When commits resumed in 2024, the production-specific theft parameters (`session_key` three-part format, `verification`, `data`) were still absent from the repository. The public repo is a facade.

---

## 6. Seven Documented Falsehoods from NameSilo

When confronted with the above evidence, NameSilo LLC (the domain registrar) issued statements containing seven demonstrable falsehoods. Each is refuted by the technical record:

### Falsehood 1: "Domain Compromise" (the site was hacked)

**Reality:** The theft architecture consists of 8 coordinated PHP endpoints, a 5.3-year gap in the GitHub commit history during which production code evolved, and JavaScript-level transaction hijacking. This is not the result of a compromise — it is a deliberately engineered system built and maintained over years.

### Falsehood 2: "No Prior Reports"

**Reality:** Multiple prior reports existed and were publicly accessible:
- **VirusTotal:** 6 of 93 security vendors flagged xmrwallet.com as malicious
- **Trustpilot:** User complaints documenting fund theft
- **BitcoinTalk:** Scam warnings posted by community members
- **r/Monero:** The domain was banned from the subreddit in **2018** — eight years before NameSilo's claim of no prior reports

### Falsehood 3: "Registrant Innocence" (the domain owner is a victim)

**Reality:** The registrant:
- Maintains **4 escape/redirect domains**, each prepaid for **5–10 years**
- **Deleted 21+ GitHub issues** reporting theft — active evidence suppression
- **Hired developers** to maintain and evolve the theft infrastructure
- Operates under the alias `nathroy` with contact `royn5094@protonmail.com`

### Falsehood 4: "Immediate Remediation"

**Reality:** The theft code remained in production during and after NameSilo's public statement. Zero commits were made to address any of the documented theft mechanisms. The transaction hijacking JavaScript (`raw_tx_and_hash.raw = 0`) was still live. No endpoint was modified. No parameter was removed.

### Falsehood 5: "VirusTotal Delisting Success"

**Reality:** NameSilo publicly praised the removal of **Fortinet's phishing detection** from VirusTotal — without verifying that the underlying phishing code had been removed. It had not. NameSilo celebrated the removal of the *warning* while the *threat* remained fully operational. This is the registrar equivalent of celebrating that the smoke detector was disabled while the building burns.

### Falsehood 6: "Abuse Report Recency"

**Reality:** NameSilo shifted the burden of proof to researchers, implying that the recency of formal abuse reports absolved them. The r/Monero ban dates to 2018. The theft architecture predates all formal reports. The registrant's deletion of 21+ GitHub issues demonstrates active suppression of the reporting pipeline.

### Falsehood 7: "Investigation Reopening"

**Reality:** NameSilo's "reopened investigation" consisted of contacting the scammer directly and documenting his claims as findings — without independent technical analysis. The registrar accepted the operator's denials at face value while ignoring the code-level evidence provided by researchers.

---

## 7. Infrastructure IOCs

### Domains

| Domain | Registrar | Registration | Expiry | Purpose |
|---|---|---|---|---|
| `xmrwallet.com` | NameSilo | ~2016 | 2026+ | Primary theft site |
| Escape domain 1 | NameSilo | Prepaid | 5–10yr | Redirect/fallback |
| Escape domain 2 | NameSilo | Prepaid | 5–10yr | Redirect/fallback |
| Escape domain 3 | NameSilo | Prepaid | 5–10yr | Redirect/fallback |
| Escape domain 4 | NameSilo | Prepaid | 5–10yr | Redirect/fallback |

### Network Infrastructure

- **Hosting:** Shared infrastructure, rotated periodically
- **Tor:** .onion mirror maintained for operational resilience
- **MX records:** Configured for the domain (operator receives email at domain)
- **NS records:** NameSilo default nameservers
- **Cookies:** Session tracking cookies persist across visits
- **Analytics:** See Section 8

*Full IOC list with specific IPs, onion addresses, and DNS records maintained in the primary evidence repository.*

---

## 8. Google Trackers — In a "Privacy" Wallet

xmrwallet.com markets itself as a privacy-focused Monero wallet. Its production code includes the following Google tracking infrastructure:

| Tracker | ID / Type | Purpose |
|---|---|---|
| **Google Tag Manager (GTM)** | Container deployed | Centralized tag management |
| **Google Analytics (UA)** | `UA-116766241-1` | Legacy analytics — user behavior tracking |
| **Google Analytics 4 (GA4)** | Active property | Modern analytics — event-based tracking |
| **DoubleClick** | Pixel/tag active | Google advertising network integration |

A wallet that claims to protect user privacy while feeding every pageview, click, and session to Google's advertising infrastructure is not a privacy tool. It is a surveillance tool with a privacy label.

The Google Analytics property `UA-116766241-1` is a stable identifier that links all xmrwallet.com traffic to a single Google Analytics account controlled by the operator.

---

## 9. Security Vendor Detections

As of the last check:

- **VirusTotal:** 6 of 93 vendors flagged `xmrwallet.com` as malicious
- **Fortinet:** Classified as **Phishing** (subsequently delisted — see Falsehood 5)
- **ScamAdviser:** Trust score **1 out of 100**
- Additional vendors: Various classifications including malware, phishing, and suspicious

The low detection rate (6/93) reflects the general difficulty of detecting application-layer theft in web wallets via automated scanning. The theft is in the JavaScript and PHP logic, not in the network signatures that most automated scanners look for.

---

## 10. Custom CAPTCHA System (March 2026)

In March 2026, xmrwallet.com deployed a custom CAPTCHA system — replacing standard solutions with a bespoke implementation. This confirms at least a **second developer** is actively working on the project.

**CAPTCHA components:**

- **Proof-of-Work (PoW):** Client-side computational challenge
- **Slider verification:** Drag-to-complete UI element
- **Trajectory analysis:** Mouse movement pattern tracking

**Purpose:** Block automated analysis tools and abuse reporters from accessing the site programmatically.

**Result:** The custom CAPTCHA was **defeated within hours** of deployment. A 100% bypass was achieved, restoring full automated access. The implementation, while novel in combination, contained exploitable weaknesses in each component.

The deployment of a custom CAPTCHA — rather than using an off-the-shelf solution like hCaptcha or Turnstile — suggests the operator cannot or will not integrate with legitimate service providers, likely due to abuse policy enforcement.

---

## 11. What Victims Should Do

If you have ever logged into xmrwallet.com, your private view key has been compromised. If you have funds in a wallet accessed through xmrwallet.com, act immediately.

### Immediate Steps

1. **Move all funds NOW.** Use the [official Monero GUI or CLI wallet](https://www.getmonero.org/downloads/) on a clean machine. Restore your wallet from your 25-word mnemonic seed. Send your entire balance to a new wallet that has never touched xmrwallet.com.

2. **Do NOT contact xmrwallet.com support.** The "support" system (`/support_login.html`) is itself a data exfiltration endpoint. Any interaction provides the operator with additional session data.

3. **Report the crime:**
   - **IC3** (FBI Internet Crime Complaint Center): [ic3.gov](https://www.ic3.gov/)
   - **FTC** (Federal Trade Commission): [reportfraud.ftc.gov](https://reportfraud.ftc.gov/)
   - **ICANN** (domain abuse): [icann.org/compliance/complaint](https://www.icann.org/compliance/complaint)
   - **Local law enforcement:** File a police report with the amount stolen

4. **Use safe alternatives going forward:**
   - [getmonero.org](https://www.getmonero.org/) — Official Monero project, GUI and CLI wallets
   - [Cake Wallet](https://cakewallet.com/) — Open-source mobile wallet
   - [Feather Wallet](https://featherwallet.org/) — Lightweight desktop wallet
   - **Ledger / Trezor** — Hardware wallets with Monero support

### Key Principle

A legitimate Monero wallet **never needs your private view key on a server.** If any web wallet transmits your keys to a backend, it is not a wallet — it is a trap.

---

## Revision History

| Date | Change |
|---|---|
| 2026-05-07 | Initial technical breakdown compiled and mirrored |

---

*This document is part of the PhishDestroy evidence archive. It is published across multiple platforms and pinning services to ensure permanence. For the full investigation, see [phishdestroy.io](https://phishdestroy.io) and the associated GitHub repositories.*
