#!/usr/bin/env python3
"""Read the existing source pipeline, then apply the template without double-wrapping."""
from pathlib import Path
import concurrent.futures,json,os,subprocess,sys,urllib.request,shutil
T=Path(__file__).resolve().parents[1]
ROOT=T.parent
config=json.loads((ROOT/'site.config.json').read_text())
source_repo=config['source_repository'];branch=config['source_branch']
local_mode=os.environ.get('GITHUB_REPOSITORY','').lower()==source_repo.lower() or '--local' in sys.argv
def retain(path,data):
 if path.endswith('.html') and b'pd-workspace' in data:return False
 if path.startswith('assets/') and path.split('/')[-1] in ['theme.css','app.js','data-bridge.js','source-config.js','search-index.json','pd-mark.svg']:return False
 dest=T/'upstream/docs'/path;dest.parent.mkdir(parents=True,exist_ok=True)
 tmp=dest.with_suffix(dest.suffix+'.pending');tmp.write_bytes(data);tmp.replace(dest)
 return True
if local_mode:
 count=0
 for p in (ROOT/'docs').rglob('*'):
  if p.is_file():count+=bool(retain(str(p.relative_to(ROOT/'docs')),p.read_bytes()))
 print('Read',count,'files from the current repository. Original HTML templates retained.')
else:
 headers={'Accept':'application/vnd.github+json','User-Agent':'PhishDestroy-Template'}
 if os.environ.get('GH_TOKEN'):headers['Authorization']='Bearer '+os.environ['GH_TOKEN']
 req=urllib.request.Request('https://api.github.com/repos/'+source_repo+'/git/trees/'+branch+'?recursive=1',headers=headers)
 with urllib.request.urlopen(req,timeout=30) as response:tree=json.load(response)['tree']
 items=[x['path'] for x in tree if x['type']=='blob' and x['path'].startswith('docs/') and '/.~' not in x['path']]
 def fetch(path):
  with urllib.request.urlopen('https://raw.githubusercontent.com/'+source_repo+'/'+branch+'/'+path,timeout=60) as response:data=response.read()
  return retain(path[5:],data)
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:count=sum(pool.map(fetch,items))
 print('Refreshed',count,'source files.')
subprocess.run([sys.executable,str(T/'scripts/build.py')],cwd=ROOT,check=True)
