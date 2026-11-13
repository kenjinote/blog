"""Read draft JA source/decoded HTML; finite mathematical checks, not translation approval."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from fractions import Fraction
from itertools import product
import hashlib,importlib.util,json,math,random,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
shared=module('eccshared',D/'verify_batch_033.py')
v=module('eccvalue',D/'ecc034_revised_code.py')
FENCE=chr(96)*3

def auxiliary():
    repetition=[]
    p=Fraction(1,100)
    for n in (3,5,7):
        direct=sum(p**sum(bits)*(1-p)**(n-sum(bits)) for bits in product((0,1),repeat=n) if sum(bits)>n//2)
        formula=sum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(n//2+1,n+1))
        assert direct==formula;repetition.append(dict(n=n,probability=str(direct),patterns=2**n))
    assert repetition[0]['probability']=='149/500000'
    entropy=-.1*math.log2(.1)-.9*math.log2(.9)
    assert abs(entropy-.4689955935892812)<1e-14
    limit=math.log(2);db=10*math.log10(limit)
    assert abs(db+1.5917453895486158)<1e-12
    efficiencies=[1, .5, .1, .01, .001]
    energies=[math.expm1(x*math.log(2))/x for x in efficiencies]
    assert all(x>limit for x in energies) and all(a>b for a,b in zip(energies,energies[1:]))
    assert Fraction(1,10**16)/Fraction(1,10**18)==100
    assert 16*(1+7)==2**7 and Fraction(3,15)==Fraction(1,5)
    # A 128-bit contiguous interval need not fit in 16 byte symbols.
    touched=[len({j//8 for j in range(offset,offset+128)}) for offset in range(8)]
    assert touched==[16]+[17]*7
    llr=0
    for sigma in (.25,.5,1,2):
        for y in (-3,-1,0,.1,1,3):
            logratio=(-(y-1)**2+(y+1)**2)/(2*sigma**2)
            assert math.isclose(logratio,2*y/sigma**2,abs_tol=1e-12);llr+=1
    # Independent carryless multiplication/reduction, not candidate gf_mul.
    def mul(a,b):
        value=0
        for j in range(8):
            if b&(1<<j):value^=a<<j
        for j in range(14,7,-1):
            if value&(1<<j):value^=0x11d<<(j-8)
        return value
    def power(a,e):
        r=1
        for _ in range(e):r=mul(r,a)
        return r
    def conv(a,b):
        r=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):r[i+j]^=mul(x,y)
        return r
    def evaluate(a,x):
        out=0
        for j,c in enumerate(a):out^=mul(c,power(x,j))
        return out
    assert len({power(2,i) for i in range(255)})==255 and power(2,255)==1
    rng=random.Random(340014);forney=0
    for nu in range(1,5):
        for _ in range(32):
            xs=rng.sample(range(1,256),nu);ys=[rng.randrange(1,256) for x in xs]
            locator=[1]
            for x in xs:locator=conv(locator,[1,x])
            syndromes=[]
            for j in range(1,2*nu+1):
                total=0
                for x,y in zip(xs,ys):total^=mul(y,power(x,j))
                syndromes.append(total)
            omega=conv(syndromes,locator)[:2*nu]
            derivative=[locator[j] if j%2 else 0 for j in range(1,len(locator))]
            for x,y in zip(xs,ys):
                inv=power(x,254)
                assert evaluate(locator,inv)==0
                den=evaluate(derivative,inv);assert den
                assert mul(evaluate(omega,inv),power(den,254))==y
                forney+=1
            for j in range(1,nu+1):
                out=syndromes[j+nu-1]
                for i in range(1,nu+1):out^=mul(locator[i],syndromes[j+nu-i-1])
                assert out==0
    for eps in (0,.1,.5,.9,1):
        bad=2*eps-eps*eps;good=eps*eps
        assert math.isclose((1-bad)+(1-good),2*(1-eps),abs_tol=1e-14)
    return dict(repetition=repetition,bscEntropyAtPointOne=entropy,bscCapacity=1-entropy,
        awgnWidebandLinearLimit=limit,awgnWidebandDbLimit=db,positiveEfficiencyBounds=energies,
        wattsToAttowatts=100,burstByteSymbolsByOffset=touched,bpskLlrCases=llr,
        primitiveElementOrder=255,multiErrorForneyMagnitudes=forney,multiErrorForneyPatterns=128,
        becPolarConservationCases=5,scope='Finite arithmetic/model checks;not all-input execution,hardware,full QR,LDPC/Polar implementations or performance measurements.')

def main():
    site=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
    audit=json.loads((D/'batch-034-source-audit.json').read_text(encoding='utf-8'))
    entry=audit['versions']['ja'];p=ROOT/entry['path'];text=p.read_text(encoding='utf-8')
    original=subprocess.run(['git','show',audit['baselineCommit']+':'+entry['path']],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
    assert hashlib.sha256(original.encode()).hexdigest()==entry['sha256']
    for key in ('date','slug','image','draft'):
        assert re.findall('^'+key+':.*$',text,re.M)==re.findall('^'+key+':.*$',original,re.M)
    assert shared.shared.taxonomy(text)==shared.shared.taxonomy(original)
    assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,9)))
    assert 'lastmod: "2026-11-13"' in text and 'mermaid: true' in text
    graphs=shared.shared.graphs(text);assert len(graphs)==4
    assert [len(re.findall(r'-->|---|-- "(?:Yes|No)" -->',g)) for g in graphs]==[10,7,9,5]
    code=re.search('^'+FENCE+r'python\n(.*?)^'+FENCE,text,re.M|re.S)[1]
    candidate=(D/'ecc034_revised_code.py').read_text(encoding='utf-8')
    assert code.rstrip()==candidate.rstrip()
    shown=re.search('^'+FENCE+r'text\n(.*?)^'+FENCE,text,re.M|re.S)[1]
    run=subprocess.run([sys.executable,'-c',code],capture_output=True,text=True,encoding='utf-8')
    assert run.returncode==0 and run.stdout==shown
    href=entry['canonical'];html=(site/href.removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
    article=shared.Article();article.feed(html)
    tex=shared.source_math(text)
    assert shared.shared.render.expressions(''.join(article.math))==tex
    assert all(g.strip() in shared.unescape(html) for g in graphs)
    assert code in article.codes and shown in article.codes
    refs=set(re.findall(r'\]\((https://[^)]+)\)',text));assert len(refs)==10 and refs<=set(article.links)
    nav=shared.shared.PageParser();nav.feed(html.split('</aside>',1)[0]+'</aside>')
    urls={lang:e['canonical'] for lang,e in audit['versions'].items()}
    assert nav.canonical==href and nav.language=='ja' and nav.alternates==dict(urls,**{'x-default':href}) and nav.options==urls
    assert '"datePublished":"'+entry['datePublished']+'"' in html and '"dateModified":"2026-11-13' in html
    assert len([row for row in article.rows if len(row)==4])==6
    for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
    doc=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),
        allPassed=True,sourcePath=entry['path'],sourceSha256=shared.shared.digest(p),
        originalSha256=entry['sha256'],sourceRead='Complete revised JA lines1–250,251–500,501–end; later small metadata/definition/reference patch read separately.',
        texExpressions=sum(tex.values()),diagrams=4,diagramEdges=[10,7,9,5],references=len(refs),
        executableCodeSha256=hashlib.sha256(code.rstrip().encode()).hexdigest(),
        candidateExact=True,articleCodeExecution=dict(exitCode=run.returncode,stdout=run.stdout,stderr=run.stderr,displayedOutputExact=True),
        exactSourceHtmlMath=True,exactGraphs=True,exactHtmlCodeAndOutput=True,
        titleDateNavigationAndAssetsPreserved=True,auxiliary=auxiliary(),
        reviewedTranslationsAdded=0,publicationPending=True,
        limitations=['Japanese working draft only;not translation approval or frozen source yet.',
        'Other 12 translations remain old; original EN has been read, other11 bodies unread.',
        'No browser/KaTeX/Mermaid runtime, full site, native-language review, hardware or benchmark certification.'])
    out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:doc[k] for k in ('allPassed','texExpressions','diagrams','references','reviewedTranslationsAdded')}))
if __name__=='__main__':main()
