"""Frozen JA and fully read revised Indonesian static checks; reading approval is separate."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from collections import Counter
from html import unescape
import hashlib,importlib.util,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review';FENCE=chr(96)*3
spec=importlib.util.spec_from_file_location('pair',D/'verify_batch_034_ja_en.py');pair=importlib.util.module_from_spec(spec);spec.loader.exec_module(pair)
shared=pair.shared

def main():
    site=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
    audit=json.loads((D/'batch-035-source-audit.json').read_text(encoding='utf-8'))
    batch=json.loads((D/'batch-035.json').read_text(encoding='utf-8'))
    ja=(ROOT/audit['versions']['ja']['path']).read_text(encoding='utf-8')
    source_hash=hashlib.sha256(ja.encode()).hexdigest();assert source_hash==batch['frozenSourceHash']
    repairs=json.loads((D/'batch-035-escape-repair.json').read_text(encoding='utf-8'))
    for v in repairs['versions']:
        if v['language'] not in ('zh-cn','zh-tw','es','ko','pt','fr','de','hi','id'):assert shared.shared.digest(ROOT/v['path'])==v['repairedSha256']
    for k,e in batch['reviews'].items():
        assert shared.shared.digest(ROOT/'content'/k)==e['translationHash']
    urls={};texts={}
    for lang,e in audit['versions'].items():
        t=(ROOT/e['path']).read_text(encoding='utf-8');texts[lang]=t
        slug=json.loads(re.search(r'^slug: (.*)$',t,re.M)[1]);urls[lang]='https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/'+slug+'/'
    core=[x.strip() for x in re.findall(r'\$\$(.*?)\$\$',ja,re.S)];assert len(core)==38
    translated=[x.replace(' がマルティン＝レーフ・ランダム',' acak menurut Martin-Löf') for x in core]
    refs=set(re.findall(r'\]\((https://[^)]+)\)',ja));assert len(refs)==8
    versions=[]
    for lang in ('id',):
        e=audit['versions'][lang];text=texts[lang]
        original=subprocess.run(['git','show',audit['baselineCommit']+':'+e['path']],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
        assert hashlib.sha256(original.encode()).hexdigest()==e['sha256']
        for key in ('title','date','slug','image','draft'):
            assert re.findall('^'+key+':.*$',text,re.M)==re.findall('^'+key+':.*$',original,re.M)
        assert shared.shared.taxonomy(text)==shared.shared.taxonomy(original)
        assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,8)))
        assert not any(ord(c)<32 and c not in '\n\r' for c in text)
        assert re.findall('^'+FENCE+r'(\w+)\n',text,re.M)==['mermaid','text','text','mermaid']
        blocks=re.findall('^'+FENCE+r'text\n(.*?)^'+FENCE,text,re.M|re.S);assert len(blocks)==2
        assert blocks[0].startswith('Berry(m):\n') and 'ComputeK(x) >= m' in blocks[0]
        assert blocks[1].startswith('SearchProof(r):\n') and 'm >= r' in blocks[1]
        display=[x.strip() for x in re.findall(r'\$\$(.*?)\$\$',text,re.S)]
        assert Counter(display)==Counter(core if lang=='ja' else translated)
        graphs=shared.shared.graphs(text);shape=lambda g:re.sub(r'"[^"\n]*"','""',g)
        assert len(graphs)==2 and [g.count('-->') for g in graphs]==[6,5]
        assert list(map(shape,graphs))==list(map(shape,shared.shared.graphs(ja)))
        assert set(re.findall(r'\]\((https://[^)]+)\)',text))==refs
        html=(site/urls[lang].removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8');a=shared.Article();a.feed(html)
        tex=shared.source_math(text);assert shared.shared.render.expressions(''.join(a.math))==tex
        assert all(g.strip() in unescape(html) for g in graphs) and all(b in a.codes for b in blocks)
        assert len([row for row in a.rows if len(row)==3])==12 and refs<=set(a.links)
        strong=22;assert text.count('<strong>')==text.count('</strong>')==html.count('<strong>')==strong
        nav=shared.shared.PageParser();nav.feed(html.split('</aside>',1)[0]+'</aside>')
        assert nav.canonical==urls[lang] and nav.language==lang and nav.alternates==dict(urls,**{'x-default':urls['ja']}) and nav.options==urls
        modified=json.loads(re.search(r'^lastmod: (.*)$',text,re.M)[1]);assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',modified)
        assert '"datePublished":"2026-10-14T02:00:00+09:00"' in html and '"dateModified":"'+modified in html
        assert json.loads(re.search(r'^title: (.*)$',text,re.M)[1]) in unescape(html)
        assert not re.search(r'[\uac00-\ud7af\u3040-\u30ff\u3400-\u9fff\u0400-\u052f\u0600-\u06ff\u0900-\u097f\u0e00-\u0e7f]',text)
        article=''.join(a.all)
        phrase='bilangan bulat positif terkecil yang tidak dapat didefinisikan dalam kurang dari dua puluh kata'
        assert len(phrase.split())==14 and phrase in article
        assert all(t in article for t in ['0010010000111111...','empat belas kata','distribusi titik','proses stasioner ergodik pada alfabet berhingga','kesahihan semantik','likelihood','0,9997'])
        assert 'เมื่อ' not in text
        versions.append(dict(language=lang,path=e['path'],sha256=shared.shared.digest(ROOT/e['path']),sourceSha256=source_hash,
            originalSha256=e['sha256'],texExpressions=sum(tex.values()),displayMath=len(display),coreDisplayBlocks=38,
            diagrams=2,diagramEdges=[6,5],references=8,pseudocodeBlocks=2,articleExecutablePrograms=0,
            mathHtmlExact=True,pseudocodeHtmlExact=True,proseFragmentsPreserved=pair.prose_fragments(text,html),strongSpansPreserved=strong,
            datesTaxonomyImageAndNavigationPassed=True,indonesianBerry14WordsAndThaiIntrusionRemoved=True,passed=True))
    for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
    result=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=True,versions=versions,
        sourceFrozenUnchanged=True,other2MechanicalRepairsUnchanged=True,priorNineReviewsUnchanged=True,reviewedTranslationsAdded=0,publicationPending=True,
        priorFiniteEvidence=['docs/translation-review/batch-035-original-finite-probe.json','docs/translation-review/batch-035-ja-auxiliary.json'],
        scope='Selected Indonesian static source/HTML consistency, not automatic semantic approval. Prior finite evidence and17unit tests referenced,not rerun. Original/revised full reading separately recorded. No executable article programs, K/Omega oracle,theorem proof,real LLM/corpus/NCD experiments,browser/KaTeX/Mermaid execution,native/full-site/publication certification.')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(allPassed=True,versions=versions)))
if __name__=='__main__':main()
