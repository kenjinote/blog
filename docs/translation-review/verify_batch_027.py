"""Selected St Petersburg source/HTML and arithmetic; not a prose approval."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone,timedelta
from html import unescape
from decimal import Decimal as Q,localcontext
import argparse,hashlib,importlib.util,itertools,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/"docs/translation-review"
sys.path.insert(0,str(ROOT/"scripts"));from check_multilingual import PageParser
spec=importlib.util.spec_from_file_location("render",D/"verify_batch_013_rendering.py")
render=importlib.util.module_from_spec(spec);spec.loader.exec_module(render)
FENCE=chr(96)*3
def digest(p):
    return hashlib.sha256(p.read_text(encoding="utf-8-sig").replace("\r\n","\n").encode()).hexdigest()
def strip(s):
    return re.sub(r"^"+FENCE+r".*?^"+FENCE+r"[^\n]*","",s,flags=re.M|re.S)
def graphs(s):
    return re.findall(r"^"+FENCE+r"mermaid\n(.*?)^"+FENCE,s,re.M|re.S)
def taxonomy(s):
    h=s.split("---",2)[1]
    return tuple(re.search(r"(?ms)^"+k+r":(.*?)(?=^[A-Za-z]|\Z)",h)[1].strip() for k in ("categories","tags"))
def auxiliary():
    paths=0
    for k in range(1,13):
        total=0;first_tail=0
        for bits in itertools.product([0,1],repeat=k):
            n=next((i for i,b in enumerate(bits,1) if b==0),k+1)
            total+=2**min(n,k);first_tail+=n<=k;paths+=1
        assert F(total,2**k)==k+1
        assert F(first_tail,2**k)==1-F(1,2**k)
    assert paths==8190
    for k in range(1,65):
        assert sum((F(2**n,2**n) for n in range(1,k+1)),F(0))==k
        assert sum((F(n,2**n) for n in range(1,k+1)),F(0))==2-F(k+2,2**k)
    fees=[]
    with localcontext() as ctx:
        ctx.prec=90;ln2=Q(2).ln();m=128
        def gain(w,c):
            a=w-c
            return Q(2)+sum((Q(2)**(-n)*(1+a*Q(2)**(-n)).ln()/ln2 for n in range(1,m+1)),Q(0))-w.ln()/ln2
        for w,expected in [(Q(10),"4.97"),(Q(100),"7.79"),(Q(1000),"10.95")]:
            lo=Q(0);hi=w
            assert gain(w,lo)>0 and gain(w,hi)<0
            for _ in range(100):
                mid=(lo+hi)/2
                if gain(w,mid)>0:lo=mid
                else:hi=mid
            assert lo.quantize(Q(".01"))==hi.quantize(Q(".01"))==Q(expected)
            fees.append({"w":str(w),"feeRounded":expected,"terms":m,
              "positiveOmittedTailUpperBound":str(w*Q(4)**(-m)/(3*ln2))})
    return {"binarySequenceLengths":12,"binarySequencesEnumerated":paths,"finiteSeriesCases":64,
      "logWealthFeeExamples":fees,
      "scope":"Once per validator invocation,not per language. Full finite binary-sequence enumeration independently checks the capped contract and stopping CDF;finite series and Decimal fee calculations separately scoped. Not article-program execution,infinite-limit machine proof,interval-rounding proof or human-choice evidence."}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("site",type=Path)
    ap.add_argument("--languages",nargs="+",required=True);ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args();assert not args.output.exists()
    audit=json.loads((D/"batch-027-source-audit.json").read_text(encoding="utf-8"))
    source=ROOT/audit["versions"]["ja"]["path"];tex=render.expressions(strip(source.read_text(encoding="utf-8")))
    assert sum(tex.values())==16
    urls={l:v["canonical"] for l,v in audit["versions"].items()}
    external={"https://faculty.econ.ucsb.edu/~tedb/Courses/GraduateTheoryUCSB/Bernoulli.pdf",
      "https://www.stanford.edu/class/psych205/papers/Tversky-Kahneman-1981.pdf"}
    versions=[]
    for lang in args.languages:
        p=ROOT/audit["versions"][lang]["path"];text=p.read_text(encoding="utf-8-sig")
        original=subprocess.run(["git","show",audit["baselineCommit"]+":"+p.relative_to(ROOT).as_posix()],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",check=True).stdout
        assert hashlib.sha256(original.replace("\r\n","\n").encode()).hexdigest()==audit["versions"][lang]["sha256"]
        assert taxonomy(text)==taxonomy(original)
        header=text.split("---",2)[1]
        assert re.findall(r"^date:.*$",header,re.M)==['date: "2026-09-10T05:00:00+09:00"']
        assert re.findall(r"^lastmod:.*$",header,re.M)==['lastmod: "2026-10-30"']
        for k in ["slug","image"]:
            assert re.findall(r"^"+k+r":.*$",header,re.M)==re.findall(r"^"+k+r":.*$",original.split("---",2)[1],re.M)
        assert re.findall(r"^(?:math|mermaid): true$",header,re.M)==["math: true","mermaid: true"]
        assert re.findall(r"^## (\d+)\.",text,re.M)==list(map(str,range(1,8)))
        assert re.findall(r"^"+FENCE+r"(\w+)\n",text,re.M)==["mermaid"]
        gs=graphs(text);assert len(gs)==1 and len(re.findall(r"-->|-\.->",gs[0]))==8
        assert render.expressions(strip(text))==tex
        html=(args.site/urls[lang].removeprefix("https://kenji.blog/")/"index.html").read_text(encoding="utf-8")
        parser=PageParser();parser.feed(html.split("</aside>",1)[0]+"</aside>")
        assert parser.canonical==urls[lang] and parser.language==lang
        assert parser.alternates==dict(urls,**{"x-default":urls["ja"]}) and parser.options==urls
        article=render.ArticleText();article.feed(html)
        assert render.expressions("".join(article.parts))==tex
        assert gs[0].strip() in unescape(html)
        prefix="" if lang=="ja" else lang+"/"
        internal={"https://kenji.blog/"+prefix+"p/"+slug+"/" for slug in ("law-of-large-numbers","two-envelopes-paradox","bayes-theorem")}
        refs=set(re.findall(r"\]\((https://[^)]+)\)",text))
        assert refs==external|internal and all(u in html for u in refs)
        assert all((args.site/u.removeprefix("https://kenji.blog/")/"index.html").is_file() for u in internal)
        assert '"datePublished":"2026-09-10T05:00:00+09:00"' in html
        assert '"dateModified":"2026-10-30' in html and "katex" in html and "mermaid" in html
        title=json.loads(re.search(r"^title: (.*)$",header,re.M)[1]);assert title in unescape(html)
        assert hashlib.sha256((ROOT/audit["image"]["path"]).read_bytes()).hexdigest()==audit["image"]["sha256"]
        versions.append({"language":lang,"path":p.relative_to(ROOT).as_posix(),"sha256":digest(p),
          "sourceSha256":digest(source),"texExpressions":16,"diagrams":1,"diagramEdges":[8],
          "articleExecutablePrograms":0,"references":len(refs),"datePublished":audit["versions"][lang]["datePublished"],"passed":True})
    result={"version":1,"checkedAt":datetime.now(timezone(timedelta(hours=9))).isoformat(),
      "allPassed":True,"versions":versions,"sharedAuxiliaryChecks":auxiliary(),
      "sourceAuditSha256":hashlib.sha256((D/"batch-027-source-audit.json").read_bytes()).hexdigest(),
      "reviewedTranslationsAdded":0,"limitations":["Selected source/decodedHTML/auxiliary checks do not certify full prose or add ledger records.",
        "No article executable programs;auxiliary calculations distinct.",
        "Not native-language,browser visual/runtime,historical Latin original or financial/empirical-choice certification.",
        "Other languages/publication pending;full article goal active."]}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":True,"versions":len(versions),"texEach":16,"diagramsEach":1,"edgesEach":8,"auxiliary":result["sharedAuxiliaryChecks"]}))
if __name__=="__main__":main()
