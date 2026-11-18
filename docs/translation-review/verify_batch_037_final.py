from pathlib import Path
from datetime import datetime,timezone,timedelta
from html import unescape
import hashlib,importlib.util,json,re,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
spec=importlib.util.spec_from_file_location('pair',D/'verify_batch_034_ja_en.py');pair=importlib.util.module_from_spec(spec);spec.loader.exec_module(pair);shared=pair.shared
audit=json.loads((D/'batch-037-source-audit.json').read_text(encoding='utf-8'))
doc=json.loads((D/'batch-037.json').read_text(encoding='utf-8'))
texts={l:(ROOT/v['path']).read_text(encoding='utf-8') for l,v in audit['versions'].items()}
urls={l:'https://kenji.blog/'+('' if l=='ja' else l+'/')+'p/godels-incompleteness-theorems/' for l in texts}
def check(lang,html):
 t=texts[lang];a=shared.Article();a.feed(html)
 tex=shared.source_math(t);graphs=shared.shared.graphs(t)
 assert shared.shared.render.expressions(''.join(a.math))==tex
 assert len(re.findall(r'\$\$(.*?)\$\$',t,re.S))==2
 assert re.findall(r'^## (\d+)\.',t,re.M)==list(map(str,range(1,9)))
 assert len(graphs)==4 and [g.count('-->') for g in graphs]==[3,5,4,4]
 assert all(g.strip() in unescape(html) for g in graphs)
 assert re.findall('^'+chr(96)*3+r'(\w+)\n',t,re.M)==['mermaid']*4
 refs=set(re.findall(r'\]\((https://[^)]+)\)',t));internal=set(re.findall(r'\]\((/(?:[a-z-]+/)?p/[^)]+)\)',t))
 assert len(refs)==4 and len(internal)==3 and refs|internal<=set(a.links)
 assert t.count('<strong>')==html.count('<strong>')==6
 prose=pair.prose_fragments(re.sub(r'\[([^\]]+)\]\(/(?:[a-z-]+/)?p/[^)]+\)',r'\1',t),html)
 nav=shared.shared.PageParser();nav.feed(html.split('</aside>',1)[0]+'</aside>')
 assert nav.canonical==urls[lang] and nav.language==lang and nav.alternates==dict(urls,**{'x-default':urls['ja']}) and nav.options==urls
 assert '"datePublished":"2026-09-14T00:00:51+09:00"' in html
 modified=json.loads(re.search(r'^lastmod: (.*)$',t,re.M)[1]);assert '"dateModified":"'+modified in html
 assert json.loads(re.search(r'^title: (.*)$',t,re.M)[1]) in unescape(html) and 'eyecatch-v2' in html
 assert re.findall(r'\$\$(.*?)\$\$',t,re.S)==re.findall(r'\$\$(.*?)\$\$',texts['ja'],re.S)
 shape=lambda g:re.sub(r'"[^"\n]*"','""',g)
 assert list(map(shape,graphs))==list(map(shape,shared.shared.graphs(texts['ja'])))
 if lang=='ar':
  bp=shared.BidiValues();bp.feed(html);assert bp.rtl and not bp.active
 return dict(language=lang,sha256=hashlib.sha256(t.encode()).hexdigest(),texExpressions=sum(tex.values()),proseFragmentsPreserved=prose,diagrams=4,diagramEdges=16,allPassed=True)
if __name__=='__main__':
 site=Path(sys.argv[1]);out=D/'batch-037-final-validation.json';assert not out.exists()
 ledger=json.loads((ROOT/'data/translation_reviews.json').read_text(encoding='utf-8'))['reviews']
 assert len(doc['reviews'])==12 and len(ledger)==456
 assert hashlib.sha256(texts['ja'].encode()).hexdigest()==doc['frozenSourceHash']
 versions=[]
 for lang,t in texts.items():
  if lang!='ja':
   key=audit['versions'][lang]['path'].removeprefix('content/');e=doc['reviews'][key]
   assert e['translationHash']==ledger[key]['translationHash']==hashlib.sha256(t.encode()).hexdigest()
   assert e['sourceHash']==ledger[key]['sourceHash']==doc['frozenSourceHash']
  versions.append(check(lang,(site/('' if lang=='ja' else lang)/'p/godels-incompleteness-theorems/index.html').read_text(encoding='utf-8')))
 r=dict(checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=True,versions=versions,publicationPending=True,scope='Final static validation of all13 exact reviewed revisions and ledger hashes. No browser/native/fullsite certification.')
 out.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(dict(versions=len(versions),texExpressions=sum(v['texExpressions'] for v in versions),proseFragments=sum(v['proseFragmentsPreserved'] for v in versions),allPassed=True)))
