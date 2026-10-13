#!/usr/bin/env python3
"""Apply a maintainable design layer to the original PhishDestroy pages.

Run after refreshing upstream/docs. Original scripts, field identifiers and
datasets stay intact. No credentials or build-time secrets are required.
"""
from pathlib import Path
from bs4 import BeautifulSoup, Tag
import json, re, shutil, hashlib, os
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
UP = ROOT / 'upstream' / 'docs'
OUT = ROOT.parent / 'docs'
CONFIG = json.loads((ROOT.parent / 'site.config.json').read_text())
BASE = CONFIG['source_site_url'].rstrip('/') + '/'
ORIGIN = (os.environ.get('SITE_URL') or CONFIG['site_url']).rstrip('/')
PATHS = {
 'grid':'<rect x="3" y="3" width="7" height="7" rx="1.4"/><rect x="14" y="3" width="7" height="7" rx="1.4"/><rect x="3" y="14" width="7" height="7" rx="1.4"/><rect x="14" y="14" width="7" height="7" rx="1.4"/>',
 'file':'<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
 'shield':'<path d="m12 3 8 3v6c0 5-8 9-8 9s-8-4-8-9V6Z"/><path d="m8 12 3 3 5-6"/>',
 'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'activity':'<path d="M3 12h4l3-7 4 14 3-7h4"/>',
 'globe':'<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/>',
 'network':'<rect x="9" y="2" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="16" y="16" width="6" height="6" rx="1"/><path d="M12 8v4M5 16v-4h14v4"/>',
 'box':'<path d="m12 3 9 5v9l-9 5-9-5V8Z"/><path d="m3 8 9 5 9-5M12 13v9M7 5.8l9 5"/>',
 'external':'<path d="M15 3h6v6M21 3l-9 9M10 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-5"/>',
 'arrow':'<path d="M7 17 17 7M7 7h10v10"/>',
 'down':'<path d="M12 3v12m-5-5 5 5 5-5M4 16v4h16v-4"/>',
 'search':'<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',
 'chevron':'<path d="m9 5 7 7-7 7"/>',
 'menu':'<path d="M4 6h16M4 12h16M4 18h16"/>',
 'refresh':'<path d="M20 10a8 8 0 0 0-14-5L3 8m0-5v5h5M4 14a8 8 0 0 0 14 5l3-3m0 5v-5h-5"/>',
 'close':'<path d="m6 6 12 12M6 18 18 6"/>',
 'up':'<path d="m6 14 6-6 6 6"/>',
 'warning':'<path d="m12 3 10 18H2Z"/><path d="M12 9v5m0 3v.1"/>',
 'dollar':'<path d="M12 2v20m5-16H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
 'mail':'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
 'check':'<path d="m5 12 4 4L19 6"/>',
 'github':'<path d="M9 19c-4 1-4-2-6-2m12 4v-3.4a3 3 0 0 0-.8-2.3c2.8-.3 5.8-1.4 5.8-6.3a5 5 0 0 0-1.3-3.5 4.6 4.6 0 0 0-.1-3.5s-1.1-.4-3.6 1.3a12 12 0 0 0-6.5 0C6 .6 4.9 1 4.9 1a4.6 4.6 0 0 0-.1 3.5A5 5 0 0 0 3.5 8c0 4.9 3 6 5.8 6.3a3 3 0 0 0-.8 2.3V21"/>',
 'copy':'<rect x="8" y="8" width="12" height="13" rx="2"/><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"/>',
 'fingerprint':'<path d="M5 10a7 7 0 0 1 14 0M3 13v-3a9 9 0 0 1 18 0v3M8 13v-3a4 4 0 0 1 8 0v4a10 10 0 0 1-2 6M12 10v5a9 9 0 0 1-2 6M5 14a13 13 0 0 1-1 5M8 16a10 10 0 0 1-1 5M19 14a14 14 0 0 1-1 6"/>'
}
def icon(name):
 return '<svg class="pd-icon" viewBox="0 0 24 24" aria-hidden="true">'+PATHS.get(name,PATHS['file'])+'</svg>'
