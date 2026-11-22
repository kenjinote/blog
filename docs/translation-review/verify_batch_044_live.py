"""Verify Batch 044 pages after a successful GitHub Pages deploy."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime,timezone,timedelta
import argparse,json,urllib.request
ROOT=Path(__file__).resolve().parents[2]; DOCS=ROOT/'docs'/'translation-review'; BUNDLE=ROOT/'content'/'post'/'AI開発の壁'
LANGS=('ja','en','zh-cn','zh-tw','es','ko','pt','fr','de','hi','id','ar','ru')
class Page(HTMLParser):
 def __init__(self): super().__init__(); self.lang=''; self.direction=''; self.canonical=[]; self.hreflang={}; self.alts=[]; self.text=[]; self.title=[]; self.in_title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html': self.lang=a.get('lang',''); self.direction=a.get('dir','')
  if tag=='link' and 'canonical' in a.get('rel','').split(): self.canonical.append(a.get('href',''))
  if tag=='link' and a.get('hreflang'): self.hreflang[a['hreflang']]=a.get('href','')
  if tag=='img': self.alts.append(a.get('alt',''))
  if tag=='title': self.in_title=True
 def handle_endtag(self,tag):
  if tag=='title': self.in_title=False
 def handle_data(self,data):
  self.text.append(data)
  if self.in_title: self.title.append(data)
def title_for(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md')
 return re.search(r'^title:\s*["\'](.*?)["\']\s*$',f.read_text(encoding='utf8'),re.M).group(1)
def alts_for(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md')
 return set(re.findall(r'!\[([^\]]+)\]\(img(?:_1)?\.webp\)',f.read_text(encoding='utf8')))
import re
parser=argparse.ArgumentParser(); parser.add_argument('--ci-run',required=True,type=int); parser.add_argument('--commit',required=True); args=parser.parse_args()
req=urllib.request.Request(f'https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}',headers={'User-Agent':'kenji.blog-translation-review/1.0','Accept':'application/vnd.github+json'})
with urllib.request.urlopen(req,timeout=30) as r: run=json.load(r)
if run.get('conclusion')!='success' or not run.get('head_sha','').startswith(args.commit): raise SystemExit('CI run is not successful for the specified commit')
preview=json.loads((DOCS/'batch-044-preview-validation.json').read_text(encoding='utf8')); expected={x['url'] for x in preview['pages']}; records=[]
for item in preview['pages']:
 lang=item['language']; url=item['url']; req=urllib.request.Request(url,headers={'User-Agent':'kenji.blog-translation-review/1.0'})
 with urllib.request.urlopen(req,timeout=30) as r:
  raw=r.read().decode('utf8','replace'); p=Page(); p.feed(raw); text=unescape(' '.join(p.text)); checks={'http200':r.status==200,'finalUrl':r.geturl()==url,'canonical':p.canonical==[url],'language':p.lang==lang,'arabicRtl':lang!='ar' or p.direction=='rtl','title':title_for(lang) in ''.join(p.title),'hreflangCount':len(p.hreflang)==14,'hreflangTargets':set(p.hreflang.values())==expected,'lastmod':'2026-11-23' in raw,'datedContext':'2025' in text,'localizedImageAlt':alts_for(lang).issubset(set(p.alts)) and all(a not in ('img.png','img_1.png') for a in p.alts)}
  records.append({'language':lang,'url':url,'status':r.status,'checks':checks,'passed':all(checks.values())})
passed=len(records)==13 and all(x['passed'] for x in records)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'ciRun':args.ci_run,'ciUrl':f'https://github.com/kenjinote/blog/actions/runs/{args.ci_run}','deployedCommit':args.commit,'allPassed':passed,'scope':'Batch 044 Japanese AI development essay and 12 translations; live HTTP validates title, canonical, lang/RTL, original-date context, localized image alt text, and hreflang entries/targets.','pages':records,'limitations':['AI review only; no human/native-speaker certification.','Browser/device visual review was not performed.']}
(DOCS/'publication-044.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
if passed:
 path=DOCS/'batch-044.json'; data=json.loads(path.read_text(encoding='utf8')); data['publicationPending']=False; data['publication']={'record':'docs/translation-review/publication-044.json','ciRun':args.ci_run,'deployedCommit':args.commit,'allPassed':True}; data['scope']=data['scope'].replace('Local build and live publication checks remain pending.','Local build passed and all 13 live pages passed post-deploy checks.'); path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'allPassed':passed,'pages':len(records),'failures':[x for x in records if not x['passed']]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)
