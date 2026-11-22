"""Record the AI-era programmer article review and localized claim corrections."""
import hashlib,json,os,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; DOCS=ROOT/'docs/translation-review'
ARTICLE='AI時代のプログラマーはどう生き残るべきか'; SOURCE=f'post/{ARTICLE}/index.md'
LANGS=('en','zh-cn','es','ko','pt','zh-tw','hi','fr','de','ar','ru','id'); DATE='2026-11-23'
def digest(p): return hashlib.sha256(p.read_text(encoding='utf-8-sig').replace('\r\n','\n').encode()).hexdigest()
src_hash=digest(ROOT/'content'/SOURCE); reviews={}
for lang in LANGS:
 key=f'post/{ARTICLE}/index.{lang}.md'; p=ROOT/'content'/key
 reviews[key]={
  'reviewKind':'ai','reviewedAt':DATE,'reviewer':'Codex (AI)','source':SOURCE,'sourceHash':src_hash,'translationHash':digest(p),
  'checks':{
   'meaning':{'status':'checked','note':'Reviewed the Japanese argument and localized replacement passages across the full article bundle. Reframed AI capability, job-market, and productivity statements as task-dependent opinions rather than established facts; aligned all language versions on the same caveats and practical advice.'},
   'terminology':{'status':'checked','note':'Checked the localized terminology for AI assistants and coding agents, software productivity, automation, codebase context, domain knowledge, legal accountability, review, and tests.'},
   'mathematics':{'status':'checked','note':'Marked both productivity and automation equations as illustrative, unvalidated sketches; removed the unsupported formula-derived market-value and near-certain automation conclusions. No numeric derivation is claimed.'},
   'code':{'status':'checked','note':'Reviewed the three Mermaid diagrams as article illustrations; they were retained, not executed as software. Hugo static build is used to ensure the article pages render.'},
   'links':{'status':'checked','note':'Added and verified the primary Google DORA 2025 report and METR 2025 randomized-trial references. Existing article links were retained; their full destination set was not re-audited in this pass.'}},
  'summary':'Revised the full article bundle’s framing of AI developer productivity, automation, internal data, legal accountability, testing, and job-demand predictions; added bounded primary research evidence.',
  'languageSpecificFindings':'Localized the introduction, equation caveats, non-empirical conclusions, AI/human capability boundary, data access conditions, legal-responsibility caveat, testing recommendation, and employment uncertainty. Preserved the original article structure and technical illustrations.',
  'limitations':['AI review only; no human or native-speaker certification.','The unchanged prose was not independently retranslated line by line; this pass focused on the complete argument structure and the revised claims across all localized versions.','The DORA report is survey/qualitative evidence; the METR trial covers 16 experienced contributors, 246 mature-repository tasks, and early-2025 tools. Neither supports universal claims about every developer or tool.','No legal advice is provided; accountability varies by jurisdiction, contract, role, and applicable regulation.','The full-site translation-review goal remains active.']}
batch={'version':1,'article':ARTICLE,'frozenSourceHash':src_hash,'reviewedAt':DATE,'reviews':reviews,'primarySources':[{'title':'Google DORA 2025 State of AI-assisted Software Development Report','url':'https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/','checkedAt':DATE},{'title':'METR randomized trial: Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity','url':'https://arxiv.org/abs/2507.09089','checkedAt':DATE}],'publicationPending':True,'scope':'Revised the full Japanese article and localized matching passages in all 12 language versions; marked conceptual formulas as unvalidated, removed unsupported mathematical deductions and deterministic automation predictions, qualified developer-role, company-data, legal-accountability, testing, and labor-demand claims, and added current primary research references. One-bundle static preview and publication checks pending.'}
(DOCS/'batch-041.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# The translation-review CLI emits Japanese paths; force UTF-8 on Windows subprocess streams.
env=os.environ.copy();env['PYTHONIOENCODING']='utf-8';env['PYTHONUTF8']='1'
for key in reviews:
 cmd=[sys.executable,'scripts/translation_reviews.py','record',key,'--source',SOURCE,'--reviewer','Codex (AI)','--date',DATE,'--kind','ai','--evidence','docs/translation-review/batch-041.json']
 r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',env=env)
 if r.returncode: raise RuntimeError(key+' '+r.stderr+r.stdout)
r=subprocess.run([sys.executable,'scripts/translation_reviews.py','check'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',env=env)
if r.returncode: raise RuntimeError(r.stderr+r.stdout)
print(json.dumps({'recorded':len(reviews),'sourceHash':src_hash,'ledgerCheck':r.stdout.strip()},ensure_ascii=False))
