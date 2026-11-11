"""Selected cooperation source/HTML and finite arithmetic,not prose approval."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone,timedelta
from html import unescape
import argparse,hashlib,importlib.util,json,re,subprocess,itertools
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
spec=importlib.util.spec_from_file_location('shared',D/'verify_batch_028.py')
shared=importlib.util.module_from_spec(spec);spec.loader.exec_module(shared)

def auxiliary():
    pay={('C','C'):(-1,-1),('C','D'):(-10,0),('D','C'):(0,-10),('D','D'):(-5,-5)}
    efficient=[a for a,v in pay.items() if not any(all(w[i]>=v[i] for i in (0,1)) and any(w[i]>v[i] for i in (0,1)) for w in pay.values())]
    assert efficient==[('C','C'),('C','D'),('D','C')]
    nash=[]
    for a,v in pay.items():
        if all(v[i]>=pay[tuple(('D' if a[j]=='C' else 'C') if j==i else a[j] for j in (0,1))][i] for i in (0,1)):nash.append(a)
    assert nash==[('D','D')]
    assert {''.join(a):sum(v) for a,v in pay.items()}=={'CC':-2,'CD':-10,'DC':-10,'DD':-10}
    for k in range(101):
        q=F(k,100)
        for i in (0,1):
            def u(own,other):return pay[(own,other) if i==0 else (other,own)][i]
            assert q*u('D','C')+(1-q)*u('D','D')-(q*u('C','C')+(1-q)*u('C','D'))==5-4*q>=1
    def trace(left,right,error_round=None):
        moves=[]
        for t in range(8):
            def action(strategy,i):return 'D' if strategy=='ALLD' else 'C' if not moves else moves[-1][1-i]
            a=(action(left,0),action(right,1))
            if t==error_round:a=('D',a[1])
            moves.append(a)
        return moves
    traces={pair:trace(*pair) for pair in [('TFT','TFT'),('TFT','ALLD'),('ALLD','ALLD')]}
    assert [''.join(a) for a in trace('TFT','TFT',1)]==['CC','DC','CD','DC','CD','DC','CD','DC']
    deltas=sorted(set([F(k,100) for k in range(100)]+[F(1,1000),F(999,1000)]))
    cluster_cases=tail_cases=0
    for delta in deltas:
        tt=-1/(1-delta);td=-10-5*delta/(1-delta);dd=-5/(1-delta)
        for pair,expected in [(('TFT','TFT'),tt),(('TFT','ALLD'),td),(('ALLD','ALLD'),dd)]:
            moves=traces[pair];scores=[pay[a][0] for a in moves]
            actual=sum(delta**t*s for t,s in enumerate(scores))+delta**8*scores[-1]/(1-delta)
            assert actual==expected;tail_cases+=1
        threshold=5*(1-delta)/(9-5*delta);assert 0<threshold<1 and 9-5*delta>0
        ps=set([F(k,100) for k in range(101)]+[threshold,threshold-F(1,100000),threshold+F(1,100000)])
        for p in sorted(ps):
            if not 0<=p<=1:continue
            value=p*tt+(1-p)*td
            assert value-dd==(p*(9-5*delta)-5*(1-delta))/(1-delta)
            assert (value>dd)==(p>threshold);cluster_cases+=1
        assert td-dd==-5
    delta=F(9,10);assert 5*(1-delta)/(9-5*delta)==F(1,9)
    examples={F(0):F(-55),F(1,20):F(-211,4),F(1,9):F(-50),F(1,5):F(-46)}
    for p,score in examples.items():assert p*(-1/(1-delta))+(1-p)*(-10-5*delta/(1-delta))==score
    return {'pureProfiles':4,'paretoEfficientPureProfiles':['CC','CD','DC'],'uniquePureNash':'DD','cooperationBeliefValues':101,'playersEach':2,'discountValues':len(deltas),'deterministicStrategyPairs':3,'roundsEach':8,'discountedPrefixPlusExactTailCases':tail_cases,'clusterMatchingCases':cluster_cases,'isolatedTftDifference':'-5','exampleDelta':'9/10','exampleMatchingThreshold':'1/9','numericTableCases':4,'tftErrorTraceRounds':8,'scope':'Once per invocation,finite exact auxiliary arithmetic and traces. Not article programs,population-update simulation,ESS/SPE/all-strategy proof,biological data reanalysis or tournament reproduction. Rare-cluster resident baseline and negative score meaning read separately in prose.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--languages',nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--expected-modified',action='append',default=[])
    args=ap.parse_args();assert not args.output.exists()
    audit_path=D/'batch-031-source-audit.json';audit=json.loads(audit_path.read_text(encoding='utf-8'))
    source=ROOT/audit['versions']['ja']['path'];source_text=source.read_text(encoding='utf-8');tex=shared.render.expressions(shared.strip(source_text));assert sum(tex.values())==10
    urls={l:v['canonical'] for l,v in audit['versions'].items()};dates=dict.fromkeys(urls,'2026-11-12')
    for value in args.expected_modified:
        lang,day=value.split('=',1);assert lang in args.languages
        datetime.strptime(day,'%Y-%m-%d');assert '2026-11-12'<=day<=datetime.now(timezone(timedelta(hours=9))).date().isoformat();dates[lang]=day
    external={'https://public.websites.umich.edu/~axe/research/Axelrod%20and%20Hamilton%20EC%201981.pdf','https://www.ocw.mit.edu/courses/14-15j-networks-spring-2018/pages/lecture-and-recitation-notes/recitation-10-notes/','https://www.cs.cornell.edu/~rafael/networks-html/chapter1.html','https://science.umd.edu/faculty/wilkinson/Carter%26Wilk_PRSB13.pdf'}
    versions=[]
    for lang in args.languages:
        v=audit['versions'][lang];p=ROOT/v['path'];text=p.read_text(encoding='utf-8');h=text.split('---',2)[1]
        original=subprocess.run(['git','show',audit['baselineCommit']+':'+v['path']],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
        assert hashlib.sha256(original.encode()).hexdigest()==v['sha256'] and shared.taxonomy(text)==shared.taxonomy(original)
        assert re.findall(r'^date:.*$',h,re.M)==v['headerDateLines'] and re.findall(r'^lastmod:.*$',h,re.M)==['lastmod: "'+dates[lang]+'"']
        for key in ('slug','image'):assert re.findall(r'^'+key+r':.*$',h,re.M)==re.findall(r'^'+key+r':.*$',original.split('---',2)[1],re.M)
        assert re.findall(r'^(?:math|mermaid): true$',h,re.M)==['math: true','mermaid: true']
        assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,7))) and not re.search(r'^# ',text,re.M)
        assert re.findall('^'+shared.FENCE+r'(\w+)\n',text,re.M)==['mermaid','mermaid']
        graphs=shared.graphs(text);assert [g.count('-->') for g in graphs]==[6,6]
        assert [re.sub(r'"[^"\n]*"','""',g) for g in graphs]==[re.sub(r'"[^"\n]*"','""',g) for g in shared.graphs(source_text)]
        assert shared.render.expressions(shared.strip(text))==tex
        html=(args.site/urls[lang].removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
        parser=shared.PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>')
        assert parser.canonical==urls[lang] and parser.language==lang and parser.alternates==dict(urls,**{'x-default':urls['ja']}) and parser.options==urls
        article=shared.render.ArticleText();article.feed(html);assert shared.render.expressions(''.join(article.parts))==tex
        assert all(g.strip() in unescape(html) for g in graphs)
        internal='https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/prisoners-dilemma/'
        refs=set(re.findall(r'\]\((https://[^)]+)\)',text));assert refs==external|{internal} and all(u in html for u in refs)
        assert (args.site/internal.removeprefix('https://kenji.blog/')/'index.html').is_file()
        assert '"datePublished":"'+v['datePublished']+'"' in html and '"dateModified":"'+dates[lang] in html
        assert 'katex.min.js' in html and 'mermaid' in html and json.loads(re.search(r'^title: (.*)$',h,re.M)[1]) in unescape(html)
        for number in ('-55','-50','-46','1/20','1/9','1/5'):assert number in html
        for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
        versions.append({'language':lang,'path':v['path'],'sha256':shared.digest(p),'sourceSha256':shared.digest(source),'texExpressions':10,'diagrams':2,'diagramEdges':[6,6],'articleExecutablePrograms':0,'references':5,'datePublished':v['datePublished'],'dateModified':dates[lang],'passed':True})
    doc={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'allPassed':True,'versions':versions,'sharedAuxiliaryChecks':auxiliary(),'sourceAuditSha256':hashlib.sha256(audit_path.read_bytes()).hexdigest(),'reviewedTranslationsAdded':0,'limitations':['Selected source/decodedHTML/finite arithmetic,not automatic prose approval or ledger entry.','No browser/native speaker,tournament reproduction or biological data reanalysis.','Baseline libraries already present;flags document requirements. Other translations/publication pending;whole goal active.']}
    args.output.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':True,'versions':len(versions),'texEach':10,'edgesEach':[6,6],'auxiliary':doc['sharedAuxiliaryChecks']}))

if __name__=='__main__':main()
