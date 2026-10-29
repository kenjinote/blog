"""Validate explicitly selected Fermat article versions; never approves or records prose."""
from pathlib import Path
import argparse,json,re,hashlib,importlib.util,random,subprocess,tempfile,contextlib,io,math,sys
from datetime import datetime,timezone,timedelta
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[2];FOLDER=ROOT/'content/post/フェルマーの小定理と暗号化';SLUG='fermats-little-theorem-cryptography-implementation'
spec=importlib.util.spec_from_file_location('cpp_helpers',Path(__file__).with_name('verify_batch_018.py'));cpp=importlib.util.module_from_spec(spec);spec.loader.exec_module(cpp)
sys.path.insert(0,str(ROOT/'scripts'));from check_multilingual import PageParser

def digest(p):return hashlib.sha256(p.read_text(encoding='utf-8-sig').replace('\r\n','\n').encode()).hexdigest()
class CodeParser(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.active=False;self.blocks=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='code':
            lang=a.get('data-lang')
            if not lang:
                lang=next((s.removeprefix('language-') for s in a.get('class','').split() if s.startswith('language-')),None)
            if lang in ('cpp','python'):self.active=True;self.blocks.append([lang,''])
    def handle_data(self,data):
        if self.active:self.blocks[-1][1]+=data
    def handle_endtag(self,tag):
        if tag=='code':self.active=False
def graph_edges(g):return re.findall(r'^\s*(\w+).*?--.*?>\s*(\w+)',g,re.M)
def sequence_edges(g):return re.findall(r'^\s*(Alice|Bob)->>(Alice|Bob):',g,re.M)
def expected_fermat(n,bases):
    if n<2:return False
    if n<=3:return True
    if n%2==0:return False
    return all(pow(a,n-1,n)==1 for a in bases)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--languages',nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();assert not a.output.exists()
    ja=(FOLDER/'index.md').read_text(encoding='utf-8');fence=chr(96)*3
    codes_ja=re.findall(r'^'+fence+r'(cpp|python)\n(.*?)^'+fence,ja,re.M|re.S);assert [x[0] for x in codes_ja]==['cpp','python','python']
    graphs_ja=re.findall(r'^'+fence+r'mermaid\n(.*?)^'+fence,ja,re.M|re.S);assert [len(graph_edges(graphs_ja[0])),len(sequence_edges(graphs_ja[1]))]==[13,6]
    external={'https://dlmf.nist.gov/27.2#E8','https://cacr.uwaterloo.ca/hac/about/chap4.pdf','https://docs.openssl.org/master/man3/BN_generate_prime/','https://www.rfc-editor.org/rfc/rfc8017.html','https://docs.python.org/3/library/random.html','https://gcc.gnu.org/onlinedocs/gcc/_005f_005fint128.html'}
    nums=list(range(2001))+[341,561,1105,1729,104729,1000000007,2**63-1,18446744073709551557,2**64-1]
    rng=random.Random(22029);nums+= [rng.getrandbits(64) for _ in range(64)]
    commands=[];expected=[];kinds={'M':0,'P':0,'F':0,'invalid':0}
    def add(command,result,kind):commands.append(command);expected.append(str(result));kinds[kind]+=1
    limits=[0,1,2,3,2**32-1,2**63-1,2**63,2**64-2,2**64-1]
    for x in limits:
        for y in limits:
            for m in limits[1:]:
                add(f'M {x} {y} {m}',x*y%m,'M');add(f'P {x} {y} {m}',pow(x,y,m),'P')
    for _ in range(2048):
        x,y,m=rng.getrandbits(64),rng.getrandbits(64),rng.randrange(1,2**64)
        add(f'M {x} {y} {m}',x*y%m,'M');add(f'P {x} {y} {m}',pow(x,y,m),'P')
    for n in nums:add(f'F {n} 2 2 3',int(expected_fermat(n,[2,3])),'F')
    for n,bases in [(561,[2]),(561,[3]),(1105,[2,3]),(1105,[5]),(5,[2,3]),(7,[2,5])]:add('F '+str(n)+' '+str(len(bases))+' '+' '.join(map(str,bases)),int(expected_fermat(n,bases)),'F')
    for command in ['M 2 3 0','P 2 3 0','F 9 0','F 2 0','F 5 1 0','F 5 1 1','F 5 1 4','F 9 2 3 8']:add(command,'ERROR','invalid')
    harness=r'''
int main() {
    char mode;
    while (std::cin >> mode) {
        try {
            if (mode == 'F') {
                u64 n; unsigned count; std::cin >> n >> count;
                std::vector<u64> bases(count);
                for (u64& a : bases) std::cin >> a;
                std::cout << fermat_passes(n, bases) << '\n';
            } else {
                u64 a,b,m; std::cin >> a >> b >> m;
                std::cout << (mode == 'M' ? mul_mod(a,b,m) : power_mod(a,b,m)) << '\n';
            }
        } catch (const std::invalid_argument&) { std::cout << "ERROR\n"; }
    }
}'''
    result=[]
    for lang in a.languages:
        p=FOLDER/('index.md' if lang=='ja' else 'index.'+lang+'.md');text=p.read_text(encoding='utf-8-sig');codes=re.findall(r'^'+fence+r'(cpp|python)\n(.*?)^'+fence,text,re.M|re.S);assert codes==codes_ja
        graphs=re.findall(r'^'+fence+r'mermaid\n(.*?)^'+fence,text,re.M|re.S);assert len(graphs)==2 and graph_edges(graphs[0])==graph_edges(graphs_ja[0]) and sequence_edges(graphs[1])==sequence_edges(graphs_ja[1])
        assert len(re.findall(r'^## [1-9]\. ',text,re.M))==9
        assert 'date: "2026-09-11T22:00:00+09:00"' in text and 'lastmod: 2026-10-29' in text
        assert 'slug: "'+SLUG+'"' in text and 'image: "img/eyecatch.jpg"' in text and (FOLDER/'img/eyecatch.jpg').exists()
        refs=set(re.findall(r'\]\((https://[^)]+)\)',text));internal={'https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/'+s+'/' for s in ['rsa-encryption-math-explained-for-beginners','cpp-fast-prime-testing-miller-rabin']};assert refs==external|internal
        url='https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/'+SLUG+'/'
        html=(a.site/url.removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8');parser=PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>');assert parser.canonical==url and parser.language==lang
        assert all(u in html for u in refs) and all((a.site/u.removeprefix('https://kenji.blog/')/'index.html').is_file() for u in internal)
        assert '"datePublished":"2026-09-11T22:00:00+09:00"' in html and '"dateModified":"2026-10-29' in html
        prose=re.sub(r'^'+fence+r'.*?^'+fence+r'[^\n]*','',text,flags=re.M|re.S);math_expected=cpp.rendering.expressions(prose)
        ja_prose=re.sub(r'^'+fence+r'.*?^'+fence+r'[^\n]*','',ja,flags=re.M|re.S)
        assert math_expected==cpp.rendering.expressions(ja_prose), 'Source/translation TeX differs'
        body=cpp.rendering.ArticleText();body.feed(html);assert cpp.rendering.expressions(''.join(body.parts))==math_expected
        assert 'katex' in html and 'mermaid' in html
        parsed=CodeParser();parsed.feed(html);assert [(l,c.strip()) for l,c in parsed.blocks]==[(l,c.strip()) for l,c in codes]
        # Complete Python programs, then direct function checks against independent arithmetic.
        stdout=[];spaces=[]
        for _,code in codes[1:]:
            ns={'__name__':'__main__'};capture=io.StringIO()
            with contextlib.redirect_stdout(capture):exec(compile(code,str(p),'exec'),ns)
            stdout.append(capture.getvalue());spaces.append(ns)
        assert stdout[0]=='1000000007 passes bases 2,3: True\n1105 passes bases 2,3: True\n1105 passes base 5: False\n'
        assert stdout[1]=='Public key (n, e): (3233, 17)\nPrivate key (n, d): (3233, 2753)\n65 -> 2790 -> 65\nAll 3233 representatives round-trip.\n'
        f=spaces[0]['fermat_passes'];r=spaces[1]
        for n in nums:assert f(n,[2,3])==expected_fermat(n,[2,3])
        for n,bases in [(561,[2]),(561,[3]),(1105,[2,3]),(1105,[5])]:assert f(n,bases)==expected_fermat(n,bases)
        bad_f=[(9,[],ValueError),(2,[],ValueError),(5,[0],ValueError),(5,[1],ValueError),(5,[4],ValueError),(9,[3,8],ValueError),(5.0,[2],TypeError),(True,[2],TypeError),(5,[True],TypeError),(5,[2.0],TypeError),(5,None,TypeError)]
        for n,bases,error in bad_f:
            try:f(n,bases)
            except error:pass
            else:raise AssertionError('Invalid Fermat input accepted')
        inverse_cases=0
        for m in range(2,101):
            for x in range(-50,51):
                g,s,t=r['extended_gcd'](x,m);assert g==math.gcd(x,m) and x*s+m*t==g
                if g==1:assert r['mod_inverse'](x,m)==pow(x,-1,m)
                else:
                    try:r['mod_inverse'](x,m)
                    except ValueError:pass
                    else:raise AssertionError('Noninvertible input accepted')
                inverse_cases+=1
        for m in range(3233):
            c=r['rsa_primitive'](m,17,3233);assert c==pow(m,17,3233) and r['rsa_primitive'](c,2753,3233)==m
        bad_r=[(-1,17,3233,ValueError),(3233,17,3233,ValueError),(65,0,3233,ValueError),(65,-1,3233,ValueError),(0,1,0,ValueError),(0,1,1,ValueError),(True,17,3233,TypeError),(65,17.0,3233,TypeError),(65,17,3233.0,TypeError)]
        for value,e,m,error in bad_r:
            try:r['rsa_primitive'](value,e,m)
            except error:pass
            else:raise AssertionError('Invalid representative/exponent/modulus accepted')
        inverse_invalid=[(1,0,ValueError),(1,1,ValueError),(1,-3,ValueError),(True,5,TypeError),(1,5.0,TypeError)]
        for x,m,error in inverse_invalid:
            try:r['mod_inverse'](x,m)
            except error:pass
            else:raise AssertionError('Invalid inverse input accepted')
        tmp=Path(tempfile.mkdtemp(prefix='kenji-fermat-'+lang+'-'));builds=[]
        for name,flags in [('optimized',['-O2','-Werror','-pedantic-errors']),('ubsan',['-O1','-Werror','-pedantic-errors','-fsanitize=undefined','-fno-sanitize-recover=undefined'])]:
            full=cpp.compile_code(codes[0][1],tmp,lang+'-main-'+name,flags)
            assert cpp.execute(full)==['1000000007 passes bases 2,3: 1','1105 passes bases 2,3: 1','1105 passes base 5: 0']
            driver=cpp.compile_code(codes[0][1].split('int main()')[0]+harness,tmp,lang+'-driver-'+name,flags)
            actual=cpp.execute(driver,'\n'.join(commands)+'\n');assert actual==expected,(lang,name,next(((i,x,y) for i,(x,y) in enumerate(zip(actual,expected)) if x!=y),'length'))
            builds.append({'mode':name,'cases':len(commands),'kindCounts':kinds,'completeProgramOutputExact':True,'allArithmeticAndFermatCasesExact':True})
        result.append({'language':lang,'sha256':digest(p),'canonical':url,'texExpressions':sum(math_expected.values()),'allTexPreserved':True,'diagramEdges':[13,6],'codeBlocks':3,'cppBuilds':builds,'pythonCompleteProgramsExact':2,'pythonFermatCases':len(nums)+4,'pythonInvalidFermatCases':len(bad_f),'pythonExtendedGcdAndInverseCases':inverse_cases,'pythonInvalidInverseCases':len(inverse_invalid),'rsaRepresentativesRoundTrip':3233,'pythonInvalidRsaCases':len(bad_r),'referencesExact':True,'passed':True})
        print(json.dumps({'language':lang,'passed':True,'cppCasesPerMode':len(commands),'texExpressions':sum(math_expected.values())}),flush=True)
    a.output.write_text(json.dumps({'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'compiler':'WSL GCC13.3/C++17,Python'+sys.version.split()[0],'scope':'Selected versions only. Exact finite arithmetic references use Python integers/pow/gcd,not a mirrored C++ multiplication implementation. No prose approval or review-date writes.','versions':result,'limitations':['Finite arithmetic cases,not exhaustive uint64 proof.','No performance,constant-time,production-key-generation,cryptographic-library or native-language certification.','Math/diagram source and generated HTML checked;no browservisual/KaTeX or Mermaid runtime rendering certification.'],'publicationPending':True},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
