"""Verify the calm-jazz playlist pages after a successful GitHub Pages deploy."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime, timezone, timedelta
from urllib.parse import quote
import argparse, json, re, urllib.request, urllib.error
ROOT=Path(__file__).resolve().parents[2]; DOCS=ROOT/'docs/translation-review'; BUNDLE=ROOT/'content/post/落ち着いたジャズ'
LANGS=['ja','en','zh-cn','es','ko','pt','zh-tw','hi','fr','de','ar','ru','id']
class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.lang=''; self.direction=''; self.canonical=[]; self.hreflang={}; self.links=[]; self.text=[]; self.title=[]; self.descriptions=[]; self.in_title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html': self.lang=a.get('lang',''); self.direction=a.get('dir','')
  if tag=='link' and 'canonical' in a.get('rel','').split(): self.canonical.append(a.get('href',''))
  if tag=='link' and a.get('hreflang'): self.hreflang[a['hreflang']]=a.get('href','')
  if tag=='a' and a.get('href'): self.links.append(a['href'])
  if tag=='meta' and a.get('name','').lower()=='description': self.descriptions.append(a.get('content',''))
  if tag=='title': self.in_title=True
 def handle_endtag(self,tag):
  if tag=='title': self.in_title=False
 def handle_data(self,data):
  self.text.append(data)
  if self.in_title: self.title.append(data)
def metadata(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md'); s=f.read_text(encoding='utf8')
 title=json.loads(re.search(r'^title:\s*(.*?)\s*$',s,re.M).group(1))
 slug=json.loads(re.search(r'^slug:\s*(.*?)\s*$',s,re.M).group(1))
 description=json.loads(re.search(r'^description:\s*(.*?)\s*$',s,re.M).group(1))
 return title,slug,description
parser=argparse.ArgumentParser(); parser.add_argument('--ci-run',required=True,type=int); parser.add_argument('--commit',required=True); args=parser.parse_args()
try:
 req=urllib.request.Request(f'https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}',headers={'User-Agent':'kenji.blog-translation-review/1.0','Accept':'application/vnd.github+json'})
 with urllib.request.urlopen(req,timeout=30) as r: run=json.load(r)
 if run.get('conclusion')!='success' or not run.get('head_sha','').startswith(args.commit): raise SystemExit('CI run is not successful for the specified commit')
except urllib.error.HTTPError as error:
 if error.code!=403: raise
 req=urllib.request.Request(f'https://github.com/kenjinote/blog/actions/runs/{args.ci_run}?review_check=1',headers={'User-Agent':'Mozilla/5.0 kenji.blog-translation-review/1.0'})
 with urllib.request.urlopen(req,timeout=30) as r: ci_page=r.read().decode('utf8','replace')
 if '<span class="h4 color-fg-default">Success</span>' not in ci_page or args.commit[:7] not in ci_page: raise SystemExit('GitHub run page does not confirm success for the specified commit')
_,ja_slug,_=metadata('ja'); ja_url='https://kenji.blog/p/'+quote(ja_slug,safe='')+'/'
req=urllib.request.Request(ja_url,headers={'User-Agent':'kenji.blog-translation-review/1.0'})
with urllib.request.urlopen(req,timeout=30) as r:
 raw=r.read().decode('utf8','replace'); root=Page(); root.feed(raw); expected=set(root.hreflang.values())
if len(expected)!=13 or len(root.hreflang)!=14: raise SystemExit('Japanese page does not expose the expected 13 hreflang targets')
records=[]
for lang in LANGS:
 url=next((u for u in expected if (lang=='ja' and re.search(r'https://kenji\.blog/p/',u)) or (lang!='ja' and f'/{lang}/p/' in u)),None)
 title,_,description=metadata(lang)
 if not url: raise SystemExit(f'Missing hreflang URL for {lang}')
 req=urllib.request.Request(url,headers={'User-Agent':'kenji.blog-translation-review/1.0'})
 with urllib.request.urlopen(req,timeout=30) as r:
  raw=r.read().decode('utf8','replace'); p=Page(); p.feed(raw); visible=unescape(' '.join(p.text))
  checks={'http200':r.status==200,'finalUrl':r.geturl()==url,'canonical':p.canonical==[url],'language':p.lang==lang,'arabicRtl':lang!='ar' or p.direction=='rtl','title':title in ''.join(p.title),'description':len(p.descriptions)==1 and unescape(p.descriptions[0])==description,'lastmod':'2026-11-23' in raw,'originalDate':'2022-09-08' in raw,'videoEmbed':'hOJ76cZEt08' in raw,'hreflangCount':len(p.hreflang)==14,'hreflangTargets':set(p.hreflang.values())==expected}
  records.append({'language':lang,'url':url,'status':r.status,'checks':checks,'passed':all(checks.values())})
passed=len(records)==13 and all(x['passed'] for x in records)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'ciRun':args.ci_run,'ciUrl':f'https://github.com/kenjinote/blog/actions/runs/{args.ci_run}','deployedCommit':args.commit,'allPassed':passed,'scope':'Batch 048 calm-jazz article Japanese source plus twelve translations; live HTTP validates title, canonical, language/RTL, original publication and updated dates, embedded video identity, and hreflang targets.','pages':records,'limitations':['AI review only; no human/native-speaker certification.','The full video audio, captions, and licensing were not independently reviewed.','No rendered browser/device visual QA was performed.']}
(DOCS/'publication-048.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
if passed:
 path=DOCS/'batch-048.json'; data=json.loads(path.read_text(encoding='utf8')); data['publicationPending']=False; data['publication']={'record':'docs/translation-review/publication-048.json','ciRun':args.ci_run,'deployedCommit':args.commit,'allPassed':True}; path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'allPassed':passed,'pages':len(records),'failures':[x for x in records if not x['passed']]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)
