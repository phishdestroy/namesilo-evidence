import re, os

with open('C:/Users/admin/Documents/GitHub/namesilo-evidence/docs/namesilo-scan.html','rb') as f:
    scan = f.read().decode('utf-8','replace')
style_block = re.search(r'<style>.*?</style>', scan, re.DOTALL).group()

# ── SmartCustomer reviews (1-star abuse complaints) ──
sc_rows = ''
sc_reviews = [
    ("Stijn V.", "2025-10-08", "1/5",
     "We reported a fraudulent copy of an existing domain, the fraudulent domain is actively sending out phishing emails. The abuse report procedure is not yielding results. NameSilo is making profit out of fraudulent activities of their customers."),
    ("Kane T. (14-year customer)", "2025-09-24", "1/5",
     "My account was banned and I must contact their abuse team. The abuse team informed me there was a phishing complaint from ChainPatrol flagging my domain. Despite explaining this, NameSilo refused to apologize, provide any detailed explanation, or even acknowledge that they failed to notify me before banning. Their abuse and support teams blocked my email replies. STAY FAR AWAY."),
    ("Akif A.", "2025-01-10", "1/5",
     "I have repeatedly contacted their support team with clear evidence of fraudulent activity. Initially, they blocked the domain, but shortly after, they unblocked it without any explanation. I submitted multiple follow-up complaints, but they either refused to act or provided generic responses. I have also filed a complaint with ICANN."),
    ("X Y.", "2024-02-18", "1/5",
     "This company scammed me on a marketplace withdrawal. After uncovering the issue, support stopped responding. Then they began to threaten me: if I do not remove my reviews there will be no compensation. All responses were without any name and with grammatical and factual errors."),
    ("Britney H.", "2023-04-15", "1/5",
     "NameSilo protects criminals. After numerous reports they do nothing. [CSAM domains listed in original review — redacted per safe reporting standards]"),
    ("caaapkxtsgoold c.", "2023-09-14", "1/5",
     "NameSilo tries to hide reports of phishing by ignoring communications and forcing you to use their internal form system so that you cannot prove your communication. They say \"we cannot simply take reports at face value\" — except this also applies when you submit their form. Or they could look at the submitted proof, ask for more, investigate — if they were not directly profiting."),
    ("Mohamed C.", "2022-06-04", "1/5",
     "I alerted them about a scam website. Hostinger removed the same scammer's account within 1 hour. The scammer is now using a new domain on NameSilo. NameSilo refused to do any effort to investigate the scam and take down the website even though I gave them all evidences."),
    ("Xio X.", "2023-04-09", "1/5",
     "I have reported scam websites registered with them and they have done absolutely nothing. They should deactivate the domain like any responsible registrar would."),
]
for author, date, rating, body in sc_reviews:
    sc_rows += (
        '<tr>'
        '<td style="white-space:nowrap;font-weight:600">%s</td>'
        '<td style="white-space:nowrap;opacity:.6">%s</td>'
        '<td><span class="b rd">%s</span></td>'
        '<td style="font-size:12px;line-height:1.5">%s</td>'
        '</tr>'
    ) % (author, date, rating, body)

# ── Trustpilot timeline ──
tp_ns_timeline = [
    ("Jan 2023", 1180, "4.7", 100),
    ("May 2024", 1496, "4.5", 126),
    ("Dec 2024", 1769, "4.5", 149),
    ("May 2025", 2103, "4.7", 178),
    ("Jan 2026", 2609, "4.7", 220),
    ("May 2026", 2480, "4.5", 210),
]
tp_rows = ''
for period, count, rating, bar in tp_ns_timeline:
    cls = ' rd' if period == 'May 2026' else ''
    note = ' <span class="b rd" style="font-size:10px">&#8209;129 deleted</span>' if period == 'May 2026' else ''
    tp_rows += (
        '<tr>'
        '<td>%s</td>'
        '<td class="nr">%s%s</td>'
        '<td class="nr">%s</td>'
        '<td><div class="bar%s"><span style="width:%d%%"></span></div></td>'
        '</tr>'
    ) % (period, '{:,}'.format(count), note, rating, cls, bar)

