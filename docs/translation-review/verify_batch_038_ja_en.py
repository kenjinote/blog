from pathlib import Path
from datetime import datetime,timezone,timedelta
from html import unescape
import hashlib,importlib.util,json,re,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review';F=chr(96)*3
spec=importlib.util.spec_from_file_location('pair',D/'verify_batch_034_ja_en.py');pair=importlib.util.module_from_spec(spec);spec.loader.exec_module(pair);shared=pair.shared
site=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
audit=json.loads((D/'batch-038-source-audit.json').read_text(encoding='utf-8'))
doc=json.loads((D/'batch-038.json').read_text(encoding='utf-8'))
texts={l:(ROOT/v['path']).read_text(encoding='utf-8') for l,v in audit['versions'].items()}
urls={l:'https://kenji.blog/'+('' if l=='ja' else l+'/')+'p/cantors-diagonal-argument/' for l in texts}
cover=json.loads((D/'batch-038-cover-revision.json').read_text(encoding='utf-8'));versions=[]
assert hashlib.sha256(texts['ja'].encode()).hexdigest()==doc['frozenSourceHash']
for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
assert hashlib.sha256((ROOT/cover['newAsset']).read_bytes()).hexdigest()==cover['newAssetSha256']
for change in cover['changes']:
 if change['path'].endswith(('index.md','index.en.md')):continue
 assert hashlib.sha256((ROOT/change['path']).read_text(encoding='utf-8').encode()).hexdigest()==change['after']
for lang in ('ja','en'):
 t=texts[lang];html=(site/('' if lang=='ja' else lang)/'p/cantors-diagonal-argument/index.html').read_text(encoding='utf-8')
 a=shared.Article();a.feed(html);tex=shared.source_math(t)
 assert shared.shared.render.expressions(''.join(a.math))==tex
 displays=re.findall(r'\$\$(.*?)\$\$',t,re.S);assert len(displays)==9
 assert displays==re.findall(r'\$\$(.*?)\$\$',texts['ja'],re.S)
 graphs=shared.shared.graphs(t);assert len(graphs)==2 and [g.count('-->') for g in graphs]==[5,3]
 assert all(g.strip() in unescape(html) for g in graphs)
 shape=lambda g:re.sub(r'"[^"\n]*"','""',re.sub(r'^\s*%%.*$','',g,flags=re.M))
 assert list(map(shape,graphs))==list(map(shape,shared.shared.graphs(texts['ja'])))
 assert re.findall('^'+F+r'(\w+)\n',t,re.M)==['mermaid']*2
 refs=set(re.findall(r'\]\((https://[^)]+)\)',t));internal=set(re.findall(r'\]\((/(?:[a-z-]+/)?p/[^)]+)\)',t))
 assert len(refs)==3 and len(internal)==6 and refs|internal<=set(a.links)
 assert t.count('<strong>')==html.count('<strong>')
 assert not re.search(r'^#{1,6} .*\$|^#{1,6} .*\]\(',t,re.M)
 normalized=re.sub(r'\[([^\]]+)\]\(/(?:[a-z-]+/)?p/[^)]+\)',r'\1',t)
 prose=pair.prose_fragments(normalized.replace("\u201c",chr(34)).replace("\u201d",chr(34)),html.replace("&ldquo;","&#34;").replace("&rdquo;","&#34;").replace("&#8220;","&#34;").replace("&#8221;","&#34;").replace("\u201c",chr(34)).replace("\u201d",chr(34)))
 nav=shared.shared.PageParser();nav.feed(html.split('</aside>',1)[0]+'</aside>')
 assert nav.canonical==urls[lang] and nav.language==lang and nav.alternates==dict(urls,**{'x-default':urls['ja']}) and nav.options==urls
 assert '"datePublished":"2026-09-14T13:11:25+09:00"' in html and '"dateModified":"2026-11-19' in html
 assert json.loads(re.search(r'^title: (.*)$',t,re.M)[1]) in unescape(html) and 'eyecatch-v2' in html
 assert '\\mathfrak{c}=2^{\\aleph_0}' in t and '2^{\\aleph_0}=\\aleph_1' in t
 versions.append(dict(language=lang,sha256=hashlib.sha256(t.encode()).hexdigest(),texExpressions=sum(tex.values()),displayMath=9,diagrams=2,diagramEdges=[5,3],proseFragmentsPreserved=prose,strongSpans=t.count('<strong>'),externalReferences=3,internalReferences=6,allPassed=True))
# Finite illustration sanity checks only; not a proof of uncountability or CH.
digit_cases=[dict(original=d,replacement=2 if d==1 else 1) for d in range(10)]
assert all(x['replacement'] in (1,2) and x['replacement']!=x['original'] for x in digit_cases)
r=dict(checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=True,versions=versions,digitRuleCases=digit_cases,publicationPending=True,reviewedTranslationsAdded=0,scope='Original/revised JA and EN fully read; static HTML checks and ten finite digit cases only. No executable article code; no browser KaTeX/Mermaid, fullsite, human/native or theorem certification. Other11translations unread.')
out.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(r))
