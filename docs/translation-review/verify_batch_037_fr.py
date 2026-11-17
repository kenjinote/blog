from pathlib import Path
from datetime import datetime,timezone,timedelta
from html import unescape
import hashlib,importlib.util,json,re,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review';F=chr(96)*3
spec=importlib.util.spec_from_file_location('pair',D/'verify_batch_034_ja_en.py');pair=importlib.util.module_from_spec(spec);spec.loader.exec_module(pair);shared=pair.shared
site=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
doc=json.loads((D/'batch-037.json').read_text(encoding='utf-8'));audit=json.loads((D/'batch-037-source-audit.json').read_text(encoding='utf-8'));cover=json.loads((D/'batch-037-cover-revision.json').read_text(encoding='utf-8'))
changes={v['path']:v for v in cover['changes']};urls={}
for lang,e in audit['versions'].items():
 t=(ROOT/e['path']).read_text(encoding='utf-8');assert hashlib.sha256(t.encode()).hexdigest()=={'ar': '818fed0280f5c82e08d736d12ceb93b60877a57bafb02293902f88071da333c2', 'de': '35c651dc448c3f1da639ccbabf5db1ea9a9670937eecc4e12d6da142a7d544db', 'en': '4cc373b94aea7ba0b39417bf4381c22883e055eca6a6dbe34ded4ff1796ca1a6', 'es': '65db3abf4f3a40931553c941ef77d936a3dcb37f5de514f2354207ec377cc44f', 'fr': 'c8944bb6959a29ce580d8ac18efe5613c0baa7e4e9c8316c0e671f187275a48c', 'hi': '9cdb5d05f6ec7a46c6406267c2f72eb7d483501cb445f1d18d826c2dc10bdafb', 'id': '23ea03c01371970271c1aee2d5e20df3c6e407ae49f2d2cba103c6221c6b121e', 'ko': '807878a8d613a30560c4226290db321d8e1026fa28c1e1845d65bb24859fc905', 'ja': '4768e83cb5bc16d0753c3b460e0e81a0de8df159e4b2e0638aa3a73ddff8d777', 'pt': 'a061bff28269ddec120de1b38296fdf72f6f4c8f7e68ebc3109c4637cef6ac4b', 'ru': 'ea2d360c5a927bad5c44b8093def861db0a8bc6c25868419d737fc9d00e4fa7c', 'zh-cn': 'a923c5cc07e3c70618c84ad65cf4936c18527f6e34193802325bbb141517dd5c', 'zh-tw': '9b959dda04cc6163152bf99b2097b1b8bf768c6d28ef70832d6decf61cf8af69'}[lang]
 slug=json.loads(re.search(r'^slug: (.*)$',t,re.M)[1]);urls[lang]='https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/'+slug+'/'
p=ROOT/audit['versions']['fr']['path'];t=p.read_text(encoding='utf-8');digest=hashlib.sha256(t.encode()).hexdigest();assert digest=='c8944bb6959a29ce580d8ac18efe5613c0baa7e4e9c8316c0e671f187275a48c'
ja=(ROOT/audit['versions']['ja']['path']).read_text(encoding='utf-8');assert hashlib.sha256(ja.encode()).hexdigest()==doc['frozenSourceHash']
html=(site/'fr/p/godels-incompleteness-theorems/index.html').read_text(encoding='utf-8');a=shared.Article();a.feed(html)
tex=shared.source_math(t);assert shared.shared.render.expressions(''.join(a.math))==tex
assert len(re.findall(r'\$\$(.*?)\$\$',t,re.S))==2
assert re.findall(r'^## (\d+)\.',t,re.M)==list(map(str,range(1,9)))
graphs=shared.shared.graphs(t);assert len(graphs)==4 and [g.count('-->') for g in graphs]==[3,5,4,4]
assert all(g.strip() in unescape(html) for g in graphs)
assert re.findall('^'+F+r'(\w+)\n',t,re.M)==['mermaid']*4
refs=set(re.findall(r'\]\((https://[^)]+)\)',t));internal=set(re.findall(r'\]\((/fr/p/[^)]+)\)',t))
assert len(refs)==4 and len(internal)==3 and refs|internal<=set(a.links)
assert t.count('<strong>')==html.count('<strong>')==6
prose=pair.prose_fragments(re.sub(r'\[([^\]]+)\]\(/fr/p/[^)]+\)',r'\1',t),html)
nav=shared.shared.PageParser();nav.feed(html.split('</aside>',1)[0]+'</aside>')
assert nav.canonical==urls['fr'] and nav.language=='fr' and nav.alternates==dict(urls,**{'x-default':urls['ja']}) and nav.options==urls
assert '"datePublished":"2026-09-14T00:00:51+09:00"' in html and '"dateModified":"2026-11-17' in html
assert json.loads(re.search(r'^title: (.*)$',t,re.M)[1]) in unescape(html)
assert 'eyecatch-v2' in html and hashlib.sha256((ROOT/cover['newAsset']).read_bytes()).hexdigest()==cover['newAssetSha256']
for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
assert not any(ord(c)<32 and c not in '\n\r' for c in t)
assert re.findall(r'\$\$(.*?)\$\$',t,re.S)==re.findall(r'\$\$(.*?)\$\$',ja,re.S)
shape=lambda g:re.sub(r'"[^"\n]*"','""',g)
assert list(map(shape,graphs))==list(map(shape,shared.shared.graphs(ja)))
r=dict(checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=True,language='fr',sourceSha256=digest,texExpressions=sum(tex.values()),displayMath=2,diagrams=4,diagramEdges=[3,5,4,4],executablePrograms=0,proseFragmentsPreserved=prose,strongSpans=6,externalReferences=4,internalReferences=3,datesTitleNavigationCoverPassed=True,reviewedTranslationsAdded=0,publicationPending=True,scope='French static source/HTML match; original/revised fully read.5translations unread; French registration pending. No browser KaTeX/Mermaid execution, fullsite/publication or theorem-proof certification.')
out.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(r))
