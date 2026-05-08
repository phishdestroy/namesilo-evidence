# Google Analytics on a "Privacy Wallet" + Victim Reports

---

## Part 1 — Google Analytics & Tag Manager: Why This Is a Red Flag

### The claim vs. reality

xmrwallet.com markets itself as:
> *"Send and receive Monero instantly. All while remaining in complete control of your coins & your keys."*

The reality, observed in live network traffic:

| Third-party tracker | Requests | Data sent to Google |
|---|---|---|
| `www.googletagmanager.com` | 12 | Page loads, user agent, referrer |
| `region1.analytics.google.com` | 5 | Full session behavior, timing |
| `www.google-analytics.com` | 3 | Page navigation, clicks |
| `stats.g.doubleclick.net` | 1 | Ad network tracking pixel |
| `www.google.com` | 3 | reCAPTCHA / signaling |

**Google Analytics ID confirmed in production code:**
```
UA-116766241-1
```

### Why Google Analytics is incompatible with a privacy wallet

**1. Google receives every page visit inside your wallet session.**

When you navigate to `/dashboard`, `/send`, `/receive`, `/transactions` — Google Analytics fires a pageview event. Google now knows:
- You use a Monero wallet
- Which pages you visited and in what order
- How long you spent on each page
- Your IP address (even with "anonymization", the full IP is processed server-side before truncation)
- Your browser fingerprint, screen resolution, language, timezone

This is not theoretical. These requests were captured in real traffic.

**2. Google Tag Manager is worse than Analytics alone.**

GTM is a JavaScript container loaded from Google's servers. It can inject **any** tracking code at any time — without changing the site's own source code. The site owner can add new trackers, pixel fires, or data collection scripts through the GTM dashboard alone, without a code deploy.

This means:
- The GitHub repository is irrelevant as a trust anchor
- Tracking behavior can change at any moment without public notice
- There is no way to audit what GTM is currently running without live traffic analysis

**3. Google Tag Manager as an attack surface.**

GTM accounts are secured only by a Google account password. If the GTM account (`GTM-XXXXX`) is compromised:
- An attacker can inject arbitrary JavaScript into the wallet page
- This JavaScript runs in the same browser context as the wallet
- It can read `localStorage`, `sessionStorage`, DOM content, form inputs — including seed phrases typed into the UI
- No code change to the wallet itself is required

This is not a hypothetical: GTM account hijacking has been documented as an attack vector in e-commerce (Magecart-style attacks). A Monero wallet is a significantly higher-value target.

**4. DoubleClick / Ad network on a financial privacy tool.**

`stats.g.doubleclick.net` is Google's advertising network tracker. Its presence on a financial privacy application is unexplainable by any legitimate technical requirement. It serves no wallet functionality. Its sole purpose is to track users across the web for ad targeting.

### Industry standard

For reference: no serious privacy-focused cryptocurrency tool loads Google Analytics or GTM. 

- **Monero GUI** (getmonero.org) — no analytics, no third-party JS
- **Feather Wallet** — no analytics, no third-party JS  
- **MyMonero** (official) — no GTM, no DoubleClick
- **Monerujo** (Android) — open source, no analytics

Running Google Analytics on a Monero wallet is not a minor oversight. It is a fundamental contradiction of the product's stated purpose.

---

## Part 2 — Victim Reports

The following reports were collected from public review platforms. Sources are linked.

> ⚠️ Note: Some negative reviews on Trustpilot have responses from xmrwallet.com claiming users were "using a phishing clone." This is the standard response. Our technical analysis confirms the funds loss mechanism exists in the **real** xmrwallet.com — not just clones.

---

### Trustpilot — www.trustpilot.com/review/www.xmrwallet.com

---

**"They stole $200 from me"**
> *"They are scammers. They stole $200 from me, leaving me high and dry. Don't trust them with a single cent! Avoid them at all costs!"*
— Trustpilot, page 3

xmrwallet.com response: *"I believe you are referring to a clone (phishing) site."*

---

**"Transferred to some other wallets"**
> *"This site is a scam, it worked good at first. I bookmarked it and using it for few days but one day i tried to move all funds out of it, it transferred to some other wallets instead of my mentioned wallet. They are scammers. Stay away."*
— Trustpilot, page 2

---

