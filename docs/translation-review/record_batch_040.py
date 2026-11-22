"""Record full AI review of the Stable Diffusion article in all translations."""
import hashlib,json,subprocess,sys,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; DOCS=ROOT/'docs/translation-review'
ARTICLE='AI(StableDiffusion)を使ってイラスト画像生成する方法'; SOURCE=f'post/{ARTICLE}/index.md'
LANGS=('en','zh-cn','es','ko','pt','zh-tw','hi','fr','de','ar','ru','id'); DATE='2026-11-23'
def digest(p): return hashlib.sha256(p.read_text(encoding='utf-8-sig').replace('\r\n','\n').encode()).hexdigest()
src_hash=digest(ROOT/'content'/SOURCE); reviews={}
for lang in LANGS:
 key=f'post/{ARTICLE}/index.{lang}.md'; p=ROOT/'content'/key
 reviews[key]={
  'reviewKind':'ai','reviewedAt':DATE,'reviewer':'Codex (AI)','source':SOURCE,'sourceHash':src_hash,'translationHash':digest(p),
  'checks':{
   'meaning':{'status':'checked','note':'Read the complete Japanese source and this complete translation. Matched the revised setup sequence, GPU availability caveat, model attribution, and usage/license limitations.'},
   'terminology':{'status':'checked','note':'Checked localized Stable Diffusion, latent diffusion, Google Colab, Diffusers, prompt, GPU, model card, license, and textual-inversion terminology.'},
   'mathematics':{'status':'not_applicable','note':'No equations, quantitative derivations, or numerical claims requiring calculation are present.'},
   'code':{'status':'checked','note':'Compared every code block with the Hugging Face model card and current Diffusers API pattern: current package install, DiffusionPipeline dtype, EasyNegative textual-inversion loading, CUDA placement, and prompt inference. Code was statically reviewed, not run in a live Colab GPU runtime.'},
   'links':{'status':'checked','note':'Added and checked primary references for Colab resource limits, Diffusers pipeline and textual-inversion APIs, the Counterfeit model card/license, EasyNegative embedding repository, and CompVis research/code.'}},
  'summary':'Full article review and translation alignment; corrected model attribution and modernized the Colab/Diffusers example with GPU availability, embedding setup, and model-license caveats.',
  'languageSpecificFindings':'Read the complete localized article. Replaced the inaccurate single-university development claim, translated current Colab access and license caveats, aligned the code/API tokens, and retained the same prompt, figures, and article intent.',
  'limitations':['AI review only; no human or native-speaker certification.','The notebook code was not executed in Google Colab or on a GPU; runtime/package compatibility may change.','Colab GPU access and model/dataset repositories can change; checked on 2026-11-23.','No legal opinion is given about model, training-data, or generated-image rights.','Full-site translation-review goal remains active.']}
batch={'version':1,'article':ARTICLE,'frozenSourceHash':src_hash,'reviewedAt':DATE,'reviews':reviews,'publicationPending':True,'scope':'Read and revised the complete Japanese article and all 12 translations; checked model attribution, current Colab GPU availability caveat, Diffusers pipeline and EasyNegative textual-inversion code, model license notes and primary references. Local static production build and publication checks pending.'}
(DOCS/'batch-040.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for key in reviews:
 cmd=[sys.executable,'scripts/translation_reviews.py','record',key,'--source',SOURCE,'--reviewer','Codex (AI)','--date',DATE,'--kind','ai','--evidence','docs/translation-review/batch-040.json']
 env=os.environ.copy(); env['PYTHONIOENCODING']='utf-8'; env['PYTHONUTF8']='1'
 r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',env=env)
 if r.returncode: raise RuntimeError(key+' '+r.stderr+r.stdout)
r=subprocess.run([sys.executable,'scripts/translation_reviews.py','check'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',env=env)
if r.returncode: raise RuntimeError(r.stderr+r.stdout)
print(json.dumps({'recorded':len(reviews),'sourceHash':src_hash,'ledgerCheck':r.stdout.strip()},ensure_ascii=False))
