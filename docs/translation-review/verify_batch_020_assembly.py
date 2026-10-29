"""Join preserved Rust executions to current full-version HTML; no prose approval."""
from pathlib import Path
import argparse,json,re,hashlib,importlib.util
from urllib.parse import urlsplit,unquote
from datetime import datetime,timezone,timedelta
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('sieve_checks',Path(__file__).with_name('verify_batch_020.py'));check=importlib.util.module_from_spec(spec);spec.loader.exec_module(check)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();assert not a.output.exists()
    audit=json.loads((ROOT/'docs/translation-review/batch-020-source-audit.json').read_text(encoding='utf-8'))
    proofs={}
    for name in ['ja-en-cn-tw','es-ko','pt-fr','de-id','hi-ru-ar']:
        p=ROOT/('docs/translation-review/batch-020-'+name+'-validation.json');x=json.loads(p.read_text(encoding='utf-8'))
        for v in x['versions']:assert v['language'] not in proofs;proofs[v['language']]=(p,v)
    assert set(proofs)==set(audit['versions']) and len(proofs)==13
    expected={l:v['canonical'] for l,v in audit['versions'].items()}
    codes_ja=re.findall(r'^```rust\n(.*?)^```',(check.FOLDER/'index.md').read_text(encoding='utf-8'),re.M|re.S)
    math_ja=check.rendering.expressions(re.sub(r'^```.*?^```[^\n]*','',(check.FOLDER/'index.md').read_text(encoding='utf-8'),flags=re.M|re.S))
    result=[]
    for lang,(p,v) in proofs.items():
        source=ROOT/audit['versions'][lang]['path'];text=source.read_text(encoding='utf-8-sig');assert check.digest(source)==v['sha256']
        url=expected[lang];html=(a.site/unquote(urlsplit(url).path).lstrip('/')/'index.html').read_text(encoding='utf-8')
        parser=check.PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>');assert parser.canonical==url and parser.language==lang
        assert parser.alternates==dict(expected,**{'x-default':expected['ja']}) and parser.options==expected
        rust=check.RustCode();rust.feed(html);codes=re.findall(r'^```rust\n(.*?)^```',text,re.M|re.S)
        assert codes==codes_ja and [s.strip() for s in rust.blocks]==[s.strip() for s in codes]
        math=check.rendering.expressions(re.sub(r'^```.*?^```[^\n]*','',text,flags=re.M|re.S));assert math==math_ja and sum(math.values())==8
        body=check.rendering.ArticleText();body.feed(html);assert check.rendering.expressions(''.join(body.parts))==math
        alt=re.findall(r'!\[([^\]]+)\]\(Animation_Sieb_des_Eratosthenes.gif\)',text);images=[i for i in rust.images if 'Animation_Sieb_des_Eratosthenes' in i.get('src','')]
        assert len(alt)==len(images)==1 and alt[0] and images[0].get('alt')==alt[0]
        assert '"datePublished":"2023-04-09T12:54:24+09:00"' in html and '"dateModified":"2026-10-29' in html
        assert len(v['executions'])==4
        for run in v['executions']:
            assert run['samplePrimes']==168 and run['sampleOutputExact'] and run['fullVectorBoundsComparedToIndependentTrialDivision']==2161 and run['usizeMaxCheckedAddPanic']
        result.append({'language':lang,'sha256':v['sha256'],'canonical':url,'executionEvidence':p.relative_to(ROOT).as_posix(),'executions':v['executions'],'texExpressions':8,'allTexPreserved':True,'rustBlocksExact':2,'imageAltPreserved':True,'datePublishedPreserved':True,'all14HreflangAnd13SidebarUrlsExact':True})
    gif=check.FOLDER/'Animation_Sieb_des_Eratosthenes.gif';assert hashlib.sha256(gif.read_bytes()).hexdigest()==audit['gif']['sha256']
    a.output.write_text(json.dumps({'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'scope':'Fresh all13version HTML/exactRust/exactTeX/metadata/imagealt/expected language-map checks,joined to preserved actual Rust executions. Does not claim duplicate new executable runs or automated prose approval.','versions':result,'texExpressions':104,'rustBlocksExact':26,'fullVectorBoundComparisons':2161*4*13,'completeProgramRunsWith168ExactOutputs':4*13,'gifSha256':audit['gif']['sha256'],'publicationPending':True,'limitations':['AI,not human/native-speaker certification.','Finite bounds<=100000,Rust1.90Windows64bit,not everyusize/target.','No timing benchmark,hugeallocation,fullanimation/browservisual/KaTeX or cryptographic audit.']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'versions':13,'texExpressions':104,'rustBlocks':26,'fullVectorComparisons':2161*4*13}))

if __name__=='__main__':main()