def fragment(markup):
 return BeautifulSoup(markup,'html.parser')
def append_markup(parent, markup):
 for el in list(fragment(markup).contents): parent.append(el)
def make(tag, **attrs):
 s=BeautifulSoup('','html.parser');return s.new_tag(tag,attrs=attrs)
def slug(text):
 return re.sub('[^a-z0-9]+','-',text.lower()).strip('-')

NAV=[('WORKSPACE',[
 ('Overview','index.html#overview','grid','overview'),
 ('Investigation reports','index.html#reports','file','reports'),
 ('Evidence library','index.html#evidence','fingerprint','evidence'),
 ('Timeline','index.html#timeline','clock','timeline')]),
 ('INTELLIGENCE',[
 ('Live analytics','index.html#analytics','activity','analytics'),
 ('IOC explorer','feed-ioc.html','globe','feed-ioc'),
 ('Domain list','namesilo-domains.html','box','namesilo-domains'),
 ('PrivacyGuardian','namesilo-privacyguardian.html','shield','namesilo-privacyguardian'),
 ('Behavioral patterns','behavioral-patterns.html','network','behavioral-patterns')]),
 ('RESOURCES',[
 ('Downloads & mirrors','index.html#resources','down','resources')])]

RELATED=[('NameSilo','namesilo-evidence','IANA #1479'),('NICENIC','nicenic-evidence','IANA #3765'),('Trustname','trustname-evidence','IANA #4318'),('ShortDot','shortdot-evidence','7 gTLD registry')]
def sidebar(page):
 links=''
 for heading,rows in NAV:
  links+='<div class="pd-nav-label">'+heading+'</div>'
  for title,href,i,key in rows:
   current=(key=='overview' and page=='index') or key==page or (key=='reports' and page in ['namesilo-scan','namesilo-clusters','namesilo-reviews'])
   extra='<span class="pd-count">6</span>' if key=='reports' else ''
   links+=f'<a class="pd-nav-link{" pd-active" if current else ""}" data-nav="{key}" href="{href}">{icon(i)}<span>{title}</span>{extra}</a>'
 own=CONFIG['source_repository'].split('/')[-1]
 links+='<div class="pd-nav-label">RELATED INVESTIGATIONS</div>'
 for name,repo,sub in RELATED:
  if repo!=own:links+=f'<a class="pd-nav-link" href="https://phishdestroy.github.io/{repo}/" title="{name} abuse investigation · {sub}">{icon("shield")}<span>{name} investigation</span></a>'
 return f'''<aside class="pd-sidebar" id="pd-sidebar" aria-label="Research navigation">
 <a class="pd-brand" href="index.html#overview" aria-label="PhishDestroy research overview"><span class="pd-brand-mark"><svg viewBox="0 0 36 42" fill="none" aria-hidden="true"><path d="m18 2 15 6v12c0 10-15 20-15 20S3 30 3 20V8Z" stroke="currentColor" stroke-width="1.7"/><path d="m11 13 7-3 7 3v7l-7 9-7-9Z" fill="currentColor"/><path d="m14 19 3 3 6-7" stroke="#162014" stroke-width="2"/></svg></span><span class="pd-wordmark">PhishDestroy<small>Research intelligence</small></span></a>
 <a href="index.html#overview" class="pd-project"><div class="pd-project-logo">N</div><div><strong>NameSilo Investigation</strong><span>Registrar · IANA #1479</span></div>{icon('chevron')}</a>
 <nav aria-label="Main navigation">{links}</nav>
 <div class="pd-sidebar-bottom"><div class="pd-integrity"><strong><span class="pd-dot"></span>Open research. Public evidence.</strong><p>Original sources, reproducible data<br>and a traceable investigation.</p></div><div class="pd-sidebar-links"><span>TLP:CLEAR</span><a href="https://github.com/phishdestroy/namesilo-evidence" target="_blank" rel="noopener">GitHub {icon('external')}</a></div></div>
 </aside><div class="pd-mobile-overlay" id="pd-overlay"></div>'''

