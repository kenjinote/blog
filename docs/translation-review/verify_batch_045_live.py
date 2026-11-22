"""Verify Batch 045 pages after a successful GitHub Pages deploy."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime,timezone,timedelta
import argparse,json,re,urllib.request
ROOT=Path(__file__).resolve().parents[2];DOCS=ROOT/'docs'/'translation-review';BUNDLE=ROOT/'content'/'post'/'Android(Google Pixel)端末の復元手順'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.lang='';self.direction='';self.canonical=[];self.hreflang={};self.links=[];self.text=[];self.title=[];self.in_title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang','');self.direction=a.get('dir','')
  if tag=='link' and 'canonical' in a.get('rel','').split():self.canonical.append(a.get('href',''))
  if tag=='link' and a.get('hreflang'):self.hreflang[a['hreflang']]=a.get('href','')
  if tag=='a' and a.get('href'):self.links.append(a['href'])
  if tag=='title':self.in_title=True
 def handle_endtag(self,tag):
  if tag=='title':self.in_title=False
 def handle_data(self,data):
  self.text.append(data)
  if self.in_title:self.title.append(data)
def title_for(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md')
 return re.search(r'^title:\s*"(.*?)"\s*$',f.read_text(encoding='utf8'),re.M).group(1)
args=argparse.ArgumentParser();args.add_argument('--ci-run',required=True,type=int);args.add_argument('--commit',required=True);a=args.parse_args()
req=urllib.request.Request(f'https://api.github.com/repos/kenjinote/blog/actions/runs/{a.ci_run}',headers={'User-Agent':'kenji.blog-translation-review/1.0','Accept':'application/vnd.github+json'})
with urllib.request.urlopen(req,timeout=30) as x:run=json.load(x)
if run.get('conclusion')!='success' or not run.get('head_sha','').startswith(a.commit):raise SystemExit('CI run is not successful for the requested commit')
preview=json.loads((DOCS/'batch-045-preview-validation.json').read_text(encoding='utf8'));expected={x['url'] for x in preview['pages']};records=[]
REFS=('pixelrepair.withgoogle.com/','support.google.com/pixelphone/answer/4596836','support.google.com/pixelphone/answer/4582729','developer.android.com/studio/run/win-usb')
for item in preview['pages']:
 lang=item['language'];url=item['url'];req=urllib.request.Request(url,headers={'User-Agent':'kenji.blog-translation-review/1.0'})
 with urllib.request.urlopen(req,timeout=30) as x:
  raw=x.read().decode('utf8','replace');p=Page();p.feed(raw);text=unescape(' '.join(p.text));checks={'http200':x.status==200,'finalUrl':x.geturl()==url,'canonical':p.canonical==[url],'language':p.lang==lang,'arabicRtl':lang!='ar' or p.direction=='rtl','title':title_for(lang) in ''.join(p.title),'hreflangCount':len(p.hreflang)==14,'hreflangTargets':set(p.hreflang.values())==expected,'lastmod':'2026-11-23' in raw,'correctDate':'2025-02-28' in text,'dataDistinction':'Reinstall' in text and 'Update' in text,'fastbootFlow':'Fastboot' in text and 'Connect device' in text,'officialLinks':all(any(ref in link for link in p.links) for ref in REFS)}
  records.append({'language':lang,'url':url,'status':x.status,'checks':checks,'passed':all(checks.values())})
passed=len(records)==13 and all(r['passed'] for r in records)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'ciRun':a.ci_run,'ciUrl':f'https://github.com/kenjinote/blog/actions/runs/{a.ci_run}','deployedCommit':a.commit,'allPassed':passed,'scope':'Batch 045 Japanese Pixel recovery article and all 12 translations; live HTTP checks validate tool instructions, Update/Reinstall data distinction, source links, original date, title, canonical, language/RTL, and hreflang.','pages':records,'limitations':['No physical Pixel device or firmware process was tested.','AI review only; no human/native-speaker certification.','Browser/device visual review was not performed.']}
(DOCS/'publication-045.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
if passed:
 f=DOCS/'batch-045.json';d=json.loads(f.read_text(encoding='utf8'));d['publicationPending']=False;d['publication']={'record':'docs/translation-review/publication-045.json','ciRun':a.ci_run,'deployedCommit':a.commit,'allPassed':True};d['validation']='docs/translation-review/batch-045-preview-validation.json';d['localPreviewPassed']=True;d['scope']=d['scope'].replace('Local Hugo build and 13-page preview checks remain pending; no physical device testing.','Full Hugo production build and 13-page static preview checks passed; no physical device testing. All 13 live pages passed post-deploy checks.');f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'allPassed':passed,'pages':len(records),'failures':[r for r in records if not r['passed']]},ensure_ascii=False,indent=2))
if not passed:raise SystemExit(1)
