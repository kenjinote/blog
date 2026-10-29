"""Compile selected reviewed sieve versions and compare full vectors to trial division."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,math,random,re,subprocess,tempfile,sys
from urllib.parse import urlsplit,unquote
from html.parser import HTMLParser
from datetime import datetime,timezone,timedelta
ROOT=Path(__file__).resolve().parents[2]
FOLDER=ROOT/'content/post/エラトステネスの篩を使って1000以下の素数を列挙する方法'
sys.path.insert(0,str(ROOT/'scripts'));from check_multilingual import PageParser
spec=importlib.util.spec_from_file_location('rendering',Path(__file__).with_name('verify_batch_013_rendering.py'));rendering=importlib.util.module_from_spec(spec);spec.loader.exec_module(rendering)

class RustCode(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.active=False;self.blocks=[];self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='code' and ('language-rust' in a.get('class','').split() or a.get('data-lang')=='rust'):self.active=True;self.blocks.append('')
        if tag=='img':self.images.append(a)
    def handle_data(self,data):
        if self.active:self.blocks[-1]+=data
    def handle_endtag(self,tag):
        if tag=='code':self.active=False

def digest(p):return hashlib.sha256(p.read_text(encoding='utf-8-sig').replace('\r\n','\n').encode()).hexdigest()

def compile_run(code,work,name,flags):
    source=work/(name+'.rs');source.write_text(code,encoding='utf-8');exe=work/(name+'.exe')
    c=subprocess.run(['rustc','--edition=2021','-D','warnings',*flags,str(source),'-o',str(exe)],capture_output=True,text=True,encoding='utf-8',timeout=90)
    assert c.returncode==0 and not c.stderr,c.stderr
    r=subprocess.run([str(exe)],capture_output=True,text=True,encoding='utf-8',timeout=90)
    assert r.returncode==0 and not r.stderr,(r.returncode,r.stderr)
    return r.stdout

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--languages',nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();assert not a.output.exists()
    audit=json.loads((ROOT/'docs/translation-review/batch-020-source-audit.json').read_text(encoding='utf-8'))
    refs={'https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif','https://creativecommons.org/licenses/by-sa/3.0/','https://introcs.cs.princeton.edu/java/41analysis/','https://doc.rust-lang.org/reference/types/boolean.html','https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees'}
    primes=[n for n in range(2,100001) if all(n%d for d in range(2,math.isqrt(n)+1))]
    rng=random.Random(20020);cases=set(range(2001));cases.update(rng.randrange(0,100001) for _ in range(128));cases.update([99999,100000])
    for p in [47,97,127,251,311]:cases.update([p*p-1,p*p,p*p+1])
    for p in range(11,17):cases.update([(1<<p)-1,1<<p,(1<<p)+1])
    cases=sorted(cases);expected_sample=''.join(str(p)+'\n' for p in primes if p<=1000)
    ja=(FOLDER/'index.md').read_text(encoding='utf-8');ja_codes=re.findall(r'^```rust\n(.*?)^```',ja,re.M|re.S);assert len(ja_codes)==2
    expected_math=rendering.expressions(re.sub(r'^```.*?^```[^\n]*','',ja,flags=re.M|re.S));assert sum(expected_math.values())==8
    assert expected_math['p^2'+chr(92)+'le n']==1 and expected_math['2'+chr(92)+'le k<p']==1 and expected_math['O(n'+chr(92)+'log'+chr(92)+'log n)']==1
    gif=(FOLDER/'Animation_Sieb_des_Eratosthenes.gif').read_bytes();assert hashlib.sha256(gif).hexdigest()==audit['gif']['sha256']
    assert audit['gif']['windowsTlsVerifiedFetch']['exactLocalBytesMatch']
    results=[]
    for lang in a.languages:
        p=FOLDER/('index.md' if lang=='ja' else 'index.'+lang+'.md');text=p.read_text(encoding='utf-8-sig')
        codes=re.findall(r'^```rust\n(.*?)^```',text,re.M|re.S);assert codes==ja_codes
        assert text.count('\ndate: ')==1 and 'date: 2023-04-09T12:54:24+09:00' in text and 'lastmod: 2026-10-29' in text
        assert 'math: true' in text and 'image: "img.webp"' in text and (FOLDER/'img.webp').exists()
        assert len(re.findall(r'^## ',text,re.M))==4
        assert 'slug: "'+audit['versions'][lang]['slug']+'"' in text
        actual_refs=set(re.findall(r'\]\((https://[^)]+)\)',text));assert actual_refs==refs
        prose=re.sub(r'^```.*?^```[^\n]*','',text,flags=re.M|re.S)
        assert '`None`' in prose and '`expect`' in prose
        alt=re.findall(r'!\[([^\]]+)\]\(Animation_Sieb_des_Eratosthenes.gif\)',text);assert len(alt)==1 and alt[0]
        url=audit['versions'][lang]['canonical'];html=(a.site/unquote(urlsplit(url).path).lstrip('/')/'index.html').read_text(encoding='utf-8')
        page=PageParser();page.feed(html.split('</aside>',1)[0]+'</aside>');assert page.canonical==url and page.language==lang
        assert '"datePublished":"2023-04-09T12:54:24+09:00"' in html and '"dateModified":"2026-10-29' in html
        parsed=RustCode();parsed.feed(html);assert [s.strip() for s in parsed.blocks]==[s.strip() for s in codes]
        images=[i for i in parsed.images if 'Animation_Sieb_des_Eratosthenes' in i.get('src','')];assert len(images)==1 and images[0].get('alt')==alt[0]
        body=rendering.ArticleText();body.feed(html);md_math=rendering.expressions(re.sub(r'^```.*?^```[^\n]*','',text,flags=re.M|re.S));assert md_math==expected_math and rendering.expressions(''.join(body.parts))==md_math
        work=Path(tempfile.mkdtemp(prefix='kenji-sieve-'+lang+'-'));runs=[]
        for block,(code,fn) in enumerate(zip(codes,['sieve','sieve_odd']),1):
            helper=code[:code.index('fn main()')]
            helper+='\nfn main() {\n const PRIMES: &[usize] = &['+','.join(map(str,primes))+'];\n const CASES: &[usize] = &['+','.join(map(str,cases))+'];\n'
            helper+=' for &n in CASES { let end=PRIMES.partition_point(|&p| p<=n); assert_eq!('+fn+'(n).as_slice(), &PRIMES[..end], "n={}",n); }\n'
            helper+=' let hook=std::panic::take_hook(); std::panic::set_hook(Box::new(|_| {})); assert!(std::panic::catch_unwind(|| '+fn+'(usize::MAX)).is_err()); std::panic::set_hook(hook);\n'
            helper+=' println!("passed {} bounds and checked_add overflow",CASES.len());\n}\n'
            for mode,flags in [('debug-checked',['-C','opt-level=0','-C','overflow-checks=yes','-C','debug-assertions=yes']),('optimized-checked',['-O','-C','overflow-checks=yes'])]:
                sample=compile_run(code,work,f'block{block}-{mode}',flags);assert sample==expected_sample
                harness=compile_run(helper,work,f'harness{block}-{mode}',flags);assert harness==f'passed {len(cases)} bounds and checked_add overflow\n'
                runs.append({'block':block,'mode':mode,'samplePrimes':168,'sampleOutputExact':True,'fullVectorBoundsComparedToIndependentTrialDivision':len(cases),'usizeMaxCheckedAddPanic':True})
        results.append({'language':lang,'sha256':digest(p),'canonical':url,'mathExpressions':8,'rustCodeBlocks':2,'htmlCodeExact':True,'imageAltPreserved':True,'gifBytesUnchanged':True,'externalTargets':sorted(refs),'executions':runs})
        print(json.dumps({'language':lang,'passed':True,'boundsPerBlockPerMode':len(cases),'texExpressions':8}),flush=True)
    a.output.write_text(json.dumps({'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'compiler':subprocess.check_output(['rustc','--version','--verbose'],text=True),'independentReference':'Python integer trial division through100000, embedded full prime vector, exact equality per bound; not a mirrored sieve.','versions':results,'limitations':['Finite bounds<=100000 under Rust1.90 Windows64bit; not every usize or target.','No speed benchmark, huge memory-allocation test, full animation visual/browser/KaTeX audit or native-speaker certification.','usizeMAX uses catch_unwind with temporary silent panic hook to verify explicit checked_add rejection; no huge allocation attempted.','Prose review is recorded separately; this script never approves a translation.'],'publicationPending':True},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
