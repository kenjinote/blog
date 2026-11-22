"""Verify Batch 043 pages after a successful GitHub Pages deployment."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime, timezone, timedelta
import argparse, json, re, urllib.request
ROOT=Path(__file__).resolve().parents[2]; DOCS=ROOT/'docs'/'translation-review'
LANGS=('ja','en','zh-cn','zh-tw','es','ko','pt','fr','de','hi','id','ar','ru')
BUNDLE=ROOT/'content'/'post'/'AI開発におけるGPUメモリ不足の解消テクニック'
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
 if not m: raise ValueError(f'Missing title in {f}')
 return unescape(m.group(1).replace("''","'"))
parser=argparse.ArgumentParser(); parser.add_argument('--ci-run',required=True,type=int); parser.add_argument('--commit',required=True,help='Full deployed Git commit SHA'); args=parser.parse_args()
req=urllib.request.Request(f'https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}',headers={'User-Agent':'kenji.blog-translation-review/1.0','Accept':'application/vnd.github+json'})
with urllib.request.urlopen(req,timeout=30) as response: run=json.load(response)
if run.get('conclusion')!='success' or not run.get('head_sha','').startswith(args.commit): raise SystemExit('Specified CI run is not successful for the deployed commit')
preview=json.loads((DOCS/'batch-043-preview-validation.json').read_text(encoding='utf8'))
expected={page['url'] for page in preview['pages']}; results=[]
for lang in LANGS:
 url=f'https://kenji.blog/{"p/" if lang=="ja" else lang+"/p/"}ai-gpu-vram-optimization-cpu-offloading/'
 req=urllib.request.Request(url,headers={'User-Agent':'kenji.blog-translation-review/1.0'})
 with urllib.request.urlopen(req,timeout=30) as response:
  html=response.read().decode('utf8','replace'); page=Page(); page.feed(html); text=unescape(' '.join(page.text))
  checks={'http200':response.status==200,'finalUrl':response.geturl()==url,'canonical':page.canonical==[url],'language':page.lang==lang,'arabicRtl':lang!='ar' or page.direction=='rtl','title':title_for(lang) in ''.join(page.title),'fullHreflang':len(page.hreflang)==14 and set(page.hreflang.values())==expected,'lastmod':'2026-11-23' in html,'correctionNote':all(term in text for term in ('FlashAttention','PagedAttention','QLoRA')),'primarySourceLinks':all(any(ref in link for link in page.links) for ref in REFS),'updatedCode':bool(re.search(r'dtype.{0,160}&#34;auto&#34;',html)) and 'train_micro_batch_size_per_gpu' in unescape(html)}
  results.append({'language':lang,'url':url,'status':response.status,'lastModified':response.headers.get('Last-Modified'),'checks':checks,'passed':all(checks.values())})
passed=len(results)==13 and all(p['passed'] for p in results)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'ciRun':args.ci_run,'ciUrl':f'https://github.com/kenjinote/blog/actions/runs/{args.ci_run}','deployedCommit':args.commit,'allPassed':passed,'scope':'Batch 043: Japanese GPU memory article and all 12 translations. Live HTTP checks cover status, final URL, canonical, language, Arabic RTL, title, lastmod, correction note, seven primary source links, updated code examples, and all 14 hreflang entries/targets.','pages':results,'limitations':['AI review only; no human/native-speaker certification.','No GPU model-loading, training, or performance tests.','Browser/device visual review was not performed.']}
(DOCS/'publication-043.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
if passed:
 path=DOCS/'batch-043.json'; batch=json.loads(path.read_text(encoding='utf8')); batch['publicationPending']=False; batch['publication']={'record':'docs/translation-review/publication-043.json','ciRun':args.ci_run,'deployedCommit':args.commit,'allPassed':True}; batch['scope']=batch['scope'].replace('Post-deploy checks remain pending.','CI succeeded and all 13 live pages passed post-deploy checks.'); path.write_text(json.dumps(batch,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'allPassed':passed,'pages':len(results),'failures':[p for p in results if not p['passed']]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)
