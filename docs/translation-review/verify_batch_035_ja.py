"""Selected revised Japanese source/HTML checks; full reading is separately recorded."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from html import unescape
import hashlib,importlib.util,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review';FENCE=chr(96)*3
spec=importlib.util.spec_from_file_location('pair',D/'verify_batch_034_ja_en.py');pair=importlib.util.module_from_spec(spec);spec.loader.exec_module(pair)
shared=pair.shared

def main():
    site=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
    audit=json.loads((D/'batch-035-source-audit.json').read_text(encoding='utf-8'))
    e=audit['versions']['ja'];p=ROOT/e['path'];text=p.read_text(encoding='utf-8')
    original=subprocess.run(['git','show',audit['baselineCommit']+':'+e['path']],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
    assert hashlib.sha256(original.encode()).hexdigest()==e['sha256']
    for key in ('title','date','slug','image','draft'):
        assert re.findall('^'+key+':.*$',text,re.M)==re.findall('^'+key+':.*$',original,re.M)
    assert shared.shared.taxonomy(text)==shared.shared.taxonomy(original)
    assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,8)))
    assert not any(ord(c)<32 and c not in '\n\r' for c in text)
    assert not re.search(r'[\u0400-\u052f\u0600-\u06ff\u0900-\u097f\u0e00-\u0e7f\uac00-\ud7af]',text)
    assert '@TICK@' not in text and '@FENCE@' not in text and '**' not in text
    assert re.findall('^'+FENCE+r'(\w+)\n',text,re.M)==['mermaid','text','text','mermaid']
    blocks=re.findall('^'+FENCE+r'text\n(.*?)^'+FENCE,text,re.M|re.S);assert len(blocks)==2
    assert blocks[0].startswith('Berry(m):\n') and 'ComputeK(x) >= m' in blocks[0]
    assert blocks[1].startswith('SearchProof(r):\n') and 'm >= r' in blocks[1]
    assert len(re.findall(r'\$\$(.*?)\$\$',text,re.S))==38
    urls={}
    for lang,entry in audit['versions'].items():
        source=(ROOT/entry['path']).read_text(encoding='utf-8-sig')
        if lang!='ja':assert hashlib.sha256(source.encode()).hexdigest()==entry['sha256']
        slug=json.loads(re.search(r'^slug: (.*)$',source,re.M)[1])
        urls[lang]='https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/'+slug+'/'
    html=(site/urls['ja'].removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
    a=shared.Article();a.feed(html);tex=shared.source_math(text)
    assert shared.shared.render.expressions(''.join(a.math))==tex
    graphs=shared.shared.graphs(text);assert len(graphs)==2 and [g.count('-->') for g in graphs]==[6,5]
    assert all(g.strip() in unescape(html) for g in graphs)
    assert all(b in a.codes for b in blocks)
    assert len([row for row in a.rows if len(row)==3])==12
    refs=set(re.findall(r'\]\((https://[^)]+)\)',text));assert len(refs)==8 and refs<=set(a.links)
    for label in ['小数部分','接頭複雑性 $K$','同じ定数 $c$','擬似コード','健全性','左計算可算（left-c.e.）','半測度','最小記述長（MDL）原理']:
        assert '<strong>'+label+'</strong>' in text
    for label in ['小数部分','擬似コード','健全性','左計算可算（left-c.e.）','半測度','最小記述長（MDL）原理']:
        assert '<strong>'+label+'</strong>' in html
    assert text.count('<strong>')==text.count('</strong>')==html.count('<strong>')==22
    nav=shared.shared.PageParser();nav.feed(html.split('</aside>',1)[0]+'</aside>')
    assert nav.canonical==urls['ja'] and nav.language=='ja' and nav.alternates==dict(urls,**{'x-default':urls['ja']}) and nav.options==urls
    modified=json.loads(re.search(r'^lastmod: (.*)$',text,re.M)[1]);assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',modified)
    assert '"datePublished":"2026-10-14T02:00:00+09:00"' in html and '"dateModified":"'+modified in html
    assert json.loads(re.search(r'^title: (.*)$',text,re.M)[1]) in unescape(html)
    for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
    prior=json.loads((D/'batch-035-original-finite-probe.json').read_text(encoding='utf-8'));aux=json.loads((D/'batch-035-ja-auxiliary.json').read_text(encoding='utf-8'))
    assert prior['passed'] and len(prior['countingCases'])==153 and aux['gammaIntegers']==1023 and aux['rationalHuffmanProfiles']==965 and aux['sequentialCodewordRoundTrips']==1022
    result=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=True,
        language='ja',path=e['path'],sourceSha256=shared.shared.digest(p),originalSha256=e['sha256'],
        texExpressions=sum(tex.values()),displayMath=38,diagrams=2,diagramEdges=[6,5],references=8,
        pseudocodeBlocks=2,articleExecutablePrograms=0,pseudocodeHtmlExact=True,mathHtmlExact=True,
        proseFragmentsPreserved=pair.prose_fragments(text,html),tableHeaderAndDataRows=12,
        all22StrongSpansPreserved=True,datesTaxonomyImageAndNavigationPassed=True,
        other12OriginalTranslationHashesUnchanged=True,
        auxiliary='docs/translation-review/batch-035-ja-auxiliary.json',priorFiniteEvidence='docs/translation-review/batch-035-original-finite-probe.json',
        reviewedTranslationsAdded=0,publicationPending=True,
        scope='Selected Japanese static HTML and prior finite arithmetic/coding evidence, not semantic approval of translations. Full original/revised reading separately recorded. No C/K/Omega oracle, theorem certification, complete compressor/LLM/corpus experiment, native review, browser/KaTeX/Mermaid execution, full-site or publication certification.')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
