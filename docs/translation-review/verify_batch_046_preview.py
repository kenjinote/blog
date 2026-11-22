"""Validate the local production render of the search-algorithms bundle."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime, timezone, timedelta
import json, os, re
ROOT=Path(__file__).resolve().parents[2]
DEST=Path(os.environ.get('TEMP','/tmp'))/'kenji-batch-046-preview'
BUNDLE=ROOT/'content/post/search-algorithms-linear-binary-hash-table-principles'
LANGS=('ja','en','zh-cn','zh-tw','es','ko','pt','fr','de','hi','id','ar','ru')
class Page(HTMLParser):
 def __init__(self): super().__init__(); self.lang=''; self.direction=''; self.canonical=[]; self.hreflang={}; self.links=[]; self.text=[]; self.title=[]; self.in_title=False; self.code=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html': self.lang=a.get('lang',''); self.direction=a.get('dir','')
  if tag=='link' and 'canonical' in a.get('rel','').split(): self.canonical.append(a.get('href',''))
  if tag=='link' and a.get('hreflang'): self.hreflang[a['hreflang']]=a.get('href','')
  if tag=='a' and a.get('href'): self.links.append(a['href'])
  if tag=='title': self.in_title=True
  if tag in ('pre','code'): self.code+=1
 def handle_endtag(self,tag):
  if tag=='title': self.in_title=False
  if tag in ('pre','code'): self.code=max(0,self.code-1)
 def handle_data(self,data):
  self.text.append(data)
  if self.in_title: self.title.append(data)
def metadata(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md'); s=f.read_text(encoding='utf8')
 title=re.search(r'^title:\s*"(.*?)"\s*$',s,re.M).group(1)
 slug=re.search(r'^slug:\s*["\'](.*?)["\']\s*$',s,re.M).group(1).lower().replace('(','').replace(')','').replace(' ','-')
 return f,title,slug
if not DEST.exists(): raise SystemExit(f'Hugo output missing: {DEST}')
results=[]; pages=[]
for lang in LANGS:
 src,title,slug=metadata(lang); rel=Path('p') if lang=='ja' else Path(lang)/'p'; f=DEST/rel/slug/'index.html'
 if not f.is_file(): results.append({'language':lang,'found':False,'path':str(f),'passed':False}); continue
 raw=f.read_text(encoding='utf8',errors='replace'); p=Page(); p.feed(raw); text=unescape(' '.join(p.text)); pages.append((lang,p))
 checks={'canonicalSingle':len(p.canonical)==1,'language':p.lang==lang,'arabicRtl':lang!='ar' or p.direction=='rtl','title':title in ''.join(p.title),'lastmod':'2026-11-23' in raw,'pythonComplexityLink':any('docs.python.org/3.14/builtins/time-complexity.html' in u for u in p.links),'oldWrongPointerLinkRemoved':not any('c-language-pointers-memory-management-stack-heap' in u for u in p.links),'codeRendered':'binary_search' in text and 'HashTable' in text,'correctedCaveat':('average' in text.lower() or 'average-case' in text.lower() or 'espera' in text.lower() or 'moyenne' in text.lower() or 'Durchschnitt' in text or '平均' in text or '평균' in text or 'औसत' in text or 'средн' in text or 'متوسط' in text or 'rata-rata' in text),'hreflangCount':len(p.hreflang)==14}
 results.append({'language':lang,'url':p.canonical[0] if p.canonical else '', 'checks':checks,'passed':all(checks.values())})
urls={r.get('url') for r in results if r.get('url')}
for lang,p in pages:
 row=next(r for r in results if r['language']==lang); row['checks']['hreflangTargets']=set(p.hreflang.values())==urls; row['passed']=all(row['checks'].values())
passed=len(results)==13 and len(urls)==13 and all(r['passed'] for r in results)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'passed':passed,'build':'hugo --environment production --minify --destination %TEMP%/kenji-batch-046-preview','article':'探索アルゴリズム（線形、二分探索とハッシュテーブルの原理）','pages':results,'limitations':['Local production render only; live deployment check pending.','Python examples were syntax-parsed but not executed or benchmarked.','AI translation review only; no human/native-speaker certification.']}
(ROOT/'docs/translation-review/batch-046-preview-validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'passed':passed,'pages':len(results),'failures':[r for r in results if not r['passed']]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)

