"""Selected source/HTML and finite exact checks; no prose approval."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone,timedelta
from html import unescape
from html.parser import HTMLParser
import argparse,hashlib,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
spec=importlib.util.spec_from_file_location('shared',D/'verify_batch_028.py')
shared=importlib.util.module_from_spec(spec);spec.loader.exec_module(shared)

def auxiliary():
    pay={('C','C'):(-1,-1),('C','D'):(-10,0),('D','C'):(0,-10),('D','D'):(-5,-5)}
    efficient=[a for a,v in pay.items() if not any(all(w[i]>=v[i] for i in (0,1)) and any(w[i]>v[i] for i in (0,1)) for w in pay.values())]
    assert efficient==[('C','C'),('C','D'),('D','C')]
    equilibria=[a for a,v in pay.items() if all(v[i]>=pay[tuple('D' if j==i and a[i]=='C' else 'C' if j==i else a[j] for j in (0,1))][i] for i in (0,1))]
    assert equilibria==[('D','D')]
    assert {''.join(a):sum(v) for a,v in pay.items()}=={'CC':-2,'CD':-10,'DC':-10,'DD':-10}
    for k in range(101):
        p=F(k,100)
        for i in (0,1):
            def u(own,other):return pay[(own,other) if i==0 else (other,own)][i]
            eu_d=p*u('D','C')+(1-p)*u('D','D');eu_c=p*u('C','C')+(1-p)*u('C','D')
            assert eu_d-eu_c==5-4*p>=1
    deltas=sorted(set([F(k,100) for k in range(100)]+[F(1,5),F(1,5)-F(1,1000),F(1,5)+F(1,1000)]))
    delayed=0
    for delta in deltas:
        coop=-1/(1-delta);dev=delta*(-5)/(1-delta)
        assert (coop>=dev)==(delta>=F(1,5))
        assert (coop-dev)==(5*delta-1)/(1-delta)
        # Observe C for n rounds, deviate once, then best-respond D to punishment.
        for n in range(6):
            prefix=sum(-delta**t for t in range(n))
            value=prefix+delta**n*dev
            assert value-coop==delta**n*(dev-coop);delayed+=1
        assert pay[('D','D')][0]>pay[('C','D')][0]
    def trace(error_round=None):
        moves=[]
        for t in range(8):
            a=('C','C') if not moves else (moves[-1][1],moves[-1][0])
            if t==error_round:a=('D',a[1])
            moves.append(a)
        return [''.join(a) for a in moves]
    assert trace()==['CC']*8
    assert trace(1)==['CC','DC','CD','DC','CD','DC','CD','DC']
    return {'pureProfiles':4,'paretoEfficientPureProfiles':['CC','CD','DC'],'uniquePureNash':'DD','mixedBeliefValues':101,'playersEach':2,'discountValues':len(deltas),'delayedDeviationCases':delayed,'tftTraces':2,'roundsEach':8,'scope':'Once per invocation. Exact finite auxiliary arithmetic/traces, not article programs, empirical tournament reproduction, browser execution, all-strategy or real-world proof. General strict dominance and SPE argument separately read in prose.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--languages',nargs='+',required=True);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();assert not args.output.exists()
    audit_path=D/'batch-030-source-audit.json';audit=json.loads(audit_path.read_text(encoding='utf-8'))
    source=ROOT/audit['versions']['ja']['path'];source_text=source.read_text(encoding='utf-8')
    tex=shared.render.expressions(shared.strip(source_text));assert sum(tex.values())==9
    urls={l:v['canonical'] for l,v in audit['versions'].items()}
    refs={'https://public.websites.umich.edu/~axe/research/Axelrod%20and%20Hamilton%20EC%201981.pdf','https://www.ocw.mit.edu/courses/14-15j-networks-spring-2018/pages/lecture-and-recitation-notes/recitation-10-notes/'}
    versions=[]
    for lang in args.languages:
        v=audit['versions'][lang];p=ROOT/v['path'];text=p.read_text(encoding='utf-8');h=text.split('---',2)[1]
        original=subprocess.run(['git','show',audit['baselineCommit']+':'+v['path']],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
        assert hashlib.sha256(original.encode()).hexdigest()==v['sha256']
        assert shared.taxonomy(text)==shared.taxonomy(original)
        assert re.findall(r'^date:.*$',h,re.M)==v['headerDateLines']
        assert re.findall(r'^lastmod:.*$',h,re.M)==['lastmod: "2026-11-11"']
        for key in ('slug','image','math','mermaid'):
            assert re.findall(r'^'+key+r':.*$',h,re.M)==re.findall(r'^'+key+r':.*$',original.split('---',2)[1],re.M)
        assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,7)))
        assert re.findall('^'+shared.FENCE+r'(\w+)\n',text,re.M)==['mermaid','mermaid']
        graphs=shared.graphs(text);assert [g.count('-->') for g in graphs]==[6,6]
        assert [re.sub(r'"[^"\n]*"','""',g) for g in graphs]==[re.sub(r'"[^"\n]*"','""',g) for g in shared.graphs(source_text)]
        assert shared.render.expressions(shared.strip(text))==tex
        html=(args.site/urls[lang].removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
        parser=shared.PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>')
        assert parser.canonical==urls[lang] and parser.language==lang
        assert parser.alternates==dict(urls,**{'x-default':urls['ja']}) and parser.options==urls
        article=shared.render.ArticleText();article.feed(html)
        assert shared.render.expressions(''.join(article.parts))==tex
        assert all(g.strip() in unescape(html) for g in graphs)
        assert set(re.findall(r'\]\((https://[^)]+)\)',text))==refs and all(u in html for u in refs)
        assert '"datePublished":"'+v['datePublished']+'"' in html
        assert '"dateModified":"2026-11-11' in html
        assert 'katex.min.js' in html and 'mermaid' in html
        assert json.loads(re.search(r'^title: (.*)$',h,re.M)[1]) in unescape(html)
        cells=['(-1, -1)','(-10, 0)','(0, -10)','(-5, -5)']
        for cell in cells:assert cell in html
        if lang=='ar':
            class BidiPairs(HTMLParser):
                def __init__(self):super().__init__();self.active=False;self.pairs=[]
                def handle_starttag(self,tag,attrs):
                    if tag=='bdi':
                        assert dict(attrs).get('dir')=='ltr';self.active=True;self.pairs.append('')
                def handle_data(self,data):
                    if self.active:self.pairs[-1]+=data
                def handle_endtag(self,tag):
                    if tag=='bdi':self.active=False
            pairs=BidiPairs();pairs.feed(html);assert pairs.pairs==cells
            assert re.search(r'<html\b[^>]*\blang=ar\b[^>]*\bdir=rtl\b',html)
        for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
        versions.append({'language':lang,'path':v['path'],'sha256':shared.digest(p),'sourceSha256':shared.digest(source),'texExpressions':9,'diagrams':2,'diagramEdges':[6,6],'articleExecutablePrograms':0,'references':2,'datePublished':v['datePublished'],'dateModified':'2026-11-11','passed':True})
    result={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'allPassed':True,'versions':versions,'sharedAuxiliaryChecks':auxiliary(),'sourceAuditSha256':hashlib.sha256(audit_path.read_bytes()).hexdigest(),'reviewedTranslationsAdded':0,'limitations':['Selected source/decoded HTML/finite arithmetic only;not automatic prose approval or ledger record.','No native speaker/browser/KaTeX/Mermaid execution or tournament reproduction.','Other11 prose and publication pending;full goal active.']}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'versions':len(versions),'texEach':9,'edgesEach':[6,6],'auxiliary':result['sharedAuxiliaryChecks']}))

if __name__=='__main__':main()