def topbar(title):
 return f'''<header class="pd-topbar"><button type="button" class="pd-icon-btn pd-mobile-menu" id="pd-menu" aria-label="Open navigation" aria-controls="pd-sidebar" aria-expanded="false">{icon('menu')}</button><div class="pd-breadcrumb">{icon('shield')}<a href="index.html">Research</a><span>/</span><b>{title}</b></div><div class="pd-top-actions"><span class="pd-status" data-state="loading" id="pd-status"><span class="pd-dot"></span><span id="pd-status-text">Connecting to source</span></span><button type="button" class="pd-search-trigger" data-command-open aria-label="Search reports and sections">{icon('search')}<span>Search investigation...</span><kbd>⌘ K</kbd></button><button type="button" class="pd-icon-btn" data-refresh aria-label="Refresh source data" title="Refresh source data">{icon('refresh')}</button><a class="pd-icon-btn" href="https://github.com/phishdestroy/namesilo-evidence" target="_blank" rel="noopener" title="Open source repository" aria-label="Open source repository">{icon('github')}</a></div></header>'''

def dialogs():
 downloads=[('CSV','SIEM-ready indicators','Domain, severity, category and feed sources',BASE+'ioc/indicators.csv'),('TXT','All malicious domains','Plain-text blocklist · full classified set',BASE+'ioc/domains_all_malicious.txt'),('TXT','High-confidence domains','HIGH severity · ready for your security tools',BASE+'ioc/domains_high.txt'),('JSON','Full analytics snapshot','Registration, geography and infrastructure data','https://raw.githubusercontent.com/phishdestroy/namesilo-evidence/main/data/index.json'),('STIX','STIX 2.1 intelligence bundle','For MISP and OpenCTI integrations','https://raw.githubusercontent.com/phishdestroy/namesilo-evidence/main/data/ioc/stix-bundle.json'),('JSON','Evidence manifest','Source evidence and SHA-256 checksums',BASE+'evidence/evidence_manifest.json')]
 rows=''.join(f'<a class="pd-export-option" href="{url}" target="_blank" rel="noopener"><span class="pd-export-format">{fmt}</span><span><strong>{title}</strong><small>{desc}</small></span>{icon("down")}</a>' for fmt,title,desc,url in downloads)
 close=f'<button class="pd-icon-btn" type="button" data-close-dialog aria-label="Close dialog">{icon("close")}</button>'
 return f'''<dialog id="pd-command" class="pd-dialog" aria-label="Search investigation"><div class="pd-command-input">{icon('search')}<input id="pd-command-input" type="search" placeholder="Search reports, evidence, analytics..." aria-label="Search reports and sections" autocomplete="off">{close}</div><div class="pd-command-results" id="pd-command-results"></div><div class="pd-command-foot"><span>↑ ↓ to navigate · Enter to open</span><span>Esc to close</span></div></dialog>
 <dialog id="pd-downloads" class="pd-dialog" aria-labelledby="pd-download-title"><div class="pd-dialog-head"><h2 id="pd-download-title">Download intelligence</h2>{close}</div><p class="pd-export-description">Choose a format. Files come directly from the original PhishDestroy repository and retain its update schedule.</p><div class="pd-export-options">{rows}</div></dialog>
 <dialog id="pd-lightbox" class="pd-dialog pd-lightbox" aria-labelledby="pd-evidence-title"><div class="pd-dialog-head"><h2 id="pd-evidence-title">Evidence viewer</h2>{close}</div><div class="pd-lightbox-stage" id="pd-image-stage"><img id="pd-evidence-image" alt=""></div><div class="pd-lightbox-tools"><button class="pd-icon-btn" type="button" id="pd-image-prev" aria-label="Previous evidence">←</button><span id="pd-image-count"></span><button class="pd-icon-btn" type="button" id="pd-image-next" aria-label="Next evidence">→</button><button class="pd-btn" type="button" id="pd-image-zoom">Original size</button><a id="pd-image-original" target="_blank" rel="noopener">Open original ↗</a></div></dialog>
 <button class="pd-backtop" type="button" aria-label="Back to top" id="pd-backtop" hidden>{icon('up')}</button><div class="pd-toast" id="pd-toast" role="status" hidden></div>'''

