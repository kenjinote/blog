"""Verify the FizzBuzz pages after a successful GitHub Pages deploy."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime, timezone, timedelta
import argparse, json, re, urllib.request, json as json_module
ROOT=Path(__file__).resolve().parents[2]
DOCS=ROOT/'docs/translation-review'
BUNDLE=ROOT/'content/post/FizzBuzz'
LANGS=['ja','en','zh-cn','es','ko','pt','zh-tw','hi','fr','de','ar','ru','id']
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
 match=re.search(r'^title:\s*(.*?)\s*$',s,re.M); value=match.group(1)
 if value.startswith("'") and value.endswith("'"): title=value[1:-1].replace("''", "'")
 elif value.startswith('"'): title=json_module.loads(value)
 else: title=value
 return title
parser=argparse.ArgumentParser(); parser.add_argument('--ci-run',required=True,type=int); parser.add_argument('--commit',required=True); args=parser.parse_args()
req=urllib.request.Request(f'https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}',headers={'User-Agent':'kenji.blog-translation-review/1.0','Accept':'application/vnd.github+json'})
with urllib.request.urlopen(req,timeout=30) as r: run=json.load(r)
if run.get('conclusion')!='success' or not run.get('head_sha','').startswith(args.commit): raise SystemExit('CI run is not successful for the specified commit')
expected={('https://kenji.blog/' if lang=='ja' else f'https://kenji.blog/{lang}/')+'p/fizzbuzz/' for lang in LANGS}; records=[]
for lang in LANGS:
 url=('https://kenji.blog/' if lang=='ja' else f'https://kenji.blog/{lang}/')+'p/fizzbuzz/'
 req=urllib.request.Request(url,headers={'User-Agent':'kenji.blog-translation-review/1.0'})
 with urllib.request.urlopen(req,timeout=30) as r:
  raw=r.read().decode('utf8','replace'); p=Page(); p.feed(raw); visible=unescape(' '.join(p.text)); title=metadata(lang)
  checks={'http200':r.status==200,'finalUrl':r.geturl()==url,'canonical':p.canonical==[url],'language':p.lang==lang,'arabicRtl':lang!='ar' or p.direction=='rtl','title':title in ''.join(p.title),'lastmod':'2026-11-23' in raw,'originalDate':'2025-04-18' in raw,'codeRendered':'FizzBuzz' in visible and 'output' in visible,'badGermanLinkAbsent':lang!='de' or not any('state-management-history-redux-context-recoil-zustand' in u for u in p.links),'portugueseConclusion':lang!='pt' or 'Conclusão' in visible,'hreflangCount':len(p.hreflang)==14,'hreflangTargets':set(p.hreflang.values())==expected}
  records.append({'language':lang,'url':url,'status':r.status,'checks':checks,'passed':all(checks.values())})
passed=len(records)==13 and all(x['passed'] for x in records)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'ciRun':args.ci_run,'ciUrl':f'https://github.com/kenjinote/blog/actions/runs/{args.ci_run}','deployedCommit':args.commit,'allPassed':passed,'scope':'Batch 047 FizzBuzz Japanese source plus twelve translations; live HTTP validates title, canonical, language/RTL, original publication and last-modified dates, rendered code, localized fixes, and hreflang targets.','pages':records,'limitations':['AI review only; no human/native-speaker certification.','Python examples were syntax-parsed but not executed.','No rendered browser/device visual QA was performed.']}
(DOCS/'publication-047.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
if passed:
 path=DOCS/'batch-047.json'; data=json.loads(path.read_text(encoding='utf8')); data['publicationPending']=False; data['publication']={'record':'docs/translation-review/publication-047.json','ciRun':args.ci_run,'deployedCommit':args.commit,'allPassed':True}; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'allPassed':passed,'pages':len(records),'failures':[x for x in records if not x['passed']]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)