**"17.44 XMR — all gone"**
> *"I followed the owner's instructions [...] only to realize that my 17.44 XMR was all gone. I looked at my financial establishment, and the 17.44 XMR did in fact transfer to XMRwallet.com on March 8th. I have both the TxID & TX Key. I then also checked with walletmymonero and was able to confirm that my balance is 0.00."*
— Trustpilot, page 3

---

**"Funds stolen, no access"**
> *"Whatever you do, do NOT try to use this wallet. I created one this morning and initiated a transfer to my wallet. Since then I have been UNABLE TO ACCESS MY FUNDS."*
— Trustpilot, page 4

---

**"Transaction ID bd1e596d... — cannot verify"**
> *"I need to confirm my transfer in the exchanger, but why can't I verify the transaction using the private viewing key? Gives an error or does not find the payment. I wrote to the site's technical support by email asking them to provide me with a key for a transaction with ID bd1e596df30fa8f1e655c79ccfbca993d71844a5147a7dbfe71e4f695bb39f9b, but I've been waiting for a response for several days."*
— Trustpilot

---

**"Probably phishing scam, all funds were stolen"**
> *"Probably fishing scam, all funds were stolen. I can't blame xmrwallet.com because it could happen by other reasons, but anyway, don't use web wallet, use local wallet."*
— Trustpilot, page 4

---

### Sitejabber — www.sitejabber.com/reviews/xmrwallet.com
Rating: **1.5 / 5 stars** (4 reviews)

---

**Анна М. (Russia)**
> *"Yes its fake its not monero its scammers! Check get monero! Ban this! Reported bad fake! Stupid coder"*

---

**Никита Т. (Russia)**
> *"I do deposit 590 monero 2 day gone and they steal it! Please ban this site and FBI need arest it!"*
— **590 XMR stolen** (~$177,000 at current prices)

---

**colleen v.**
> *"Create wallet - put 20 xmr next day 0 xmr - Scammers owner! Report. Its not official site its fake site"*

---

### Scam-Detector — www.scam-detector.com

> *"SCAMMERS! I started dealing with them last year, i did not do my research well before i jumped in. I blamed myself for trusting them blindly, I lost contact when i wanted withdrawal, no response from customer support too."*

---

### ScamAdviser — www.scamadviser.com/check-website/xmrwallet.com

**Trust score: very low**

Notable findings from their automated analysis:
- Domain registrar has high percentage of fraud sites
- Owner identity hidden via privacy service
- Low Tranco rank (low traffic for a claimed major wallet)

---

### BitcoinTalk — bitcointalk.org

Thread: **[WARNING] XMRWallet.com Scams - Stay vigilant!**
URL: https://bitcointalk.org/index.php?topic=5540097.0

Public warning thread exists on the largest cryptocurrency forum.

---

## Part 3 — Pattern: Fake Positive Reviews

Trustpilot rating as of 2026-02-18: **4.2 / 5** (82 reviews)

Several observations raise concerns about review authenticity:

- Majority of positive reviews use near-identical phrasing: *"fast, secure, private, easy to use"*
- Many positive reviewers have only 1 review on their Trustpilot account
- Negative reviews consistently receive identical template responses from the operator
- The operator response to fund loss reports: always *"you used a phishing clone"* — never an acknowledgment of any architectural issue
- No positive review mentions the Google Analytics tracking, the session_key structure, or any technical detail — suggesting reviewers never inspected network traffic

---

## Summary

| Finding | Source |
|---|---|
| Google Analytics UA-116766241-1 on wallet pages | Live traffic capture |
| Google Tag Manager loading from Google CDN | Live traffic capture |
| DoubleClick ad tracker fired during wallet session | Live traffic capture |
| GTM enables arbitrary JS injection without code deploy | Architectural fact |
| Multiple reports of funds disappearing after deposit | Trustpilot, Sitejabber, Scam-Detector |
| 590 XMR ($177k) reported stolen in single incident | Sitejabber |
| Public scam warning thread on BitcoinTalk | bitcointalk.org/topic/5540097 |
| ScamAdviser: very low trust score | scamadviser.com |

**If you lost funds on xmrwallet.com:** document your TxID, wallet address, and the date of the loss. Contact us via GitHub issues. The more documented victims, the stronger the case for formal action.

---

*Collected by PhishDestroy Research | https://github.com/phishdestroy/destroylist*  
*Evidence base: live network capture 2026-02-18 + public review platforms*