def footer():
 return '''<footer class="pd-source-footer"><div>Research, findings and source material: <a href="https://phishdestroy.github.io/namesilo-evidence/" target="_blank" rel="noopener">PhishDestroy</a>. Historical report figures retain their original dates; live analytics show the source fetch date.<br><a href="https://phishdestroy.io" target="_blank" rel="noopener">phishdestroy.io</a> &nbsp; · &nbsp; <a href="https://phishdestroy.eth.limo" target="_blank" rel="noopener">phishdestroy.eth.limo</a></div><div>TLP:CLEAR &nbsp; · &nbsp; <a href="LICENSE">MIT License</a> &nbsp; · &nbsp; 2026</div></footer>'''

def prepare(s, name):
 s.body['class']=['pd-workspace'];s.body['data-page']=name
 for h in s.find_all(['h1','h2','h3']):
  if h.string:h.string=re.sub(r'^[^A-Za-z0-9]+','',str(h.string)).strip()
 for a in s.find_all('a',href=True):
  if a['href'].startswith('ioc/'):a['href']=BASE+a['href']
  href=a['href'];parsed=urlsplit(href)
  if parsed.path and not parsed.scheme and not parsed.netloc and not (UP/parsed.path).exists():
   original_files={'THE-LIES.md':'case/THE-LIES.md','PROOFS.md':'PROOFS.md','PRESSURE.md':'case/PRESSURE.md','CONNECTION.md':'case/CONNECTION.md'}
   if parsed.path in original_files:a['href']='https://github.com/phishdestroy/namesilo-evidence/blob/main/'+original_files[parsed.path]
   else:a['href']=urljoin(BASE+name+'.html',href)
   a['target']='_blank';a['data-original-reference']='true'
  if a.get('target')=='_blank':a['rel']='noopener noreferrer'
 for img in s.find_all('img'):
  if not img.get('alt'):img['alt']=''
  src=img.get('src','');parsed=urlsplit(src)
  if parsed.path and not parsed.scheme and not parsed.netloc and not (UP/parsed.path).exists():
   img['src']=urljoin(BASE+name+'.html',src);img['data-original-attachment']='true'
 for e in s.find_all(['input','select']):
  if not e.get('aria-label'):e['aria-label']=e.get('placeholder') or {'catF':'Filter by category'}.get(e.get('id'),'Filter investigation data')
 # Keep source attribution while using accurate metadata for this new workspace.
 for meta in s.select('meta[name="description"],meta[property="og:description"],meta[name="twitter:description"]'):
  meta['content']='Explore PhishDestroy’s NameSilo research: original reports, evidence, searchable domain lists, live analytics and downloadable intelligence.'
 for meta in s.select('meta[property="og:url"]'):meta['content']=ORIGIN+'/'+('' if name=='index' else name+'.html')
 for canon in s.select('link[rel="canonical"]'):canon['href']=ORIGIN+'/'+('' if name=='index' else name+'.html')
 oldicon=s.find('link',rel='icon')
 if oldicon:oldicon.decompose()
 s.head.append(s.new_tag('link',rel='icon',type='image/svg+xml',href='assets/pd-mark.svg'))
 s.head.append(s.new_tag('meta',attrs={'name':'theme-color','content':'#111416'}))
 s.head.append(s.new_tag('link',rel='stylesheet',href='assets/theme.css'))
 s.head.append(s.new_tag('script',src='assets/source-config.js'))
 data_script=s.new_tag('script',src='assets/data-bridge.js');s.head.append(data_script)
 for img in s.find_all('img'):
  src=img.get('src','')
  if '212284100-' in src:img.decompose()
 return s

