"""Selected source/HTML and finite English examples; semantic reading recorded separately."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from itertools import permutations
from collections import Counter
from html import unescape
import hashlib,importlib.util,json,math,random,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review';FENCE=chr(96)*3
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
base=module('eccjabase',D/'verify_batch_034_ja.py');shared=base.shared
v=base.v

def english_auxiliary():
    bound_cases=0
    for n in range(1,32,2):
        for percent in range(1,50):
            p=percent/100
            prob=math.fsum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(n//2+1,n+1))
            div=.5*math.log(.5/p)+.5*math.log(.5/(1-p))
            assert prob<=math.exp(-n*div)+1e-14;bound_cases+=1
    assert math.isclose(float(2**500)/10**150,3.273390607896142,rel_tol=1e-14)
    assert 2*128%256==16*16%256==0
    assert math.isclose(100*(1-30000/(10000*5000)),99.94,abs_tol=1e-12)
    assert v.gf_pow(2,8)==0x1d
    msg=[1,0,1,1];word=v.hamming_encode(msg);assert word==[1,0,1,1,0,1,0]
    received=word.copy();received[2]^=1
    syndrome=[sum(v.H[r][j]*received[j] for j in range(7))%2 for r in range(3)]
    assert syndrome==[0,1,1] and v.hamming_decode(received)==msg
    payload=list(b'VOYAGER-1');pts=[v.gf_pow(2,i) for i in range(15)];cw=v.rs_encode(payload,pts)
    original=json.loads((D/'batch-034-original-code-probe.json').read_text(encoding='utf-8'))
    old=next(row for row in original['results'] if row['language']=='en')
    observed=json.loads(re.search(r'GF\(2\^8\) RS Codeword\s*:\s*(\[[^\n]+)',old['actualStdout'])[1])
    assert cw==observed and len(set(pts))==15
    old_patterns=[]
    for count in range(4):
        r=cw.copy()
        for index,magnitude in list(zip([1,6,13],[255,165,60]))[:count]:r[index]^=magnitude
        got=v.rs_decode(r,pts,9,3);assert got==payload
        old_patterns.append(dict(errors=count,received=r,recovered=got))
    # Separate carryless arithmetic and permutation determinant, not solver internals.
    def mul(a,b):
        z=0
        for j in range(8):
            if b&(1<<j):z^=a<<j
        for j in range(14,7,-1):
            if z&(1<<j):z^=0x11d<<(j-8)
        return z
    def power(x,n):
        r=1
        for _ in range(n):r=mul(r,x)
        return r
    rng=random.Random(340015);determinants=0
    for k in range(1,6):
        for _ in range(20):
            xs=rng.sample(range(256),k)
            a=[[power(x,j) for j in range(k)] for x in xs];det=0
            for perm in permutations(range(k)):
                term=1
                for i,j in enumerate(perm):term=mul(term,a[i][j])
                det^=term # in characteristic two both permutation signs equal one
            rhs=1
            for i in range(k):
                for j in range(i+1,k):rhs=mul(rhs,xs[j]^xs[i])
            assert det==rhs and det!=0;determinants+=1
    return dict(chernoffModelCases=bound_cases,exponentialCodebookExample=True,regularLdpcZerosPercent=99.94,
        hammingMessage=msg,hammingCodeword=word,hammingSyndrome=syndrome,
        primitiveEighthPower=0x1d,originalEnglishEvaluationPoints=pts,originalEnglishActualCodeword=cw,
        oldEnglishZeroThroughThreeErrorPatterns=old_patterns,independentVandermondeDeterminants=determinants,
        scope='Finite auxiliary arithmetic and decoder cases, not hardware measurements, asymptotic theorem proofs or full QR/LDPC/Polar implementations.')

def prose_fragments(text,html):
    text=text.split('---',2)[2];text=shared.shared.strip(text)
    text=re.sub(shared.shared.render.PATTERN,'@MATHCUT@',text)
    text=re.sub(r'<[^>]+>','',text)
    text=re.sub(r'\[([^\]]+)\]\(https://[^)]+\)',r'\1',text)
    text=text.replace(chr(96),'').replace('**','')
    # Hugo smart punctuation changes prose apostrophes only. TeX/code checks
    # above remain exact and do not use this prose-only normalization.
    def norm(s):return re.sub(r'\s+','',unescape(s).replace('\u2019',chr(39)).replace('\u2018',chr(39)))
    a=shared.Article();a.feed(html);actual=norm(''.join(a.all));pieces=[]
    for line in text.splitlines():
        line=re.sub(r'^\s*(?:#{1,6}|[-*>]|\d+\.)\s*','',line)
        for part in re.split(r'@MATHCUT@|\|',line):
            part=norm(part)
            if len(part)>=12 and not re.fullmatch(r'[:\-]+',part):pieces.append(part)
    missing=[piece for piece in pieces if piece not in actual];assert not missing,missing
    return len(pieces)

def main():
    site=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
    audit=json.loads((D/'batch-034-source-audit.json').read_text(encoding='utf-8'))
    source=ROOT/audit['versions']['ja']['path'];ja=source.read_text(encoding='utf-8')
    assert shared.shared.digest(source)=='371d428b34995ba3dcbb39f9aa0e35db27a6bdda9a92840815fc1c9b690041da'
    code=(D/'ecc034_revised_code.py').read_text(encoding='utf-8')
    core=[m[1].strip() for m in re.finditer(r'\$\$(.*?)\$\$',ja,re.S)];assert len(core)==47
    refs=set(re.findall(r'\]\((https://[^)]+)\)',ja));assert len(refs)==10
    urls={}
    for lang,entry in audit['versions'].items():
        text=(ROOT/entry['path']).read_text(encoding='utf-8')
        slug=json.loads(re.search(r'^slug: (.*)$',text,re.M)[1])
        urls[lang]='https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/'+slug+'/'
    translated={k:k.replace('だが同時に','but simultaneously').replace('2元符号では ','for binary codes: ').replace(' の位',' place') for k in core}
    graphs=shared.shared.graphs(ja);versions=[]
    for lang in ('ja','en'):
        entry=audit['versions'][lang];p=ROOT/entry['path'];text=p.read_text(encoding='utf-8')
        original=subprocess.run(['git','show',audit['baselineCommit']+':'+entry['path']],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
        assert hashlib.sha256(original.encode()).hexdigest()==entry['sha256']
        for key in ('date','slug','image','draft'):
            assert re.findall('^'+key+':.*$',text,re.M)==re.findall('^'+key+':.*$',original,re.M)
        assert shared.shared.taxonomy(text)==shared.shared.taxonomy(original)
        assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,9)))
        assert 'lastmod: "2026-11-13"' in text and 'mermaid: true' in text
        assert set(re.findall(r'\]\((https://[^)]+)\)',text))==refs
        display=[m[1].strip() for m in re.finditer(r'\$\$(.*?)\$\$',text,re.S)]
        expected=core if lang=='ja' else list(translated.values())
        assert not Counter(expected)-Counter(display)
        assert len(display)==(47 if lang=='ja' else 55)
        actual_graphs=shared.shared.graphs(text);assert len(actual_graphs)==4
        shape=lambda g:re.sub(r'"[^"\n]*"','""',g)
        assert list(map(shape,actual_graphs))==list(map(shape,graphs))
        actual_code=re.search('^'+FENCE+r'python\n(.*?)^'+FENCE,text,re.M|re.S)[1]
        shown=re.search('^'+FENCE+r'text\n(.*?)^'+FENCE,text,re.M|re.S)[1]
        assert actual_code.rstrip()==code.rstrip()
        run=subprocess.run([sys.executable,'-c',actual_code],capture_output=True,text=True,encoding='utf-8')
        assert run.returncode==0 and run.stdout==shown
        html=(site/urls[lang].removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
        article=shared.Article();article.feed(html);tex=shared.source_math(text)
        assert shared.shared.render.expressions(''.join(article.math))==tex
        assert all(g.strip() in unescape(html) for g in actual_graphs)
        assert actual_code in article.codes and shown in article.codes
        assert refs<=set(article.links) and len([row for row in article.rows if len(row)==4])==6
        nav=shared.shared.PageParser();nav.feed(html.split('</aside>',1)[0]+'</aside>')
        assert nav.canonical==urls[lang] and nav.language==lang and nav.alternates==dict(urls,**{'x-default':urls['ja']}) and nav.options==urls
        header=text.split('---',2)[1];published=json.loads(re.search(r'^date: (.*)$',header,re.M)[1])
        assert '"datePublished":"'+published+'"' in html and '"dateModified":"2026-11-13' in html
        assert json.loads(re.search(r'^title: (.*)$',header,re.M)[1]) in unescape(html)
        if lang=='en':
            assert not re.search(r'[\u3040-\u30ff\u4e00-\u9fff]',text)
            assert all(t in ''.join(article.all) for t in ['99.94%','[1,0,1,1]','[0,1,1]','[1,6,13]','1..15','0x1D'])
        for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
        versions.append(dict(language=lang,path=entry['path'],sha256=shared.shared.digest(p),
            sourceSha256=shared.shared.digest(source),originalSha256=entry['sha256'],texExpressions=sum(tex.values()),
            displayMath=len(display),coreDisplayBlocks=47,diagrams=4,diagramEdges=[10,7,9,5],references=10,
            articleExecutablePrograms=1,executableCodeSha256=hashlib.sha256(actual_code.rstrip().encode()).hexdigest(),
            programExitCode=run.returncode,stdout=run.stdout,stderr=run.stderr,displayedOutputExact=True,
            codeAndOutputHtmlExact=True,mathHtmlExact=True,proseFragmentsPreserved=prose_fragments(text,html),
            datesTaxonomyImageAndNavigationPassed=True,passed=True))
    doc=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=True,versions=versions,
        auxiliaryChecks=english_auxiliary(),priorCandidateFiniteEvidence='docs/translation-review/batch-034-candidate-code-validation.json',
        priorJapaneseArithmeticEvidence='docs/translation-review/batch-034-ja-validation-r4.json',
        reviewedTranslationsAdded=0,publicationPending=True,
        limitations=['Static source/HTML and finite arithmetic; full original/revised semantic reading is recorded separately.',
        'Only JA and EN covered; other11translation bodies remain unread.',
        'No browser/KaTeX/Mermaid execution, native-language, full-site, real hardware, benchmark or complete QR/LDPC/Polar implementation certification.'])
    out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(allPassed=True,versions=[{k:v[k] for k in ('language','texExpressions','displayMath','proseFragmentsPreserved')} for v in versions],reviewedTranslationsAdded=0)))
if __name__=='__main__':main()
