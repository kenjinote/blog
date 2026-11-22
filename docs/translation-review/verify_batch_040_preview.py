from pathlib import Path
from html.parser import HTMLParser
from html import unescape
import re,json,sys,os,hashlib
from datetime import datetime,timedelta,timezone
sys.stdout.reconfigure(encoding='utf-8')
root=Path('content/post/AI(StableDiffusion)を使ってイラスト画像生成する方法'); site=Path(os.environ['TEMP'])/'kenji-batch040-preview/public'
langs=('ja','en','zh-cn','zh-tw','es','ko','pt','fr','de','hi','id','ar','ru')
class P(HTMLParser):
 def __init__(self): super().__init__(); self.lang=''; self.canonical=[]; self.href={}; self.text=[]
 def handle_data(self,data): self.text.append(data)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html': self.lang=a.get('lang','')
  if tag=='link' and 'canonical' in a.get('rel','').split(): self.canonical.append(a.get('href'))
  if tag=='link' and a.get('hreflang'): self.href[a['hreflang']]=a.get('href')
allpages=list(site.rglob('index.html')); results=[]
for lang in langs:
 fname='index.md' if lang=='ja' else f'index.{lang}.md'; text=(root/fname).read_text(encoding='utf-8-sig'); title=re.search(r"^title: ['\"]?(.*?)['\"]?$",text,re.M).group(1)
 prefix=lang if lang!='ja' else None; found=[]
 for path in allpages:
  rel=path.relative_to(site)
  if prefix and (not rel.parts or rel.parts[0]!=prefix): continue
  if prefix and (len(rel.parts)!=4 or rel.parts[1]!='p'): continue
  if not prefix and (len(rel.parts)!=3 or rel.parts[0]!='p'): continue
  body=path.read_text(encoding='utf-8');
  if unescape(title) in unescape(body): found.append((path,body))
 if len(found)!=1: results.append({'lang':lang,'foundCount':len(found),'passed':False}); continue
 path,body=found[0]; parser=P();parser.feed(body)
 plain=''.join(parser.text)
 checks={'langMatches':parser.lang==lang,'oneCanonical':len(parser.canonical)==1,'fourPrimaryRefs':all(x in body for x in ['research.google.com/colaboratory/faq.html','huggingface.co/docs/diffusers/using-diffusers/loading','huggingface.co/datasets/gsdf/EasyNegative','github.com/CompVis/stable-diffusion']),'codeUpdated':'DiffusionPipeline.from_pretrained' in plain and 'load_textual_inversion' in plain and 'diffusers==0.8.0' not in plain,'dateMetadata':'2026-11-23' in body,'hreflangGroup':len(parser.href)==14,'pathMatchesLang':(lang=='ja' and 'https://kenji.blog/p/' in parser.canonical[0]) or (lang!='ja' and f'https://kenji.blog/{lang}/p/' in parser.canonical[0])}
 results.append({'lang':lang,'path':str(path.relative_to(site)),'url':parser.canonical[0] if parser.canonical else None,'checks':checks,'passed':all(checks.values())})
passed=len(results)==13 and all(r['passed'] for r in results)
receipt={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'passed':passed,'build':'Hugo production/minified static preview of the complete 13-page article bundle','pages':results,'scope':'All 13 language pages checked for language attribute, unique canonical, localized title, four primary references, updated pipeline and embedding code, lastmod, 14 hreflang tags, and locale-specific canonical path.','limitations':['One-article bundle preview, not a full-site build.','Notebook code not executed in a live Google Colab GPU runtime.','Static HTML review only; no browser/device rendering or human/native-speaker review.']}
Path('docs/translation-review/batch-040-preview-validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'pages':len(results),'passed':passed,'failed':[r for r in results if not r['passed']]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)

