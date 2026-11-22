"""Verify Batch 046 pages after a successful GitHub Pages deploy."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime, timezone, timedelta
import argparse, json, re, urllib.request
ROOT=Path(__file__).resolve().parents[2]
DOCS=ROOT/'docs/translation-review'
BUNDLE=ROOT/'content/post/search-algorithms-linear-binary-hash-table-principles'
class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.lang=''; self.direction=''; self.canonical=[]; self.hreflang={}; self.links=[]; self.text=[]; self.title=[]; self.in_title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html': self.lang=a.get('lang',''); self.direction=a.get('dir','')
  if tag=='link' and 'canonical' in a.get('rel','').split(): self.canonical.append(a.get('href',''))
  if tag=='link' and a.get('hreflang'): self.hreflang[a['hreflang']]=a.get('href','')
  if tag=='a' and a.get('href'): self.links.append(a['href'])
  if tag=='title': self.in_title=True
 def handle_endtag(self,tag):
  if tag=='title': self.in_title=False
 def handle_data(self,data):
  self.text.append(data)
  if self.in_title: self.title.append(data)
def metadata(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md'); s=f.read_text(encoding='utf8')
 title=re.search(r'^title:\s*"(.*?)"\s*$',s,re.M).group(1)
 slug=re.search(r'^slug:\s*["\'](.*?)["\']\s*$',s,re.M).group(1).lower().replace('(','').replace(')','').replace(' ','-')
 return title,slug
parser=argparse.ArgumentParser(); parser.add_argument('--ci-run',required=True,type=int); parser.add_argument('--commit',required=True); args=parser.parse_args()
req=urllib.request.Request(f'https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}',headers={'User-Agent':'kenji.blog-translation-review/1.0','Accept':'application/vnd.github+json'})
with urllib.request.urlopen(req,timeout=30) as r: run=json.load(r)
if run.get('conclusion')!='success' or not run.get('head_sha','').startswith(args.commit): raise SystemExit('CI run is not successful for the specified commit')
preview=json.loads((DOCS/'batch-046-preview-validation.json').read_text(encoding='utf8')); expected={x['url'] for x in preview['pages']}; records=[]
for item in preview['pages']:
 lang=item['language']; url=item['url']; title,slug=metadata(lang); req=urllib.request.Request(url,headers={'User-Agent':'kenji.blog-translation-review/1.0'})
 with urllib.request.urlopen(req,timeout=30) as r:
  raw=r.read().decode('utf8','replace'); p=Page(); p.feed(raw); text=unescape(' '.join(p.text))
  checks={'http200':r.status==200,'finalUrl':r.geturl()==url,'canonical':p.canonical==[url],'language':p.lang==lang,'arabicRtl':lang!='ar' or p.direction=='rtl','title':title in ''.join(p.title),'lastmod':'2026-11-23' in raw,'pythonComplexityLink':any('docs.python.org/3.14/builtins/time-complexity.html' in u for u in p.links),'badPointerLinkAbsent':not any('c-language-pointers-memory-management-stack-heap' in u for u in p.links),'codeRendered':'binary_search' in text and 'HashTable' in text,'hreflangCount':len(p.hreflang)==14,'hreflangTargets':set(p.hreflang.values())==expected}
  records.append({'language':lang,'url':url,'status':r.status,'checks':checks,'passed':all(checks.values())})
passed=len(records)==13 and all(x['passed'] for x in records)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'ciRun':args.ci_run,'ciUrl':f'https://github.com/kenjinote/blog/actions/runs/{args.ci_run}','deployedCommit':args.commit,'allPassed':passed,'scope':'Batch 046 search-algorithms Japanese source plus twelve translations; live HTTP validates title, canonical, language/RTL, lastmod, rendered code, the official Python reference, removal of the wrong pointer link, and hreflang targets.','pages':records,'limitations':['AI review only; no human/native-speaker certification.','Code snippets were syntax-parsed but not executed or benchmarked.','No rendered browser/device visual QA was performed.']}
(DOCS/'publication-046.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
if passed:
 path=DOCS/'batch-046.json'; data=json.loads(path.read_text(encoding='utf8')); data['publicationPending']=False; data['publication']={'record':'docs/translation-review/publication-046.json','ciRun':args.ci_run,'deployedCommit':args.commit,'allPassed':True}; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'allPassed':passed,'pages':len(records),'failures':[x for x in records if not x['passed']]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)
