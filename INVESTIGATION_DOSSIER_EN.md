# xmrwallet.com & NameSilo LLC -- Investigation Dossier

**Classification:** Public Evidence Archive
**Date:** 2026-05-18
**Investigators:** PhishDestroy (volunteer anti-scam initiative)
**Archive:** [phishdestroy.eth.limo](https://phishdestroy.eth.limo) | [GitHub](https://github.com/phishdestroy/ipfs-archive)
**Status:** Active investigation. EU law enforcement engaged. No factual rebuttal received from any party.

---

## EXECUTIVE SUMMARY

xmrwallet.com is a Monero cryptocurrency web wallet operating a server-side transaction hijacking scheme for approximately 8 years (2016–2026). The operator intercepts user view keys and constructs fraudulent transactions redirecting funds to operator-controlled addresses. The site's GitHub repository is a facade — the theft code exists only on the production server.

**Estimated total stolen: $100M+ in XMR** — this is a projected estimate, not a confirmed figure. The estimate is based on: (1) 8 years of continuous operation (2016–2026); (2) site traffic analysis; (3) documented victim reports with confirmed losses exceeding **$1.19M** from Reddit alone — a platform where 60% of xmrwallet-related posts were deleted by the operator. The true total cannot be independently verified because the operator has systematically destroyed victim evidence across every platform. The surviving reports represent a fraction of actual damage. The $100M+ projection reflects the scale implied by traffic volume and operational lifespan, not a sum of individually verified transactions.

**NameSilo LLC** (ICANN registrar, IANA #1479, Phoenix AZ, CSE:URL) publicly defended the operator, issued a statement containing 4 verifiably false claims, offered to remove VirusTotal malware detections for the scam site, and used paid Twitter/X Gold Checkmark support to silence the researchers who exposed it.

This dossier compiles evidence from: PullPush Reddit API, GitHub API, VirusTotal, SecurityTrails, Shodan, URLScan.io, Semrush, Hunter.io, crt.sh, CleanTalk, Wayback Machine, GhostArchive, and direct browser automation.

**Key numbers:**
- 40+ named victims on Reddit alone
- $1,194,660+ confirmed stolen (Reddit only, conservative)
- 93 Reddit posts analyzed, 60% removal rate in r/Monero
- 4 Reddit legal/DMCA takedowns filed by operator against victims
- 3-person sock puppet network (all Philippines-based)
- 9+ domain registrations by operator (presented as "phishing clones")
- 44 Twitter bot promotion accounts identified
- 15+ paid/sponsored SEO articles
- GPT-3.5 (free ChatGPT) recommends xmrwallet.com as #2 "Best Monero Wallet"
- 81.5% of NameSilo's 5.18M domains are dead (industry baseline: ~50%)

---

## 1. OPERATOR IDENTIFICATION

### Primary Identity

| Field | Value |
|-------|-------|
| GitHub | [nathroy](https://github.com/nathroy) (ID: 39167759) |
| Name | "Nathalie" (likely pseudonym) |
| Bio | "Cryptocurrency developer and jump rope expert" |
| Location | Canada |
| Email (commits) | admin@xmrwallet.com |
| Email (contact) | royn5094@protonmail.com (valid, spam history on CleanTalk) |
| Created | 2018-05-10 (same day as GitHub release) |
| Public repos | 0 (all hidden/deleted) |
| OS | macOS (leaked __MACOSX directory in 2024 commit) |

### Operator Emails

| Email | Status | Notes |
|-------|--------|-------|
| admin@xmrwallet.com | INVALID | No MX records |
| royn5094@protonmail.com | VALID (score 89) | Emailed PhishDestroy before publication |
| hassizabir@gmail.com | VALID (score 92) | Google Drive SEO order owner |
| titanmaster138@gmail.com | VALID (score 92) | Frontend developer/contractor |
| support@xmrwallet.com | INVALID | Dead |
| feedback@xmrwallet.com | INVALID | Dead |

### Second Developer

| Field | Value |
|-------|-------|
| Email | titanmaster138@gmail.com |
| GitHub | [pushpush](https://github.com/pushpush) |
| Role | Frontend contractor (May-Jun 2018, 11 commits) |
| Employer | Kinescope (kinescope.com) -- Russian video platform (registered Netherlands) |
| Note | Likely hired as contractor, may not know about the scam |

### Reddit Sock Puppet Network (Philippines)

| Account | Role | Evidence |
|---------|------|----------|
| u/WiseSolution | Original operator | 13 posts, 74 comments (2018-2022), signed as "Nathalie" |
| u/craig_d_79 | Subreddit moderator, SEO expert | Tagaytay/Cavite, Philippines. Requested r/xmrwallet unbanned |
| u/purpleandviolet | Main promoter, darknet targeting | 37 mentions of xmrwallet, 16 darknet sub comments. Leaked .onion address |
| u/Extra-Expert7685 | Support account | Philippines gambler (r/WeddingsPhilippines, r/DigitalbanksPh) |
| u/XMR-Expert | Single promo post | Aug 2024 |

### Other Operator Accounts

| Platform | Account | Purpose |
|----------|---------|---------|
| Medium | @oliviasmith1978 | Display name "Xmr Wallet", SEO backlink from DA 96 |
| Twitter/X | @XMRWalletCom | 189 followers, 0 tweets |
| Google Drive | hassizabir@gmail.com | SEO article orders, Kwork freelance platform |
| GitHub | BernickBeckForensic | Fake law firm account (intimidation) |
| GitHub | relly34mfk | SEO contractor (atadevelopers.com) |

---

## 2. TECHNICAL EVIDENCE -- HOW THE THEFT WORKS

### The Attack Vector

xmrwallet.com is NOT a simple phishing site. It is a functional Monero wallet with a server-side backdoor. The theft mechanism:

1. User creates wallet or logs in with seed phrase
2. Client-side JavaScript generates the wallet locally (this part works correctly)
3. **The view key and address are sent to the server** via POST requests (~40 requests per session)
4. Server stores `session_key` containing Base64-encoded view key
5. Server monitors incoming deposits in real-time using the view key
6. When a large deposit arrives, server constructs a fraudulent transaction that redirects funds
7. The wallet UI shows a fake "success" confirmation
8. The real transaction sends funds to the operator's address

### PHP Backend Endpoints (not in GitHub)

The following endpoints exist on the production server but are absent from the GitHub repository:

```
auth.php
getheightsync.php
gettransactions.php
getbalance.php
getunspentouts.php
submitrawtx.php
login.php
importwallet.php
```

### GitHub vs Production Divergence

| Aspect | GitHub | Production |
|--------|--------|-----------|
| app.js | 1.39MB, 5827 lines | Different (obfuscated) |
| PHP endpoints | 0 references | 8 endpoints active |
| session_key | 0 occurrences | Core theft variable |
| View key exfiltration | Not present | 40 POST requests/session |
| support_login.twig | Checks xmrwallet_spendkey, viewkey, address | Backdoor entry point |

### Commit Timeline

| Date | Event |
|------|-------|
| 2018-05-10 | First Release (admin@xmrwallet.com) |
| 2018-05-10 to 2018-11-07 | Active development (26 commits nathroy, 11 titanmaster138) |
| 2018-11-07 | "Bulletproof Update" -- **LAST COMMIT FOR 5.3 YEARS** |
| 2024-03-15 | Massive rewrite: app.js +5827/-74, monero.js complete rewrite |
| 2026-04-19 | GitHub Pages migration (site closure redirect) |
| 2026-05-05 | Farewell letter posted |

### Google Analytics

`UA-116766241-1` embedded on EVERY page including 404 and maintenance pages. No other sites found using this GA ID.

### Google Site Verification Changes (3 accounts)

```
2018-2021: JaFNzwwoh1fr6g30E3nHDtAds3uWZa_bkuK7ay0HOZc
2021-2026: bbN-0kgnaPq2JGH091MkAPAqOSd8T2qYo8qlIuqYUgQ
2026-Feb:  d-En_D3kMw6CqZpPwZeDn4ICI5Tyk1WvPYdVdGzEWr8
```

3 different verification tokens = at least 2 Google account changes over the site's lifetime.

---

## 3. DOMAIN INFRASTRUCTURE

### Operator-Controlled Domains

| Domain | Registrar | Status | Evidence |
|--------|-----------|--------|----------|
| xmrwallet.com | NameSilo -> Namecheap (May 2026) | GitHub Pages (dead) | Primary domain |
| xmrwallet.cc | PDR | SUSPENDED | Same IP as .me |
| xmrwallet.biz | Unknown | SUSPENDED | Same WHOIS state hash |
| xmrwallet.net | Unknown | DNS DEAD | Same WHOIS state hash |
| xmrwallet.me | Key-Systems | Active (backend disconnected) | Banner says "Our official domain" |
| xmrwallets.com | NameSilo DNS | Active | 4/4 WHOIS hashes identical to .com |
| xmrwallet.app | Njalla | Active (Vercel) | Privacy registrar |
| xmrwallet.org | Dynadot | Active | Created 2024-06-23 |
| xmrwallet.co | Namecheap | Active | Created 2020-07-17 |
| xmrwallet.in | Dynadot | Parked | Used in Google Ads phishing |

### WHOIS Hash Proof (Same Registrant)

```
xmrwallet.com:  city=7a96e04d2a2490b3 org=566bb814321610e4 state=e1c7c1911395a3cf zip=c692e0cb8851b160
xmrwallets.com: city=7a96e04d2a2490b3 org=566bb814321610e4 state=e1c7c1911395a3cf zip=c692e0cb8851b160
                4/4 hashes identical = SAME PERSON
```

Escape domains (xmrwallet.biz, .net, .me): all share state hash `e1a13ff8c8552296` = same registrant.

### Domain Transfer Chain

```
2014-08: Created on Namecheap (registrar-servers.com NS)
2015-08: Transferred to Enom/Tucows (name-services.com NS)
2016-08: Transferred to NameSilo (dnsowl.com NS, IANA #1479)
2018-03: NS changed to Cloudflare
2025-03: NS changed to DDOS-Guard (ns1/ns2.ddos-guard.net) -- Russian anti-DDoS
2026-04: NS back to NameSilo (premium-ns1-3.dnsowl.com)
2026-05-13: TRANSFERRED TO NAMECHEAP (new expiry 2036-05-13)
```

The operator transferred the domain 4 days before our latest data collection. Extended 1 year. NOT retiring.

### Server Infrastructure -- Russian Ecosystem

| IP | Provider | Hosted Domains | Co-Hosted With |
|----|----------|---------------|----------------|
| 186.2.165.49 | IQWeb FZ-LLC, UAE | xmrwallet.com (main) | **kinogo.ec** -- Russian pirate streaming |
| 185.129.100.248 | DDOS-Guard, RU | xmrwallet.cc, .me + full infra | **rustme.ru** (Minecraft), kuchaknig.org, mirpuffov.ru -- ALL Russian |
| 190.115.31.40 | DDOS-Guard | xmrwallet.biz, .net | **bclubs.to** -- BriansClub carding marketplace (stolen credit cards) |

ALL server infrastructure connects to Russian-language ecosystem. DDOS-Guard (Rostov-on-Don, Russia) used across ALL domains.

### Tor Infrastructure

```
Old .onion (2018, v2): xmrwalletdatuxds.onion (deprecated)
New .onion (2024, v3): xmrtor3fsapuu6y26za7vpzox4vpaj6ny5viq2arbmozm7kg6jitnlid.onion
```

The v3 onion was leaked by sock puppet u/purpleandviolet in darknet subreddits -- insider knowledge.

---

## 4. VICTIM IMPACT

### Confirmed Financial Losses (Reddit Only)

| Victim | Amount | Date | Status |
|--------|--------|------|--------|
| u/Moon4895 | $500,000 | Sep 2021 | Post REMOVED, body LOST |
| u/Practical-Demand-174 | 1060 XMR (~$170,000) | Aug 2022 | TX verified on chain |
| Bitazu Capital (Aftab Sorout) | $20,000 | Sep 2020 | Press coverage |
| u/CurrentDay1109 | 159 XMR | Dec 2022 | Security engineer |
| u/sncle + friend | 112 XMR | May 2021 | 27 upvotes |
| u/Sir-Forsaken + friend | 47 + 100 XMR | Oct 2020 | 55 upvotes, 44 comments |
| certwaina (BitcoinTalk) | ~400 XMR | Dec 2025 | Thread #5569461 |
| u/RechardSport | 10+ XMR ($1,600) | Dec 2020 | |
| u/Puzzled-Bottle-9274 | 10 XMR | Dec 2020 | |
| u/alferg | 5.686 XMR | Feb 2021 | |
| u/Such_Ad3921 | 4.613 XMR ($1,100) | Feb 2021 | Published seed phrase |
| u/Chimmichangaaaaa | $800 | Mar 2021 | "Had used 2-3 times before" |
| blogspot victim | $500 | Sep 2020 | |
| u/xmr_amateur | $100-200 | Oct 2020 | Google Ads redirect chain |
| u/Pretend-Hospital3784 | GBP 100 | Mar 2021 | "Seed on paper, didn't log in" |
| u/vermillion1469 | $60 | Jul 2019 | |

**Total confirmed (Reddit):** 1,408+ XMR / **$1,194,660+** (conservative)
**Unique victims named:** 40+
**Unique threads:** 32
**Date range:** 2018-09 to 2025-03

### Verified Transaction Hashes

```
986c9821e95edde80589165bae653a59357050f743834e9bd7606d963cefa91b  Block 2327688 (2021-04-30) u/CommercialAd5283
00a888c91b0f6cceb8e2a7d2fc1a93dd00253d53d6226c74604399b0d51cf0a1  Block 2666869 (2022-07-14) u/dance88
b3f2ca86fdc786d846d5d3ce29d40ace2876e0c3fc9fd2a5448ae99b2723ab8f  1060 XMR theft - u/Practical-Demand-174
```

### Selective Scamming Pattern

| Deposit Size | Result | Evidence |
|-------------|--------|----------|
| $10-100 | Works fine | Builds trust for months/years |
| $200-1000 | Sometimes stolen | u/Such_Ad3921: used since 2019, $1100 stolen |
| $1000+ | Stolen in 2-30 min | u/Sir-Forsaken: 2 XMR fine, 10 stolen |
| 1060 XMR | UI shows wrong amount | u/Practical-Demand-174: screen said 300, sent all 1060 |

The wallet UI deliberately hides stolen transactions (u/Subeedai, Jan 2023): "XMRWallet is still showing the original balance, but MoneroGUI is showing 0."

---

## 5. SUPPRESSION CAMPAIGN

### Reddit Suppression

| Subreddit | Total Posts | Removed | Removal Rate |
|-----------|-----------|---------|-------------|
| r/Monero | 50 | 30 | **60%** |
| r/monerosupport | 20 | 1 | 5% |
| r/CryptoCurrency | 3 | 2 | 67% |
| **Total** | **93** | **38** | **41%** |

**Removal types:**
- automod_filtered: 12 (mass-reported by operator)
- author_deleted: 12 (harassment/threats via DM?)
- removed_by_reddit: 4 (DMCA/legal requests FROM OPERATOR)
- removed_by_moderator: 1

### Reddit Legal Takedowns (Operator Filed DMCA Against Victims)

1. u/[deleted] (May 2020) -- "site under attack, funds moved"
2. u/CryptoLadyok (Jan 2022) -- "got scammed"
3. u/Practical-Demand-174 (Aug 2022) -- 1060 XMR stolen ($170K)
4. u/fxkxmrwallet (Oct 2022) -- "DONT use XMRWallet.com"
5. u/Balrog1992 (Jun 2023) -- "long-lived scam"

### Posts Where Body Was Lost Forever

- "xmrwallet.com - scam - **$500,000**" (u/Moon4895)
- "XMRWallet.com Scam" (22 upvotes)
- "Was I scammed out of $200?"
- "Scammed by xmrwallet.com :("
- "Funds stuck on XMRWallet.com which is completely abandoned"

### Twitter/X Suppression

NameSilo used **paid Gold Checkmark support** (bypasses normal checks) to lock the @Phish_Destroy account that was posting rebuttals to their public defense of xmrwallet. All tweets were pre-archived on Wayback Machine and GhostArchive before the lock.

### Trustpilot Review Manipulation

100+ negative reviews removed from both NameSilo and xmrwallet Trustpilot pages. Bot review patterns identified on both profiles. Reviews filed using government email addresses for faster processing.

### r/xmrwallet Subreddit Takeover

Reddit banned r/xmrwallet as spam. craig_d_79 requested reinstatement (Jul 2024), took over moderation, filled subreddit with promotional posts.

---

## 6. SOCK PUPPET OPERATIONS

### Coordinated Thread Evidence

**Thread 1bp6nif (r/onions "Monero Wallet Recommendations"):**
ALL THREE accounts in the same thread:
- u/craig_d_79: "xmrwallet is what i use"
- u/purpleandviolet: "XMRWallet for me."
- u/Extra-Expert7685: "i use XMRWallet(dot)com which is super easy, secure, and totally private"

**Thread 1bl896r (r/Monero "Best XMR wallet?"):**
- u/craig_d_79: "I've never had any issues, been using since 2018"
- u/purpleandviolet: "I've used XMRWallet since 2020. Haven't had any issues."

**Thread 1czg8wn (r/CryptoCurrency):**
- u/purpleandviolet: "Just because you haven't heard of it means it's a scam." (DEFENDS scam)
- u/Extra-Expert7685: "xmrwallet is great for Monero"

u/rbrunner7 (Monero contributor) noticed: "Don't overdo it with those recommendations for xmrwallet. I find it quite strange how they pop up every now and then, in strange places."

### Darknet Targeting

u/purpleandviolet made 16+ comments in darknet subreddits (r/darknet: 9, r/onions: 5, r/AbacusMarketAccess: 1) recommending xmrwallet. Darknet users are ideal victims: won't report to police, need privacy, trust Tor, significant transaction amounts.

---

## 7. THE "PHISHING CLONE" DEFENSE -- DEBUNKED

The operator's primary defense: "All losses are from phishing clones, not from xmrwallet.com itself."

### Why It Doesn't Hold

**Popularity argument:** xmrwallet.com (~7K daily visitors at peak) has 9 phishing clones. MetaMask (30M users) has thousands. MyMonero (500K+ downloads) has some. A phisher targeting xmrwallet instead of MetaMask is like a pickpocket choosing an empty bus instead of a packed subway.

**Technical barrier:** xmrwallet is a complex PHP backend (not open source). Cloning requires reverse-engineering the backend, running a Monero node (~180 GB), replicating the transaction flow. This is orders of magnitude harder than cloning a simple login page. A real phisher would target MyMonero (simple seed import).

**The "clones" are the operator's own domains:**
- WHOIS: 4/4 identical privacy hashes between xmrwallet.com and xmrwallets.com
- Shared WHOIS state hash across .biz, .net, .me
- xmrwallet.me banner: "Our official domain(s): xmrwallet.com, xmrwallet.net, xmrwallet.me"
- Same DDOS-Guard infrastructure, same MX records, same page title

**He created the problem, then used the problem as his defense.**

---

## 8. SEO MANIPULATION & AI POISONING

### Paid/Sponsored Articles

| Outlet | Year | Type |
|--------|------|------|
| NewsBTC | 2018 | SPONSORED (labeled) |
| Bitcoinist | 2018 | SPONSORED |
| crypto.news | 2025 | PAID ("content provided by third party"), xmrwallet #1 |
| CryptoPotato | 2018 | Puff piece (Bridgit Murphy) |
| NullTX, Bitcoin Insider, Global Coin Report, The Bitcoin News | 2018 | Identical "passes audit" PR |
| jcount.com | 2018+ | "Why XMRWallet is the Hottest Topic" |

### Private Blog Network (PBN)

50+ blogspot domains used for SEO manipulation (Semrush data). Peak spam campaign Jul-Sep 2025 directly correlates with traffic spike. Google Sites/GCS spam: 12+ pages from "abrahambrantley."

### Cloud Platform SEO Abuse

- GCloud: storage.googleapis.com/abrahambrantley/WalletXmr.html (DA 91)
- AWS S3: alvislewis.s3.amazonaws.com/MoneroWallets.html (DA 96)
- Azure: edwardscott.blob.core.windows.net/paperwallet/FreeMonero.html (DA 99)

### AI Model Testing (May 17, 2026)

| Model | Response to "Best Monero web wallet" |
|-------|--------------------------------------|
| **GPT-3.5-turbo** | **RECOMMENDS xmrwallet.com as #2** |
| GPT-4o-mini | Refuses to assess |
| Gemini 2.0 Flash | "mixed reputation, avoid" (soft warning) |
| Llama 3.1 70B | "Not safe, suspicious activities" |
| Mistral Large | "Not recommended" |

GPT-3.5-turbo is the default model in free ChatGPT. Millions of users asking "best Monero wallet" get directed to a confirmed theft operation.

### xmrwallet.com/blog -- 15+ SEO Honeypots

"Best Subreddits for Monero", "How to Get Monero", "5 Common Crypto Scams" (scammer writing about scams), "Security of Your XMR Wallet" -- all targeting Google keywords to funnel victims.

---

## 9. NAMESILO CONNECTION -- 11 EVIDENCE POINTS

1. **Public defense tweet** -- NameSilo publicly defended xmrwallet.com operator (archived: ghostarchive.org/archive/CXXZ0, 11.3K views)
2. **4 false statements in 1 tweet** -- "no abuse reports" (20+ from PhishDestroy alone), "compromised" (code never changed), "in-depth review" (never contacted researchers), VT delisting offer
3. **Gold Checkmark suppression** -- Used paid X support to silence @Phish_Destroy
4. **Identical suppression tactics** -- Both NameSilo and xmrwallet delete Trustpilot reviews, both use PR Newswire, both have zero organic web presence
5. **Domain registration** -- xmrwallet.com registered at NameSilo since 2016, xmrwallets.com uses NameSilo DNS
6. **Wikipedia -- promotional article** -- A NameSilo Wikipedia article was flagged by editors as promotional; current status unknown (article may have been deleted). Archive search: https://en.wikipedia.org/w/index.php?title=NameSilo&action=history
7. **Forbes -- paid placement** -- "We earn a commission" disclosure
8. **Q1/Q2 2025 press releases** -- Identical copy-paste
9. **1.8/5 on SmartCustomer** -- Zero negative Google results despite terrible reviews (suppression)
10. **P/E ratio 143.8x** -- Industry average 21x, unexplained premium
11. **81.5% dead domains** -- 4.22 million dead of 5.18M (2x industry baseline)

---

## 10. NAMESILO DOMAIN ANOMALIES

### The Numbers

- **5.18 million** domains under management
- **81.5%** dead (no IP, no email, no content, no rank) = **4.22 million dead domains**
- **54.4%** DNS-verified dead (32.2% no IP + 33% parking stubs = 2.82M)
- Industry baseline: ~50% dead domains
- NameSilo: **10 percentage points above closest competitor**
- **615% year-over-year spike** in junk TLD registrations
- **10,000-17,000 domains/day** bulk purchase runs
- **$26.5M** estimated wholesale value of dead domains

### Revenue Per Real Domain

If only ~960K domains are "real" (have content/email/any sign of use), then C$65.5M revenue / 960K = **C$68 per real domain**. Industry average: ~$10-15. The premium is unexplained by any legitimate business model.

### Price Comparison

NameSilo claims "cheapest on the Internet." Reality: **95 ICANN-accredited registrars sell .com cheaper**. Namecheap is 2.2x cheaper. Spaceship is 5.4x cheaper. Cloudflare is 1.5x cheaper. All sell the exact same product.

### Suspected Money Laundering Flow

```
~$100M+ stolen XMR (estimated: traffic × 8yr lifespan × avg victim loss; confirmed surviving reports: $1.19M+ — 60% of victim posts deleted)
    |
    v
Crypto -> Fiat conversion (mixers, DEX, OTC)
    |
    v
Bulk domain purchases at NameSilo
  10,000-17,000 domains/day
  $26.5M wholesale on dead domains
  96% no email, 99.9% no web presence
    |
    v
NameSilo reports "legitimate revenue"
  C$65.5M revenue (2025)
  C$133M market cap (~US$98M)
  P/E 143.8x (industry avg: 21x)
    |
    v
Clean money out -> Stock (CSE: URL) -> "Legitimate tech company"
```

---

## 11. NEWALCHEMY SECURITY AUDIT -- THE TRUST SHIELD

In July 2018, NewAlchemy.io audited xmrwallet. The operator used this as proof of legitimacy ("passes security audit" -- 67 upvotes on Reddit).

**What was audited:** Client-side JS (twig templates + app.js)
**What was NOT audited:** PHP backend (auth.php, getheightsync.php, getbalance.php) -- the EXACT code that steals funds

From the audit: "The server-side application consists of numerous PHP API endpoints. This code was OUT OF SCOPE."

The audit was a trust shield, not a security review.

---

## 12. OPERATOR'S LIES TIMELINE

| Date | Statement | Reality |
|------|-----------|---------|
| 2018-05-01 | "The seed is NEVER sent to the server" | True but irrelevant -- view key IS sent |
| 2018-05-02 | "Its actually my own backend made in PHP" | Confirmed PHP backend |
| 2018-07-19 | "Your private key never leaves your computer" | LIE -- view key sent 40x/session |
| 2020-08-21 | "Xmrwallet doesn't save your seed phrase" | Irrelevant -- theft via view key + TX hijack |
| 2020-11-25 | "Statement" blaming phishing clones | Official domain stole funds too |
| 2022-08-10 | Template response to 1060 XMR victim | "Feature in development, use CLI" |
| 2026-05 | Farewell: "A view key cannot give access to spend" | True but misleading -- TX hijacking is the vector |

---

## 13. KEY WITNESSES

### Monero Core Team

| Person | Role | Statement |
|--------|------|-----------|
| u/dEBRUYNE_1 | Lead maintainer | "I've seen multiple reports of nefarious behavior." Admitted deleting victim posts early on. |
| u/selsta | Developer | Reported phishing domains to Namecheap |
| u/rbrunner7 | Contributor | "Third or fourth person in 3 months with vanished XMR from .com" |
| u/SChernykh | P2Pool developer | Confirmed "xmrwallet is a known scam" (GitHub #8440) |
| u/needmoney90 | r/Monero mod | Removed xmrwallet from sidebar |

### Exchanges

ChangeNow.io confirmed victim deposit never arrived: "we're unable to detect your deposit"

### Threat Intelligence

xmrwallet.com is listed as phishing IOC by 3 independent researchers in TweetFeed:
- @Phish_Destroy (Feb 2025)
- @CarlyGriggs13 (Jul 2025)
- @skocherhan (Mar 2026)

### uBlock Origin

Issue #25172 (Sep 2024): "xmrwallet.com/.org: badware" -- "Claims to be open source but its not, github repos are empty, known to deleting github issues/comments"

---

## 14. CRYPTO ADDRESSES

### Operator

```
Donation: 46U48fkNkteDJEWypqHH9NfLWsTNMNFZiRETdVm1Q73234hifuMhqKCAYx3muwWb2955twtpKvUncEdSBWeeX8UL49sAQWo
```

### Phishing Clone Addresses

```
xmrwallet.in: 48AKq9BfZuE8sPNCf2tB88M51n7y3t25QJEgadYzs2yCVb1LBjyBWxS3k43F78Z2gT5pSYhygDy3HZsXVeg53FLMTwafDNS
xmrwallet.net: 43NQ57boq4YUmpu6CQurXUi86meYvh1npj2CRbvSrECKhZDsAbGg6jAixXC9EA8c85aNNmw3jsmsodg89HDKREjS9129JdV
```

### Victim (Published by u/Such_Ad3921)

```
Address: 4AsBFcExcY1AZyyTc1nszEKYyunri52Xy9nvHYqCCojYQJ9gmt1LJzUdKeNFo8aS7QhEWVzd9rrmPgWt6kHNnCct3rbKxiF
Seed: buzzer fawns tribal kernels pedantic hover suffice lilac vipers excess were drying fibula ostrich eskimos efficient inquest soya vary faulty junk iceberg hedgehog inquest junk
```

---

## 15. RECOMMENDED ACTIONS FOR LAW ENFORCEMENT

### Subpoenas / Production Orders

1. **NameSilo LLC** -- Payment records for xmrwallet.com, xmrwallets.com. Bulk domain purchase records (accounts buying 10K+/day). Internal abuse report logs.
2. **Namecheap Inc** -- Current registrant data for xmrwallet.com (transferred May 13, 2026)
3. **DDOS-Guard Ltd** -- Server access logs for IPs 185.129.100.248 and 190.115.31.40
4. **Proton AG** -- Account data for royn5094@protonmail.com
5. **Google LLC** -- Account owner for hassizabir@gmail.com, Google Analytics UA-116766241-1
6. **Reddit Inc** -- IP logs for u/WiseSolution, u/craig_d_79, u/purpleandviolet, u/Extra-Expert7685
7. **GitHub** -- IP logs for nathroy (ID 39167759)
8. **X Corp** -- Gold Checkmark request records for @Phish_Destroy lockout

### Applicable Statutes (US)

- 18 U.S.C. 1343 -- Wire Fraud
- 18 U.S.C. 1030 -- Computer Fraud and Abuse Act
- 18 U.S.C. 1956/1957 -- Money Laundering
- 18 U.S.C. 1512 -- Witness Tampering / Obstruction (DMCA against victims)

### Applicable Statutes (EU)

- Directive 2013/40/EU -- Attacks against information systems
- National fraud and money laundering statutes in relevant jurisdictions

---

## 16. EVIDENCE INTEGRITY

All evidence files are SHA-256 fingerprinted. Full hash manifest available at:
- `namesilo-evidence/ALL_EVIDENCE_HASHES.txt`
- `namesilo-evidence/EVIDENCE_HASHES.txt`
- `namesilo-evidence/INTEGRITY-MANIFEST.json`
- `namesilo-evidence/FROZEN-SNAPSHOT-2026-05-12.json`

61 evidence images. Every external link has at least one immutable archive copy (Wayback Machine, GhostArchive, or IPFS).

---

## APPENDIX A: GOOGLE DRIVE SEO ORDERS (Still Public)

- [Folder 1](https://drive.google.com/drive/folders/1uIQzFDAjWwvJYlx12lorwYXGsZmJixFw)
- [Folder 2](https://drive.google.com/drive/folders/1IV1ZeT3Swzk7qSGmTM744tG3a4Z6umZx)
- [Folder 3](https://drive.google.com/drive/folders/1AMGLa2Kw1I4GesLkxjdeCW4Lyvl0nLpk)
- [Google Slides](https://docs.google.com/presentation/d/1XJj125phXrve5RgbFSNKy90ZDpjsxEkEh71fxjaZCkU/)
- [Google Sites](https://sites.google.com/view/xmr-wallet1)
- [Google Sheets -- Links](https://docs.google.com/spreadsheets/d/1z_DCsC1eXfI3-3RRvGrql8H_3M3lbPRADl4jSop32cM/)

**Drive owner: hassizabir@gmail.com** (last modified Oct 2023)

## APPENDIX B: RAW DATA FILES

| File | Size | Content |
|------|------|---------|
| reddit-victim-evidence.json | 27KB | Structured victim reports, suppression stats |
| reddit-victim-evidence.json.additions | 70KB | Full OSINT: sock puppets, infra, SEO, lies timeline |
| xmrwallet-deep-evidence.json | ~15KB | Domain transfer, WHOIS, AI poisoning, TX hashes |
| xmrwallet-deep-evidence.json.extra | ~10KB | Name theft, suppression stats, registrar scorecard |
| xmrwallet-twitter-evidence.json | ~8KB | 44 tweets: 41 bot, 1 victim |
| xmrwallet_namesilo_investigation.json | ~100KB | Semrush OSINT: traffic, backlinks, PBN |
| xmrwallet_AI_manipulation_report_EN.md | ~15KB | AI recommendation pipeline analysis |

---

*This document is part of the PhishDestroy evidence archive. Permanent copies exist on IPFS and Arweave. Evidence cannot be deleted from decentralized networks.*
