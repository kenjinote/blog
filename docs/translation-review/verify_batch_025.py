"""Selected two-envelope sources and HTML, with shared exact auxiliary checks.

This validates evidence, not prose completion or browser visual rendering.
It executes no article program: these articles contain only Mermaid fences.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from datetime import datetime,timezone,timedelta
import argparse,json,re,random,hashlib,importlib.util,sys,subprocess
from html import unescape
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"scripts"))
from check_multilingual import PageParser
spec=importlib.util.spec_from_file_location("math_rendering",Path(__file__).with_name("verify_batch_013_rendering.py"))
render=importlib.util.module_from_spec(spec);spec.loader.exec_module(render)
FOLDER=ROOT/"content/post/2つの封筒のパラドックス"
def digest(p):return hashlib.sha256(p.read_text(encoding="utf-8-sig").replace("\r\n","\n").encode()).hexdigest()

def auxiliary():
    """Joint enumeration is independent of the formula being compared."""
    rng=random.Random(25030)
    priors=[{5000:F(1,2),10000:F(1,2)},{1:F(49,100),2:F(1,100),4:F(1,2)}]
    for _ in range(100):
        weights={s:rng.randrange(1,101) for s in rng.sample(range(1,17),rng.randrange(1,17))}
        total=sum(weights.values());priors.append({s:F(w,total) for s,w in weights.items()})
    observations=0
    for prior in priors:
        groups=defaultdict(list)
        for s,p in prior.items():
            groups[F(s)].append((F(2*s),p/2));groups[F(2*s)].append((F(s),p/2))
        weighted_gain=F(0)
        for x,items in groups.items():
            mass=sum(w for _,w in items);mean=sum(y*w for y,w in items)/mass
            q=prior.get(x,F(0))/(prior.get(x,F(0))+prior.get(x/2,F(0)))
            assert q==sum(w for y,w in items if y==2*x)/mass
            assert mean==2*x*q+x/2*(1-q)
            assert mean-x==x*(3*q-1)/2
            assert (mean>x)==(q>F(1,3))
            weighted_gain+=mass*(mean-x);observations+=1
        assert weighted_gain==0
    ratio=F(5,4);assert ratio**2==F(25,16) and F(2)*F(1,2)==1
    for n in range(101):
        assert sum(F(1,3)*F(2,3)**j for j in range(n+1))+F(2,3)**(n+1)==1
    for n in range(1,101):
        x=F(2**n);low=F(1,3)*F(2,3)**n/2;high=F(1,3)*F(2,3)**(n-1)/2
        q=low/(low+high);assert q==F(2,5) and 2*x*q+x/2*(1-q)==F(11,10)*x
    grid=sorted({F(j,8) for j in range(1,257)}|{F(2)**j for j in range(-8,13)})
    f=lambda x:1/(1+x)**2
    for x in grid:
        low=f(x)/2;high=f(x/2)/4;q=low/(low+high)
        assert q==f(x)/(f(x)+f(x/2)/2)>F(1,3)
        assert f(x/2)/f(x)==4*(1+x)**2/(2+x)**2<4
        assert (2*x*low+x/2*high)/(low+high)>x
    return {"finitePriors":len(priors),"jointObservationCases":observations,"normalizationIdentities":101,"geometricPosteriorCases":100,"continuousRationalCases":len(grid),"ratioMean":"5/4","meanReciprocalProduct":"1","productOfRatioMeans":"25/16","scope":"Shared exact auxiliary arithmetic once per invocation, not article code execution or universal proof. Geometric limits, finite-mean argument and continuous inequality manually checked separately. Original source-audit also contains33finite truncations; not rerun or counted here."}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("site",type=Path);ap.add_argument("--languages",nargs="+",required=True);ap.add_argument("--output",type=Path,required=True);a=ap.parse_args();assert not a.output.exists()
    audit_path=ROOT/"docs/translation-review/batch-025-source-audit.json";audit=json.loads(audit_path.read_text(encoding="utf-8"))
    urls={l:v["canonical"] for l,v in audit["versions"].items()};fence=chr(96)*3
    text_ja=(FOLDER/"index.md").read_text(encoding="utf-8")
    strip=lambda s:re.sub(r"^"+fence+r".*?^"+fence+r"[^\n]*","",s,flags=re.M|re.S)
    tex=render.expressions(strip(text_ja));assert sum(tex.values())==44
    graphs=lambda s:re.findall(r"^"+fence+r"mermaid\n(.*?)^"+fence,s,re.M|re.S)
    edges=lambda g:re.findall(r"^\s*(\w+).*?--.*?>\s*(\w+)",g,re.M)
    ja_graphs=graphs(text_ja);assert [len(edges(g)) for g in ja_graphs]==[5,6]
    external={"https://users.ox.ac.uk/~sfop0060/pdf/Two%20envelope%20paradox.pdf","https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/c1ab69cb198badcebee42d5880784439_MIT6_436JF18_rec3.pdf","https://www.stat.berkeley.edu/~wfithian/courses/stat210a/measure-theory-basics.html"}
    taxonomy=lambda s:(re.search(r"^categories:.*$",s,re.M)[0],re.search(r"^tags:\n((?:  -[^\n]*\n)+)",s,re.M)[0])
    versions=[]
    for lang in a.languages:
        p=ROOT/audit["versions"][lang]["path"];text=p.read_text(encoding="utf-8-sig")
        baseline=subprocess.run(["git","show","351e13c99:"+p.relative_to(ROOT).as_posix()],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",check=True).stdout
        assert hashlib.sha256(baseline.replace("\r\n","\n").encode()).hexdigest()==audit["versions"][lang]["sha256"]
        assert taxonomy(text)==taxonomy(baseline)
        assert text.count("\ndate: ")==1 and 'date: "2026-09-10T00:00:00+09:00"' in text
        lastmod=re.search(r"^lastmod: (\d{4}-\d{2}-\d{2})$",text,re.M)[1]
        assert "2026-10-30"<=lastmod<=datetime.now(timezone(timedelta(hours=9))).date().isoformat()
        assert "slug: 'two-envelopes-paradox'" in text and "image: 'img/two_envelopes.jpg'" in text
        assert "math: true" in text and "mermaid: true" in text
        assert re.findall(r"^## (\d+)\.",text,re.M)==list(map(str,range(1,10)))
        assert re.findall(r"^"+fence+r"(\w+)\n",text,re.M)==["mermaid","mermaid"]
        gs=graphs(text);assert [edges(g) for g in gs]==[edges(g) for g in ja_graphs]
        assert render.expressions(strip(text))==tex
        html=(a.site/urls[lang].removeprefix("https://kenji.blog/")/"index.html").read_text(encoding="utf-8")
        parser=PageParser();parser.feed(html.split("</aside>",1)[0]+"</aside>")
        assert parser.canonical==urls[lang] and parser.language==lang
        assert parser.alternates==dict(urls,**{"x-default":urls["ja"]}) and parser.options==urls
        article=render.ArticleText();article.feed(html);assert render.expressions("".join(article.parts))==tex
        assert all(g.strip() in unescape(html) for g in gs)
        prefix="" if lang=="ja" else lang+"/"
        internal={"https://kenji.blog/"+prefix+"p/"+slug+"/" for slug in ["bayes-theorem","st-petersburg-paradox"]}
        refs=set(re.findall(r"\]\((https://[^)]+)\)",text));assert refs==external|internal and all(u in html for u in refs)
        assert all((a.site/u.removeprefix("https://kenji.blog/")/"index.html").is_file() for u in internal)
        assert '"datePublished":"2026-09-10T00:00:00+09:00"' in html and ('"dateModified":"'+lastmod) in html and "katex" in html
        assert hashlib.sha256((ROOT/audit["image"]["path"]).read_bytes()).hexdigest()==audit["image"]["sha256"]
        versions.append({"language":lang,"path":p.relative_to(ROOT).as_posix(),"sha256":digest(p),"sourceSha256":digest(FOLDER/"index.md"),"texExpressions":44,"mermaidDiagrams":2,"diagramEdges":[5,6],"articleExecutablePrograms":0,"references":len(refs),"datePublished":audit["versions"][lang]["datePublished"],"lastmod":lastmod,"passed":True})
    result={"version":1,"checkedAt":datetime.now(timezone(timedelta(hours=9))).isoformat(),"allPassed":True,"versions":versions,"sharedAuxiliaryChecks":auxiliary(),"sourceAuditSha256":hashlib.sha256(audit_path.read_bytes()).hexdigest(),"limitations":["Selected versions only; no unread translation certified.","No executable article program; auxiliary arithmetic is separate.","Source and decodedHTML; no native-language/browservisual/KaTeX/Mermaidruntime certification.","Internal Bayes/StPetersburg targets exist and match language; their bodies have not been reviewed in this batch.","Primary-source reading scope is in source-notes; no entire-course certification.","Publication pending."]}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":True,"versions":len(versions),"texEach":44,"diagramsEach":2,"auxiliary":result["sharedAuxiliaryChecks"]},ensure_ascii=False))
if __name__=="__main__":main()
