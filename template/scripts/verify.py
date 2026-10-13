#!/usr/bin/env python3
"""Verify preserved content and identifiers, internal links, and embedded data."""
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlsplit, unquote
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/'docs';UP=ROOT/'upstream'/'docs'
pages={p.name:BeautifulSoup(p.read_text(),'html.parser') for p in OUT.glob('*.html')}
issues=[];fields=0;links=0;datasets={}
routes={'overview','evidence','analytics','timeline','resources'}
def words(s):
 copy=BeautifulSoup(str(s),'html.parser')
 for e in copy.find_all(['script','style']):e.decompose()
 return Counter(re.findall(r"[A-Za-zÀ-ž0-9]+(?:['’][A-Za-z]+)?",copy.get_text(' ',strip=True)))
for name,soup in pages.items():
 ids=Counter(e['id'] for e in soup.find_all(id=True))
 for key,n in ids.items():
  if n>1:issues.append(name+': duplicate ID '+key)
 if name!='404.html':
  original=BeautifulSoup((UP/name).read_text(),'html.parser')
  old_ids={e['id'] for e in original.find_all(id=True)}
  if old_ids-set(ids):issues.append(name+': missing original identifiers')
  fields+=len(original.find_all(['input','select']))
  missing=words(original)-words(soup)
  if missing:issues.append(name+': missing source words '+repr(dict(missing)))
 for e in soup.find_all(['a','link','img','script']):
  raw=e.get('href') or e.get('src') or '';url=urlsplit(raw)
  if not raw or url.scheme or url.netloc:continue
  links+=1;target=OUT/unquote(url.path) if url.path else OUT/name
  if not target.exists():issues.append(name+': missing local asset '+raw)
  if target.name in pages and url.fragment and url.fragment not in routes and not pages[target.name].find(id=unquote(url.fragment)):issues.append(name+': broken anchor '+raw)
for name in ['namesilo-domains.html','namesilo-privacyguardian.html']:
 def dataset(p):
  text=p.read_text();match=re.search(r'const\s+DATA\s*=\s*',text);data,end=json.JSONDecoder().raw_decode(text[match.end():]);return data
 old=dataset(UP/name);new=dataset(OUT/name)
 if old!=new:issues.append(name+': dataset changed')
 datasets[name]=len(new)
for p in (UP/'evidence').glob('*'):
 if p.is_file() and hashlib.sha256(p.read_bytes()).digest()!=hashlib.sha256((OUT/'evidence'/p.name).read_bytes()).digest():issues.append('Evidence bytes changed: '+p.name)
print(json.dumps({'pages':len(pages),'original_fields':fields,'local_links':links,'dataset_rows':datasets,'issues':issues},indent=2))
if issues:raise SystemExit(1)