def shell(s, name, title, content, original_scripts):
 s.body.clear()
 append_markup(s.body,'<a class="pd-skip" href="#pd-main">Skip to content</a>'+sidebar(name))
 sh=s.new_tag('div',attrs={'class':'pd-shell'});s.body.append(sh)
 append_markup(sh,topbar(title))
 main=s.new_tag('main',id='pd-main',attrs={'class':'pd-main','tabindex':'-1'});sh.append(main)
 append_markup(main,'<div id="pd-update-banner" class="pd-update-banner" hidden><span>A newer source dataset is available.</span><button class="pd-btn primary" type="button" data-refresh>Refresh data</button></div>')
 for c in content:main.append(c)
 append_markup(main,footer());append_markup(s.body,dialogs())
 for script in original_scripts:s.body.append(script)
 s.body.append(s.new_tag('script',src='assets/app.js',defer=''))
 return s

def build_index(s):
 scripts=[x.extract() for x in s.body.find_all('script')]
 main=s.body.find('main');hero=main.find('div',class_='hero').extract()
 group=hero.select_one('.hero-inner').find_all('div',recursive=False)[-1]
 live=group.find(id='hero-live').extract()
 group['class']=['pd-metrics'];group.attrs.pop('style',None)
 for i,c in enumerate(group.find_all('div',recursive=False)):
  c['class']=['pd-metric']
  scope=['SCAN','SCAN','FEED','ESTIMATE','REPORTS'][i]
  append_markup(c,f'<span class="pd-metric-index">0{i+1} / {scope}</span><span class="pd-metric-icon">{icon(["globe","activity","shield","dollar","mail"][i])}</span>')
 metrics=group.extract()
 badges=hero.find('div',class_='hero-badges').extract();badges['class']=['pd-case-badges']
 hero.find('h1').find('br').decompose()
 intro=s.new_tag('div',attrs={'class':'pd-intro'});intro.append(hero)
 eyebrow=fragment('<div class="pd-eyebrow"><span class="pd-dot"></span>Registrar intelligence / case 1479</div>').div
 hero.select_one('.hero-inner').insert(0,eyebrow)
 append_markup(hero.select_one('.hero-inner'),f'<div class="pd-action-row"><a class="pd-btn primary" href="#evidence">Explore the evidence {icon("arrow")}</a><button type="button" class="pd-btn" data-downloads-open>{icon("down")} Download intelligence</button></div>')
 hero.select_one('.hero-inner').append(badges)
 append_markup(intro,f'<aside class="pd-case-card"><div class="pd-case-label">{icon("shield")} Case record</div><strong>ICANN filed</strong><p>March 18, 2026</p><a href="#timeline">Follow the investigation {icon("arrow")}</a></aside>')
 views={name:s.new_tag('section',id='view-'+name,attrs={'class':'pd-route','data-view':name,'aria-label':label}) for name,label in [('overview','Overview'),('evidence','Evidence library'),('timeline','Investigation timeline'),('analytics','Live analytics'),('resources','Downloads and resources')]}
 for name,v in views.items():
  if name!='overview':v['hidden']=''
 titles={'evidence':('The evidence. In full.','Original exhibits, correspondence and the documented record from PhishDestroy.'),'timeline':('A decade. A documented record.','Follow the events, reports and responses in chronological order.'),'analytics':('Follow the data.','Registration activity, infrastructure and patterns from the original, continuously updated dataset.'),'resources':('Open evidence. Ready to use.','Download intelligence, inspect source files and access the original research mirrors.')}
 for name,(title,sub) in titles.items():
  append_markup(views[name],f'<div class="pd-route-title"><div class="pd-eyebrow">NameSilo / {name}</div><h1>{title}</h1><p>{sub}</p></div>')
 # Preserve original narrative blocks verbatim, assigning them to clearer views.
 report_nodes=[];mode='reports'
 for e in list(main.find_all(recursive=False)):
  if e.find('h2'):
   heading=e.find('h2').get_text(' ',strip=True)
   if heading=='What Happened':mode='evidence'
   elif heading=='Timeline':mode='timeline'
   elif heading=='Mirrors':mode='resources'
  if 'g2' in e.get('class',[]):mode='resources'
  if mode=='reports':report_nodes.append(e.extract())
  else:views[mode].append(e.extract())
 views['overview'].append(metrics)
 strip=s.new_tag('div',attrs={'class':'pd-live-strip'})
 append_markup(strip,'<div class="pd-live-strip-label"><span class="pd-dot"></span>LIVE DATA<br>FROM SOURCE</div>');strip.append(live);views['overview'].append(strip)
 analytic_nodes=s.body.find_all('div',class_='wrap',recursive=False)
 chart=analytic_nodes[0].extract();chart['class']=['wrap','pd-chart-panel'];chart.attrs.pop('style',None)
 grid=s.new_tag('div',attrs={'class':'pd-overview-grid'});grid.append(chart)
 append_markup(grid,f'''<aside class="pd-quick-panel"><h3>Investigation workspace</h3><p>Go straight to the source.</p><a class="pd-quick-link" href="feed-ioc.html">{icon('globe')}<span><strong>Explore live IOCs</strong><small>Search · filter · investigate</small></span><span class="pd-arrow">↗</span></a><a class="pd-quick-link" href="#evidence">{icon('fingerprint')}<span><strong>Review the evidence</strong><small>Original exhibits &amp; records</small></span><span class="pd-arrow">↗</span></a><a class="pd-quick-link" href="#analytics">{icon('activity')}<span><strong>Open live analytics</strong><small>Geography · patterns · growth</small></span><span class="pd-arrow">↗</span></a><div class="pd-quick-footer">{icon('check')} Public sources · Traceable data</div></aside>''')
 views['overview'].append(grid)
 report_section=s.new_tag('div',id='reports')
 for e in report_nodes:report_section.append(e)
 for i,card in enumerate(report_section.select('.hub-card')):
  ic=card.select_one('.hc-icon');ic.clear();append_markup(ic,icon(['file','network','globe','shield','activity','github'][i]));append_markup(card,'<span class="pd-card-arrow" aria-hidden="true">↗</span>')
 views['overview'].append(report_section)
 append_markup(views['overview'],'<p class="pd-report-caption">Historical report figures and current feed totals describe different snapshots. Each report retains its original scope and date.</p>')
 ag=s.new_tag('div',attrs={'class':'pd-analytics-grid'})
 jump=[]
 for i,e in enumerate(analytic_nodes[1:]):
  e.extract();h=e.find('h2');text=h.get_text(' ',strip=True);aid=slug(text);e['id']=aid
  cls=e.get('class',[])
  if i in [0,6,10,12,13]:cls+=['pd-wide']
  e['class']=cls
  ag.append(e)
  if i in [0,2,5,6,10,11,12,13]:jump.append(f'<a href="#{aid}">{text}</a>')
 append_markup(views['analytics'],'<nav class="pd-analytics-nav" aria-label="Analytics sections">'+''.join(jump)+'</nav>')
 views['analytics'].append(ag)
 # The author's statement is also retained, placed with the research resources.
 for e in s.body.find_all('div',recursive=False):
  if 'PhishDestroy / Statement' in e.get_text(' ',strip=True):
   e['class']=['pd-manifesto'];views['resources'].append(e.extract())
 tabs=fragment('<nav class="pd-tabs" aria-label="Investigation sections">'+''.join(f'<a href="#{r}" data-nav="{r}" class="{"pd-active" if r=="overview" else ""}">{label}</a>' for r,label in [('overview','Overview'),('evidence','Evidence library'),('analytics','Live analytics'),('timeline','Timeline'),('resources','Resources')])+'</nav>').nav
 content=[intro,tabs]+list(views.values())
 for script in scripts:
  if not script.get('src'):
   t=script.get_text()
   t=t.replace("color:'#484f58'","color:'#819097'").replace("grid:{color:'rgba(255,255,255,.04)'}","grid:{color:'rgba(255,255,255,.055)'}")
   t=t.replace('display:labels.length<60','display:true,maxTicksLimit:5,maxRotation:0')
   t=t.replace("var cols=counts.map(function(c){var t=c/mx;return'rgba('+(Math.round(110+t*108))+','+(Math.round(168-t*114))+','+(Math.round(215-t*164))+',0.75)';});","var cols=counts.map(function(c){var t=c/mx;return t>0.8?'#c6ef80':t>0.45?'#91b766':'#576e43';});")
   t=t.replace("msg.textContent='Add NETAPI_TOKEN to GitHub Secrets to activate.';","msg.textContent='Source unavailable. Refresh to try again.';")
   # Bound the source's otherwise unbounded wait loop if both data sources fail.
   t=t.replace("function waitCD(cb){if(typeof _chartData", "var waitDeadline=Date.now()+20000;function waitCD(cb){if(Date.now()>waitDeadline)return;if(typeof _chartData")
   script.string=t
 return shell(s,'index','NameSilo Investigation',content,scripts)