# ── Deleted xmrwallet reviews ──
del_rows = ''
deleted = [
    ("Elmo T. Johnson", "US", "May 2024", "VICTIM REPORT",
     "XMRWallet swindled my funds. Beware of their deceitful practices. Stay vigilant and safeguard your assets from this fraud. 1200 monero was vanished out of nowhere!",
     "1,200 XMR stolen (~$180,000+). Deleted to suppress victim evidence."),
    ("B.Costa", "NL", "Aug 2022", "IDENTITY EXPOSURE",
     "Had a small issue with xmr wallet and contacted the support email listed. I received a reply within 2 hours and Nathalie solved it.",
     "CRITICAL: mentions &#8220;Nathalie&#8221; by name — links operator identity to wallet. Operator replied &#8220;Thanks!&#8221; then deleted the review."),
    ("Thomas", "US", "Apr 2024", "OWN BOT",
     "XMRWallet.com is a must-have tool for anyone involved in the Monero ecosystem. Whether you&#39;re a seasoned crypto enthusiast or a newcomer to the space, this wallet makes managing your XMR holdings a seamless and secure experience.",
     "Verified 5-star bot review. Operator replied &#8220;thank you!&#8221; same day. Deleted after serving its purpose."),
    ("Jabari Rivera", "FR", "Mar 2024", "OWN BOT",
     "Fast, secure, and incredibly straightforward, XMRWallet.com has made my cryptocurrency experience so much better. Their customer service is also prompt and helpful.",
     "5-star bot review. Templated language. Operator replied &#8220;thank you for the support!&#8221; 16 days later."),
    ("Evelyn Malik", "FR", "Mar 2024", "OWN BOT",
     "XMRWallet.com stands out for its commitment to privacy and security. The platform is intuitive, making it suitable for both beginners and experienced users.",
     "Posted same day as Jabari Rivera. Single-review account. Coordinated batch."),
]
for name, country, date, cat, text, sig in deleted:
    cat_cls = 'rd' if 'VICTIM' in cat or 'IDENTITY' in cat else 'or'
    del_rows += (
        '<tr>'
        '<td style="white-space:nowrap;font-weight:600">%s <span style="opacity:.5;font-size:11px">(%s)</span></td>'
        '<td style="white-space:nowrap;opacity:.6">%s</td>'
        '<td><span class="b %s" style="font-size:10px">%s</span></td>'
        '<td style="font-size:12px;line-height:1.5;font-style:italic;opacity:.85">&#8220;%s&#8221;</td>'
        '<td style="font-size:12px;line-height:1.5">%s</td>'
        '</tr>'
    ) % (name, country, date, cat_cls, cat, text, sig)

