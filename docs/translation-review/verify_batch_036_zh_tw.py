"""Selected Japanese checks; neither translation approval nor browser execution."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from html import unescape
import hashlib,importlib.util,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review';F=chr(96)*3
spec=importlib.util.spec_from_file_location('pair',D/'verify_batch_034_ja_en.py');pair=importlib.util.module_from_spec(spec);spec.loader.exec_module(pair)
shared=pair.shared
def main():
    site=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
    audit=json.loads((D/'batch-036-source-audit.json').read_text(encoding='utf-8'))
    cover=json.loads((D/'batch-036-cover-revision.json').read_text(encoding='utf-8'))
    code=json.loads((D/'batch-036-ja-code-validation.json').read_text(encoding='utf-8'))
    changes={v['language']:v for v in cover['changes']};assert len(changes)==13
    urls={}
    for lang,e in audit['versions'].items():
        s=(ROOT/e['path']).read_text(encoding='utf-8')
        expected={'zh-tw':'8823100f840d1908433d09ba02e865782d7c1902df6ad51e1adf49b8a4942503','zh-cn':'070b7f4d533089efa6d0427a569ac2a7e94ff4d9594be2d65c104001a522502a','en':'73da7bf52d9c1906716868d27fb10226f162b798ccb5d3881914cceac398ab4d'}.get(lang,changes[lang]['after'])
        assert hashlib.sha256(s.encode()).hexdigest()==expected
        slug=json.loads(re.search(r'^slug: (.*)$',s,re.M)[1])
        urls[lang]='https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/'+slug+'/'
    p=ROOT/audit['versions']['zh-tw']['path'];text=p.read_text(encoding='utf-8')
    assert changes['ja']['before']==code['sourceSha256']
    original=subprocess.run(['git','show',audit['baselineCommit']+':'+p.relative_to(ROOT).as_posix()],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
    assert hashlib.sha256(original.encode()).hexdigest()==audit['versions']['zh-tw']['sha256']
    for key in ('title','slug','draft'):
        assert re.findall('^'+key+':.*$',text,re.M)==re.findall('^'+key+':.*$',original,re.M)
    assert shared.shared.taxonomy(text)==shared.shared.taxonomy(original)
    assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,9)))
    assert re.findall(r'^date:.*$',text,re.M)==['date: "2026-09-14T00:00:51+09:00"']
    assert not any(ord(c)<32 and c not in '\n\r' for c in text)
    html=(site/'zh-tw/p/halting-problem/index.html').read_text(encoding='utf-8')
    a=shared.Article();a.feed(html);tex=shared.source_math(text)
    assert shared.shared.render.expressions(''.join(a.math))==tex
    assert len(re.findall(r'\$\$(.*?)\$\$',text,re.S))==4
    graphs=shared.shared.graphs(text);assert len(graphs)==1 and graphs[0].count('-->')==8
    assert graphs[0].strip() in unescape(html)
    blocks=re.findall('^'+F+r'(python|text)\n(.*?)^'+F,text,re.M|re.S)
    assert [k for k,b in blocks]==['python','text','text','python','text','text']
    assert all(b in a.codes for k,b in blocks)
    py=[b for k,b in blocks if k=='python']
    assert [hashlib.sha256(b.encode()).hexdigest() for b in py]==[v['codeSha256'] for v in code['pythonPrograms']]
    refs=set(re.findall(r'\]\((https://[^)]+)\)',text));assert len(refs)==4 and refs<=set(a.links)
    internal=set(re.findall(r'\]\((/zh-tw/p/[^)]+)\)',text));assert len(internal)==3 and internal<=set(a.links)
    assert len([r for r in a.rows if len(r)==3])==3
    assert text.count('<strong>')==html.count('<strong>')
    nav=shared.shared.PageParser();nav.feed(html.split('</aside>',1)[0]+'</aside>')
    assert nav.canonical==urls['zh-tw'] and nav.language=='zh-tw' and nav.alternates==dict(urls,**{'x-default':urls['ja']}) and nav.options==urls
    assert '"datePublished":"2026-09-14T00:00:51+09:00"' in html and '"dateModified":"2026-11-15' in html
    asset=ROOT/cover['newAsset'];assert hashlib.sha256(asset.read_bytes()).hexdigest()==cover['newAssetSha256']
    assert 'eyecatch-v2' in html
    for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
    # Existing helper handles HTTPS Markdown links; normalize local article links identically.
    prose=re.sub(r'\[([^\]]+)\]\(/zh-tw/p/[^)]+\)',r'\1',text)
    fragments=pair.prose_fragments(prose,html)

    ja=(ROOT/'content/post/halting-problem/index.md').read_text(encoding='utf-8')
    core=lambda t:[re.sub(r'\\text\{[^}]*\}',r'\\text{localized}',x.strip()) for x in re.findall(r'\$\$(.*?)\$\$',t,re.S)]
    assert core(text)==core(ja)
    assert not re.search(r'[\u3040-\u30ff\u0400-\u052f\u0600-\u06ff\u0900-\u097f\u0e00-\u0e7f\uac00-\ud7af]',text)

    result=dict(checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=True,language='zh-tw',sourceSha256=hashlib.sha256(text.encode()).hexdigest(),texExpressions=sum(tex.values()),displayMath=4,diagrams=1,diagramEdges=8,executablePythonBlocks=2,textBlocks=4,mathCodeGraphHtmlExact=True,proseFragmentsPreserved=fragments,strongSpans=text.count('<strong>'),references=4,internalLinks=3,tableRows=3,datesTaxonomyNavigationPassed=True,coverReceipt='docs/translation-review/batch-036-cover-revision.json',finiteCodeEvidence='docs/translation-review/batch-036-ja-code-validation.json',reviewedTranslationsAdded=0,publicationPending=True,scope='Selected static Traditional Chinese HTML and exact prior code hashes; full source reading separately recorded. Other9 translations not read; this Chinese validation alone does not register approval. No browser Mermaid/KaTeX execution, full-site/publication certification or general halting/Collatz proof.')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