def build_report(s,name):
 scripts=[x.extract() for x in s.body.find_all('script')]
 report=s.new_tag('div',attrs={'class':'pd-report-content'})
 for el in list(s.body.contents):report.append(el.extract())
 for sb in report.select('.layout > .sb'):
  toc=s.new_tag('details',attrs={'class':'pd-report-toc'});append_markup(toc,'<summary>On this page — report sections</summary>');sb.insert_before(toc);toc.append(sb.extract())
 first=report.find('div',recursive=False)
 if first and 'phishdestroy.io' in first.get_text() and len(first.get_text())<170:
  first['class']=list(first.get('class',[]))+['pd-source-bar']
 title={'namesilo-domains':'IOC Domain List','namesilo-privacyguardian':'PrivacyGuardian Shield','namesilo-scan':'Zone Scan Report','namesilo-clusters':'Favicon Cluster Analysis','namesilo-reviews':'Review Manipulation','behavioral-patterns':'Behavioral Patterns','feed-ioc':'Live IOC Explorer'}.get(name,'Investigation')
 note=fragment(f'<div class="pd-snapshot-banner">{icon("file")}<span>Original PhishDestroy research · Content and report dates preserved.</span><a href="{BASE}{name}.html" target="_blank" rel="noopener">View source ↗</a></div>').div
 if name in ['namesilo-domains','namesilo-privacyguardian']:
  report.insert(0,fragment('<div class="pd-inline-state" id="pd-inline-state" role="status">Saved list loaded · checking original source for updates…</div>').div)
  for script in scripts:
   if script.string and re.search(r'const\s+DATA\s*=',script.string):
    # Expose only the existing dataset and its existing renderer to the update bridge.
    renderer='doFilter' if name=='namesilo-privacyguardian' else 'filter'
    if name=='namesilo-domains':script.string=script.string.replace("b1.textContent=(s+1)","b1.textContent=(total?s+1:0)")
    script.string=script.string+f'\nwindow.pdDataset=DATA; window.pdApplyDataset=function(){{{renderer}();}};\n'
 if name=='feed-ioc':
  append_markup(note,'')
  report.insert(0,fragment(f'<div class="pd-route-title"><div class="pd-eyebrow">Threat intelligence / live feed</div><h1>IOC explorer</h1><p>Search the original feed by domain, category, source and severity.</p><div class="pd-action-row"><button class="pd-btn primary" data-downloads-open type="button">{icon("down")} Export intelligence</button></div></div>').div)
 # Original report code is maintained unchanged, including table/pager behavior.
 return shell(s,name,title,[note,report],scripts)

