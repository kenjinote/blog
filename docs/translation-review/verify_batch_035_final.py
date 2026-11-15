"""Verify all13 exact reviewed versions in one assembled static preview."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from html import unescape
import hashlib,importlib.util,json,re,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review';F=chr(96)*3
spec=importlib.util.spec_from_file_location('ar',D/'verify_batch_035_ar.py');ar=importlib.util.module_from_spec(spec);spec.loader.exec_module(ar);shared=ar.shared
site=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
doc=json.loads((D/'batch-035.json').read_text(encoding='utf-8'));assert len(doc['reviews'])==12
audit=json.loads((D/'batch-035-source-audit.json').read_text(encoding='utf-8'))
texts={lang:(ROOT/e['path']).read_text(encoding='utf-8') for lang,e in audit['versions'].items()}
urls={lang:'https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/'+json.loads(re.search(r'^slug: (.*)$',t,re.M)[1])+'/' for lang,t in texts.items()}
versions=[]
for lang,t in texts.items():
    p=ROOT/audit['versions'][lang]['path'];digest=shared.shared.digest(p)
    expected=doc['frozenSourceHash'] if lang=='ja' else doc['reviews'][p.relative_to(ROOT/'content').as_posix()]['translationHash'];assert digest==expected
    prior=json.loads((D/('batch-035-ja-r2-validation.json' if lang=='ja' else f'batch-035-{lang}-validation.json')).read_text(encoding='utf-8'));assert prior['allPassed']
    v=prior if lang=='ja' else next(v for v in prior['versions'] if v['language']==lang)
    assert digest==v.get('sha256',v.get('sourceSha256'))
    html=(site/urls[lang].removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
    a=shared.Article();a.feed(html);tex=shared.source_math(t)
    assert shared.shared.render.expressions(''.join(a.math))==tex and sum(tex.values())==v['texExpressions']
    display=re.findall(r'\$\$(.*?)\$\$',t,re.S);assert len(display)==v['displayMath']
    graphs=shared.shared.graphs(t);assert len(graphs)==2 and [g.count('-->') for g in graphs]==[6,5]
    assert all(g.strip() in unescape(html) for g in graphs)
    blocks=re.findall('^'+F+r'text\n(.*?)^'+F,t,re.M|re.S);assert len(blocks)==2 and all(b in a.codes for b in blocks)
    assert re.findall('^'+F+r'(\w+)\n',t,re.M)==['mermaid','text','text','mermaid']
    refs=set(re.findall(r'\]\((https://[^)]+)\)',t));assert len(refs)==8 and refs<=set(a.links)
    assert len([r for r in a.rows if len(r)==3])==12
    assert t.count('<strong>')==html.count('<strong>')==v.get('strongSpansPreserved',22)
    prose=ar.pair.prose_fragments(t,html);assert prose==v['proseFragmentsPreserved']
    nav=shared.shared.PageParser();nav.feed(html.split('</aside>',1)[0]+'</aside>')
    assert nav.canonical==urls[lang] and nav.language==lang and nav.alternates==dict(urls,**{'x-default':urls['ja']}) and nav.options==urls
    modified=json.loads(re.search(r'^lastmod: (.*)$',t,re.M)[1])
    assert '"datePublished":"2026-10-14T02:00:00+09:00"' in html and '"dateModified":"'+modified in html
    assert json.loads(re.search(r'^title: (.*)$',t,re.M)[1]) in unescape(html)
    versions.append(dict(language=lang,path=p.relative_to(ROOT).as_posix(),sha256=digest,texExpressions=sum(tex.values()),displayMath=len(display),diagrams=2,diagramEdges=[6,5],references=8,pseudocodeBlocks=2,articleExecutablePrograms=0,proseFragmentsPreserved=prose,strongSpansPreserved=t.count('<strong>'),passed=True))
for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
result=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=True,versions=versions,reviewedTranslationsAdded=0,publicationPending=True,scope='All13 exact reviewed versions in assembled36bundle static preview. Semantic reading remains separate; no browser/runtime/fullsite certification.')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(allPassed=True,versions=len(versions),texExpressions=sum(v['texExpressions'] for v in versions),proseFragments=sum(v['proseFragmentsPreserved'] for v in versions))))
