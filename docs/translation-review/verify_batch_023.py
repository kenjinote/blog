"""Selected Fermat theorem versions: finite auxiliary arithmetic and HTML, not prose approval."""
from pathlib import Path
import argparse,json,re,hashlib,importlib.util,math
from datetime import datetime,timezone,timedelta

ROOT=Path(__file__).resolve().parents[2]
FOLDER=ROOT/'content/post/fermats-little-theorem'
spec=importlib.util.spec_from_file_location('checks',Path(__file__).with_name('verify_batch_022.py'))
check=importlib.util.module_from_spec(spec);spec.loader.exec_module(check)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--languages',nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();assert not a.output.exists()
    audit=json.loads((ROOT/'docs/translation-review/batch-023-source-audit.json').read_text(encoding='utf-8'))
    urls={l:v['canonical'] for l,v in audit['versions'].items()}
    fence=chr(96)*3;ja=(FOLDER/'index.md').read_text(encoding='utf-8')
    strip=lambda t:re.sub(r'^'+fence+r'.*?^'+fence+r'[^\n]*','',t,flags=re.M|re.S)
    tex=check.cpp.rendering.expressions(strip(ja))
    graphs_ja=re.findall(r'^'+fence+r'mermaid\n(.*?)^'+fence,ja,re.M|re.S)
    flow=lambda t:re.findall(r'^\s*(\w+).*?--.*?>\s*(\w+)',t,re.M)
    sequence=lambda t:re.findall(r'^\s*(Sender|Receiver)->>(Sender|Receiver):',t,re.M)
    assert len(graphs_ja)==2 and len(flow(graphs_ja[0]))==5 and len(sequence(graphs_ja[1]))==5
    primes=[p for p in range(2,101) if all(p%d for d in range(2,math.isqrt(p)+1))]
    fermat_cases=permutations=0
    for p in primes:
        for x in range(-100,101):
            assert pow(x,p,p)==x%p
            if x%p:
                assert pow(x,p-1,p)==1
                assert sorted((i*x)%p for i in range(1,p))==list(range(1,p))
                permutations+=1
            fermat_cases+=1
    rsa=[]
    for p,q in [(3,5),(5,7),(11,13),(61,53)]:
        n=p*q;phi=(p-1)*(q-1);e=next(e for e in range(2,phi) if math.gcd(e,phi)==1);d=pow(e,-1,phi)
        assert (e*d)%phi==1 and phi==sum(math.gcd(i,n)==1 for i in range(1,n+1))
        for m in range(n):assert pow(pow(m,e,n),d,n)==m
        rsa.append({'p':p,'q':q,'n':n,'e':e,'d':d,'allRepresentativesRoundTrip':n})
    assert pow(2,340,341)==1 and 341==11*31
    coprime=[x for x in range(1,561) if math.gcd(x,561)==1]
    assert len(coprime)==320 and all(pow(x,560,561)==1 for x in coprime) and pow(3,560,561)==375
    results=[]
    for lang in a.languages:
        p=ROOT/audit['versions'][lang]['path'];text=p.read_text(encoding='utf-8-sig');url=urls[lang]
        html=(a.site/url.removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
        parser=check.PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>')
        assert parser.canonical==url and parser.language==lang and parser.alternates==dict(urls,**{'x-default':urls['ja']}) and parser.options==urls
        assert check.cpp.rendering.expressions(strip(text))==tex
        body=check.cpp.rendering.ArticleText();body.feed(html);assert check.cpp.rendering.expressions(''.join(body.parts))==tex
        graphs=re.findall(r'^'+fence+r'mermaid\n(.*?)^'+fence,text,re.M|re.S);assert len(graphs)==2 and flow(graphs[0])==flow(graphs_ja[0]) and sequence(graphs[1])==sequence(graphs_ja[1])
        from html import unescape
        assert all(g.strip() in unescape(html) for g in graphs)
        assert not re.findall(r'^'+fence+r'(?!mermaid)[a-z]+\n',text,re.M)
        refs=set(re.findall(r'\]\((https://[^)]+)\)',text));internal={'https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/'+s+'/' for s in ['cpp-fast-prime-testing-miller-rabin','rsa-encryption-math-explained-for-beginners']}
        assert refs==internal|{'https://dlmf.nist.gov/27.2#E8','https://cacr.uwaterloo.ca/hac/about/chap4.pdf','https://www.rfc-editor.org/rfc/rfc8017.html'}
        assert all(u in html for u in refs) and all((a.site/u.removeprefix('https://kenji.blog/')/'index.html').is_file() for u in internal)
        assert text.count('\ndate: ')==1 and 'date: "2026-09-20T15:00:00+09:00"' in text and 'lastmod: 2026-10-29' in text
        assert 'slug: "fermats-little-theorem"' in text and 'image: "eyecatch.jpg"' in text and 'math: true' in text and 'mermaid: true' in text
        assert '"datePublished":"2026-09-20T15:00:00+09:00"' in html and '"dateModified":"2026-10-29' in html and 'katex' in html
        assert hashlib.sha256((FOLDER/'eyecatch.jpg').read_bytes()).hexdigest()==audit['imageSha256']
        results.append({'language':lang,'sha256':check.digest(p),'canonical':url,'texExpressions':sum(tex.values()),'allTeXPreserved':True,'diagramsExact':2,'diagramEdges':[5,5],'executableArticleCodeBlocks':0,'all14HreflangAnd13SidebarTargetsExact':True,'referencesAndMetadataExact':True,'passed':True})
    output={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'scope':'Selected versions only;HTML and mathematical source checks. Auxiliary Python arithmetic is executed once and shared,not misrepresented as executable article code or prose approval.','versions':results,'auxiliaryArithmetic':{'fermatAllIntegerFormCases':fermat_cases,'nonzeroResiduePermutationCases':permutations,'carmichaelCoprimeBases':320,'rsaCases':rsa,'rsaRepresentativesTotal':sum(x['n'] for x in rsa)},'publicationPending':True,'limitations':['AI,not human/native-language certification.','Finite auxiliary arithmetic,not exhaustive proof or a cryptographic audit.','Mermaid sources/HTML and TeX checked,no browser visual/KaTeX/Mermaid runtime certification.']}
    a.output.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'versions':len(results),'texEach':sum(tex.values()),'fermatCases':fermat_cases,'permutations':permutations,'rsaRepresentatives':sum(x['n'] for x in rsa)}))


if __name__=='__main__':main()
