"""Validate the production Hugo render of the Pixel software-repair bundle."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime,timezone,timedelta
import json,os,re
ROOT=Path(__file__).resolve().parents[2];DEST=Path(os.environ.get('TEMP','/tmp'))/'kenji-batch-045-preview'
if not DEST.exists():raise SystemExit(f'Hugo output missing: {DEST}')
LANGS=('ja','en','zh-cn','zh-tw','es','ko','pt','fr','de','hi','id','ar','ru');BUNDLE=ROOT/'content/post/Android(Google Pixel)端末の復元手順'
REFS=('pixelrepair.withgoogle.com/','support.google.com/pixelphone/answer/4596836','support.google.com/pixelphone/answer/4582729','developer.android.com/studio/run/win-usb')
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
def metadata(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md');s=f.read_text(encoding='utf8')
 title=re.search(r'^title:\s*"(.*?)"\s*$',s,re.M).group(1);slug=re.search(r'^slug:\s*["\'](.*?)["\']\s*$',s,re.M).group(1).lower().replace('(','').replace(')','').replace(' ','-')
 return f,title,slug
results=[];pages=[]
for lang in LANGS:
 src,title,slug=metadata(lang);rel=Path('p') if lang=='ja' else Path(lang)/'p';f=DEST/rel/slug/'index.html'
 if not f.is_file():results.append({'language':lang,'found':False,'path':str(f),'passed':False});continue
 raw=f.read_text(encoding='utf8',errors='replace');p=Page();p.feed(raw);text=unescape(' '.join(p.text));pages.append((lang,p))
 checks={'canonicalSingle':len(p.canonical)==1,'language':p.lang==lang,'arabicRtl':lang!='ar' or p.direction=='rtl','title':title in ''.join(p.title),'lastmod':'2026-11-23' in raw,'correctDate':'2025-02-28' in text,'dataDistinction':'Reinstall' in text and 'Update' in text,'currentFastbootFlow':'Fastboot' in text and 'Connect device' in text,'oldCarrierStepRemoved':'carrier_selection' not in raw and 'Rescue Mode' not in text,'officialLinks':all(any(ref in u for u in p.links) for ref in REFS),'hreflangCount':len(p.hreflang)==14}
 results.append({'language':lang,'url':p.canonical[0] if p.canonical else '', 'checks':checks,'passed':all(checks.values())})
urls={r.get('url') for r in results if r.get('url')}
for lang,p in pages:
 row=next(r for r in results if r['language']==lang);row['checks']['hreflangTargets']=set(p.hreflang.values())==urls;row['passed']=all(row['checks'].values())
passed=len(results)==13 and len(urls)==13 and all(r['passed'] for r in results)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'passed':passed,'build':'hugo --environment production --minify --destination %TEMP%/kenji-batch-045-preview','article':'Android(Google Pixel)端末の復元手順','pages':results,'limitations':['Local production render only; no browser/device visual review.','No physical Pixel device, firmware update, or factory reset was tested.','AI translation review only; no human/native-speaker certification.']}
(ROOT/'docs/translation-review/batch-045-preview-validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'passed':passed,'pages':len(results),'failures':[r for r in results if not r['passed']]},ensure_ascii=False,indent=2))
if not passed:raise SystemExit(1)
