"""Join preserved per-language executions to fresh all-version HTML; no prose approval."""
from pathlib import Path
import argparse,json,re,importlib.util,hashlib
from urllib.parse import urlsplit,unquote
from datetime import datetime,timezone,timedelta
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('prime_checks',Path(__file__).with_name('verify_batch_021.py'));check=importlib.util.module_from_spec(spec);spec.loader.exec_module(check)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();assert not a.output.exists()
    audit=json.loads((ROOT/'docs/translation-review/batch-021-source-audit.json').read_text(encoding='utf-8'))
    sieve=json.loads((ROOT/'docs/translation-review/batch-020-source-audit.json').read_text(encoding='utf-8'))
    proofs={}
    for name in ['ja-en','chinese','es-ko','pt-fr','de-id','hi-ru-ar']:
        p=ROOT/('docs/translation-review/batch-021-'+name+'-validation.json');x=json.loads(p.read_text(encoding='utf-8'))
        for v in x['versions']:assert v['language'] not in proofs;proofs[v['language']]=(p,v)
    assert set(proofs)==set(audit['versions']) and len(proofs)==13
    expected={l:v['canonical'] for l,v in audit['versions'].items()}
    codes_ja=re.findall(r'^```rust\n(.*?)^```',(check.FOLDER/'index.md').read_text(encoding='utf-8'),re.M|re.S);assert len(codes_ja)==1
    result=[]
    for lang,(p,v) in proofs.items():
        source=ROOT/audit['versions'][lang]['path'];text=source.read_text(encoding='utf-8-sig');h=hashlib.sha256(text.replace('\r\n','\n').encode()).hexdigest();assert h==v['sha256']
        url=expected[lang];html=(a.site/unquote(urlsplit(url).path).lstrip('/')/'index.html').read_text(encoding='utf-8')
        parser=check.helpers.PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>');assert parser.canonical==url and parser.language==lang
        assert parser.alternates==dict(expected,**{'x-default':expected['ja']}) and parser.options==expected
        rust=check.helpers.RustCode();rust.feed(html);codes=re.findall(r'^```rust\n(.*?)^```',text,re.M|re.S)
        assert codes==codes_ja and [s.strip() for s in rust.blocks]==[codes[0].strip()]
        assert not check.helpers.rendering.expressions(re.sub(r'^```.*?^```[^\n]*','',text,flags=re.M|re.S))
        body=check.helpers.rendering.ArticleText();body.feed(html);assert not check.helpers.rendering.expressions(''.join(body.parts))
        refs=set(re.findall(r'\]\((https://[^)]+)\)',text));assert refs=={'https://doc.rust-lang.org/std/vec/struct.Vec.html',sieve['versions'][lang]['canonical']} and sieve['versions'][lang]['canonical'] in html
        assert len(re.findall(r'^## ',text,re.M))==4 and text.count('\ndate: ')==1
        assert '"datePublished":"2022-09-09T07:08:49+09:00"' in html and '"dateModified":"2026-10-29' in html
        assert len(v['executions'])==2
        for run in v['executions']:assert run['samplePrimes']==168 and run['fullSampleOutputExact'] and run['fullVectorsAgainstIndependentTrialDivision']==2161
        result.append({'language':lang,'sha256':h,'canonical':url,'executionEvidence':p.relative_to(ROOT).as_posix(),'executions':v['executions'],'rustBlocksExact':1,'formalTexExpressions':0,'all14HreflangAnd13SidebarUrlsExact':True,'originalDistinctCanonicalAndDatePreserved':True,'sieveTarget':sieve['versions'][lang]['canonical']})
    a.output.write_text(json.dumps({'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'scope':'Fresh all13version HTML/exactRust/metadata/reference/expected language-map checks,joined to preserved actual Rust executions. Does not claim duplicate new executable runs or automatic prose approval.','versions':result,'fullVectorBoundComparisons':2161*2*13,'completeProgramRunsWith168ExactOutputs':2*13,'rustBlocksExact':13,'formalTexExpressions':0,'publicationPending':True,'limitations':['AI,not human/native-speaker certification.','Finite bounds<=100000,Rust1.90Windows64bit,not everyusize or target.','No usizeMAX enumeration,performance benchmark,visualbrowser/RTL or cryptographic audit.']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'versions':13,'rustBlocks':13,'fullVectorComparisons':2161*2*13,'completeProgramRuns':26}))

if __name__=='__main__':main()
