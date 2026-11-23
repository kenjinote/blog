"""Record the AI translation review for the central limit theorem article (batch 083)."""
import hashlib, json, re
from datetime import date
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CONTENT=ROOT/'content/post/central-limit-theorem'
DOCS=ROOT/'docs/translation-review'
LEDGER=ROOT/'data/translation_reviews.json'
BATCH='docs/translation-review/batch-083.json'
LANGS=('en','zh-cn','es','ko','pt','zh-tw','hi','fr','de','ar','ru','id')
TODAY='2026-11-24'
SOURCE='post/central-limit-theorem/index.md'

def digest_text(s):return hashlib.sha256(s.replace('\r\n','\n').encode('utf-8')).hexdigest()
def norm_math(s):
    s=re.sub(r'\\text\{.*?\}',r'\\text{}',s,flags=re.S)
    return re.sub(r'\s+','',s)
def code_blocks(s):return re.findall(r'```([\w-]*)\n(.*?)\n```',s,re.S)
def check(condition,message):
    if not condition:raise SystemExit(message)

ja=(CONTENT/'index.md').read_text(encoding='utf-8-sig')
ja_math=[norm_math(x) for x in re.findall(r'\$\$(.*?)\$\$',ja,re.S)]
ja_codes=code_blocks(ja)
ja_python=next(body for lang,body in ja_codes if lang=='python')
ja_logic=re.sub(r'^\s*#.*$', '',ja_python,flags=re.M).strip()
ja_mermaid=next(body for lang,body in ja_codes if lang=='mermaid')
ja_graph=re.sub(r'".*?"','"LABEL"',ja_mermaid)
source_hash=digest_text(ja)
reviews={}
for lang in LANGS:
    rel=f'post/central-limit-theorem/index.{lang}.md'
    p=ROOT/'content'/rel;s=p.read_text(encoding='utf-8-sig')
    md=[norm_math(x) for x in re.findall(r'\$\$(.*?)\$\$',s,re.S)]
    codes=code_blocks(s)
    check(md==ja_math,f'{lang}: displayed formula differs from Japanese source')
    check(len(codes)==2 and [x[0] for x in codes]==['mermaid','python'],f'{lang}: expected Mermaid and Python examples')
    py=next(body for syntax,body in codes if syntax=='python')
    logic=re.sub(r'^\s*#.*$', '',py,flags=re.M).strip()
    check(logic==ja_logic,f'{lang}: simulation logic differs')
    mermaid=next(body for syntax,body in codes if syntax=='mermaid')
    check(re.sub(r'".*?"','"LABEL"',mermaid)==ja_graph,f'{lang}: diagram structure differs')
    for target in ('gauss','taylor-and-maclaurin-series','cauchy','law-of-large-numbers'):
        suffix=f'/p/{target}/'
        expected=(f'/{lang}{suffix}' if lang not in ('ja',) else suffix)
        check(expected in s,f'{lang}: missing localized internal link {expected}')
    check('class6-prep.pdf' in s,f'{lang}: missing MIT source')
    translated_hash=digest_text(s)
    limitations=['AI-assisted editorial review; no human or native-speaker certification.','Python simulation was not executed and rendered diagrams were not visually certified.']
    reviews[rel]={
      'reviewKind':'ai','reviewedAt':TODAY,'reviewer':'Codex (AI)','source':SOURCE,
      'sourceHash':source_hash,'translationHash':translated_hash,
      'summary':'Compared the complete localized article with the Japanese source: theorem assumptions and scope, dice example, equations, characteristic-function proof, standard error, Cauchy counterexample, translated code/diagram, and localized references. Corrected two Indonesian phrasing issues without changing mathematical meaning.' if lang=='id' else 'Compared the complete localized article with the Japanese source: theorem assumptions and scope, dice example, equations, characteristic-function proof, standard error, Cauchy counterexample, translated code/diagram, and localized references.',
      'checks':{
       'meaning':{'status':'checked','note':'Theorem scope (i.i.d., finite mean, finite positive variance), what converges, use cases, and caveats match the Japanese article.'},
       'terminology':{'status':'checked','note':'CLT, standard normal, variance, standard error, characteristic function, moment-generating function, and Levy continuity theorem are used consistently.'},
       'mathematics':{'status':'checked','note':'All four displayed equations match after excluding localized explanatory text; the standard error scales as 1/sqrt(n), and the Cauchy example is correctly excluded.'},
       'code':{'status':'checked','note':'Mermaid graph structure and executable Python simulation logic match the Japanese source; code comments and labels are localized.'},
       'links':{'status':'checked','note':'MIT 18.05 primary course PDF and four internal references use the intended language-specific routes.'}},
      'limitations':limitations}

entry={'version':1,'batch':83,'article':'central-limit-theorem','reviewedAt':TODAY,
 'sourceHash':source_hash,'sources':['https://math.mit.edu/~dav/05.dir/class6-prep.pdf'],
 'scope':'Read the complete Japanese article and all twelve translations. Compared assumptions, claims, formulas, proof outline, standard-error interpretation, counterexample, simulation code, Mermaid diagram, and localized links against the source and MIT 18.05 course material.',
 'findings':['The basic i.i.d. CLT assumptions and convergence statement are consistent across all editions.','All four displayed formula blocks match after localized prose inside the equation is removed; Python logic and Mermaid graph structure match.','Corrected two Indonesian wording issues in the proof lead-in and the fourfold-sample-size standard-error explanation.','No other meaning, terminology, mathematical, code, or reference discrepancies requiring correction were found.'],
 'publicationPending':True,'reviews':reviews}
(DOCS/'batch-083.json').write_text(json.dumps(entry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ledger=json.loads(LEDGER.read_text(encoding='utf-8'))
for rel,review in reviews.items():
    ledger['reviews'][rel]={**{k:review[k] for k in ('source','reviewedAt','reviewer','sourceHash','translationHash','reviewKind')},'evidence':BATCH,'evidenceHash':hashlib.sha256(json.dumps(review,ensure_ascii=False,sort_keys=True).encode('utf-8')).hexdigest()}
LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'batch':83,'translations':len(reviews),'sourceHash':source_hash,'corrected':['id']},ensure_ascii=False))
