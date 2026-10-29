"""Selected CRT versions: executable and auxiliary finite checks, never prose approval."""
from pathlib import Path
import argparse,json,re,importlib.util,math,itertools,random,io,contextlib,sys,hashlib
from datetime import datetime,timezone,timedelta
ROOT=Path(__file__).resolve().parents[2];FOLDER=ROOT/'content/post/chinese-remainder-theorem'
spec=importlib.util.spec_from_file_location('render_checks',Path(__file__).with_name('verify_batch_022.py'));check=importlib.util.module_from_spec(spec);spec.loader.exec_module(check)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--languages',nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();assert not a.output.exists()
    audit=json.loads((ROOT/'docs/translation-review/batch-024-source-audit.json').read_text(encoding='utf-8'));urls={l:v['canonical'] for l,v in audit['versions'].items()}
    fence=chr(96)*3;ja=(FOLDER/'index.md').read_text(encoding='utf-8');code_ja=re.findall(r'^'+fence+r'python\n(.*?)^'+fence,ja,re.M|re.S);assert len(code_ja)==1
    graphs_ja=re.findall(r'^'+fence+r'mermaid\n(.*?)^'+fence,ja,re.M|re.S);assert len(graphs_ja)==1
    edges=lambda g:re.findall(r'^\s*(\w+).*?--.*?>\s*(\w+)',g,re.M);assert len(edges(graphs_ja[0]))==6
    strip=lambda s:re.sub(r'^'+fence+r'.*?^'+fence+r'[^\n]*','',s,flags=re.M|re.S)
    tex=check.cpp.rendering.expressions(strip(ja));assert sum(tex.values())==41
    external={'https://sgmathsociety.org/smsmedley/Vol-30-1/The%20History%20of%20the%20Chinese%20Reminder%20Theorem%20%28Law%20Huang%20lng%29.pdf','https://kconrad.math.uconn.edu/blurbs/ugradnumthy/crt.pdf','https://www.rfc-editor.org/rfc/rfc8017.html','https://cacr.uwaterloo.ca/hac/about/chap14.pdf','https://stacks.math.columbia.edu/tag/00DT','https://courses.csail.mit.edu/6.857/2010/handouts/faults.pdf'}
    # Independent exhaustive small-reference table, by enumeration rather than inverse sums.
    small=[]
    for m,n in itertools.combinations(range(2,13),2):
        if math.gcd(m,n)!=1:continue
        expected={(x%m,x%n):x for x in range(m*n)};assert len(expected)==m*n
        for residues,x in expected.items():small.append((residues,(m,n),x))
    singleton=[([x],[m],x%m) for m in range(2,13) for x in range(-2*m,2*m+1)]
    triples=[]
    for moduli in [(3,5,7),(4,9,25),(5,8,9)]:
        total=math.prod(moduli)
        expected={tuple(x%m for m in moduli):x for x in range(total)};assert len(expected)==total
        triples.extend((residues,moduli,x) for residues,x in expected.items())
    rng=random.Random(24029);large=[];moduli=(2**127-1,2**61-1,2**32);total=math.prod(moduli)
    assert all(math.gcd(x,y)==1 for x,y in itertools.combinations(moduli,2))
    for _ in range(128):
        x=rng.getrandbits(768)*rng.choice([-1,1]);residues=[x%m + rng.randrange(-10,11)*m for m in moduli];large.append((residues,moduli,x%total))
    invalid=[([],[],ValueError),([2],[3,5],ValueError),([2,3],[3],ValueError),([0],[0],ValueError),([2],[-3],ValueError),([0],[1],ValueError),([2.5],[3],TypeError),([True],[3],TypeError),([0],[True],TypeError),([0],[3.0],TypeError),([1,3],[4,6],ValueError),([0,1],[4,6],ValueError),([0,0],[3,3],ValueError),([0,0,0],[6,10,15],ValueError),(['2'],[3],TypeError),(None,[3],TypeError),([2],None,TypeError),(2,[3],TypeError)]
    versions=[]
    for lang in a.languages:
        p=ROOT/audit['versions'][lang]['path'];text=p.read_text(encoding='utf-8-sig');code=re.findall(r'^'+fence+r'python\n(.*?)^'+fence,text,re.M|re.S);assert code==code_ja
        graphs=re.findall(r'^'+fence+r'mermaid\n(.*?)^'+fence,text,re.M|re.S);assert len(graphs)==1 and edges(graphs[0])==edges(graphs_ja[0])
        url=urls[lang];html=(a.site/url.removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8');parser=check.PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>')
        assert parser.canonical==url and parser.language==lang and parser.alternates==dict(urls,**{'x-default':urls['ja']}) and parser.options==urls
        assert check.cpp.rendering.expressions(strip(text))==tex
        article=check.cpp.rendering.ArticleText();article.feed(html);assert check.cpp.rendering.expressions(''.join(article.parts))==tex
        rendered=check.CodeParser();rendered.feed(html);assert [(l,b.strip()) for l,b in rendered.blocks]==[('python',code[0].strip())]
        from html import unescape
        assert graphs[0].strip() in unescape(html)
        internal='https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/rsa-encryption-math-explained-for-beginners/'
        refs=set(re.findall(r'\]\((https://[^)]+)\)',text));assert refs==external|{internal} and all(u in html for u in refs)
        assert (a.site/internal.removeprefix('https://kenji.blog/')/'index.html').is_file()
        assert len(re.findall(r'^## [1-9]\. ',text,re.M))==9
        assert text.count('\ndate: ')==1 and 'date: "2026-09-14T13:11:25+09:00"' in text
        lastmod=re.search(r'^lastmod: (\d{4}-\d{2}-\d{2})$',text,re.M)[1]
        datetime.strptime(lastmod,'%Y-%m-%d')
        assert '2026-10-29' <= lastmod <= datetime.now(timezone(timedelta(hours=9))).date().isoformat()
        assert 'image: "eyecatch.jpg"' in text and 'slug: "chinese-remainder-theorem"' in text and 'math: true' in text and 'mermaid: true' in text
        assert '"datePublished":"2026-09-14T13:11:25+09:00"' in html and ('"dateModified":"'+lastmod) in html and 'katex' in html
        assert hashlib.sha256((FOLDER/'eyecatch.jpg').read_bytes()).hexdigest()==audit['imageSha256']
        ns={'__name__':'__main__'};capture=io.StringIO()
        with contextlib.redirect_stdout(capture):exec(compile(code[0],str(p),'exec'),ns)
        assert capture.getvalue()=='Sunzi solution: 23\nCombined modulus: 105\n';crt=ns['chinese_remainder_theorem'];inverse=ns['mod_inverse']
        for residues,moduli,x in singleton+small+triples+large:assert crt(residues,moduli)==x
        assert crt(iter([-1,8]),iter([3,5]))==8
        for residues,moduli,error in invalid:
            try:crt(residues,moduli)
            except error:pass
            else:raise AssertionError('Invalid input accepted')
        inverse_cases=0
        for m in range(2,101):
            for x in range(-50,51):
                g,s,t=ns['_extended_gcd'](x,m);assert g==math.gcd(x,m) and x*s+m*t==g
                if g==1:assert inverse(x,m)==pow(x,-1,m)
                else:
                    try:inverse(x,m)
                    except ValueError:pass
                    else:raise AssertionError('Noninvertible input accepted')
                inverse_cases+=1
        bad_inverse=[(1,0,ValueError),(1,1,ValueError),(1,-3,ValueError),(True,5,TypeError),(1,5.0,TypeError)]
        for x,m,error in bad_inverse:
            try:inverse(x,m)
            except error:pass
            else:raise AssertionError('Invalid inverse input accepted')
        for c in range(3233):
            mp,mq=pow(c,53,61),pow(c,49,53);h=(mp-mq)*pow(53,-1,61)%61
            assert crt([mp,mq],[61,53])==mq+53*h==pow(c,2753,3233)
        for x,y in itertools.product(range(105),repeat=2):
            assert crt([(x+y)%m for m in [3,5,7]],[3,5,7])==(x+y)%105
            assert crt([(x*y)%m for m in [3,5,7]],[3,5,7])==x*y%105
        versions.append({'language':lang,'sha256':check.digest(p),'canonical':url,'texExpressions':41,'allTeXPreserved':True,'pythonBlocksExact':1,'completeProgramOutputExact':True,'singleModulusSignedCases':len(singleton),'smallPairCases':len(small),'smallTripleCases':len(triples),'largeSignedCases':128,'generatorInputsExact':True,'invalidCrtCases':len(invalid),'extendedGcdAndInverseCases':inverse_cases,'invalidInverseCases':len(bad_inverse),'rsaCrtAllRepresentatives':3233,'rnsAddAndMultiplyCases':22050,'diagramEdges':6,'referencesMetadataLanguageMapsExact':True,'passed':True})
    # A finite polynomial evaluation bijection illustrates, not proves, interpolation.
    evaluations={tuple((a0+a1*x+a2*x*x)%7 for x in [0,1,3]):(a0,a1,a2) for a0,a1,a2 in itertools.product(range(7),repeat=3)};assert len(evaluations)==343
    output={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'pythonVersion':sys.version.split()[0],'scope':'Explicit selected versions only. Each complete article program executed and functions compared against independent enumeration/Python arithmetic. Auxiliary interpolation check once per invocation. No prose approval or ledger writes.','versions':versions,'auxiliaryInterpolationEvaluationBijection':343,'publicationPending':True,'limitations':['Finite inputs,not exhaustive proof or cryptographic audit.','Contract rejects noncoprime systems,unitmoduli andempty systems;does not implement generalizedCRT.','No timing/constant-time/production-key-validation or native-language certification.','Diagram source and HTML/TeX checked,no browser visual/runtime certification.']}
    a.output.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'versions':len(versions),'texEach':41,'smallPairsEach':len(small),'smallTriplesEach':len(triples),'rsaCrtEach':3233,'rnsCasesEach':22050}))


if __name__=='__main__':main()
