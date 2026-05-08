# PROOFS.md — Complete Evidence Dossier

> **This is the single file to share.** Every piece of evidence — every email verbatim, every lie disproven, every screenshot described, every archive link — in one place. If you only have one URL, send this.
>
> **They are trying to erase this.** Twitter locked. Bing delisting in progress. DDoS in progress. This file exists on GitHub, GitHub Pages, IPFS, Wayback Machine, archive.today, GhostArchive, and any surface that will hold it. The cost of suppression scales linearly with the number of mirrors. The cost of mirroring is logarithmic. We win by making the takedown count infeasible.

---

## Table of contents

1. [The parties](#1-the-parties)
2. [Complete timeline](#2-complete-timeline)
3. [EVIDENCE A — The operator's emails (verbatim)](#3-evidence-a--the-operators-emails)
4. [EVIDENCE B — NameSilo's statement: four sentences, four lies](#4-evidence-b--namesilos-statement-four-lies)
5. [EVIDENCE C — The public rebuttal tweets (verbatim, now invisible)](#5-evidence-c--the-public-rebuttal-tweets)
6. [EVIDENCE D — The smoking gun: X cleared us, lock stayed](#6-evidence-d--the-smoking-gun)
7. [EVIDENCE E — Three registrars suspended, one defended](#7-evidence-e--registrar-comparison)
8. [EVIDENCE F — Technical proof: xmrwallet is a drainer](#8-evidence-f--technical-proof)
9. [EVIDENCE G — The pressure campaign](#9-evidence-g--the-pressure-campaign)
10. [EVIDENCE H — "Feel free to subpoena the domain registrar"](#10-evidence-h--the-subpoena-line)
11. [All exhibits with SHA-256](#11-all-exhibits-with-sha-256)
12. [Permanent mirrors & IPFS](#12-permanent-mirrors--ipfs)
13. [Materials available on request](#13-materials-available-on-request)
14. [How to verify](#14-how-to-verify)
15. [License — explicit consent for legal use](#15-license)

---

## 1. The parties

| Party | Identity | Role |
|---|---|---|
| **The operator** | Alias `nathroy` / initials N.R. Email: `royn5094@protonmail.com`. | Runs `xmrwallet[.]com` — a ~10-year Monero private-key drainer. Est. $10M-$20M stolen. Hosting: $550/mo bulletproof in Belize, behind Russian DDoS-Guard. Owns at least 7 related domains, 5 of which were suspended by other registrars. Paid for some domains **10 years** in advance. |
| **The registrar** | **NameSilo, LLC** — US-based, ICANN-accredited domain registrar (Phoenix, AZ). X/Twitter: [@namesilo](https://twitter.com/namesilo). Holds a **Gold Checkmark** (Verified Organization) on X — paid corporate tier with direct access to live human X moderators. | Holds `xmrwallet.com` registration. Publicly defended the operator on March 13, 2026. Refused to suspend. Committed in writing to helping operator scrub VirusTotal detections. |
| **The researchers** | **PhishDestroy Research** — anti-phishing threat intelligence. X/Twitter: [@Phish_Destroy](https://twitter.com/Phish_Destroy) (currently locked). 350,000+ malicious domains documented. 54+ trusted partners. | Reported the domain (20+ times since 2023), published technical breakdown, posted public rebuttals, escalated to ICANN Contractual Compliance on March 18, 2026. Account locked on X after publishing the receipts. |

---

## 2. Complete timeline

| Date | Event | Evidence |
|---|---|---|
| **~2016** | `xmrwallet[.]com` goes live. Server-side key exfiltration active from day one — 8 PHP endpoints, `session_key` carrying private view key in base64. | [Evidence F](#8-evidence-f--technical-proof) |
| **2023-2026** | PhishDestroy submits **20+ delivery-receipted abuse reports** to NameSilo's own portal about `xmrwallet[.]com` and operator-linked mirrors. All receipted. All ignored. | Delivery receipts forwarded to ICANN Mar 18, 2026 |
| **2026-02-16** | Operator (N.R., `royn5094@protonmail.com`) emails PhishDestroy. Subject: `[9] xmr wallet .com`. Asks for report removal. Claims site is legitimate. **Never claims a hack.** | [Exhibit 10](#exhibit-10--operator-email) |
| **2026-02-16** | PhishDestroy replies same day with full technical breakdown. Warning: *"What happens next depends entirely on how you choose to proceed."* | [Exhibit 11](#exhibit-11--phishdestroy-reply) |
| **2026-02-17** | Operator responds: **"Feel free to subpoena the domain registrar for my information."** | [Evidence H](#10-evidence-h--the-subpoena-line) |
| **2026-02-22** | @ImCryptOpus tweets: XMRWallet shut down, $10M+ stolen. Third-party reporting predates NameSilo's statement. | [Exhibit 07](#exhibit-07--cryptopus-quote) |
| **2026-03-12** | @Phish_Destroy confronts NameSilo: *"9 reports is no joke anymore."* | [Exhibit 08](#exhibit-08--confrontation-tweets) |
| **2026-03-13** | **NameSilo publishes the four-lie statement.** Calls operator "the victim." Denies abuse reports. Commits to scrubbing VirusTotal. | [Exhibit 08](#exhibit-08--confrontation-tweets), [Evidence B](#4-evidence-b--namesilos-statement-four-lies) |
| **2026-03-14** | @Phish_Destroy replies: *"New service from NameSilo: helping scammers get VirusTotal bans removed."* | [Exhibit 08](#exhibit-08--confrontation-tweets) |
| **2026-03-16** | @Phish_Destroy publishes full rebuttal thread. 4+ tweets. Tags NameSilo, other registrars. | [Evidence C](#5-evidence-c--the-public-rebuttal-tweets) |
| **2026-03-18** | @Phish_Destroy escalates to ICANN Compliance + law enforcement, publicly. | [Exhibit 03](#exhibit-03--namesilo-is-lying) |
| **2026-03-??** | **@Phish_Destroy permanently locked.** X email: *"violation against inauthentic behaviors."* No tweet cited. No rule named. | [Evidence D](#6-evidence-d--the-smoking-gun) |
| **2026-04-15** | X Support appeal result: **"no violation, restored to full functionality."** Account **still locked.** Gold subscription **still billed.** | [Evidence D](#6-evidence-d--the-smoking-gun) |
| **Ongoing** | Bing search delisting attempts targeting `phishdestroy.io` | Webmaster Tools data (in preparation) |
| **Ongoing** | DDoS against `phishdestroy.io` — source-IPs correlate with "njan la" reseller infrastructure | Analysis publishing on phishdestroy.io |

---

## 3. EVIDENCE A — The operator's emails

### Exhibit 10 — Operator email

- **Date:** February 16, 2026
- **From:** `nathroy <royn5094@protonmail.com>`
- **To:** `abuse@phishdestroy.io`
- **Subject:** `[9] xmr wallet .com`
- **Note in email client:** "This sender's public key has not been trusted yet."

**Full text (verbatim from screenshot):**

> Hi,
>
> You are incorrect with your report. There is no phishing going on with xmrwallet.com, this is the official domain name for xmrwallet.
>
> We are an open source crypto wallet that is non-custodial, we don't store seeds or keys, everything is done in your browser locally.
>
> Please remove your report on us, thank you.
>
> N.R.

**Why this is evidence:**

1. **The operator defends the site as his own work.** He says "we are an open source crypto wallet." He takes ownership. He does not claim it was hacked or compromised.
2. **He states "we don't store seeds or keys, everything is done in your browser locally."** This is provably false — the production site exfiltrates the private view key via `session_key` on every transaction.
3. **He never claims a hack.** This directly contradicts NameSilo's later claim (March 13) that the "domain was compromised a few months ago." The operator's own position is that the site is operating normally.
4. **ProtonMail sender** — privacy-oriented email. Alias `nathroy`. Combined with Belize bulletproof hosting and DDoS-Guard, this is a privacy-maximizing infrastructure stack consistent with deliberate operational security, not a casual web project.

**Screenshot:** [`evidence/01-operator-email-feb16.png`](evidence/01-operator-email-feb16.png)
**SHA-256:** `919b5ee4c0f3a889381c644b557736d35625c69abaddd0ec7a8251eb514b0111`

---

### Exhibit 11 — PhishDestroy reply

- **Date:** February 16, 2026 (same day)
- **From:** `abuse@phishdestroy.io`
- **To:** `nathroy`

**Full text (verbatim from screenshot):**

> Hello,
>
> Let's keep this clear and professional.
>
> Analysis of phishing schemes and wallet abuse is a specialized field, and this case has already raised multiple technical indicators that warrant attention. The observations are based on actual production behavior and are reproducible.
>
> At the moment, this is not a full audit — just a focused review driven by professional interest.
>
> **Key Technical Observations**
>
> — Client-side transaction is generated but **explicitly discarded**:
>
> `raw_tx_and_hash.raw = 0`
>
> Only metadata (amount, address, fee, etc.) is submitted to the backend.
>
> — Backend receives transaction parameters and can **construct its own transaction independently** of the client-generated one.
>
> — Presence of **production-only parameters** not reflected in the public repository:
> - `session_key` (contains encoded address and private view key)
> - `verification` (spend key signature proof)
> - `timestamp`
> - encrypted data payload
>
> — `session_key` structure indicates repeated transmission of:
> - full wallet address
> - private view key (base64-encoded)
>
> — Existence of **non-standard transaction type**:
>
> `type == 'swept'`
>
> paired with "Unknown transaction id", indicating server-side initiated operations not traceable via standard tooling.
>
> — Observable divergence between **public GitHub code and production behavior**, including additional parameters and altered auth flow.
>
> **Important**
>
> — The current assessment stands and is technically grounded
> — The behavior aligns with known high-risk transaction handling patterns
> — Dismissing findings without addressing these mechanics does not change the conclusion
>
> If this remains a technical discussion, it stays at this level.
>
> If it escalates — through continued denial or misrepresentation — it may justify a **complete end-to-end audit** with full documentation, reproducible evidence, and formal submission to relevant security and infrastructure channels.
>
> **Final note**
>
> Nothing here is based on assumptions — only on observable system behavior and verifiable logic.
>
> **What happens next depends entirely on how you choose to proceed.**
>
> Regards

**Why this is evidence:**

1. **Professional, same-day, complete technical briefing.** The operator cannot claim he wasn't warned or didn't understand what was found.
2. **Explicit exit ramp:** *"What happens next depends entirely on how you choose to proceed."* The operator was given a clean exit before any escalation. He chose not to take it.
3. **The technical findings are documented in the email itself** — 8 PHP endpoints, `session_key` exfiltration, `raw_tx_and_hash.raw = 0`, production-only parameters. These are the same findings that later appeared in the published technical breakdown.
4. **Establishes the escalation chain was initiated by the operator, not PhishDestroy.** Every subsequent step was a documented response to an action by the operator or his registrar.

**Screenshot:** [`evidence/01-phishdestroy-reply-feb16.png`](evidence/01-phishdestroy-reply-feb16.png)
**SHA-256:** `ecced35149dbf19dff7399cd86708d28aff7b8ab044e132c4c92cafbe222a753`

---

## 4. EVIDENCE B — NameSilo's statement: four lies

### Exhibit 08 — Confrontation tweets + NameSilo's reply

The NameSilo statement was published as a **direct reply** to @Phish_Destroy's investigation thread. The screenshots capture the full context.

**March 12, @Phish_Destroy (verbatim):**

> @namesilo, what exactly is your problem? We already have NiceNIC, WebNic, Key-Systems GmbH, and PublicDomainRegistry — even though they usually aren't very talkative either, they actually banned your scammer's domains, yet you are protecting him? 9 reports is no joke anymore.

**March 13, @namesilo official reply (verbatim — the Gold Checkmark Verified Organization account):**

> Our Abuse team conducted an in-depth review into this case and it seems that domain was compromised a few months ago (during which a copy of the webpage was replaced with a crypto-drainer). Prior to that, we had received no abuse reports related to this domain. After an extensive [Show more]

*Full text continues with commitment to "working with the registrant to remove the website from VT reports."*

**Engagement:** 3 replies, 3 retweets, 1 like, 11K views

**March 14, @Phish_Destroy reply (verbatim):**

> New service from NameSilo: their abuse team is helping scammers get VirusTotal bans removed, even though the malicious activity is still there and has always been there. We have already documented this, proved it, and helped get several related domains flagged.
>
> Please repost pic.x.com/1hBahW4hZ2

**Engagement:** 2 retweets, 107 likes, 3K views

**Permanent archive of NameSilo's tweet:** [ghostarchive.org/archive/CXXZ0](https://ghostarchive.org/archive/CXXZ0)
**Screenshot:** [`evidence/03-namesilo-statement-mar13.png`](evidence/03-namesilo-statement-mar13.png)
**SHA-256:** `ad29e1d3d4803ff37c88ef860bef6de9e62f6ce533657f2e5c5460eb2e0b8ebf`

---

### The four lies — each one disproven

#### LIE #1: "Domain was compromised a few months ago."

**NameSilo's claim:** `xmrwallet[.]com` was a legitimate Monero wallet that got hacked, and the code was secretly replaced with a drainer "a few months ago."

**The truth:** The theft code **is** the website. It has been the website for approximately a decade. Server-side analysis shows:
- 8 PHP endpoints dedicated to key exfiltration
- `session_key` carrying full wallet address + private view key in base64
- `raw_tx_and_hash.raw = 0` — client-side transaction explicitly discarded
- Production-only parameters (`session_key`, `verification`, `timestamp`, encrypted payload) that do not exist in the public GitHub repo
- Non-standard `type == 'swept'` transaction — server-side sweep, not user-initiated

**What "compromise" would look like if real:** A diff between the GitHub repo and deployed code. DNS/hosting/TLS changes around the compromise window. An incident-response statement naming the vector. **NameSilo provided none of this. The operator provided none of this.**

**Disproven by:** Technical breakdown at [phishdestroy.io/xmrwallet-namesilo-exposed](https://phishdestroy.io/xmrwallet-namesilo-exposed); operator's own email defending the site as his own work ([Exhibit 10](#exhibit-10--operator-email))

**VERDICT: FALSE.**

---

#### LIE #2: "Prior to that, we had received no abuse reports."

**NameSilo's claim:** No prior abuse complaints on file for `xmrwallet[.]com`.

**The truth:** PhishDestroy alone submitted **20+ delivery-receipted abuse reports** through NameSilo's own portal between 2023 and 2026. Every one generated a confirmation page, ticket ID, or automated acknowledgement from NameSilo's own intake system.

Beyond PhishDestroy: the CryptOpus tweet of February 22, 2026 ([Exhibit 07](#exhibit-07--cryptopus-quote)) confirms public third-party reporting going back years. The @Phish_Destroy tweet of March 12 explicitly states *"9 reports is no joke anymore"* — contradicting NameSilo's claim **one day before they made it**.

**Two possible readings:**
1. NameSilo's abuse team genuinely doesn't know what reports it received → ICANN compliance failure
2. NameSilo knows and lied → deliberate false public statement

**Disproven by:** PhishDestroy delivery receipts (forwarded to ICANN Compliance March 18, 2026); CryptOpus tweet; @Phish_Destroy Mar 12 tweet citing "9 reports"

**VERDICT: FALSE.**

---

#### LIE #3: "After an extensive review... not involving the registrant."

**NameSilo's claim:** Their review was independent, and the operator was not party to its conclusions.

**The truth:** The operator wrote to PhishDestroy on February 16, 2026 — weeks before NameSilo's statement — defending the site as his own work. He never claimed a hack. He never claimed a compromise. He said *"There is no phishing going on with xmrwallet.com"* and *"we don't store seeds or keys."*

NameSilo's tweet then adopted a "compromise" narrative the operator himself never advanced. Either:
- The "extensive review" never consulted the registrant (in which case it's not extensive), or
- It did consult him and adopted a framing he didn't support (nonsensical without a third party providing the narrative)

**Disproven by:** [Exhibit 10](#exhibit-10--operator-email) — the operator's own email, predating NameSilo's statement by 25 days

**VERDICT: FALSE.**

---

#### LIE #4: "Working with the registrant to remove the website from VT reports."

**NameSilo's claim:** They committed publicly to helping the operator get `xmrwallet[.]com` removed from VirusTotal's threat detections.

**The truth:** This sentence is the most damning, and NameSilo did not lie about it — they actually said it and meant it. Consider what is being committed to:

- A registrar's small in-house abuse team
- Looking at a phishing site flagged by **6+ authoritative security vendors** (Fortune-500-grade telemetry providers)
- That has been **suspended at 3 other registrars** on the same evidence
- That has been live for **~10 years**
- Publicly announcing they will **help the operator get those detections removed**

A registrar has no business disputing the threat-intelligence findings of every authoritative vendor. This is not abuse handling. **This is active obstruction of consumer-protection telemetry on behalf of a confirmed thief.**

As @Phish_Destroy wrote on March 16: *"Is helping a scammer clear their VT record a new registrar service? We proved this wallet was created to steal funds from day one. The owner is actively wiping reviews and trying to take down entire GitHub accounts. Like client, like registrar."*

**VERDICT: STATED AS WRITTEN. DAMNING AS WRITTEN.**

---

## 5. EVIDENCE C — The public rebuttal tweets

All tweets by @Phish_Destroy (Gold Checkmark, ~6.5K followers, 45K posts, never warned, never restricted). Account now locked — these screenshots are the canonical copies.

### Exhibit 03 — "@NameSilo is lying"

- **Date:** March 16, 2026
- **Engagement:** 2 replies, 3 retweets, 39 likes, 8.5K views

**Full text (verbatim):**

> Let's be direct.
>
> @NameSilo is lying.
>
> They claimed xmrwallet[.]com was "compromised" — hacked by a third party.
>
> The operator's own emails to us, written BEFORE NameSilo got involved, prove the "hack" story was fabricated.
>
> We have the receipts.
>
> #xmrwallet #NameSilo #MoneroScam

**Also visible in same screenshot — ICANN escalation tweet (March 18):**

> Because no response or action has been provided, and due to what appears to be deliberately false statements made to protect a fraud operator, we have forwarded the full investigation materials to @ICANN Contractual Compliance, relevant regulatory authorities, and law [enforcement]...

**Engagement on ICANN tweet:** 4.5K views

**Screenshot:** [`evidence/04-tweet-namesilo-is-lying.png`](evidence/04-tweet-namesilo-is-lying.png)
**SHA-256:** `c556e13ff0e4265cbba76b6a518f0862dee67467c1b264181e27eef8046eda6a`

---

### Exhibit 06 — "Press secretary" thread

- **Date:** March 16, 2026
- **Engagement on main tweet:** 1 reply, 8 retweets, 14 likes, 5.3K views

**Main tweet (verbatim):**

> THREAD: @NameSilo is acting as press secretary for a $2M+ Monero theft operation.
> xmrwallet[.]com steals private keys since 2016. 6 security vendors flag it. 3 registrars suspended it.
> NameSilo called the scammer "the victim" and is helping him remove @virustotal warnings.
> Our pic.x.com/4gqu7zRvr5

**Thread replies (verbatim):**

> @key_systems Are you a spokesperson for Scamer too? Just like NameSilo? Six reports have been ignored — is everything OK? xmrwallet[.]me

> Or did you also investigate and conclude that it's not one of the 7 domains, 5 of which were successfully blocked? Or is a client who paid for 10 years is simply impossible to ban?

> Is helping a scammer clear their VT record a new registrar service?
>
> We proved this wallet was created to steal funds from day one. The owner is actively wiping reviews and trying to take down entire GitHub accounts. Like client, like registrar.

**Screenshot:** [`evidence/04-tweet-press-secretary.png`](evidence/04-tweet-press-secretary.png)
**SHA-256:** `c9007cb4acf1a264fb82e36a57708a1c35e4b6824eb2734a6a7dff095588bd84`

---

### Exhibit 04 — "Honest question for @NameSilo"

- **Date:** March 16, 2026
- **Engagement:** 1 reply, 2 retweets, 72 likes, 7.9K views

**Full text (verbatim):**

> Honest question for @NameSilo:
>
> Who is this operator to you?
>
> Employee? Contractor? Friend of support staff? Relative?
>
> Because he told us "subpoena the registrar" like a man who already had your answer.
>
> 3 registrars suspended him. You wrote him a defense.
>
> Who pays for the [Show more]

**Follow-up tweet (same screenshot, verbatim):**

> We've now proven that @NameSilo's abuse team intentionally lied in their public response.
>
> The operator's emails — written before NameSilo got involved — contradict every claim they made.
>
> NameSilo is covering for this operator. The reason is theirs to explain.
>
> Our job was [Show more]

*Below this tweet: a PhishDestroy platform card showing "350K+ Emails Scanned, 54+ Trusted Partners Integrated" and the phishdestroy.io URL.*

**Screenshot:** [`evidence/04-tweet-honest-question.png`](evidence/04-tweet-honest-question.png)
**SHA-256:** `bbb0ecd0b7164bf91ace59bc0de01ae953a828a34765b36b89e07479e76ee674`

---

### Exhibit 07 — CryptOpus quote

- **Date:** @Phish_Destroy quoting @ImCryptOpus from February 22, 2026

**CryptOpus original tweet (verbatim):**

> JUST IN: has been taken down
>
> XMRWallet was reportedly shut down after allegedly operating for more than a decade as a fraudulent #Monero wallet, with estimates suggesting over $10M in user funds were stolen. Until the takedown, the suspected (...

**Why it matters:** Independent third-party confirmation from a crypto news account, weeks before NameSilo's statement. The scam was publicly known. NameSilo's "we received no abuse reports" fails against this alone.

**Screenshot:** [`evidence/04-tweet-cryptopus-quote.png`](evidence/04-tweet-cryptopus-quote.png)
**SHA-256:** `6ffd3020793e9d850f0f10f7b4406b165e7d266d692a647ecb24eab9840e7f7f`

---

## 6. EVIDENCE D — The smoking gun

### How X Gold Checkmark works

The **Gold Checkmark** (Verified Organization) on X costs organizations real money per month. Its main perk: **direct access to a live human support agent at X**. Not the automated system. A person.

Both NameSilo and PhishDestroy hold one. PhishDestroy bought it assuming it would protect against drive-by troll reports. NameSilo used theirs to file a takedown.

### Email #1 — The lock

After the ICANN escalation tweet (March 18), @Phish_Destroy was permanently locked. X sent:

> *"Our support team has determined that a violation against inauthentic behaviors [occurred]. We will not overturn our decision."*

**No tweet quoted. No specific rule cited. No example.** This is not what automated rule enforcement looks like. This is what a human-agent decision looks like, after a complaint from a paying corporate account.

### Email #2 — The contradiction

**Date:** April 15, 2026
**From:** `X <notify@x.com>`
**To:** `Jack Fake-Killer` (PhishDestroy account holder, mailbox `abuse@phishdestroy.io`)
**Subject:** `[4] Your account has been restored`

**Full email text (verbatim from screenshot):**

> Hello,
>
> We have reviewed your appeal request for account, @Phish_Destroy.
>
> Our automated systems have determined there was no violation and have restored your account to full functionality.
>
> Thanks,
> X Support

### The contradiction, spelled out

1. X's **own automation** reviewed the case and found **no violation**.
2. X's **own system** sent a restoration email with the subject line `[4] Your account has been restored`.
3. The account is **still locked** as of May 2026.
4. The Gold Checkmark subscription is **still being billed**.
5. PhishDestroy **cannot access their own posts** — the tweets rebutting NameSilo are invisible to the account that authored them.
6. No third email retracted Email #2. It stands, contradicting reality.

### Only two possible readings

1. Email #2 is real → The automation cleared the account → A human agent manually overrode the machine after a Gold-tier complaint → **The lock the automation lifted is being maintained by a paid corporate complaint.**
2. Email #2 is wrong → X sent a false restoration notice and never corrected it → Continuing to bill a paid subscriber for a frozen account.

**Either reading = same conclusion: Concierge censorship that you can buy.**

**Screenshot (email body):** [`evidence/06-x-support-no-violation.png`](evidence/06-x-support-no-violation.png)
**SHA-256:** `2753d02ffeb1b2853bdc33ddec888e3652d9d3829b265e1228c8f28b53b86efa`

**Screenshot (subject line):** [`evidence/06-x-support-subject-restored.png`](evidence/06-x-support-subject-restored.png)
**SHA-256:** `482d0ebba1656c3b338957e40cda0abc7a0017eb6ad08f2a0d639468298ccaf3`

---

## 7. EVIDENCE E — Registrar comparison

The same evidence package was sent to all registrars holding operator-linked mirrors of the drainer.

| Registrar | Action on identical evidence | Time to action |
|---|---|---|
| **PublicDomainRegistry (PDR)** | **Suspended** | Days |
| **WebNic** | **Suspended** | Days |
| **NICENIC** | **Suspended** | Days |
| **NameSilo** | Public defense + offer to scrub VirusTotal | **Never** |

**Key context:**
- NICENIC is documented by PhishDestroy as one of the slowest and laziest abuse handlers on the internet. **NICENIC still suspended.** NameSilo did not.
- The operator had **7 domains** across multiple registrars. **5 were successfully blocked.** (Source: Exhibit 06 thread: *"it's not one of the 7 domains, 5 of which were successfully blocked"*)
- The operator had paid for some domains **10 years in advance** — infrastructure-level investment in a scam operation, not a casual project.
- **Key-Systems GmbH** was also confronted by @Phish_Destroy for ignoring 6 reports on `xmrwallet[.]me` (Source: Exhibit 06 thread)

**The variable is not the evidence. The variable is the registrar.**

---

## 8. EVIDENCE F — Technical proof

**Full breakdown:** [phishdestroy.io/xmrwallet-namesilo-exposed](https://phishdestroy.io/xmrwallet-namesilo-exposed)
**GitHub technical repo:** [github.com/phishdestroy/DO-NOT-USE-xmrwallet-com](https://github.com/phishdestroy/DO-NOT-USE-xmrwallet-com)

### How xmrwallet[.]com steals funds

The production site diverges from the public GitHub repository. The production site:

1. **Discards the user's transaction:** `raw_tx_and_hash.raw = 0` — the transaction the user thinks they're signing is explicitly thrown away.
2. **Constructs a parallel server-side transaction** using the user's parameters — independently of the client-side one.
3. **Injects production-only parameters** absent from the public GitHub repo:
   - `session_key` — carries the **full wallet address** and **private view key**, base64-encoded
   - `verification` — spend key signature proof
   - `timestamp`
   - encrypted data payload
4. **Transmits `session_key` to operator infrastructure** on every transaction — giving the operator full read access to every wallet.
5. **Uses `type == 'swept'`** transaction paired with "Unknown transaction id" — the signature of a server-initiated key sweep, not a user-initiated transaction.
6. **Observable divergence** between the public GitHub code and production behavior, including additional parameters and altered auth flow.

### What this means

- **This is not a compromised wallet.** This is a wallet engineered to steal from day one.
- **The operator's own public GitHub repo is a decoy.** The production code does not match it.
- **The operator stated in his email** ([Exhibit 10](#exhibit-10--operator-email)): *"we don't store seeds or keys, everything is done in your browser locally."* The production site does the opposite — it transmits the private view key to the server on every transaction.

### PhishDestroy platform

**Screenshot:** [`evidence/09-phishdestroy-platform.png`](evidence/09-phishdestroy-platform.png)
**SHA-256:** `de5b430bb4cad5a422ddf1bb6a8c348fffdf0673e7ea8bfface4fb312f46b087`

The PhishDestroy Threat Intelligence Platform: 350,000+ malicious domains scanned, 54+ trusted partners. This is the operation NameSilo tried to silence — not a hobbyist account, not a troll, not a competitor.

---

## 9. EVIDENCE G — The pressure campaign

### G1 — The operator's track record (pre-2026)

The operator has a documented, years-long history of suppressing critics:

- Filed **false DMCA takedowns** against GitHub repos documenting the drainer
- **Mass-reported** Trustpilot reviews until removed
- Coordinated reporting against **BitcoinTalk** warning threads
- Reported **YouTube** technical analysis videos
- Targeted **X/Twitter researchers** via puppet accounts and the report button
- **Actively wiping reviews** and trying to take down entire GitHub accounts (documented in Exhibit 06: *"The owner is actively wiping reviews and trying to take down entire GitHub accounts. Like client, like registrar."*)

### G2 — NameSilo replicates the pattern (March 2026+)

| Action | Status |
|---|---|
| **@Phish_Destroy permanently locked on X** — via Gold Checkmark live-support channel, not automation | Still locked. X cleared on appeal. Lock not lifted. |
| **Bing search delisting attempts** targeting `phishdestroy.io` content | Tracked. Webmaster Tools shows inbound complaints. |
| **DDoS traffic** against `phishdestroy.io` from IPs correlated with NameSilo's "njan la" reseller infrastructure | Mitigated. Source-IP analysis in preparation. |
| **Coordinated reporting** against PhishDestroy's GitHub repos, Medium articles, public mirrors | Monitored. Any successful takedown will be documented in a follow-up commit. |

### G3 — "njan la" — NameSilo's largest abuse-tolerant reseller

- "njan la" was the dominant supplier of bulletproof crypto-scam domains during 2022-2024 (peak of crypto-drainer and pig-butchering epidemics)
- Charged 2x-5x premium pricing for domains visibly used in active fraud
- Suspended public API around the time aggregate abuse reporting surfaced the volume
- A non-trivial fraction of NameSilo-registered domains in PhishDestroy's 2022-2024 abuse logs trace through this reseller
- DDoS traffic targeting PhishDestroy post-publication has source-IP correlation with "njan la" infrastructure

### G4 — Why the pressure campaign is itself evidence

Registrars whose customers are caught running scams **do not behave this way.** The normal response is silence. NameSilo:
- Published a public defense
- Committed to scrubbing security detections
- Paid for and used platform-level access to silence the witness
- Continued the campaign across multiple surfaces

**A registrar that goes this far, this publicly, this consistently, on behalf of a single operator, has reasons that cannot be explained by ordinary commercial relationships.**

---

## 10. EVIDENCE H — The subpoena line

**Date:** February 17, 2026 — **24 days before NameSilo published their defense**
**From:** Operator (N.R.)
**To:** `abuse@phishdestroy.io`

> **"Feel free to subpoena the domain registrar for my information."**

A guy running a ten-year crypto drainer. $550/mo bulletproof hosting in Belize. Russian DDoS-Guard. ProtonMail. And he calmly invites a security-research organization to subpoena his own registrar.

**Nobody behaves like that with a registrar that might shut them down.**

**Nobody behaves like that unless they already know how the registrar will react.**

Twenty-four days later, that registrar called him "the victim" in public.

**Status:** Raw mail-log form, full SMTP headers, DKIM signatures, receiving-side timestamps. Available to ICANN Compliance and law enforcement on request.

---

## 11. All exhibits with SHA-256

| # | Description | File | SHA-256 |
|---|---|---|---|
| 10 | Operator email (Feb 16) | [`01-operator-email-feb16.png`](evidence/01-operator-email-feb16.png) | `919b5ee4c0f3a889381c644b557736d35625c69abaddd0ec7a8251eb514b0111` |
| 11 | PhishDestroy reply (Feb 16) | [`01-phishdestroy-reply-feb16.png`](evidence/01-phishdestroy-reply-feb16.png) | `ecced35149dbf19dff7399cd86708d28aff7b8ab044e132c4c92cafbe222a753` |
| 08 | NameSilo statement + context (Mar 12-14) | [`03-namesilo-statement-mar13.png`](evidence/03-namesilo-statement-mar13.png) | `ad29e1d3d4803ff37c88ef860bef6de9e62f6ce533657f2e5c5460eb2e0b8ebf` |
| 03 | "@NameSilo is lying" + ICANN tweet (Mar 16-18) | [`04-tweet-namesilo-is-lying.png`](evidence/04-tweet-namesilo-is-lying.png) | `c556e13ff0e4265cbba76b6a518f0862dee67467c1b264181e27eef8046eda6a` |
| 04 | "Honest question" + "we've proven" (Mar 16) | [`04-tweet-honest-question.png`](evidence/04-tweet-honest-question.png) | `bbb0ecd0b7164bf91ace59bc0de01ae953a828a34765b36b89e07479e76ee674` |
| 06 | "Press secretary" thread (Mar 16) | [`04-tweet-press-secretary.png`](evidence/04-tweet-press-secretary.png) | `c9007cb4acf1a264fb82e36a57708a1c35e4b6824eb2734a6a7dff095588bd84` |
| 07 | CryptOpus quote (Feb 22) | [`04-tweet-cryptopus-quote.png`](evidence/04-tweet-cryptopus-quote.png) | `6ffd3020793e9d850f0f10f7b4406b165e7d266d692a647ecb24eab9840e7f7f` |
| D1 | X Support "no violation" (Apr 15) | [`06-x-support-no-violation.png`](evidence/06-x-support-no-violation.png) | `2753d02ffeb1b2853bdc33ddec888e3652d9d3829b265e1228c8f28b53b86efa` |
| D2 | X Support "restored" subject (Apr 15) | [`06-x-support-subject-restored.png`](evidence/06-x-support-subject-restored.png) | `482d0ebba1656c3b338957e40cda0abc7a0017eb6ad08f2a0d639468298ccaf3` |
| PD | PhishDestroy platform | [`09-phishdestroy-platform.png`](evidence/09-phishdestroy-platform.png) | `de5b430bb4cad5a422ddf1bb6a8c348fffdf0673e7ea8bfface4fb312f46b087` |

Machine-readable: [`EVIDENCE_HASHES.txt`](EVIDENCE_HASHES.txt)

---

## 12. Permanent mirrors & IPFS

This story lives on every surface that will hold it. If any mirror goes down, the rest remain. New mirrors are added on every takedown attempt.

### Active mirrors

| Surface | URL | Type | Can they delete it? |
|---|---|---|---|
| **Canonical site** | [phishdestroy.io/namesilo-killed-our-twitter](https://phishdestroy.io/namesilo-killed-our-twitter) | HTML | Only via hosting provider |
| **GitHub repo** | [github.com/phishdestroy/namesilo-xmrwallet-coverup](https://github.com/phishdestroy/namesilo-xmrwallet-coverup) | Markdown + evidence/ | DMCA only (US) |
| **GitHub Pages** | [phishdestroy.github.io/namesilo-xmrwallet-coverup](https://phishdestroy.github.io/namesilo-xmrwallet-coverup/) | HTML mirror | Same as above |
| **Codeberg** | codeberg.org/phishdestroy/namesilo-xmrwallet-coverup | Full repo mirror | Germany — DMCA doesn't apply |
| **GitLab** | gitlab.com/phishdestroy/namesilo-xmrwallet-coverup | Full repo mirror | Different company, different process |
| **SourceHut** | sr.ht/~phishdestroy/namesilo-xmrwallet-coverup | Full repo mirror | Minimal platform, different jurisdiction |
| **Medium (main)** | [phishdestroy.medium.com/namesilo-lied...](https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e) | Article | Platform moderation |
| **Medium (earlier)** | [phishdestroy.medium.com/xmrwallet-com...](https://phishdestroy.medium.com/xmrwallet-com-2953f35b8a79) | Article | Platform moderation |
| **dev.to** | dev.to/phishdestroy/namesilo-lied | Article | Community platform, hard to suppress |
| **HackerNoon** | *Submit after GitHub push* | Article | Blockchain-backed publishing |
| **Mirror.xyz** | *Publish after GitHub push* | Article + evidence | **On-chain, permanent, no takedowns** |
| **GhostArchive** | [ghostarchive.org/archive/CXXZ0](https://ghostarchive.org/archive/CXXZ0) | NameSilo's tweet | Immutable snapshot |
| **Wayback Machine** | *Submit all URLs after push* | Every page | Extremely hard to remove |
| **archive.today** | *Submit all URLs after push* | Every page | **Europe — US DMCA doesn't work** |
| **Technical breakdown** | [phishdestroy.io/xmrwallet-namesilo-exposed](https://phishdestroy.io/xmrwallet-namesilo-exposed) | HTML | Only via hosting provider |
| **GitHub (technical)** | [github.com/phishdestroy/DO-NOT-USE-xmrwallet-com](https://github.com/phishdestroy/DO-NOT-USE-xmrwallet-com) | Technical evidence | DMCA only (US) |
| **IPFS** | *CID to be published after pinning* | Immutable, decentralized | **No. Content-addressed. Anyone can re-pin.** |
| **Arweave** | *TX ID to be published after upload* | Permanent storage | **No. Pay once, stored forever. No takedowns.** |
| **Filecoin** | *Via web3.storage deals* | Redundant storage | **No. Decentralized storage deals.** |
| **Nostr** | *Publish key posts after push* | Decentralized social | **No central server. No moderation.** |
| **Radicle** | *Push repo after GitHub* | P2P git hosting | **No central server to take down.** |

### Immutable / decentralized archiving plan

Because NameSilo and the operator are actively attempting to erase every surface, we use **different jurisdictions + different protocols**. A US DMCA takedown doesn't work on a German server. A platform complaint doesn't work on a blockchain. A hosting takedown doesn't work on IPFS. They would need to file in 10+ different places under 10+ different legal frameworks simultaneously. That's the point.

**Layer 1 — Blockchain / permanent (no takedowns possible):**
1. **IPFS** — Pin evidence/ + key docs via web3.storage/Pinata. Content-addressed = immutable. Anyone can re-pin the CID.
2. **Arweave** — Upload full evidence package. Pay once, stored forever. No mechanism to delete.
3. **Filecoin** — Redundant decentralized storage via web3.storage deals.
4. **Mirror.xyz** — Publish article on-chain. Ethereum-backed. Permanent.
5. **Radicle** — Push git repo to P2P git hosting. No central server.
6. **Nostr** — Publish key evidence posts. Decentralized protocol, no moderation layer.

**Layer 2 — Different jurisdictions (DMCA-resistant):**
7. **Codeberg** (Germany) — Full repo mirror. US DMCA doesn't apply.
8. **GitLab** (Netherlands) — Full repo mirror. Different company, different legal process.
9. **SourceHut** (US, but indie) — Full repo mirror. Minimal platform, owner-operated.
10. **archive.today** (Europe) — Snapshot every URL. DMCA doesn't work.

**Layer 3 — Web archives (extremely hard to remove):**
11. **Wayback Machine** — Submit every URL. Requires formal legal process to remove.
12. **GhostArchive** — Already holds NameSilo's tweet. Submit article mirrors.

**Layer 4 — Publishing platforms (community protection):**
13. **dev.to** — Article ready (article.devto.md).
14. **HackerNoon** — Blockchain-backed publishing platform.
15. **Medium** — Already published.

**Layer 5 — Wayback pre-formed save links:**
- `https://web.archive.org/save/https://phishdestroy.io/namesilo-killed-our-twitter`
- `https://web.archive.org/save/https://github.com/phishdestroy/namesilo-xmrwallet-coverup`
- `https://web.archive.org/save/https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e`
- `https://web.archive.org/save/https://codeberg.org/phishdestroy/namesilo-xmrwallet-coverup`
- `https://web.archive.org/save/https://gitlab.com/phishdestroy/namesilo-xmrwallet-coverup`

### How to help mirror

If you want to help keep this alive:

```bash
# Clone and pin to IPFS
git clone https://github.com/phishdestroy/namesilo-xmrwallet-coverup.git
cd namesilo-xmrwallet-coverup
ipfs add -r evidence/ PROOFS.md README.md
# Share the CID

# Submit to Wayback Machine
curl -s "https://web.archive.org/save/https://github.com/phishdestroy/namesilo-xmrwallet-coverup"

# Submit to archive.today
# Paste URL at https://archive.ph/
```

Every mirror they have to take down costs them time, money, and public credibility. Every mirror we add costs us one command.

---

## 13. Materials available on request

| Material | Available to |
|---|---|
| Full operator email thread (Feb 16-17, 2026), including "subpoena the registrar" line | ICANN Compliance, law enforcement, court order |
| 20+ NameSilo abuse-report delivery receipts (2023-2026) | ICANN Compliance, anyone testing the "no abuse reports" claim |
| Server-side capture of 8 `xmrwallet[.]com` PHP endpoints | ICANN Compliance, security vendors, prosecutors |
| Source-IP DDoS analysis (NameSilo/"njan la" infrastructure) | Public on phishdestroy.io when complete |
| Internal SMTP/DKIM headers for operator emails | Court order, ICANN Compliance |

Contact: **[abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)** — subject line must identify your role.

---

## 14. How to verify

```bash
git clone https://github.com/phishdestroy/namesilo-xmrwallet-coverup.git
cd namesilo-xmrwallet-coverup/evidence
sha256sum -c ../EVIDENCE_HASHES.txt
```

All 10 files must report `OK`. If any fails, the local copy has been tampered with — open an Issue.

---

## 15. License

Published under **CC BY 4.0** with an **explicit evidentiary-use grant** ([`LICENSE`](LICENSE)):

Any victim, prosecutor, regulator, ICANN compliance officer, law-enforcement agency, court, journalist, or researcher may reproduce, transmit, display, and cite this evidence package — in whole or in part — in any filing, complaint, proceeding, publication, or official record. No further permission required from PhishDestroy.

**Take it. Use it. File it. Attach it. Cite it. Mirror it. Pin it. They can't erase all of us.**

---

*Last updated: May 7, 2026. Every update is committed to git with a timestamp. Mirrored across GitHub, GitHub Pages, IPFS, Wayback, archive.today, GhostArchive, and growing.*

*Contact: [abuse@phishdestroy.io](mailto:abuse@phishdestroy.io) (general) · [report@phishdestroy.io](mailto:report@phishdestroy.io) (victims)*
