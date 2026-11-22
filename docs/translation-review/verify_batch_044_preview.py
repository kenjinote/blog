"""Validate the production Hugo render of the AI development wall article bundle."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime, timezone, timedelta
import json, os, re
ROOT=Path(__file__).resolve().parents[2]; DEST=Path(os.environ.get('TEMP','/tmp'))/'kenji-batch-044-preview'
if not DEST.exists(): raise SystemExit(f'Hugo output missing: {DEST}')
LANGS=('ja','en','zh-cn','zh-tw','es','ko','pt','fr','de','hi','id','ar','ru'); BUNDLE=ROOT/'content/post/AI開発の壁'
class Page(HTMLParser):
 def __init__(self): super().__init__(); self.lang=''; self.direction=''; self.canonical=[]; self.hreflang={}; self.links=[]; self.text=[]; self.title=[]; self.alts=[]; self.in_title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html': self.lang=a.get('lang',''); self.direction=a.get('dir','')
  if tag=='link' and 'canonical' in a.get('rel','').split(): self.canonical.append(a.get('href',''))
  if tag=='link' and a.get('hreflang'): self.hreflang[a['hreflang']]=a.get('href','')
  if tag=='a' and a.get('href'): self.links.append(a['href'])
  if tag=='img': self.alts.append(a.get('alt',''))
  if tag=='title': self.in_title=True
 def handle_endtag(self,tag):
  if tag=='title': self.in_title=False
 def handle_data(self,data):
  self.text.append(data)
  if self.in_title: self.title.append(data)
def metadata(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md'); s=f.read_text(encoding='utf8')
 title=re.search(r'^title:\s*["\'](.*?)["\']\s*$',s,re.M).group(1)
 slug=re.search(r'^slug:\s*["\'](.*?)["\']\s*$',s,re.M).group(1).lower()
 return title,slug
def source_alts(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md')
 return set(re.findall(r'!\[([^\]]+)\]\(img(?:_1)?\.webp\)',f.read_text(encoding='utf8')))
pages=[]; results=[]
for lang in LANGS:
 title,slug=metadata(lang); rel=Path('p') if lang=='ja' else Path(lang)/'p'; f=DEST/rel/slug/'index.html'
 if not f.is_file(): results.append({'language':lang,'found':False,'expectedPath':str(f),'passed':False}); continue
 raw=f.read_text(encoding='utf8',errors='replace'); p=Page(); p.feed(raw); text=unescape(' '.join(p.text)); pages.append((f,p))
 checks={'canonicalSingle':len(p.canonical)==1,'language':p.lang==lang,'arabicRtl':lang!='ar' or p.direction=='rtl','title':title in ''.join(p.title),'lastmod':'2026-11-23' in raw,'datedContext':'2025' in text,'localizedImageAlt':source_alts(lang).issubset(set(p.alts)) and all(a not in ('img.png','img_1.png') for a in p.alts),'hreflangCount':len(p.hreflang)==14}
 results.append({'language':lang,'url':p.canonical[0] if p.canonical else '', 'checks':checks,'passed':all(checks.values())})
urls={r.get('url') for r in results if r.get('url')}
for _,p in pages:
 row=next((r for r in results if r.get('language')==p.lang),None)
 if row and row.get('checks'):
  row['checks']['hreflangTargets']=set(p.hreflang.values())==urls; row['passed']=all(row['checks'].values())
passed=len(results)==13 and len(urls)==13 and all(r['passed'] for r in results)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'passed':passed,'build':'hugo --environment production --minify --destination %TEMP%/kenji-batch-044-preview','article':'AI開発の壁','pages':results,'limitations':['Local production render only; no browser/device visual review.','AI review only; no human/native-speaker certification.']}
(ROOT/'docs/translation-review/batch-044-preview-validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'passed':passed,'pages':len(results),'failures':[r for r in results if not r['passed']]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)
