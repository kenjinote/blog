"""Record AI review of all XSS/CSRF translations (batch 084)."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[2]
CONTENT=ROOT/'content/post/cross-site-scripting-xss-csrf-security'
LEDGER=ROOT/'data/translation_reviews.json'
DOCS=ROOT/'docs/translation-review'
BATCH='docs/translation-review/batch-084.json'
LANGS=('en','zh-cn','es','ko','pt','zh-tw','hi','fr','de','ar','ru','id')
TODAY='2026-11-24';SOURCE='post/cross-site-scripting-xss-csrf-security/index.md'
OFFICIAL=[
'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html',
'https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html',
'https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html',
'https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html',
'https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF',
'https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie']
def digest(s):return hashlib.sha256(s.replace('\r\n','\n').encode('utf-8')).hexdigest()
def check(ok,msg):
 if not ok:raise SystemExit(msg)
def blocks(s):return re.findall(r'^[ \t]*```([\w-]*)[ \t]*\r?\n(.*?)^[ \t]*```[ \t]*$',s,re.M|re.S)
def norm_diagram(s):return re.sub(r'(?m)^(\s*subgraph)\s+.+$',r'\1 LABEL',re.sub(r'".*?"','"LABEL"',s))
def external_links(s):return re.findall(r'\]\((https?://[^)]+)\)',s)
ja=(CONTENT/'index.md').read_text(encoding='utf-8-sig')
ja_blocks=blocks(ja);source_hash=digest(ja)
check([x[0] for x in ja_blocks]==['http','html','mermaid'],'Unexpected Japanese code examples')
ja_diagram=norm_diagram(ja_blocks[2][1])
reviews={}
for lang in LANGS:
 rel=f'post/cross-site-scripting-xss-csrf-security/index.{lang}.md';p=ROOT/'content'/rel;s=p.read_text(encoding='utf-8-sig');cs=blocks(s)
 check(len(cs)==3 and [x[0] for x in cs]==['http','html','mermaid'],f'{lang}: code block structure differs')
 check(cs[:2]==ja_blocks[:2],f'{lang}: CSP header or CSRF demonstration differs')
 check(norm_diagram(cs[2][1])==ja_diagram,f'{lang}: diagram structure differs')
 check(external_links(s)==OFFICIAL,f'{lang}: reference list differs')
 for marker in ('HttpOnly','SameSite=Strict','SameSite=Lax','SameSite=None','HMAC','attacker.invalid','bank.example'):
  check(marker in s,f'{lang}: missing {marker}')
 check(len(re.findall(r'^#{2,4}\s',s,re.M))==19,f'{lang}: section structure differs')
 sh=digest(s)
 limitations=['AI-assisted editorial review; no human or native-speaker certification.','Illustrative attack examples and policy snippets were not executed in an application.']
 reviews[rel]={'reviewKind':'ai','reviewedAt':TODAY,'reviewer':'Codex (AI)','source':SOURCE,'sourceHash':source_hash,'translationHash':sh,
  'summary':'Compared the complete localized article with Japanese and current OWASP/MDN guidance: XSS categories and impact, output encoding/CSP/HttpOnly, cookie sending conditions, CSRF tokens and signed double-submit, SameSite scope and limitations, examples, and references.',
  'checks':{
   'meaning':{'status':'checked','note':'XSS and CSRF mechanisms are distinguished; browser cookie conditions, origin/same-site scope, mitigations, and their limitations match the Japanese source.'},
   'terminology':{'status':'checked','note':'Stored, reflected, and DOM-based XSS; output encoding; CSP; HttpOnly; CSRF token; HMAC; Origin; and SameSite terminology remain distinct.'},
   'mathematics':{'status':'not_applicable','note':'No mathematical claims or calculations are present.'},
   'code':{'status':'checked','note':'The CSP header and reserved-domain CSRF form are identical to Japanese; Mermaid graph structure is preserved with localized labels.'},
   'links':{'status':'checked','note':'All six OWASP and MDN references are present and match the primary/current guidance cited in the article.'}},
  'limitations':limitations}
entry={'version':1,'batch':84,'article':'cross-site-scripting-xss-csrf-security','reviewedAt':TODAY,'sourceHash':source_hash,
 'sources':OFFICIAL,'scope':'Read the complete Japanese article and all twelve translations. Compared taxonomy, threats, output encoding/CSP/HttpOnly, CSRF assumptions and token patterns, SameSite scope and limitations, code examples, diagram, and references with official OWASP cheat sheets and MDN.',
 'findings':['All editions preserve the distinction between executing script in the same-origin browser context (XSS) and inducing cookie-authenticated cross-site requests (CSRF).','The article limits the form attack to a SameSite=None; Secure scenario without token or Origin checks and notes that browser third-party-cookie controls can block it.','The naive Double Submit equality check is identified as insufficient when cookie injection is possible; the signed, session-bound HMAC form is recommended.','CSP is explicitly an additional layer; SameSite and HttpOnly are not presented as substitutes for application-level protections.','All snippets, diagram structure, and six official references match across languages; no material translation discrepancy requiring correction was found.'],
 'publicationPending':False,'publicationStatus':'Re-review only; no source or translation content changed, so no deployment was required.','reviews':reviews}
(DOCS/'batch-084.json').write_text(json.dumps(entry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ledger=json.loads(LEDGER.read_text(encoding='utf-8'))
for rel,review in reviews.items():
  record={k:review[k] for k in ('source','reviewedAt','reviewer','sourceHash','translationHash','reviewKind')};record['evidence']=BATCH;record['evidenceHash']=hashlib.sha256(json.dumps(review,ensure_ascii=False,sort_keys=True).encode('utf-8')).hexdigest();ledger['reviews'][rel]=record
LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'batch':84,'translations':len(reviews),'sourceHash':source_hash},ensure_ascii=False))
