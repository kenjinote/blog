from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime, timezone, timedelta
import json, os, re
ROOT=Path(__file__).resolve().parents[2]
DEST=Path(os.environ.get('TEMP','/tmp'))/'kenji-batch-043-preview'
if not DEST.exists(): raise SystemExit(f'Hugo output missing: {DEST}')
LANGS=('ja','en','zh-cn','zh-tw','es','ko','pt','fr','de','hi','id','ar','ru')
BUNDLE=ROOT/'content/post/AI開発におけるGPUメモリ不足の解消テクニック'
SLUG='ai-gpu-vram-optimization-cpu-offloading'
REFS=('huggingface.co/docs/accelerate/main/concept_guides/big_model_inference','huggingface.co/docs/transformers/main/quantization/bitsandbytes','proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract.html','arxiv.org/abs/2309.06180','proceedings.neurips.cc/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract.html','deepspeed.ai/tutorials/zero-offload/','apple.com/mac-studio/specs/')
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
def title_for(lang):
 f=BUNDLE/('index.md' if lang=='ja' else f'index.{lang}.md')
 m=re.search(r'^title:\s*[\'\"]?(.*?)[\'\"]?\s*$',f.read_text(encoding='utf8'),re.M)
 if not m: raise ValueError(f'missing title: {f}')
 return unescape(m.group(1).replace("''","'"))
pages=[]
for lang in LANGS:
 rel=Path('p') if lang=='ja' else Path(lang)/'p'; f=DEST/rel/SLUG/'index.html'
 if f.is_file():
  p=Page(); p.feed(f.read_text(encoding='utf8',errors='replace')); pages.append((f,p))
results=[]; urls=set()
for lang in LANGS:
 found=[(f,p) for f,p in pages if p.lang==lang]
 if len(found)!=1: results.append({'language':lang,'found':len(found),'passed':False}); continue
 f,p=found[0]; url=p.canonical[0] if p.canonical else ''; urls.add(url); body=f.read_text(encoding='utf8',errors='replace'); text=unescape(' '.join(p.text))
 checks={'canonicalSingle':len(p.canonical)==1,'language':p.lang==lang,'arabicRtl':lang!='ar' or p.direction=='rtl','title':title_for(lang) in ''.join(p.title),'lastmod':'2026-11-23' in body,'currentCorrectionNote':'FlashAttention' in text and 'PagedAttention' in text and 'QLoRA' in text,'primarySourceLinks':all(any(ref in u for u in p.links) for ref in REFS),'updatedCode':bool(re.search(r'dtype.{0,160}&#34;auto&#34;',body)) and 'train_micro_batch_size_per_gpu' in unescape(body)}
 results.append({'language':lang,'url':url,'checks':checks,'passed':all(checks.values())})
expected=urls
for f,p in pages:
 row=next((r for r in results if r.get('language')==p.lang),None)
 if row and row.get('checks'):
  row['checks']['fullHreflangSet']=len(p.hreflang)==14
  row['checks']['hreflangTargets']=set(p.hreflang.values())==expected
  row['passed']=all(row['checks'].values())
passed=len(results)==13 and len(urls)==13 and all(r['passed'] for r in results)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'passed':passed,'build':'hugo --environment production --minify --destination %TEMP%/kenji-batch-043-preview','article':'AI開発におけるGPUメモリ不足の解消テクニック','pages':results,'limitations':['Local production render only; no browser/device visual review.','No GPU model-loading, training, or performance tests.','AI translation review only; no human/native-speaker certification.']}
(ROOT/'docs/translation-review/batch-043-preview-validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'passed':passed,'pages':len(results),'failures':[r for r in results if not r['passed']]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)