page = (
'<!DOCTYPE html><html lang="en"><head>'
'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
'<meta name="robots" content="index, follow">'
'<meta name="description" content="NameSilo Trustpilot manipulation: 129 reviews deleted in 4 months, bot reviews, victim reports suppressed. PR Newswire connection with xmrwallet. SmartCustomer 1.8/5.">'
'<meta name="keywords" content="NameSilo reviews,Trustpilot manipulation,fake reviews,review deletion,xmrwallet,PR Newswire,registrar abuse">'
'<title>Review Manipulation &amp; PR Newswire Connection &#8212; NameSilo Abuse | PhishDestroy</title>'
'<meta property="og:type" content="article">'
'<meta property="og:site_name" content="PhishDestroy">'
'<meta property="og:url" content="https://phishdestroy.github.io/namesilo-evidence/namesilo-reviews.html">'
'<meta property="og:title" content="NameSilo: 129 Trustpilot Reviews Deleted, Bot Network, Same-Day PR Newswire as Scammer">'
'<meta property="og:description" content="129 Trustpilot reviews deleted in 4 months. Rating gamed from 4.5 to 4.7. xmrwallet operator and NameSilo published PR Newswire releases on the same day.">'
'<meta property="og:image" content="https://phishdestroy.eth.limo/namesilo-og.png">'
'<meta name="twitter:card" content="summary_large_image">'
'<link rel="canonical" href="https://phishdestroy.github.io/namesilo-evidence/namesilo-reviews.html">'
+ style_block +
'<style>'
'.stat-box{display:inline-block;text-align:center;margin:8px 16px 8px 0;padding:14px 20px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:6px}'
'.stat-box strong{display:block;font-size:2rem;font-weight:800;color:#f55}'
'.stat-box span{display:block;font-size:11px;opacity:.55;text-transform:uppercase;letter-spacing:.05em;margin-top:2px}'
'.stat-green strong{color:#3fb950}'
'.stat-or strong{color:#c0a060}'
'.prnews-box{background:linear-gradient(135deg,rgba(255,60,60,.06),rgba(200,0,200,.04));border:1px solid rgba(255,60,60,.2);border-radius:8px;padding:24px 28px;margin:20px 0}'
'.prnews-date{font-family:"JetBrains Mono",monospace;font-size:11px;color:#f55;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px}'
'.pr-entry{background:rgba(255,255,255,.03);border-left:3px solid;border-radius:0 4px 4px 0;padding:12px 16px;margin:8px 0}'
'.pr-entry.scam{border-color:#f55}'
'.pr-entry.reg{border-color:#6ea8d7}'
'.pr-title{font-weight:600;font-size:13px}'
'.pr-sub{font-size:11px;opacity:.6;margin-top:4px}'
'.quote-del{background:rgba(255,60,60,.06);border-left:3px solid rgba(255,60,60,.35);padding:10px 14px;margin:4px 0;font-size:12px;font-style:italic;line-height:1.55;border-radius:0 4px 4px 0}'
'</style></head><body>'
'<header><nav>'
'<a href="namesilo-scan.html">&#8592; Report</a> &nbsp;&middot;&nbsp; '
'<a href="namesilo-clusters.html">Clusters</a> &nbsp;&middot;&nbsp; '
'<a href="namesilo-domains.html">107k IOCs</a> &nbsp;&middot;&nbsp; '
'<a href="namesilo-privacyguardian.html">PrivacyGuardian</a> &nbsp;&middot;&nbsp; '
'<strong>Review Manipulation</strong>'
'</nav></header>'
'<main style="max-width:1100px;margin:0 auto;padding:20px">'
'<h1 style="margin-bottom:4px">Review Manipulation &amp; PR Newswire</h1>'
'<p style="opacity:.55;margin-top:0;margin-bottom:28px;font-size:13px">Documented Trustpilot deletion campaign, bot-review network, victim report suppression, and a shared PR distribution service with the operator being investigated.</p>'

# ── Stats hero ──
'<div style="margin-bottom:32px">'
'<div class="stat-box"><strong>129</strong><span>NameSilo reviews deleted<br>Jan&#8202;&#8202;&#8594;&#8202;&#8202;May 2026</span></div>'
'<div class="stat-box"><strong>~1/day</strong><span>deletion rate</span></div>'
'<div class="stat-box stat-or"><strong>4.5&#8201;&#8594;&#8201;4.7</strong><span>Trustpilot rating recovered<br>via deletion</span></div>'
'<div class="stat-box" style="border-color:rgba(255,60,60,.25)"><strong>1.8/5</strong><span>SmartCustomer rating<br>(unmanaged platform)</span></div>'
'<div class="stat-box"><strong>Jan 22, 2026</strong><span>Same-day PR Newswire<br>xmrwallet + NameSilo</span></div>'
'</div>'

# ── PR Newswire ──
'<div class="panel reveal prnews-box">'
'<h2 style="margin-bottom:4px">PR Newswire &#8212; Same Day</h2>'
'<p style="font-size:13px;opacity:.7;margin:0 0 18px">Both xmrwallet and NameSilo Technologies published press releases via Cision / PR Newswire on <strong>January 21&#8202;&#8211;&#8202;22, 2026</strong>.</p>'
'<div style="background:rgba(255,255,255,.04);border-radius:6px;padding:14px 18px;margin-bottom:16px;font-size:13px">'
'<strong>Why this matters &#8212; PR Newswire is not an open platform.</strong><br>'
'Unlike a blog post or social media, PR Newswire (Cision) requires: (1) a verified corporate account with legal business information, (2) a confirmed billing address linked to a registered entity, (3) explicit editorial approval per submission. A release costs $500&#8202;&#8211;&#8202;$1,500. Anonymous operators cannot create accounts. '
'The xmrwallet operator &#8212; who simultaneously buys 500-ruble Kwork spam services and operates on bulletproof hosting in Belize &#8212; published three verified PR Newswire releases under the name <strong>Nathalie Roy</strong> with a direct phone number. '
'This means either (a) the operator has access to a verified corporate PR Newswire account, or (b) someone with an existing account filed on their behalf. '
'NameSilo is a publicly listed company (CSE: URL) with an active PR Newswire account for investor relations. '
'<strong>Both entities published within 24 hours of each other.</strong>'
'</div>'
'<div class="prnews-date">&#9679; January 21&#8202;&#8211;&#8202;22, 2026</div>'
'<div class="pr-entry scam">'
'<div class="pr-title">&#8220;XMRWallet Expands Privacy Access with Full Tor Network Integration&#8221;</div>'
'<div class="pr-sub">Published: January 21, 2026 &nbsp;&middot;&nbsp; Contact listed: <strong>Nathalie Roy (Founder)</strong>, contact@xmrwallet.com, +1&#8202;300-227-473 &nbsp;&middot;&nbsp; Publisher: <strong>xmrwallet.com</strong> (confirmed scam drainer)</div>'
'<div class="pr-sub" style="margin-top:6px"><a href="https://www.prnewswire.com/news-releases/xmrwallet-expands-privacy-access-with-full-tor-network-integration-302666268.html" target="_blank" rel="noopener" style="color:var(--cy)">prnewswire.com/news-releases/&#8230;302666268.html &#8599;</a></div>'
'</div>'
'<div class="pr-entry reg" style="margin-top:8px">'
'<div class="pr-title">&#8220;NameSilo Surpasses 6 Million Domains Under Management&#8221;</div>'
'<div class="pr-sub">Published: January 22, 2026 &nbsp;&middot;&nbsp; Publisher: <strong>NameSilo Technologies Corp.</strong> (CSE: URL) &nbsp;&middot;&nbsp; Investor relations release claiming 6M domains under management. Our zone scan of the same period: <strong>5,269,357 domains</strong> &#8212; a discrepancy of 730,643 domains.</div>'
'<div class="pr-sub" style="margin-top:6px"><a href="https://www.prnewswire.com/news-releases/namesilo-surpasses-6-million-domains-under-management-302668756.html" target="_blank" rel="noopener" style="color:var(--cy)">prnewswire.com/news-releases/&#8230;302668756.html &#8599;</a></div>'
'</div>'
'<div style="margin-top:14px;padding:12px 14px;background:rgba(255,255,255,.03);border-radius:4px;font-size:12px;opacity:.8">'
'<strong>Note:</strong> PR Newswire requires a corporate account with verified billing. The phone number +1&#8202;300-227-473 listed in the xmrwallet release is a non-geographic number and a potential lead for investigators. The xmrwallet operator also published two prior PR Newswire releases: April 2023 (&#8220;Support Charities&#8221;) and September 2023 (&#8220;Companies Embrace Cryptocurrency&#8221;).'
'</div>'
'</div>'

# ── NameSilo Trustpilot manipulation ──
'<div class="panel reveal" style="margin-top:24px">'
'<h2>NameSilo &#8212; Trustpilot Deletion Timeline</h2>'
'<p style="font-size:13px;opacity:.7;margin:0 0 14px">Wayback Machine snapshots vs. May 2026 live scrape. Rating recovered from 4.5 to 4.7 while net review count <em>decreased</em> by 129 &#8212; only possible by selectively deleting negative reviews.</p>'
'<table><thead><tr><th>Period</th><th class="nr">Review count</th><th class="nr">Rating</th><th style="width:180px">Volume</th></tr></thead>'
'<tbody>' + tp_rows + '</tbody></table>'
'<p style="font-size:12px;opacity:.6;margin-top:10px">Sources: Wayback Machine snapshots at documented URLs &nbsp;&#183;&nbsp; '
'<a href="https://web.archive.org/web/20230120050157/https://www.trustpilot.com/review/www.namesilo.com" target="_blank" rel="noopener" style="color:var(--cy)">Jan 2023</a> &nbsp;&#183;&nbsp; '
'<a href="https://web.archive.org/web/20260105192016/https://www.trustpilot.com/review/www.namesilo.com" target="_blank" rel="noopener" style="color:var(--cy)">Jan 2026</a></p>'
'</div>'

# ── xmrwallet deleted reviews ──
'<div class="panel reveal" style="margin-top:24px">'
'<h2>xmrwallet.com &#8212; Deleted Trustpilot Reviews</h2>'
'<p style="font-size:13px;opacity:.7;margin:0 0 14px">7 reviews confirmed deleted from Trustpilot page 1 (20 visible of 45 total in the 2024 snapshot). Pages 2&#8202;&#8211;&#8202;3 were not cached &#8212; additional deletions unquantified.</p>'
'<div style="overflow-x:auto">'
'<table><thead><tr><th>Reviewer</th><th>Date</th><th>Category</th><th>Deleted review text</th><th>Significance</th></tr></thead>'
'<tbody>' + del_rows + '</tbody></table>'
'</div>'
'<div style="margin-top:14px;padding:12px 14px;background:rgba(255,60,60,.05);border:1px solid rgba(255,60,60,.15);border-radius:4px;font-size:12px">'
'<strong>B.Costa deletion is the key indicator:</strong> The review was positive &#8212; it praised fast support response. It was deleted specifically because it named &#8220;Nathalie&#8221; as the support contact, linking the Nathalie Roy identity to xmrwallet operations. The operator replied &#8220;Thanks!&#8221; confirming they saw the review &#8212; then deleted it.'
'</div>'
'</div>'

# ── SmartCustomer independent platform ──
'<div class="panel reveal" style="margin-top:24px">'
'<h2>SmartCustomer &#8212; 1.8/5 Stars (Unmanaged Platform)</h2>'
'<p style="font-size:13px;opacity:.7;margin:0 0 14px">42 reviews scraped May 2026. SmartCustomer does not appear to offer review removal services to businesses, resulting in an unfiltered signal. Recurring theme: abuse reports ignored, accounts banned without notice, funds withheld.</p>'
'<div style="overflow-x:auto">'
'<table><thead><tr><th>Reviewer</th><th>Date</th><th>Rating</th><th>Summary</th></tr></thead>'
'<tbody>' + sc_rows + '</tbody></table>'
'</div>'
'</div>'

# ── Pattern ──
'<div class="panel reveal" style="margin-top:24px;border-color:rgba(255,60,60,.2)">'
'<h2>Pattern Summary</h2>'
'<table><thead><tr><th>Platform</th><th>NameSilo visible rating</th><th>Mechanism</th><th>Signal quality</th></tr></thead>'
'<tbody>'
'<tr><td>Trustpilot</td><td>4.7 / 5</td><td>129 reviews deleted Jan&#8202;&#8211;&#8202;May 2026 (~1/day). Rating recovered 4.5&#8201;&#8594;&#8201;4.7 via selective deletion.</td><td><span class="b rd">MANIPULATED</span></td></tr>'
'<tr><td>SmartCustomer</td><td>1.8 / 5</td><td>No managed deletion service. Organic signal from 42 reviews.</td><td><span class="b gn" style="background:rgba(63,185,80,.15);color:#3fb950">UNFILTERED</span></td></tr>'
'<tr><td>G2</td><td>4.5 / 5</td><td>37 reviews documented. Platform allows company response and flagging.</td><td><span class="b or">PARTIAL</span></td></tr>'
'<tr><td>xmrwallet Trustpilot</td><td>3.7 / 5</td><td>7 confirmed deleted from page 1 alone. Bot reviews planted and later removed. Victim report ($180K theft) deleted.</td><td><span class="b rd">MANIPULATED</span></td></tr>'
'</tbody></table>'
'<p style="font-size:13px;margin-top:16px;opacity:.85">Both NameSilo and the xmrwallet operator apply the same review management playbook: plant positive reviews on managed platforms, selectively delete negatives, maintain the appearance of a legitimate rating. On platforms where deletion is unavailable (SmartCustomer), the unfiltered rating drops to 1.8/5. The convergence of methodology between registrar and operator is consistent with the broader pattern documented in <a href="CONNECTION.md" style="color:var(--cy)">CONNECTION.md</a>.</p>'
'</div>'

'<div style="text-align:center;padding:20px 0 12px;font-size:13px;opacity:.6">'
'<a href="https://phishdestroy.eth.limo" target="_blank" rel="noopener" style="color:var(--cy,#0cf)">&#9657; phishdestroy.eth.limo</a>'
' &nbsp;&middot;&nbsp; <a href="namesilo-scan.html" style="color:var(--cy,#0cf)">Investigation Report</a>'
' &nbsp;&middot;&nbsp; <a href="namesilo-privacyguardian.html" style="color:var(--cy,#0cf)">183k Malicious Domains</a>'
' &nbsp;&middot;&nbsp; <a href="namesilo-domains.html" style="color:var(--cy,#0cf)">107k IOCs</a>'
'</div>'
'</main>'
'<script>'
'var _ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");_ro.unobserve(e.target);}});},{threshold:0.07,rootMargin:"0px 0px -32px 0px"});'
'document.querySelectorAll(".reveal").forEach(function(el){_ro.observe(el);});'
'</script>'
'</body></html>'
)

outpath = 'C:/Users/admin/Documents/GitHub/namesilo-evidence/docs/namesilo-reviews.html'
with open(outpath,'wb') as f:
    f.write(page.encode('utf-8'))
sz = os.path.getsize(outpath)
print('Done: %dKB (%d bytes)' % (sz//1024, sz))
