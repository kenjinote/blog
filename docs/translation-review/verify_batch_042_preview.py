"""Validate the production Hugo render of the local AI image setup article bundle."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime, timezone, timedelta
import json, os, re

ROOT=Path(__file__).resolve().parents[2]
DEST=Path(os.environ.get('TEMP', '/tmp'))/'kenji-batch-042-preview'
if not DEST.exists(): raise SystemExit(f"Hugo output missing: {DEST}")
LANGS=('ja','en','zh-cn','zh-tw','es','ko','pt','fr','de','hi','id','ar','ru')
BUNDLE=ROOT/'content/post/AI画像生成ツールのローカル環境構築マニュアル'
SLUG='local-ai-image-generation-setup'
class Page(HTMLParser):
 def __init__(self): super().__init__(); self.lang=''; self.direction=''; self.canonical=[]; self.hreflang={}; self.links=[]; self.text=[]; self.title=[]; self.in_title=False
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

def fm_title(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md')
 m=re.search(r"^title:\s*['\"]?(.*?)['\"]?\s*$",f.read_text(encoding='utf8'),re.M)
 if not m: raise ValueError(f'missing title {f}')
 return unescape(m.group(1).replace("''", "'"))
pages=[]
for lang in LANGS:
 relative=Path('p') if lang=='ja' else Path(lang)/'p'
 f=DEST/relative/SLUG/'index.html'
 if f.is_file():
  p=Page(); p.feed(f.read_text(encoding='utf8',errors='replace')); pages.append((f,p))
results=[]
expected_urls=set()
for lang in LANGS:
 candidates=[(f,p) for f,p in pages if p.lang==lang]
 if len(candidates)!=1:
  results.append({'language':lang,'found':len(candidates),'passed':False}); continue
 f,p=candidates[0]; url=p.canonical[0] if p.canonical else ''
 expected_urls.add(url)
 text=unescape(' '.join(p.text)); body=f.read_text(encoding='utf8',errors='replace')
 refs=('docs.comfy.org/installation/comfyui_portable_windows','github.com/AUTOMATIC1111/stable-diffusion-webui','github.com/lllyasviel/Fooocus','docs.comfy.org/registry/claim-my-node')
 checks={'canonicalSingle':len(p.canonical)==1,'hreflangSet':len(p.hreflang)==14,'language':p.lang==lang,'arabicRtl':lang!='ar' or p.direction=='rtl','title':fm_title(lang) in ''.join(p.title),'lastmod': '2026-11-23' in body,'correctionNote':'ComfyUI' in text and 'Fooocus' in text and 'safetensors' in text,'officialLinks':all(any(u in link for link in p.links) for u in refs),'articleContent':'Stable Diffusion' in text and 'ControlNet' in text}
 results.append({'language':lang,'url':url,'checks':checks,'passed':all(checks.values())})
urls={r.get('url') for r in results if r.get('url')}
expected_hrefs=urls
for f,p in pages:
 if p.lang in LANGS:
  row=next((r for r in results if r.get('language')==p.lang),None)
  if row and row.get('checks'):
   row['checks']['hreflangTargets']=set(p.hreflang.values())==expected_hrefs
   row['passed']=all(row['checks'].values())
passed=len(results)==13 and len(urls)==13 and all(r['passed'] for r in results)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'passed':passed,'build':'hugo --environment production --minify --destination %TEMP%/kenji-batch-042-preview','article':'AI画像生成ツールのローカル環境構築マニュアル','pages':results,'limitations':['Local production render only; no browser/device visual review.','No GPU installation or performance testing.','AI translation review only; no human/native-speaker certification.']}
(ROOT/'docs/translation-review/batch-042-preview-validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'passed':passed,'pages':len(results),'failures':[r for r in results if not r['passed']]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)
