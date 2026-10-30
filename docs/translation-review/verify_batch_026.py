"""Selected Bayes source/HTML checks; these do not certify prose or browser rendering."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone,timedelta
from html import unescape
import argparse,hashlib,importlib.util,itertools,json,re,subprocess,sys

ROOT=Path(__file__).resolve().parents[2]
D=ROOT/"docs/translation-review"
sys.path.insert(0,str(ROOT/"scripts"))
from check_multilingual import PageParser
spec=importlib.util.spec_from_file_location("render",D/"verify_batch_013_rendering.py")
render=importlib.util.module_from_spec(spec);spec.loader.exec_module(render)
FENCE=chr(96)*3
def digest(p):
    return hashlib.sha256(p.read_text(encoding="utf-8-sig").replace("\r\n","\n").encode()).hexdigest()
def strip(s):
    return re.sub(r"^"+FENCE+r".*?^"+FENCE+r"[^\n]*","",s,flags=re.M|re.S)
def graphs(s):
    return re.findall(r"^"+FENCE+r"mermaid\n(.*?)^"+FENCE,s,re.M|re.S)
def edges(g):
    return re.findall(r'^\s*(\w+)(?:\[.*?\])?\s*(-->|-\.->)(?:\|[^|\n]*\|)?\s*(\w+)',g,re.M)
def taxonomy(s):
    h=s.split("---",2)[1]
    return tuple(re.search(r"(?ms)^"+k+r":(.*?)(?=^[A-Za-z]|\Z)",h)[1].strip() for k in ("categories","tags"))

def auxiliary():
    joint=reverse=zero_a=0
    for a,b,c,d in itertools.product(range(6),repeat=4):
        total=a+b+c+d
        # Rows: A,A^c; columns: B,B^c.
        if not total or not a+c:continue
        p_ab=F(a,total);p_a=F(a+b,total);p_b=F(a+c,total)
        posterior=F(a,a+c)
        assert posterior==p_ab/p_b
        joint+=1
        if a+b:
            assert posterior==F(a,a+b)*p_a/p_b
            reverse+=1
        else:
            assert posterior==0
            zero_a+=1
    assert (joint,reverse,zero_a)==(1260,1230,30)
    # Independently enumerate the 128 assignments of a seven-variable toy DAG.
    # These arbitrary CPDs are auxiliary data, not clinical measurements.
    masses=[]
    bern=lambda bit,p:p if bit else 1-p
    for a,l,g,d,s1,s2,t in itertools.product((0,1),repeat=7):
        p_d=F(1+a+2*l+3*g,10)
        mass=(bern(a,F(1,4))*bern(l,F(1,3))*bern(g,F(1,5))
              *bern(d,p_d)*bern(s1,F(4,5) if d else F(1,10))
              *bern(s2,F(3,4) if d else F(1,5))
              *bern(t,F(99,100) if d else F(1,20)))
        masses.append((d,t,mass))
    assert sum(m for _,_,m in masses)==1
    p_d=sum(m for d,_,m in masses if d)
    assert p_d==F(151,600)
    p_t=sum(m for _,t,m in masses if t)
    p_dt=sum(m for d,t,m in masses if d and t)
    assert p_dt/p_t==F(99,100)*p_d/(F(99,100)*p_d+F(1,20)*(1-p_d))==F(14949,17194)
    return {"jointFormulaTables":joint,"reverseFormulaTables":reverse,
            "zeroPriorAWithPositiveB":zero_a,"undefinedBExcluded":36,
            "toyDagAssignments":len(masses),"toyDagTotalMass":"1",
            "toyDagPrior":"151/600","toyDagPosterior":"14949/17194",
            "scope":"Exact auxiliary enumeration once per invocation. Not article-program execution, clinical evidence, BNN training, BO optimization, or a universal proof. Source-audit arithmetic for medical counts, conditional independence/XOR, finite coins and posterior mode/prediction is preserved separately, not recounted as rerun."}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("site",type=Path)
    ap.add_argument("--languages",nargs="+",required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args();assert not args.output.exists()
    audit=json.loads((D/"batch-026-source-audit.json").read_text(encoding="utf-8"))
    urls={l:v["canonical"] for l,v in audit["versions"].items()}
    ja=(ROOT/audit["versions"]["ja"]["path"]).read_text(encoding="utf-8")
    tex=render.expressions(strip(ja));assert sum(tex.values())==22
    topology=[edges(g) for g in graphs(ja)]
    assert [len(e) for e in topology]==[9,7]
    assert [a for _,a,_ in topology[1]].count("-->")==6
    assert [a for _,a,_ in topology[1]].count("-.->")==1
    external={
        "https://bayes.wustl.edu/Manual/an.essay.pdf",
        "https://web.stanford.edu/class/stats200/Lecture20.pdf",
        "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/statistical-guidance-reporting-results-studies-evaluating-diagnostic-tests-guidance-industry-and-fda",
        "https://scikit-learn.org/stable/modules/naive_bayes.html",
        "https://ermongroup.github.io/cs228-notes/representation/directed/",
        "https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf",
        "https://arxiv.org/abs/1206.2944",
        "https://arxiv.org/abs/1505.05424",
        "https://arxiv.org/abs/1906.02530",
    }
    versions=[]
    for lang in args.languages:
        p=ROOT/audit["versions"][lang]["path"];text=p.read_text(encoding="utf-8-sig")
        original=subprocess.run(["git","show","987c31d250bafe6f40ab1a37cf827c00571e5f42:"+p.relative_to(ROOT).as_posix()],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",check=True).stdout
        assert hashlib.sha256(original.replace("\r\n","\n").encode()).hexdigest()==audit["versions"][lang]["sha256"]
        assert taxonomy(text)==taxonomy(original)
        for key,value in (("date","2026-09-20T15:15:00+09:00"),("slug","bayes-theorem"),("image","eyecatch.jpg")):
            assert re.findall(r"^"+key+r': "([^"]+)"$',text,re.M)==[value]
        assert re.findall(r"^lastmod:.*$",text,re.M)==['lastmod: "2026-10-30"']
        assert re.findall(r"^## (\d+)\.",text,re.M)==list(map(str,range(1,11)))
        assert re.findall(r"^"+FENCE+r"(\w+)\n",text,re.M)==["mermaid","mermaid"]
        gs=graphs(text);assert [edges(g) for g in gs]==topology
        assert render.expressions(strip(text))==tex
        html=(args.site/urls[lang].removeprefix("https://kenji.blog/")/"index.html").read_text(encoding="utf-8")
        parser=PageParser();parser.feed(html.split("</aside>",1)[0]+"</aside>")
        assert parser.canonical==urls[lang] and parser.language==lang
        assert parser.alternates==dict(urls,**{"x-default":urls["ja"]}) and parser.options==urls
        article=render.ArticleText();article.feed(html)
        assert render.expressions("".join(article.parts))==tex
        assert all(g.strip() in unescape(html) for g in gs)
        prefix="" if lang=="ja" else lang+"/"
        internal={"https://kenji.blog/"+prefix+"p/"+slug+"/" for slug in ("law-of-large-numbers","two-envelopes-paradox")}
        refs=set(re.findall(r"\]\((https://[^)]+)\)",text))
        assert refs==external|internal and all(u in html for u in refs)
        assert all((args.site/u.removeprefix("https://kenji.blog/")/"index.html").is_file() for u in internal)
        assert '"datePublished":"2026-09-20T15:15:00+09:00"' in html
        assert '"dateModified":"2026-10-30' in html and "katex" in html and "mermaid" in html
        assert hashlib.sha256((ROOT/audit["image"]["path"]).read_bytes()).hexdigest()==audit["image"]["sha256"]
        versions.append({"language":lang,"path":p.relative_to(ROOT).as_posix(),"sha256":digest(p),
                         "sourceSha256":digest(ROOT/audit["versions"]["ja"]["path"]),
                         "texExpressions":22,"diagrams":2,"diagramEdges":[9,7],
                         "probabilisticNetworkEdges":6,"inferenceAnnotationEdges":1,
                         "articleExecutablePrograms":0,"references":len(refs),
                         "datePublished":audit["versions"][lang]["datePublished"],"passed":True})
    result={"version":1,"checkedAt":datetime.now(timezone(timedelta(hours=9))).isoformat(),
            "allPassed":True,"versions":versions,"sharedAuxiliaryChecks":auxiliary(),
            "sourceAuditSha256":hashlib.sha256((D/"batch-026-source-audit.json").read_bytes()).hexdigest(),
            "reviewedTranslationsAdded":0,
            "limitations":["Selected source and decoded HTML checks do not certify full prose review or add ledger records.",
                           "No executable article program; auxiliary calculations are distinct.",
                           "Not browser visual, KaTeX/Mermaid runtime, native-language, clinical or full-primary-paper certification.",
                           "Publication pending."]}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":True,"versions":len(versions),"texEach":22,"diagramsEach":2,"auxiliary":result["sharedAuxiliaryChecks"]}))
if __name__=="__main__":main()
