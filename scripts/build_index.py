import re, os

BASE = 'C:/Users/admin/Documents/GitHub/namesilo-evidence/docs/'

with open(BASE + 'namesilo-scan.html', 'rb') as f:
    scan = f.read().decode('utf-8', 'replace')
style_block = re.search(r'<style>.*?</style>', scan, re.DOTALL).group()

page = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<title>NameSilo, LLC (IANA #1479) — Registrar Abuse Investigation | PhishDestroy</title>
<meta name="description" content="Complete zone scan of all 5,269,357 NameSilo domains. 87.3% dead or parked. 183,419 malicious domains behind their own WHOIS privacy. NameSilo publicly defended a $20M Monero drainer and committed to erasing his VirusTotal record. Filed with ICANN March 18, 2026.">
<meta name="keywords" content="NameSilo abuse, xmrwallet scam, Monero drainer, registrar abuse, ICANN compliance, domain investigation, phishing, PhishDestroy, IANA 1479">
<meta property="og:type" content="website">
<meta property="og:site_name" content="PhishDestroy">
<meta property="og:url" content="https://phishdestroy.github.io/namesilo-evidence/">
<meta property="og:title" content="NameSilo (IANA #1479) — Registrar Abuse Investigation">
<meta property="og:description" content="5,269,357 domains scanned. 87.3% dead or parked. 183,419 malicious behind NameSilo's own privacy shield. NameSilo defended a $20M Monero drainer — in writing, on their official account.">
<meta property="og:image" content="https://phishdestroy.eth.limo/namesilo-og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="NameSilo (IANA #1479) — Registrar Abuse Investigation">
<meta name="twitter:description" content="5.27M domains scanned. 87.3% dead/parked. 183,419 malicious. NameSilo defended a $20M Monero drainer on their official account.">
<link rel="canonical" href="https://phishdestroy.github.io/namesilo-evidence/">
<link rel="icon" href="https://phishdestroy.eth.limo/assets/favicon-32x32.png" type="image/png">
<meta name="llms-txt" content="https://phishdestroy.github.io/namesilo-evidence/llms.txt">
''' + style_block + '''
<style>
.hub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin:24px 0}
.hub-card{background:var(--s2);border:1px solid var(--bdr);border-radius:8px;padding:20px 22px;display:flex;flex-direction:column;transition:.15s;text-decoration:none;color:inherit}
.hub-card:hover{background:var(--s3);border-color:rgba(255,255,255,.15);transform:translateY(-1px)}
.hub-card.primary{border-color:rgba(110,168,215,.3);background:rgba(110,168,215,.04)}
.hub-card.danger{border-color:rgba(218,54,51,.3);background:rgba(218,54,51,.04)}
.hc-icon{font-size:22px;margin-bottom:10px}
.hc-title{font-size:14px;font-weight:700;margin-bottom:4px;color:var(--tx)}
.hc-desc{font-size:12px;opacity:.6;line-height:1.5;flex:1;margin-bottom:12px}
.hc-stat{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--cy);border-top:1px solid var(--bdr);padding-top:8px;margin-top:auto}
.hc-stat.red{color:var(--rd)}
.ev-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin:20px 0}
.ev-card{background:var(--s2);border:1px solid var(--bdr);border-radius:6px;overflow:hidden}
.ev-card img{width:100%;display:block;opacity:.9;transition:.15s}
.ev-card img:hover{opacity:1}
.ev-cap{padding:10px 12px;font-size:11px;opacity:.6;line-height:1.4}
.tl-row{display:flex;gap:16px;padding:10px 0;border-bottom:1px solid var(--bdr2);font-size:13px;align-items:baseline}
.tl-date{font-family:"JetBrains Mono",monospace;color:var(--tx3);white-space:nowrap;min-width:90px;font-size:11px}
.tl-text{line-height:1.5}
.tl-text strong{color:var(--tx)}
.lie-grid{display:grid;gap:12px;margin:20px 0}
.lie-card{background:rgba(218,54,51,.04);border:1px solid rgba(218,54,51,.2);border-radius:6px;padding:16px 18px}
.lie-claim{font-size:12px;font-family:"JetBrains Mono",monospace;color:var(--tx2);margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(218,54,51,.15)}
.lie-fact{font-size:13px;line-height:1.55;opacity:.85}
.lie-verdict{display:inline-block;margin-top:8px;font-family:"JetBrains Mono",monospace;font-size:10px;font-weight:700;padding:2px 8px;border-radius:3px;background:rgba(218,54,51,.15);color:#f88}
.lie-verdict.ok{background:rgba(63,185,80,.15);color:#3fb950}
.mirror-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px;margin:16px 0}
.mirror-card{background:var(--s2);border:1px solid var(--bdr);border-radius:6px;padding:12px 14px}
.mirror-card a{color:var(--cy);font-size:13px;font-family:"JetBrains Mono",monospace;word-break:break-all;text-decoration:none}
.mirror-card a:hover{text-decoration:underline}
.mirror-label{font-size:10px;opacity:.45;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
</style>
</head>
<body>
<header><nav>
  <a href="https://phishdestroy.eth.limo" target="_blank" rel="noopener">phishdestroy.eth.limo</a>
  &nbsp;&middot;&nbsp; <strong>NameSilo Investigation</strong>
  &nbsp;&middot;&nbsp; <a href="https://github.com/phishdestroy/namesilo-evidence" target="_blank" rel="noopener">GitHub</a>
</nav></header>

<main style="max-width:1100px;margin:0 auto;padding:20px 24px">

<!-- HERO -->
<div class="hero" style="padding:48px 0 36px">
  <div class="hero-inner">
    <div class="hero-badges">
      <span class="hb live">ACTIVE INVESTIGATION</span>
      <span class="hb tlp">TLP:CLEAR</span>
      <span class="hb iana">IANA #1479</span>
      <span class="hb tlp">ICANN Filed · Mar 18, 2026</span>
    </div>
    <h1>NameSilo, LLC<br><strong>Registrar Abuse Investigation</strong></h1>
    <p class="hero-sub">5,269,357 domains scanned &nbsp;·&nbsp; Complete zone file census &nbsp;·&nbsp; PhishDestroy Research</p>
    <div style="display:flex;flex-wrap:wrap;gap:20px;margin-top:28px">
      <div><div style="font-size:2.2rem;font-weight:800;color:var(--rd);line-height:1">5,269,357</div><div style="font-size:11px;opacity:.5;text-transform:uppercase;letter-spacing:.06em;margin-top:2px">Domains scanned</div></div>
      <div><div style="font-size:2.2rem;font-weight:800;color:var(--rd);line-height:1">87.3%</div><div style="font-size:11px;opacity:.5;text-transform:uppercase;letter-spacing:.06em;margin-top:2px">Dead or parked</div></div>
      <div><div style="font-size:2.2rem;font-weight:800;color:var(--rd);line-height:1">183,419</div><div style="font-size:11px;opacity:.5;text-transform:uppercase;letter-spacing:.06em;margin-top:2px">Malicious (PG-shielded)</div></div>
      <div><div style="font-size:2.2rem;font-weight:800;color:var(--or);line-height:1">$10–20M</div><div style="font-size:11px;opacity:.5;text-transform:uppercase;letter-spacing:.06em;margin-top:2px">Estimated victim losses</div></div>
      <div><div style="font-size:2.2rem;font-weight:800;color:var(--or);line-height:1">20+</div><div style="font-size:11px;opacity:.5;text-transform:uppercase;letter-spacing:.06em;margin-top:2px">Abuse reports — ignored</div></div>
    </div>
  </div>
</div>

<!-- REPORT NAVIGATION -->
<div class="st reveal" style="margin-top:36px">
  <h2>Investigation Reports</h2>
  <div class="ln"></div>
  <p style="font-size:13px;opacity:.6;margin:0 0 4px">All reports are based on the complete NameSilo zone file — no sampling. Raw data available as gzip archives in <a href="https://github.com/phishdestroy/namesilo-evidence/tree/main/pkg/raw_data" style="color:var(--cy)">pkg/raw_data/</a>.</p>
</div>

<div class="hub-grid reveal">
  <a href="namesilo-scan.html" class="hub-card primary">
    <div class="hc-icon">📋</div>
    <div class="hc-title">Zone Scan Report</div>
    <div class="hc-desc">Full investigation: methodology, HTTP scan pipeline, IOC breakdown, server fingerprint cluster analysis, chain of custody. SHA-256 verified.</div>
    <div class="hc-stat">5,269,357 domains &nbsp;·&nbsp; 2-phase scanner</div>
  </a>
  <a href="namesilo-clusters.html" class="hub-card">
    <div class="hc-icon">🔬</div>
    <div class="hc-title">Favicon Cluster Analysis</div>
    <div class="hc-desc">12 operator clusters identified via MurmurHash3 favicon fingerprinting. Identical favicon = identical operator. 328,230-domain single-server network.</div>
    <div class="hc-stat">12 clusters &nbsp;·&nbsp; MurmurHash3</div>
  </a>
  <a href="namesilo-domains.html" class="hub-card">
    <div class="hc-icon">🗂</div>
    <div class="hc-title">IOC Domain List</div>
    <div class="hc-desc">107,252 confirmed criminal domains — fully searchable with country flags, favicons, and abuse categories. Filter by type, country, or keyword.</div>
    <div class="hc-stat red">107,252 IOCs &nbsp;·&nbsp; searchable</div>
  </a>
  <a href="namesilo-privacyguardian.html" class="hub-card danger">
    <div class="hc-icon">🛡</div>
    <div class="hc-title">PrivacyGuardian Shield</div>
    <div class="hc-desc">183,419 malicious domains registered with NameSilo and shielded by PrivacyGuardian.org — NameSilo's own WHOIS privacy service. The registrar owns both.</div>
    <div class="hc-stat red">183,419 malicious &nbsp;·&nbsp; 25+ feeds</div>
  </a>
  <a href="namesilo-reviews.html" class="hub-card danger">
    <div class="hc-icon">⭐</div>
    <div class="hc-title">Review Manipulation</div>
    <div class="hc-desc">129 Trustpilot reviews deleted in 4 months. Bot review network. Victim reports suppressed. NameSilo and xmrwallet both published on PR Newswire same day.</div>
    <div class="hc-stat red">129 deleted &nbsp;·&nbsp; Jan–May 2026</div>
  </a>
  <a href="https://github.com/phishdestroy/namesilo-evidence" target="_blank" rel="noopener" class="hub-card">
    <div class="hc-icon">📁</div>
    <div class="hc-title">GitHub Evidence Repository</div>
    <div class="hc-desc">SHA-256 verified screenshots, full investigation dossier, operator intelligence, case documents, raw scan data. MIT licensed for legal/regulatory use.</div>
    <div class="hc-stat">github.com/phishdestroy/namesilo-evidence</div>
  </a>
</div>

<!-- WHAT HAPPENED -->
<div class="st reveal" style="margin-top:36px">
  <h2>What Happened</h2>
  <div class="ln"></div>
</div>

<div class="panel reveal" style="margin-top:16px">
  <p style="font-size:14px;line-height:1.75;margin:0 0 14px"><strong>xmrwallet[.]com</strong> is a Monero wallet drainer that has been running since approximately 2016. On every login, the site silently transmits the user's private view key to the operator's server via a base64-encoded <code>session_key</code> parameter. Eight PHP endpoints handle the exfiltration. <code>raw_tx_and_hash.raw&nbsp;=&nbsp;0</code> ensures all client-side transactions are discarded. The site has never been compromised — the theft code <em>is</em> the product. Estimated victim losses: <strong>$10–20M</strong>.</p>
  <p style="font-size:14px;line-height:1.75;margin:0 0 14px">PhishDestroy submitted <strong>20+ delivery-receipted abuse reports</strong> to NameSilo between 2023 and 2026. No action was taken. On <strong>March 13, 2026</strong>, NameSilo's official corporate account published a statement calling the operator "the victim," denying all reports ever arrived, and committing in writing to helping him <strong>remove his VirusTotal detections</strong>. Three other registrars — PDR, WebNic, NICENIC — reviewed the same evidence and suspended the domain within days.</p>
  <p style="font-size:14px;line-height:1.75;margin:0">When PhishDestroy published the operator's own emails proving every sentence false, NameSilo used X Gold Checkmark live-support access to lock the @Phish_Destroy research account. X's automated review cleared the account in writing on April 15, 2026. The lock remains in place. <strong>NameSilo's only documented response to this investigation: the scammer's domain was quietly transferred to Namecheap.</strong></p>
</div>

<!-- KEY EXHIBIT -->
<div class="panel reveal" style="margin-top:16px">
  <h3 style="font-size:13px;text-transform:uppercase;letter-spacing:.06em;opacity:.5;font-weight:700;margin:0 0 14px">Exhibit A — NameSilo's official statement · March 13, 2026 · 11,300 views</h3>
  <img src="evidence/03-namesilo-statement-mar13.png" alt="NameSilo official corporate tweet March 13 2026 — defending xmrwallet operator, denying abuse reports, committing to VirusTotal delisting" style="width:100%;border-radius:4px;display:block">
  <p style="font-size:11px;opacity:.5;margin:8px 0 0;font-family:'JetBrains Mono',monospace">Archived: <a href="https://ghostarchive.org/archive/CXXZ0" target="_blank" rel="noopener" style="color:var(--cy)">ghostarchive.org/archive/CXXZ0</a> &nbsp;·&nbsp; SHA-256: ad29e1d3d4803ff37c88ef860bef6de9e62f6ce533657f2e5c5460eb2e0b8ebf</p>
</div>

<!-- THE LIES -->
<div class="st reveal" style="margin-top:36px">
  <h2>NameSilo's Four Claims vs. the Record</h2>
  <div class="ln"></div>
</div>

<div class="lie-grid reveal">
  <div class="lie-card">
    <div class="lie-claim">"Domain was compromised a few months ago."</div>
    <div class="lie-fact">Exfiltration code is the product — 8 PHP endpoints, <code>session_key</code> server-side capture, <code>raw_tx_and_hash.raw=0</code>. Operator's own email (Feb 16): no hack claimed, site defended as his work.</div>
    <span class="lie-verdict">FALSE</span>
  </div>
  <div class="lie-card">
    <div class="lie-claim">"Prior to that, we had received no abuse reports."</div>
    <div class="lie-fact">20+ delivery-receipted reports submitted through NameSilo's own portal, 2023–2026. Public tweet the day before: "9 reports is no joke anymore."</div>
    <span class="lie-verdict">FALSE</span>
  </div>
  <div class="lie-card">
    <div class="lie-claim">"After an extensive review… not involving the registrant."</div>
    <div class="lie-fact">Operator contacted PhishDestroy Feb 16, defending the site as his own. NameSilo adopted a "compromise" narrative the operator himself never used.</div>
    <span class="lie-verdict">FALSE</span>
  </div>
  <div class="lie-card" style="border-color:rgba(255,160,0,.3);background:rgba(255,160,0,.04)">
    <div class="lie-claim" style="border-color:rgba(255,160,0,.2)">"Working with registrant to remove website from VT reports."</div>
    <div class="lie-fact">Written, published, on their verified corporate account. A registrar actively assisting a confirmed fraud operator in erasing consumer-protection security alerts.</div>
    <span class="lie-verdict" style="background:rgba(255,160,0,.15);color:#fba">DOCUMENTED — DAMNING</span>
  </div>
</div>

<!-- EVIDENCE GRID -->
<div class="st reveal" style="margin-top:36px">
  <h2>Key Evidence</h2>
  <div class="ln"></div>
  <p style="font-size:12px;opacity:.5;margin:4px 0 0">All screenshots SHA-256 verified. Full index: <a href="https://github.com/phishdestroy/namesilo-evidence/blob/main/case/EVIDENCE_INDEX.md" style="color:var(--cy)">EVIDENCE_INDEX.md</a></p>
</div>

<div class="ev-grid reveal">
  <div class="ev-card">
    <img src="evidence/01-operator-email-feb16.png" alt="Operator email Feb 16 2026 — no phishing claim, no hack" loading="lazy">
    <div class="ev-cap"><strong>Feb 16, 2026</strong> — Operator email: "There is no phishing." No hack claim. Sent 25 days before NameSilo's "compromise" narrative.</div>
  </div>
  <div class="ev-card">
    <img src="evidence/01-phishdestroy-reply-feb16.png" alt="PhishDestroy technical reply Feb 16" loading="lazy">
    <div class="ev-cap"><strong>Feb 16, 2026</strong> — PhishDestroy reply: 8 PHP endpoints documented, escalation notice issued.</div>
  </div>
  <div class="ev-card">
    <img src="evidence/06-x-support-no-violation.png" alt="X Support email Apr 15 2026 — no violation, restored" loading="lazy">
    <div class="ev-cap"><strong>Apr 15, 2026</strong> — X Support: "No violation. Restored to full functionality." Account still locked.</div>
  </div>
  <div class="ev-card">
    <img src="evidence/04-tweet-honest-question.png" alt="Tweet: who is this operator to you?" loading="lazy">
    <div class="ev-cap"><strong>Mar 16, 2026</strong> — "Who is this operator to you?" 7,900 views. Never answered. Account locked shortly after.</div>
  </div>
  <div class="ev-card">
    <img src="evidence/12-ghostarchive-namesilo-tweet-top.png" alt="GhostArchive — original confrontation tweet" loading="lazy">
    <div class="ev-cap"><strong>GhostArchive</strong> — archived before suppression. NameSilo's full reply thread, permanent record.</div>
  </div>
  <div class="ev-card">
    <img src="evidence/04-tweet-press-secretary.png" alt="Tweet: NameSilo acting as press secretary for Monero theft operation" loading="lazy">
    <div class="ev-cap"><strong>Mar 16, 2026</strong> — "NameSilo is acting as press secretary for a Monero theft operation." Tweets now invisible.</div>
  </div>
</div>

<!-- TIMELINE -->
<div class="st reveal" style="margin-top:36px">
  <h2>Timeline</h2>
  <div class="ln"></div>
</div>

<div class="panel reveal" style="margin-top:16px">
''' + ''.join([
    '<div class="tl-row"><span class="tl-date">%s</span><div class="tl-text">%s</div></div>' % (d, t)
    for d, t in [
        ('2016', 'xmrwallet.com goes live. <code>session_key</code> silently exfiltrates private view key on every login.'),
        ('2023–2026', 'PhishDestroy: 20+ delivery-receipted abuse reports → <code>abuse@namesilo.com</code>. <strong>Zero action.</strong>'),
        ('Feb 16, 2026', 'Operator emails PhishDestroy: "There is no phishing." No hack claim. Site defended as own work.'),
        ('Mar 12, 2026', 'PhishDestroy public tweet: "9 reports is no joke anymore."'),
        ('Mar 13, 2026', '<strong>NameSilo official tweet</strong> (11,300 views): four false claims, offer to scrub VirusTotal. PDR, WebNic, NICENIC: suspended same domain within days.'),
        ('Mar 16, 2026', 'PhishDestroy publishes operator emails. @Phish_Destroy account locked via X Gold Checkmark support.'),
        ('Mar 18, 2026', 'Full case submitted to <strong>ICANN Contractual Compliance</strong>.'),
        ('Apr 15, 2026', 'X automation: "no violation, restored to full functionality." <strong>Lock not lifted.</strong>'),
        ('May 11, 2026', 'NameSilo legal threat tweet. Zero factual rebuttal. <a href="https://github.com/phishdestroy/namesilo-evidence/blob/main/case/NAMESILO-RESPONSE-MAY2026.md" style="color:var(--cy)">Documented →</a>'),
        ('May 2026', 'DMCA filed against this investigation. Keyword/geo suppression detected. xmrwallet domain transferred to Namecheap.'),
        ('Jun 2026', 'Zone scan complete: 5,269,357 domains, 87.3% dead/parked. Site remains live. Investigation continues.'),
    ]
]) + '''
</div>

<!-- FOR VICTIMS / REGULATORS -->
<div class="g2 reveal" style="margin-top:36px;gap:16px">
  <div class="panel">
    <h3 style="font-size:13px;text-transform:uppercase;letter-spacing:.06em;opacity:.5;font-weight:700;margin:0 0 12px">For Victims of xmrwallet[.]com</h3>
    <p style="font-size:13px;opacity:.8;line-height:1.6;margin:0 0 12px">This evidence package is ready to attach to any legal or regulatory filing. MIT licensed — no further authorization needed.</p>
    <ul style="font-size:13px;opacity:.8;line-height:2;padding-left:16px;margin:0 0 12px">
      <li><a href="https://www.ic3.gov" target="_blank" rel="noopener" style="color:var(--cy)">IC3.gov (FBI)</a></li>
      <li><a href="https://reportfraud.ftc.gov" target="_blank" rel="noopener" style="color:var(--cy)">FTC — reportfraud.ftc.gov</a></li>
      <li><a href="https://www.icann.org/compliance" target="_blank" rel="noopener" style="color:var(--cy)">ICANN Contractual Compliance</a></li>
    </ul>
    <a href="mailto:report@phishdestroy.io" style="display:inline-block;background:rgba(218,54,51,.15);border:1px solid rgba(218,54,51,.3);color:#f88;padding:8px 16px;border-radius:4px;font-size:13px;text-decoration:none;font-family:'JetBrains Mono',monospace">report@phishdestroy.io</a>
  </div>
  <div class="panel">
    <h3 style="font-size:13px;text-transform:uppercase;letter-spacing:.06em;opacity:.5;font-weight:700;margin:0 0 12px">For Regulators &amp; Press</h3>
    <p style="font-size:13px;opacity:.8;line-height:1.6;margin:0 0 12px">Full case submitted to ICANN March 18, 2026. Raw materials available on request: email headers, PHP endpoint captures, abuse report receipts.</p>
    <p style="font-size:13px;opacity:.8;line-height:1.6;margin:0 0 12px">Evidence manifest with SHA-256 hashes: <a href="evidence/evidence_manifest.json" style="color:var(--cy)">evidence_manifest.json</a></p>
    <a href="mailto:abuse@phishdestroy.io" style="display:inline-block;background:rgba(110,168,215,.1);border:1px solid rgba(110,168,215,.25);color:var(--cy);padding:8px 16px;border-radius:4px;font-size:13px;text-decoration:none;font-family:'JetBrains Mono',monospace">abuse@phishdestroy.io</a>
  </div>
</div>

<!-- MIRRORS -->
<div class="st reveal" style="margin-top:36px">
  <h2>Mirrors</h2>
  <div class="ln"></div>
  <p style="font-size:12px;opacity:.5;margin:4px 0 0">This investigation is distributed across multiple platforms and protocols. No single point of failure.</p>
</div>

<div class="mirror-grid reveal">
  <div class="mirror-card" style="border-color:rgba(218,54,51,.3)">
    <div class="mirror-label">&#9679; Live site</div>
    <a href="https://phishdestroy.eth.limo" target="_blank" rel="noopener">phishdestroy.eth.limo</a>
    <div style="font-size:10px;opacity:.4;margin-top:3px">IPFS via ENS · censorship-resistant</div>
  </div>
  <div class="mirror-card">
    <div class="mirror-label">GitHub Pages</div>
    <a href="https://phishdestroy.github.io/namesilo-evidence/" target="_blank" rel="noopener">phishdestroy.github.io/namesilo-evidence</a>
  </div>
  <div class="mirror-card">
    <div class="mirror-label">Arweave (blockchain)</div>
    <a href="https://arweave.net/LUuditolJS-Y15IezfpzRI36sxhd1CIvFNOf_eAG2AU" target="_blank" rel="noopener">arweave.net/LUuditolJS&hellip;</a>
    <div style="font-size:10px;opacity:.4;margin-top:3px">Permanent · on-chain</div>
  </div>
  <div class="mirror-card">
    <div class="mirror-label">GitHub Repository</div>
    <a href="https://github.com/phishdestroy/namesilo-evidence" target="_blank" rel="noopener">github.com/phishdestroy/namesilo-evidence</a>
  </div>
  <div class="mirror-card">
    <div class="mirror-label">Codeberg</div>
    <a href="https://codeberg.org/phishdestroy/namesilo-evidence" target="_blank" rel="noopener">codeberg.org/phishdestroy</a>
  </div>
  <div class="mirror-card">
    <div class="mirror-label">GhostArchive</div>
    <a href="https://ghostarchive.org/archive/CXXZ0" target="_blank" rel="noopener">ghostarchive.org/archive/CXXZ0</a>
    <div style="font-size:10px;opacity:.4;margin-top:3px">NameSilo's Mar 13 tweet · permanent</div>
  </div>
  <div class="mirror-card">
    <div class="mirror-label">Medium</div>
    <a href="https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e" target="_blank" rel="noopener">phishdestroy.medium.com</a>
  </div>
  <div class="mirror-card">
    <div class="mirror-label">IPFS CID</div>
    <a href="https://dweb.link/ipfs/bafybeibihjlg4wdmiur2k57c6be4fkttju5kekqsyuq7kl4a3uoeg65xlq/" target="_blank" rel="noopener" style="font-size:10px">bafybei&hellip;65xlq</a>
  </div>
</div>

<div style="text-align:center;padding:32px 0 16px;font-size:12px;opacity:.4;font-family:'JetBrains Mono',monospace">
  PhishDestroy Research &nbsp;·&nbsp; <a href="https://phishdestroy.eth.limo" target="_blank" rel="noopener" style="color:var(--cy)">phishdestroy.eth.limo</a> &nbsp;·&nbsp; TLP:CLEAR &nbsp;·&nbsp; MIT License
</div>

</main>

<script>
var _ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");_ro.unobserve(e.target);}});},{threshold:0.05,rootMargin:"0px 0px -20px 0px"});
document.querySelectorAll(".reveal").forEach(function(el){_ro.observe(el);});
</script>
</body>
</html>'''

with open(BASE + 'index.html', 'wb') as f:
    f.write(page.encode('utf-8'))
print('Done:', os.path.getsize(BASE + 'index.html'), 'bytes')
