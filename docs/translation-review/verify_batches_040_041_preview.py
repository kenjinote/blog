from pathlib import Path
from html.parser import HTMLParser
from html import unescape
import json,re,os,sys,hashlib
from datetime import datetime,timedelta,timezone
sys.stdout.reconfigure(encoding='utf8')
ROOT=Path.cwd(); SITE=Path(os.environ['TEMP'])/'kenji-batches040-041-preview/public'
BUNDLES=[('AI(StableDiffusion)を使ってイラスト画像生成する方法','batch-040'),('AI時代のプログラマーはどう生き残るべきか','batch-041')]
LANGS=('ja','en','zh-cn','zh-tw','es','ko','pt','fr','de','hi','id','ar','ru')
class Page(HTMLParser):
 def __init__(self): super().__init__();self.lang='';self.dir='';self.canonical=[];self.hreflang={};self.text=[]
 def handle_data(self,d):self.text.append(d)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang','');self.dir=a.get('dir','')
  if tag=='link' and 'canonical' in a.get('rel','').split():self.canonical.append(a.get('href'))
  if tag=='link' and a.get('hreflang'):self.hreflang[a['hreflang']]=a.get('href')
allpages=list(SITE.rglob('index.html')); results=[]
for slug,batch in BUNDLES:
 bundle=ROOT/'content/post'/slug
 for lang in LANGS:
  name='index.md' if lang=='ja' else f'index.{lang}.md';src=(bundle/name).read_text('utf8'); title=re.search(r'^title:\s*(["\']?)(.*?)\1\s*$',src,re.M).group(2)
  candidates=[]
  # Match by the canonical article URL rather than rendered text, which also
  # appears in related-article cards on the rest of the site.
  slug_prefix='aistablediffusion' if batch=='batch-040' else 'how-programmers-survive-in-ai-era'
  for f in allpages:
   body=f.read_text('utf8',errors='replace')
   q=Page();q.feed(body)
   local_path='/' if lang=='ja' else f'/{lang}/'
   if q.lang==lang and q.canonical and slug_prefix in q.canonical[0].lower() and local_path in q.canonical[0]:candidates.append((f,body))
  if len(candidates)!=1:results.append({'batch':batch,'lang':lang,'found':len(candidates),'passed':False});continue
  path,body=candidates[0];p=Page();p.feed(body);plain=''.join(p.text)
  checks={'lang':p.lang==lang,'canonical':len(p.canonical)==1 and f'https://kenji.blog/{"" if lang=="ja" else lang+"/"}p/' in p.canonical[0],'hreflang14':len(p.hreflang)==14,'arabicRtl':lang!='ar' or p.dir=='rtl','title':unescape(title) in unescape(body),'lastmod':'2026-11-23' in body}
  if batch=='batch-040':checks.update({'currentPipeline':'DiffusionPipeline.from_pretrained' in plain and 'hf_hub_download' in plain and 'load_textual_inversion' in plain,'refs':all(u in body for u in ['research.google.com/colaboratory/faq.html','huggingface.co/docs/diffusers/using-diffusers/loading','huggingface.co/datasets/gsdf/EasyNegative','github.com/CompVis/stable-diffusion'])})
  else:checks.update({'unvalidatedFormulas':'2507.09089' in body and 'dora-2025-state-of-ai-assisted-software-development-report' in body,'noAutomationProbability':r'$P_{auto} \approx 1$' not in src,'allThreeDiagrams':src.count('```mermaid')==3,'preservedPublishDate':'2026-09-11' in body})
  results.append({'batch':batch,'lang':lang,'url':p.canonical[0] if p.canonical else None,'checks':checks,'passed':all(checks.values())})
passed=len(results)==26 and all(x['passed'] for x in results)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'passed':passed,'build':'Hugo production/minified build of both complete article bundles (26 localized pages).','pages':results,'limitations':['Two-bundle preview, not a full-site build.','No browser/device visual rendering.','The Stable Diffusion notebook was not run in a live GPU runtime.','AI review only; no human/native-speaker certification.']}
for _,batch in BUNDLES:Path(f'docs/translation-review/{batch}-preview-validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'pages':len(results),'passed':passed,'failures':[x for x in results if not x['passed']]},ensure_ascii=False,indent=2))
if not passed:raise SystemExit(1)
