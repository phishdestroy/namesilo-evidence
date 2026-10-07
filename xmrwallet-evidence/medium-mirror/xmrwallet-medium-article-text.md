# xmrwallet.com Scam Exposed: NameSilo Called a $2M Monero Theft a "Hack"

> **Mirrored from Medium** (phishdestroy.medium.com/xmrwallet-com-2953f35b8a79). Saved locally because Medium articles can be taken down. Original HTML also preserved in this directory.

---

xmrwallet.com Scam Exposed: NameSilo Called a $2M Monero Theft a “Hack” — Then Became the Scammer’s Press Secretary

PhishDestroy

16 min read

Mar 16, 2026

Listen

Share

A registrar fabricated a “compromise” story to protect a phishing domain flagged by Fortinet, Webroot, and 4 other security vendors. Three peer registrars suspended the same evidence. NameSilo chose to defend the thief. If they’re this committed to protecting him — perhaps they should also cover his debts to the victims.

Press enter or click to view image in full size

xmrwallet[.]com — scam which Namesilo defend

This investigation was conducted by

PhishDestroy Research

— an independent cybersecurity team that tracks, documents, and destroys phishing infrastructure. Full evidence:

phishdestroy.github.io/DO-NOT-USE-xmrwallet-com

. Repository:

github.com/phishdestroy/DO-NOT-USE-xmrwallet-com

xmrwallet.com

has operated since 2016, marketing itself as a free, open-source Monero wallet. A

live network capture

on February 18, 2026 proved the site

steals private Monero view keys on every login

hijacks transactions server-side

. Fifteen documented victims across

Trustpilot

Sitejabber

, and

BitcoinTalk

. Six security vendors on

VirusTotal

flag it as malicious. Estimated stolen:

$2M+

Abuse reports were filed with all registrars. Three suspended their domains within days. The fourth —

NameSilo, LLC

— contacted the scammer, believed his story, and published a defense so absurd it deserves a line-by-line autopsy.

NameSilo’s public statement — verbatim

“Our Abuse team conducted an in-depth review into this case and it seems that domain was compromised a few months ago (during which a copy of the webpage was replaced with a crypto-drainer). Prior to that, we had received no abuse reports related to this domain. After an extensive investigation, our team found evidence of the compromise not involving the registrant, and they immediately took steps to reverse it. The registrant is also working to get the website delisted from VT reports. Are you able to confirm if the abuse you’re seeing is recent or from this initial hack? If you have any new evidence of abuse taking place, please send it over to us (at support@namesilo.com if that’s more preferable) and we will re-open the investigation again.”

Seven claims. Seven lies. Let’s go.

LIE #1: “The domain was compromised”

NameSilo says someone hacked xmrwallet.com and injected a crypto-drainer.

The theft mechanism is not injected code. It is the

core architecture

of the application — a complete session system built across 8 PHP endpoints, transmitting the victim’s private view key 40+ times per session.

Press enter or click to view image in full size

Neimsilo, a highly experienced abuse department, is looking for ways to shield its client from the truth

Every login sends your private key to

/auth.php

. The server returns a

session_key

— not a random token, but your address and view key in Base64:

session_key = [blob]:[base64(address)]:[base64(viewkey)]

# Verify:

import base64

print(base64.b64decode(

"ZWZiYTEzZWNiOGIzNjA2NjBhM2RjYWFmYWY3Y2Y5OTE0OTcxM2QwNjRiOWQ2NDk5N2IyNDU0ZDU4ZWU2NzgwMA=="

).decode())

# → efba13ecb8b360660a3dcaafaf7cf99149713d064b9d64997b2454d58ee67800

#   ^^^ real private view key from live capture

This key is re-sent on

every request

— to

/getheightsync.php

(12×),

/gettransactions.php

(10×),

/getbalance.php

(6×),

/dashboard.html

(4×), and more. Full capture data:

PhishDestroy evidence page

When you send XMR:

raw_tx_and_hash.raw = 0    // your transaction — discarded, never broadcast

