from pathlib import Path
import json,re,hashlib,sys
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from datetime import datetime,timezone,timedelta
root=Path(__file__).resolve().parents[2];sys.path.insert(0,str(root/'scripts'));from check_multilingual import PageParser
import argparse
ap=argparse.ArgumentParser(description='Assemble preserved execution evidence with fresh all-version HTML checks; never approves prose.')
ap.add_argument('site',type=Path);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
site=args.site;out=args.output;assert not out.exists()
digest=lambda s:hashlib.sha256(s.replace('\r\n','\n').encode()).hexdigest()
audit=json.loads((root/'docs/translation-review/batch-019-source-audit.json').read_text(encoding='utf-8'))
polish=json.loads((root/'docs/translation-review/batch-019-prose-polish.json').read_text(encoding='utf-8'))
changes={v['language']:v for v in polish['changes']}
class CodeParser(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.active=False;self.blocks=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='code' and ('language-c' in a.get('class','').split() or a.get('data-lang')=='c'):self.active=True;self.blocks.append('')
 def handle_data(self,data):
  if self.active:self.blocks[-1]+=data
 def handle_endtag(self,tag):
  if tag=='code':self.active=False
proofs={}
for suffix in ['ja-en','chinese','es-ko','pt-fr','de-id','hi-ru-ar']:
 p=root/('docs/translation-review/batch-019-'+suffix+'-validation.json');doc=json.loads(p.read_text(encoding='utf-8'))
 for v in doc['versions']:assert v['language'] not in proofs;proofs[v['language']]=(p,v)
assert set(proofs)==set(audit['versions']) and len(proofs)==13
expected={l:v['canonical'] for l,v in audit['versions'].items()};versions=[]
for lang in proofs:
 p,v=proofs[lang];current=(root/audit['versions'][lang]['path']).read_text(encoding='utf-8-sig');h=digest(current)
 c=re.findall(r'^```c\n(.*?)^```',current,re.M|re.S);assert len(c)==1
 if lang in changes:
  change=changes[lang];assert h==change['afterHash'] and v['sha256']==change['beforeHash']
  assert digest(c[0])==change['codeHash'] and change['executionCodeUnchanged']
 else:assert h==v['sha256']
 url=expected[lang];html=(site/unquote(urlsplit(url).path).lstrip('/')/'index.html').read_text(encoding='utf-8')
 parser=PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>')
 assert parser.canonical==url and parser.language==lang
 assert parser.alternates==dict(expected,**{'x-default':expected['ja']})
 assert parser.options==expected
 code=CodeParser();code.feed(html);assert [s.strip() for s in code.blocks]==[c[0].strip()],lang
 lastmod=re.search(r'^lastmod: (.*)$',current,re.M).group(1)
 assert '"dateModified":"'+lastmod in html
 assert '"datePublished":"2024-08-24T09:38:10+09:00"' in html
 if lang=='hi':assert 'अभाज्य संख्या 2 या उससे बड़ा पूर्णांक होती है' in html
 if lang=='ru':assert 'статью о тесте Миллера—Рабина' in html
 assert len(re.findall(r'^## ',current,re.M))==4 and '```mermaid' not in current
 assert re.findall(r'^```text\n(.*?)^```',current,re.M|re.S)==['2 3 5 7 11 13 17 19 23 29\n']
 for e in v['executions']:
  assert e['primeClassifications']==50168 and e['validInputCases']==11 and e['invalidInputCases']==17 and e['printerCases']==12 and e['completeProgramValidCases']==6 and e['completeProgramInvalidCases']==5
 versions.append({'language':lang,'sha256':h,'codeSha256':digest(c[0]),'canonical':url,'lastmod':lastmod,'executionEvidence':p.relative_to(root).as_posix(),'executedVersionHash':v['sha256'],'executionCodeUnchangedAfterPolish':lang in changes,'executions':v['executions'],'htmlCodeExact':True,'languageAndAllArticleTranslationTargetsMatch':True,'datePublishedPreserved':True})
out.write_text(json.dumps({'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'versions':versions,'scope':'Fresh generated HTML/code/metadata/expected language maps for all13versions. Reuses preserved actual O2/UBSan execution evidence, does not falsely claim new executable runs. Hindi/Russian prose/date-only change has before/after hashes and exact unchanged-code proof. Prose review recorded separately.','totalPrimeClassificationsAcrossVersionsAndModes':50168*26,'otherExecutionCasesAcrossVersionsAndModes':51*26,'publicationPending':True},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'versions':len(versions),'classifications':50168*26,'otherCases':51*26,'exactHtmlCBlocks':len(versions)}))
