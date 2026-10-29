"""Validate selected Rust stored-prime articles; never approves prose automatically."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,math,random,re,subprocess,tempfile,sys
from urllib.parse import urlsplit,unquote
from datetime import datetime,timezone,timedelta
ROOT=Path(__file__).resolve().parents[2]
FOLDER=ROOT/'content/post/Rustで素数を列挙する'
spec=importlib.util.spec_from_file_location('sieve_helpers',Path(__file__).with_name('verify_batch_020.py'));helpers=importlib.util.module_from_spec(spec);spec.loader.exec_module(helpers)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--languages',nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();assert not a.output.exists()
    audit=json.loads((ROOT/'docs/translation-review/batch-021-source-audit.json').read_text(encoding='utf-8'))
    sieve=json.loads((ROOT/'docs/translation-review/batch-020-source-audit.json').read_text(encoding='utf-8'))
    primes=[n for n in range(2,100001) if all(n%d for d in range(2,math.isqrt(n)+1))]
    rng=random.Random(21021);cases=set(range(2001));cases.update(rng.randrange(0,100001) for _ in range(128));cases.update([99999,100000])
    for p in [47,97,127,251,311]:cases.update([p*p-1,p*p,p*p+1])
    for p in range(11,17):cases.update([(1<<p)-1,1<<p,(1<<p)+1])
    cases=sorted(cases);sample=''.join(str(p)+'\n' for p in primes if p<=1000)
    ja=(FOLDER/'index.md').read_text(encoding='utf-8');codes_ja=re.findall(r'^```rust\n(.*?)^```',ja,re.M|re.S);assert len(codes_ja)==1
    result=[]
    for lang in a.languages:
        p=FOLDER/('index.md' if lang=='ja' else 'index.'+lang+'.md');text=p.read_text(encoding='utf-8-sig');codes=re.findall(r'^```rust\n(.*?)^```',text,re.M|re.S);assert codes==codes_ja
        assert len(re.findall(r'^## ',text,re.M))==4 and text.count('\ndate: ')==1
        assert 'date: 2022-09-09T07:08:49+09:00' in text and 'lastmod: 2026-10-29' in text
        assert 'image: "images/img.webp"' in text and (FOLDER/'images/img.webp').exists()
        assert 'slug: "'+audit['versions'][lang]['slug']+'"' in text
        target=sieve['versions'][lang]['canonical'];refs=set(re.findall(r'\]\((https://[^)]+)\)',text));assert refs=={'https://doc.rust-lang.org/std/vec/struct.Vec.html',target}
        source_math=helpers.rendering.expressions(re.sub(r'^```.*?^```[^\n]*','',text,flags=re.M|re.S));assert not source_math
        url=audit['versions'][lang]['canonical'];html=(a.site/unquote(urlsplit(url).path).lstrip('/')/'index.html').read_text(encoding='utf-8')
        parser=helpers.PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>');assert parser.canonical==url and parser.language==lang
        assert '"datePublished":"2022-09-09T07:08:49+09:00"' in html and '"dateModified":"2026-10-29' in html
        rust=helpers.RustCode();rust.feed(html);assert [b.strip() for b in rust.blocks]==[codes[0].strip()]
        assert target in html and 'primes_up_to' in html and '168' in html and '997' in html
        body=helpers.rendering.ArticleText();body.feed(html);assert not helpers.rendering.expressions(''.join(body.parts))
        code=codes[0];helper=code[:code.index('fn main()')]
        helper+='\nfn main() { const PRIMES: &[usize] = &['+','.join(map(str,primes))+']; const CASES: &[usize] = &['+','.join(map(str,cases))+'];\n'
        helper+='for &n in CASES { let end=PRIMES.partition_point(|&p|p<=n);assert_eq!(primes_up_to(n).as_slice(),&PRIMES[..end],"n={}",n); } println!("passed {} bounds",CASES.len()); }\n'
        work=Path(tempfile.mkdtemp(prefix='kenji-rust-primes-'+lang+'-'));runs=[]
        for mode,flags in [('debug-checked',['-C','opt-level=0','-C','overflow-checks=yes','-C','debug-assertions=yes']),('optimized-checked',['-O','-C','overflow-checks=yes'])]:
            assert helpers.compile_run(code,work,'article-'+mode,flags)==sample
            assert helpers.compile_run(helper,work,'harness-'+mode,flags)==f'passed {len(cases)} bounds\n'
            runs.append({'mode':mode,'samplePrimes':168,'fullSampleOutputExact':True,'fullVectorsAgainstIndependentTrialDivision':len(cases)})
        h=hashlib.sha256(text.replace('\r\n','\n').encode()).hexdigest()
        result.append({'language':lang,'sha256':h,'canonical':url,'sourceMathExpressions':0,'rustBlocks':1,'htmlCodeExact':True,'sieveTarget':target,'executions':runs})
        print(json.dumps({'language':lang,'passed':True,'boundsPerMode':len(cases)}),flush=True)
    a.output.write_text(json.dumps({'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'compiler':subprocess.check_output(['rustc','--version','--verbose'],text=True),'independentReference':'Python integer trial division through100000,fullvector equality not hashes or a mirrored stored-prime algorithm.','versions':result,'limitations':['Finite bounds<=100000 withRust1.90Windows64bit,not everyusize or target.','No huge upper-bound run,performance benchmark,visualbrowser/native-language or cryptographic audit.','Arithmetic bounds justified separately; no attempt to enumerateusizeMAX.','Prose reading is separate; script does not record or approve translations.'],'publicationPending':True},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