if (type == 'swept') {     // custom theft flag — not in Monero protocol

txid = 'Unknown transaction id'

A hidden backdoor phones home automatically —

/support_login.html

with hardcoded session

8de50123dab32

. Not user-initiated. Not in the GitHub code. Documented in

cached Issue #35

The GitHub repository has a

5.3-year commit gap

(2018–2024). The Wayback Machine shows no

session_key

in 2023 — but it's in production in 2025. This system was built over years, not injected in a hack.

Does NameSilo believe a hacker built a complete PHP backend with 8 endpoints, a Base64 key exfiltration protocol, a transaction hijacking mechanism, and a hardcoded backdoor — as part of a “compromise”?

Or is NameSilo just repeating what the scammer told them?

Press enter or click to view image in full size

An Old Russian Dog That Removes the Issue

LIE #2: “We had received no abuse reports”

This is the lie that proves NameSilo never investigated anything.

Here is what existed —

publicly, for years

— before any report was filed with NameSilo:

Press enter or click to view image in full size

The Truth About the Old Russian Dog

VirusTotal

— six vendors flag xmrwallet.com.

Fortinet

(Fortune 500, FortiGuard Labs, 700,000+ organizations): “Phishing.”

Webroot/OpenText

(BrightCloud threat intel): “Malicious.”

ADMINUSLabs

: “Malicious.”

CyRadar

: “Malicious.”

Lionic

: “Malicious.”

Seclookup

: “Malicious.” These are

automated systems

— they crawl, analyze, and classify every domain on the internet continuously. They don’t file “abuse reports.” They just flag threats. The data was there for anyone to see.

URLQuery

— automated analysis flagged the domain. Public report, publicly accessible, predating 2026.

ScamAdviser

— “very low trust score.” The automated analysis notes: “registrar has high percentage of fraud sites” and “owner identity hidden via privacy service.”

Trustpilot

— multiple theft reports going back years. $200 stolen. 17.44 XMR stolen (with TxID and TX Key documented). Funds redirected to unknown wallets. Transaction verification failing.

Sitejabber

590 XMR (~$177,000) stolen

in a single report. 20 XMR stolen. Rating: 1.5/5. Reports calling the site “fake” and “scammers.”

BitcoinTalk

— the largest cryptocurrency forum in the world has a public warning thread:

“[WARNING] XMRWallet.com Scams — Stay vigilant!”

Reddit r/Monero

— the operator (u/WiseSolution) was

banned from the official Monero subreddit in 2018

. Eight years before NameSilo’s “review.”

Searching “xmrwallet.com” on VirusTotal takes

five seconds

. Googling “xmrwallet.com scam” returns a wall of warnings on the

first page

. Checking Trustpilot takes

one click

“No prior abuse reports”

means one of two things: NameSilo’s “in-depth review” didn’t include a single Google search — or they found all of this and are lying about it. Which is it, NameSilo?

Press enter or click to view image in full size

Oh, come on — how could a scammer be running a DDoS attack on the guard these days???

Press enter or click to view image in full size

Will Namesilo help set the record straight????

LIE #3: “Evidence of the compromise not involving the registrant”

Translation: NameSilo contacted the scammer, the scammer said “I was hacked,” and NameSilo wrote it down as an “investigation.”

Here’s what this “innocent registrant” has been doing:

Registered four escape domains

— xmrwallet.cc, xmrwallet.biz, xmrwallet.net, xmrwallet.me — across four different registrars, each prepaid 5–10 years. Registered

before

the investigation was published. Deliberately spread to slow coordinated takedowns. (

Full domain analysis

Deleted 21+ GitHub issues

documenting fraud — over eight years. Deleted Issues #35 and #36 (the full technical proof) the same day two escape domains were suspended. (

Archived deleted evidence

Zero technical rebuttals in eight years.

Not one network capture. Not one code audit. Not one explanation for

session_key

raw = 0

, or the backdoor. (

Cached Issue #35

Cached Issue #36

$550/month bulletproof hosting

(IQWeb FZ-LLC, Belize) behind

DDoS-Guard

(Russia) — for a “free open-source client-side” project. GitHub Pages costs $0. (

Infrastructure IOCs

Banned from r/Monero in 2018.

Operator profile

50+ paid SEO articles

across crypto media to bury negative results.

Zero donation wallets

despite claiming “funded by donations.” (

Full exposure article

Four Google trackers

(GTM, GA, GA4, DoubleClick) inside a “privacy” wallet. No legitimate Monero wallet does this — not

Monero GUI

, not

Feather Wallet

, not

Cake Wallet

, not

Monerujo

Hacked website owners publish incident reports and fix their code. This operator deletes evidence, buys escape domains, hires new developers for captcha systems, and pays for SEO campaigns.

That’s not a victim. That’s an operation.

Press enter or click to view image in full size

Is Namesilo getting carried away? Or maybe njan.la? Who over there likes scammers?

LIE #4: “They immediately took steps to reverse it”

Reverse what?

session_key

exfiltration is in production

right now

. The

raw_tx_and_hash.raw = 0

is in production

right now

. The Google trackers are firing

right now

. The DDoS-Guard hosting is active

right now

. The

Tor hidden service

runs identical code

right now

The GitHub repository has

zero commits

addressing any security incident. No changelog. No patch. No incident report.

Nothing was “reversed.” The theft code is the product. It has always been the product.

LIE #5: “The registrant is working to get delisted from VT”

This single sentence exposes NameSilo’s role completely.

Fortinet

— a Fortune 500 cybersecurity company — classified xmrwallet.com as

“Phishing.”

This classification is used by firewalls, email gateways, and security appliances protecting

700,000+ organizations worldwide

The operator’s response: not to remove the phishing code — but to

lobby VirusTotal to remove the detection

And NameSilo presents this as a

positive development

. As evidence that the registrant is acting in good faith.

Read that again. A domain flagged as “Phishing” by Fortinet is trying to get the “Phishing” label removed —

without removing the phishing code

. And the registrar is cheering them on.

A legitimate site owner who was truly hacked would

welcome

VirusTotal detections — it validates the threat existed. They would focus on removing malicious code, not security warnings. This operator is doing the opposite: leaving the code intact, removing the warnings.

NameSilo is actively assisting a flagged phishing domain in suppressing security alerts that protect potential victims.

This isn’t abuse handling. This is a PR service for a criminal.

LIE #6: “Are you able to confirm if the abuse is recent?”

The abuse is current. The abuse is continuous. The abuse has never stopped in eight years.

But the framing of this question is the real tell. NameSilo is not asking because they want to investigate. They’re asking to

shift the burden of proof

to the reporter — so they can close the case if the answer doesn’t arrive fast enough.

The evidence was in the report. The VirusTotal detections are live. The victim reports span years. Three peer registrars reviewed the same evidence and acted. NameSilo is asking researchers to do their job for them — while they do the scammer’s PR.

LIE #7: “We will re-open the investigation”

“Re-open” implies it was once open. Based on the response, NameSilo’s “investigation” consisted of calling the scammer and writing down what he said. That’s not an investigation. That’s dictation.

An actual investigation would have included: a VirusTotal search (5 seconds), a Trustpilot check (1 minute), a Google search for “xmrwallet.com scam” (10 seconds), a read of the

cached Issue #35

(10 minutes), and a basic check of the hosting infrastructure (IQWeb Belize + DDoS-Guard Russia for an “open-source” project?).

NameSilo did none of this. Or did all of it and is lying.

Three registrars protected users. NameSilo became the scammer’s lawyer.

Press enter or click to view image in full size

Neimsilo has taken in a Russian scammer who openly steals tens of thousands

The same evidence package was sent to all registrars:

PublicDomainRegistry

— xmrwallet.cc. Same operator (identical MX records

mx1/mx2.privateemail.com

, same WOT token

8a5554c915e3c17278a7

, 23 file hashes on

VirusTotal

Action: SUSPENDED.

Days. No cover story. No call to the scammer.

WebNic

— xmrwallet.biz. Same infrastructure (AS59692, same DNS, same MX, same WOT token, 23 files on

VirusTotal

Action: SUSPENDED.

Days.

NICENIC International

— xmrwallet.net. Same IP as the already-suspended .biz (

190.115.31.40

). Ten-year prepaid registration.

Action: DNS DEAD.

NameSilo

— xmrwallet.com. The primary domain. Most documented. Most flagged. Most victims. Three peers already acted on identical evidence.

Action: “The registrant is the victim. They’re working to get delisted from VT. Is the abuse recent?”

Three companies in three countries — India, Malaysia, China — independently concluded: fraud. Suspend. One company — NameSilo, USA — concluded: the scammer is the victim, let’s help him remove the warnings.

The victims NameSilo is helping the scammer hide from

Press enter or click to view image in full size

Neimsilo lies to the scammer and ignores the reports

“I do deposit 590 monero 2 day gone and they steal it! Please ban this site and FBI need arest it!” —

Sitejabber

590 XMR. ~$177,000.

“My 17.44 XMR was all gone. I have both the TxID &amp; TX Key.” —

Trustpilot

“Create wallet — put 20 xmr next day 0 xmr — Scammers owner!” —

Sitejabber

“They stole $200 from me, leaving me high and dry.” —

Trustpilot

“Transferred to some other wallets instead of my mentioned wallet.” —

Trustpilot

“Whatever you do, do NOT try to use this wallet. UNABLE TO ACCESS MY FUNDS.” —

Trustpilot

“SCAMMERS! Lost contact when I wanted withdrawal, no response from customer support.” — Scam-Detector.

These reports span

years

. The operator’s response to every victim — same template:

“You used a phishing clone.”

NameSilo’s response:

“The registrant is the victim.”

Conservative estimate: 10,000–50,000+ wallets created over 8 years.

$1.5M–$15M+

stolen at historical prices. Full victim documentation:

PhishDestroy investigation

The escape domain panic — consciousness of guilt

Press enter or click to view image in full size

Neimsilo is not a registrar but an accomplice to a criminal

Feb 4, 2026

— xmrwallet.cc registered. 8yr prepaid.

Investigation not yet published.

Feb 9

— xmrwallet.biz registered. 5yr prepaid.

Still before publication.

Feb 13

Issue #35

published. Full TX hijacking exposed.

Feb 18

Issue #36

published. 109 requests, 43 viewkey transmissions.

Feb 23

— .cc SUSPENDED. .biz SUSPENDED.

Same day:

operator deletes Issues #35 + #36.

Feb 26

— xmrwallet.net registered (10yr, same IP as .biz). xmrwallet.me registered (10yr, same IP as .cc). Four registrars. Zero GitHub commits.

Mar 8

— xmrwallet.net DNS DEAD after

abuse report

Scoreboard: 3/4 escape domains neutralized. 23 years of prepaid registrations wasted. IP recycling proves same operator: .biz IP → reused by .net. .cc IP → reused by .me. All domains share identical NS (

ddos-guard.net

), MX (

privateemail.com

), and WOT token (

8a5554c915e3c17278a7

DNS maps and WHOIS evidence

Does NameSilo believe “compromised” website owners register escape domains across 4 registrars, prepaid for decades, before the investigation is published?

The operator NameSilo calls “the victim”

Nathalie Roy

, Canada. GitHub:

nathroy

(ID: 39167759). Reddit: u/WiseSolution — banned from r/Monero (2018). ProtonMail: royn5094@protonmail.com. Self-identified on xmrwallet.com/support.html. Full profile:

PhishDestroy operator analysis

Claims “funded by donations” — zero donation wallet exists. Pays $550/month bulletproof hosting. 50+ paid SEO articles. DDoS-Guard CDN. Android app. 100+ blog posts in 10 languages. Hired a second developer for a custom captcha system in March 2026 — which was

reverse-engineered and defeated within hours

NameSilo calls this person the victim of a compromise.

The operator’s own words — emails to PhishDestroy

After xmrwallet.com was reported, the operator (

royn5094@protonmail.com

) emailed

PhishDestroy

directly. Four emails over 7 days. Zero technical rebuttals. And one sentence that reveals everything about the relationship between the operator and NameSilo.

Feb 16 — “We don’t store keys”

“We are an open source crypto wallet that is non-custodial, we don’t store seeds or keys, everything is done in your browser locally. Please remove your report on us, thank you. N.R.”

Press enter or click to view image in full size

The same day, PhishDestroy responded with a full technical breakdown:

raw_tx_and_hash.raw = 0

(client transaction discarded),

session_key

containing the victim's private view key in Base64,

type == 'swept'

(custom theft marker absent from Monero protocol), production-only parameters not in the public GitHub repository. The operator never addressed a single finding.

Feb 17 — Two emails in one day. Panic.

“This is the data we need to offer the service to users. This is not grounds for a domain suspension.”

Yesterday:

“we don’t store keys.”

Today:

“this is the data we need.”

Two mutually exclusive statements in 24 hours.

Press enter or click to view image in full size

“You are accusing without proof. The way the website was built does not verify anything was stolen, so I’m not sure what you’re going to waste your time on. If this is a legal matter, feel free to subpoena the domain registrar for my information to submit a complaint in the courts.”

Now read that last sentence again: “Feel free to subpoena the domain registrar.”

This was written on Feb 17 —

before

we contacted NameSilo,

before

the abuse report was filed, and

before

NameSilo published their “compromise” cover story. At this point, nobody knew how NameSilo would respond.

And yet the operator is not worried. Not even slightly. A scammer running a phishing operation on bulletproof hosting behind DDoS-Guard should be

terrified

of a registrar investigation. A normal scammer would say “go ahead, try” — a bluff. But this operator doesn’t bluff. This operator

actively directs us toward the registrar

, as if confident that NameSilo will take his side.

No scammer in history has ever said “please involve my registrar” — unless they already know the outcome.

Why was the operator so confident? Was it just arrogance? Or does the operator have a relationship with someone at NameSilo — a friend in support, a remote contractor, a connection that guarantees protection? We don’t know. But the sequence of events speaks for itself:

1. Feb 17 — operator says “subpoena the registrar” with zero concern.

2. Feb 23 — three other registrars suspend his domains immediately.

3. NameSilo — the one registrar the operator pointed us toward — not only refuses to act, but publishes a defense calling him “the victim” and helps him remove VirusTotal warnings.

The operator predicted NameSilo’s response before it happened. That’s either the luckiest guess in the history of cybercrime — or the operator knew something we didn’t.

Feb 18 — PhishDestroy responds with evidence and a warning.

Press enter or click to view image in full size

Feb 23 — Domains suspended. Operator panics.

The same day xmrwallet.cc and xmrwallet.biz were

SUSPENDED

by their registrars, the operator’s tone changed completely:

“I’ve communicated with my lawyer and you’ll hear from them directly soon for harassment, spamming and brand reputation damage. We’ve hired a private investigator to find your information to file the case.”

“You can literally look up Trezor, Ledger or any other major wallet, they all have complaints about stolen funds. Every single one of them. They also get their view keys to service users, that’s how it works.”

Trezor and Ledger are hardware wallets.

They do not collect private view keys server-side. They don’t have PHP backends. They don’t transmit

session_key

to a server 40 times per session. The operator either doesn't understand cryptocurrency wallets — or is counting on the reader not understanding them.

Four emails. Zero explanations for

session_key

raw = 0

swept

, or the 5.3-year GitHub divergence. From "please remove your report" to "my lawyer" in 7 days.

The lawyer has not materialized in 4 weeks.

But here’s the detail that destroys NameSilo’s entire “compromise” narrative:

In all four emails (Feb 16–23), the operator speaks in first person —

“we are an open source wallet,”

“this is how the website is run,”

“this is the data we need.”

The operator defends the code, the architecture, the data collection — as their own work.

Not once does the operator mention any hack, compromise, or unauthorized access.

On Feb 16–17, the operator told us: “this is how the website is run.” Weeks later, NameSilo told the public: “the domain was compromised.” These two statements cannot both be true.

The “compromise” story didn’t exist until NameSilo contacted the operator and needed an explanation to close the case. The operator’s own emails — written before the cover story was needed — prove the “hack” narrative was

fabricated after the fact

NameSilo received the same evidence — and the same operator emails. They chose the cover story over the evidence. They called this person “the victim.”

NameSilo’s liability: from negligence to complicity

Press enter or click to view image in full size

NameSilo hired and defended a known fraudster

Before NameSilo’s response, this was a case of registrar negligence — bad, but common. Abuse teams are slow. Things fall through cracks.

After NameSilo’s response, this is something else entirely.

NameSilo didn’t just fail to investigate. They:

Contacted the accused operator

and accepted his version as fact.

Publicly declared the operator innocent

— calling him the “victim” of a “compromise.”

Revealed they know the operator is lobbying to remove VirusTotal detections

— and presented this as progress.

Published a cover story

(“domain was compromised”) contradicted by 8 years of evidence.

Shifted the burden of proof

to the reporters: “Is the abuse recent?”

This is not an abuse team dropping the ball.

This is a registrar acting as the scammer’s press secretary.

And if NameSilo is this committed to defending the operator —

perhaps they should also be committed to making the victims whole.

Under

ICANN’s 2013 Registrar Accreditation Agreement (RAA), Section 3.18

, registrars must investigate and respond appropriately to abuse. NameSilo’s “appropriate response” was to write a press release defending the accused.

Three registrars — PublicDomainRegistry (India), WebNic (Malaysia), NICENIC (China) — in three countries, with three different legal frameworks, all independently concluded:

fraud. Suspend.

NameSilo concluded:

“the registrant is the victim.”

Every dollar stolen through xmrwallet.com

after NameSilo published that statement

was stolen by an operator that NameSilo publicly declared innocent. Every future victim can point to NameSilo’s words:

“Our team found evidence of the compromise not involving the registrant.”

NameSilo cleared the operator. NameSilo endorsed the domain. NameSilo put it in writing.

If those statements are wrong — and the evidence overwhelmingly proves they are — then NameSilo’s public endorsement directly contributed to every subsequent theft. The victims didn’t just lose money to a scammer. They lost money to a scammer

whose registrar publicly vouched for him

With this level of commitment to acting as the operator’s defense attorney, NameSilo should be equally committed to covering the operator’s debts. If you vouch for a thief — you share the bill when he gets caught.

Take action

Report xmrwallet.com as phishing:

Google Safe Browsing

— blocks in Chrome, Firefox, Safari, Edge

Netcraft

— used by ISPs and registrars globally

PhishTank

— community blocklist

APWG

— Anti-Phishing Working Group

Phish.Report

— auto-reports to 6+ platforms

→ abuse@namesilo.com — the registrar that calls it a “hack”

File ICANN complaint against NameSilo:

ICANN complaint form

— RAA Section 3.18 violation. Include NameSilo’s statement verbatim.

Report to law enforcement

(operator: Nathalie Roy, Canada):

Canadian Anti-Fraud Centre

RCMP Cybercrime

FBI IC3

(accepts international)

Europol

Interpol

Use safe wallets:

Monero GUI

— official, zero trackers

Feather Wallet

— Tor built-in, zero trackers

Cake Wallet

— iOS/Android, zero trackers

Monerujo

— Android, zero trackers

Never enter a private key or seed phrase into a website. Ever.

Full evidence — permanent, cached, verifiable

Full investigation — PhishDestroy

Deleted evidence archive

Issue #35 — cached HTML

Issue #36 — cached HTML

VirusTotal — xmrwallet.com

VirusTotal — xmrwallet.biz

VirusTotal — xmrwallet.cc

VirusTotal — xmrwallet.me

URLQuery report

ScamAdviser

BitcoinTalk warning thread

Scam exposed — article

Deleted evidence — article

Is xmrwallet safe? — article

Operator profile — article

Captcha defeated — article

Safe alternatives — article

GitHub repository — full evidence

PhishDestroy blocklist — 100,000+ domains

Press enter or click to view image in full size

I suggest that the victims ask Namesilo who will compensate them for their losses

NameSilo didn’t ignore the evidence. They read it, called the scammer, believed him, declared him innocent, and are helping him suppress security warnings. Then asked the researchers to prove the abuse is “recent.”

That’s not negligence. That’s a partnership.

NameSilo on X: "@Phish_Destroy Our Abuse team conducted an in-depth review into this case and it…

Edit description

ghostarchive.org

https://ghostarchive.org/archive/CXXZ0

Three registrars protected users. NameSilo protected the scammer — and put it in writing. Their statement will be Exhibit A in every filing from this point forward.

If you vouch for the thief, you share his bill.

Scammers delete evidence. Registrars write cover stories. We make it permanent.

PhishDestroy Research

Telegram

Twitter/X

This investigation is based on publicly available evidence, live network captures, OSINT, public review platforms, and NameSilo’s own verbatim public statement. No unauthorized access was performed. All findings are independently reproducible using the archived data. NameSilo’s response is quoted in full, unedited.

If you are a victim of xmrwallet.com: document your TxID, wallet address, and date of loss. Report to

ic3.gov

and local law enforcement. Include NameSilo’s public statement in your filing. Do NOT pay “recovery services” — they are secondary scams.