def build():
 OUT.mkdir(exist_ok=True)
 (OUT/'assets').mkdir(exist_ok=True)
 source_config={'raw_docs_base':'https://raw.githubusercontent.com/'+CONFIG['source_repository']+'/'+CONFIG['source_branch']+'/docs/'}
 (OUT/'assets/source-config.js').write_text('window.PD_SOURCE_CONFIG='+json.dumps(source_config)+';\n')
 for p in UP.rglob('*'):
  if p.is_file() and p.suffix!='.html' and p.name not in ['_headers','robots.txt','sitemap.xml']:
   dst=OUT/p.relative_to(UP);dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
 shutil.copy2(ROOT/'LICENSE',OUT/'LICENSE')
 for name in ['theme.css','app.js','data-bridge.js']:
  shutil.copy2(ROOT/'design'/name,OUT/'assets'/name)
 (OUT/'assets'/'pd-mark.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 44"><rect width="40" height="44" rx="8" fill="#111416"/><path d="m20 5 13 5v10c0 9-13 18-13 18S7 29 7 20V10Z" fill="none" stroke="#c6ef80" stroke-width="2"/><path d="m13 21 5 5 9-11" fill="none" stroke="#c6ef80" stroke-width="3"/></svg>')
 search=[];preservation={}
 for path in UP.glob('*.html'):
  if path.name=='404.html':
   if path.resolve()!=(OUT/'404.html').resolve():shutil.copy2(path,OUT/'404.html')
   continue
  original=BeautifulSoup(path.read_text(),'html.parser');orig_ids={e['id'] for e in original.find_all(id=True)};orig_fields={e['id'] for e in original.find_all(['input','select']) if e.get('id')}
  s=prepare(original,path.stem);s=build_index(s) if path.stem=='index' else build_report(s,path.stem)
  used_ids={e['id'] for e in s.find_all(id=True)}
  for i,h in enumerate(s.select('.pd-main h1,.pd-main h2,.pd-main h3')):
   title=h.get_text(' ',strip=True)
   if not title or len(title)>150:continue
   if not h.get('id'):
    candidate='section-'+slug(title);base=candidate;suffix=2
    while candidate in used_ids:candidate=base+'-'+str(suffix);suffix+=1
    h['id']=candidate;used_ids.add(candidate)
   view=h.find_parent(attrs={'data-view':True})
   dest=path.name+'#'+h['id']
   if view and title in ['The evidence. In full.','A decade. A documented record.','Follow the data.','Open evidence. Ready to use.']:dest='index.html#'+view['data-view']
   search.append({'title':title,'href':dest,'group':('NameSilo investigation' if path.stem=='index' else s.title.get_text().split('|')[0][:38])})
  after_ids={e['id'] for e in s.find_all(id=True)}
  preservation[path.name]={'original_ids':len(orig_ids),'retained_ids':len(orig_ids&after_ids),'missing_ids':sorted(orig_ids-after_ids),'original_fields':sorted(orig_fields),'missing_fields':sorted(orig_fields-after_ids)}
  (OUT/path.name).write_text(str(s),encoding='utf-8')
 (OUT/'assets'/'search-index.json').write_text(json.dumps(search,ensure_ascii=False),encoding='utf-8')
 (ROOT/'preservation-report.json').write_text(json.dumps(preservation,indent=2))
 if (UP/'robots.txt').is_file():shutil.copy2(UP/'robots.txt',OUT/'robots.txt')
 else:(OUT/'robots.txt').write_text('User-agent: *\nAllow: /\n')
 (OUT/'.nojekyll').touch()
 print(json.dumps({'pages':len(preservation),'search_entries':len(search),'preserved':preservation},indent=2))

if __name__=='__main__':build()
