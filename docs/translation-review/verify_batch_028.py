"""Selected Monty Hall source/HTML and arithmetic; not a prose approval."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone,timedelta
from html import unescape
from html.parser import HTMLParser
from urllib.parse import unquote
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

def hindi_tag_redirects(site):
    """One documented tag correction; keep both old public archive URLs."""
    target="https://kenji.blog/hi/tags/बेज़-का-प्रमेय/"
    class Links(HTMLParser):
        def __init__(self):
            super().__init__();self.canonical=None;self.refresh=None;self.links=[]
        def handle_starttag(self,tag,attrs):
            a=dict(attrs)
            if tag=="link" and a.get("rel")=="canonical":self.canonical=a.get("href")
            if tag=="meta" and a.get("http-equiv","").lower()=="refresh":self.refresh=a.get("content")
            if tag=="a":self.links.append(unquote(a.get("href","")))
    archive=site/"hi/tags/बेज़-का-प्रमेय/index.html"
    parser=Links();parser.feed(archive.read_text(encoding="utf-8"))
    assert unquote(parser.canonical)==target
    for slug in ("monty-hall-problem","bayes-theorem"):
        assert any(u.endswith("/hi/p/"+slug+"/") for u in parser.links)
    article=Links();article.feed((site/"hi/p/monty-hall-problem/index.html").read_text(encoding="utf-8"))
    assert any(u.endswith("/hi/tags/बेज़-का-प्रमेय/") for u in article.links)
    assert not any("/hi/tags/बायेस-की-प्रमेय/" in u for u in article.links)
    checks=[]
    for relative in ("hi/tags/बायेस-की-प्रमेय/","hi/tags/बायेस-की-प्रमेय/page/1/"):
        p=Links();p.feed((site/relative/"index.html").read_text(encoding="utf-8"))
        assert unquote(p.canonical)==target
        assert unquote(p.refresh)=="0; url="+target
        checks.append({"oldUrl":"https://kenji.blog/"+relative,"target":target,
                       "canonicalMatches":True,"zeroDelayMetaRefreshMatches":True})
    return {"oldTag":"बायेस की प्रमेय","newTag":"बेज़ का प्रमेय",
            "archiveContainsBothArticles":True,"articleLinksToCorrectedTag":True,
            "legacyArchives":checks,
            "scope":"Static generated alias HTML,not an HTTP301 or browser/live certification."}
def auxiliary():
    weighted_paths=0
    for k in range(101):
        q=F(k,100);paths=[]
        for chosen in range(3):
            for car in range(3):
                available=[h for h in range(3) if h!=chosen and h!=car]
                weights=[q,1-q] if len(available)==2 else [F(1)]
                paths.extend((chosen,car,h,w/F(9)) for h,w in zip(available,weights))
        weighted_paths+=len(paths)
        assert sum(w for p,c,h,w in paths)==1
        assert sum(w for p,c,h,w in paths if p==c)==F(1,3)
        assert sum(w for p,c,h,w in paths if 3-p-h==c)==F(2,3)
        for chosen in range(3):
            lower,higher=[h for h in range(3) if h!=chosen]
            for opened in (lower,higher):
                filtered=[(c,w) for p,c,h,w in paths if p==chosen and h==opened]
                mass=sum(w for c,w in filtered)
                stay=sum(w for c,w in filtered if c==chosen)/mass
                switch=sum(w for c,w in filtered if c==3-chosen-opened)/mass
                expected=(q/(1+q),1/(1+q)) if opened==lower else ((1-q)/(2-q),1/(2-q))
                assert (stay,switch)==expected
    assert weighted_paths==1212
    paths=[(p,c,h,F(1,18)) for p in range(3) for c in range(3) for h in range(3) if h!=p]
    goats=[row for row in paths if row[1]!=row[2]]
    assert len(paths)==18 and len(goats)==12 and sum(w for p,c,h,w in goats)==F(2,3)
    for chosen in range(3):
        for opened in range(3):
            if opened==chosen:continue
            rows=[(c,w) for p,c,h,w in goats if p==chosen and h==opened]
            mass=sum(w for c,w in rows)
            assert mass==F(1,9)
            assert sum(w for c,w in rows if c==chosen)/mass==F(1,2)
            assert sum(w for c,w in rows if c==3-chosen-opened)/mass==F(1,2)
    for n in [*range(3,101),1000000]:
        left_joint=F(1,n*(n-1));car_joint=F(1,n)
        assert car_joint/(left_joint+car_joint)==1-F(1,n)
        assert car_joint/(car_joint+car_joint)==F(1,2)
    return {"biasedHostValues":101,"initialChoiceCarPairsEach":9,"weightedHostPathsIncludingZeroWeights":1212,
      "uninformedElementaryPaths":18,"uninformedGoatPaths":12,"uninformedLabeledGoatObservations":6,
      "manyDoorFormulaCases":99,"scope":"Once per invocation,not per language. Rational enumeration across all3initial choices independently checks source-audit fixed-A results. Finite checks/closed forms,not million-path simulation,general-policy proof,psychological experiment or article-program execution."}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("site",type=Path)
    ap.add_argument("--languages",nargs="+",required=True);ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--expected-modified",action="append",default=[],metavar="LANG=YYYY-MM-DD")
    args=ap.parse_args();assert not args.output.exists()
    audit=json.loads((D/"batch-028-source-audit.json").read_text(encoding="utf-8"))
    source=ROOT/audit["versions"]["ja"]["path"];tex=render.expressions(strip(source.read_text(encoding="utf-8")))
    assert sum(tex.values())==18
    urls={l:v["canonical"] for l,v in audit["versions"].items()}
    modified_dates={l:"2026-11-11" for l in urls}
    for value in args.expected_modified:
        lang,day=value.split("=",1)
        assert lang in args.languages and lang in urls
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}",day)
        datetime.strptime(day,"%Y-%m-%d")
        assert "2026-11-11"<=day<=datetime.now(timezone(timedelta(hours=9))).date().isoformat()
        modified_dates[lang]=day
    external={"https://pub.math.leidenuniv.nl/~gillrd/montyhall3.pdf",
      "https://probability.ca/jeff/writing/montyfall.pdf"}
    versions=[]
    for lang in args.languages:
        p=ROOT/audit["versions"][lang]["path"];text=p.read_text(encoding="utf-8-sig")
        original=subprocess.run(["git","show",audit["baselineCommit"]+":"+p.relative_to(ROOT).as_posix()],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",check=True).stdout
        assert hashlib.sha256(original.replace("\r\n","\n").encode()).hexdigest()==audit["versions"][lang]["sha256"]
        expected_taxonomy=original
        if lang=="hi":
            assert original.count("'बायेस की प्रमेय'")==1
            expected_taxonomy=original.replace("'बायेस की प्रमेय'","'बेज़ का प्रमेय'")
        assert taxonomy(text)==taxonomy(expected_taxonomy)
        header=text.split("---",2)[1]
        if lang=="hi":assert not any("\u0980"<=c<="\u09ff" for c in text)
        assert re.findall(r"^date:.*$",header,re.M)==['date: "2026-09-10T00:00:00+09:00"']
        assert re.findall(r"^lastmod:.*$",header,re.M)==['lastmod: "'+modified_dates[lang]+'"']
        for k in ["slug","image"]:
            assert re.findall(r"^"+k+r":.*$",header,re.M)==re.findall(r"^"+k+r":.*$",original.split("---",2)[1],re.M)
        assert re.findall(r"^(?:math|mermaid): true$",header,re.M)==["math: true","mermaid: true"]
        assert re.findall(r"^## (\d+)\.",text,re.M)==list(map(str,range(1,7)))
        assert re.findall(r"^"+FENCE+r"(\w+)\n",text,re.M)==["mermaid","mermaid"]
        gs=graphs(text);assert len(gs)==2 and len(re.findall(r"-->|-\.->",gs[0]))==15
        assert re.findall(r':\s*([0-9]+)\s*$',gs[1],re.M)==["2","1"]
        assert re.sub(r'"[^"\n]*"','""',gs[0])==re.sub(r'"[^"\n]*"','""',graphs(source.read_text(encoding="utf-8"))[0])
        if lang=="en":
            assert 'HostB_or_C --> Stay1["Stay: Win"]' in gs[0]
            assert 'HostB_or_C --> Switch1["Switch: Lose"]' in gs[0]
        assert render.expressions(strip(text))==tex
        html=(args.site/urls[lang].removeprefix("https://kenji.blog/")/"index.html").read_text(encoding="utf-8")
        parser=PageParser();parser.feed(html.split("</aside>",1)[0]+"</aside>")
        assert parser.canonical==urls[lang] and parser.language==lang
        assert parser.alternates==dict(urls,**{"x-default":urls["ja"]}) and parser.options==urls
        article=render.ArticleText();article.feed(html)
        assert render.expressions("".join(article.parts))==tex
        assert all(g.strip() in unescape(html) for g in gs)
        prefix="" if lang=="ja" else lang+"/"
        internal={"https://kenji.blog/"+prefix+"p/"+slug+"/" for slug in ("law-of-large-numbers","bayes-theorem")}
        refs=set(re.findall(r"\]\((https://[^)]+)\)",text))
        assert refs==external|internal and all(u in html for u in refs)
        assert all((args.site/u.removeprefix("https://kenji.blog/")/"index.html").is_file() for u in internal)
        assert '"datePublished":"2026-09-10T00:00:00+09:00"' in html
        assert ('"dateModified":"'+modified_dates[lang]) in html and "katex" in html and "mermaid" in html
        title=json.loads(re.search(r"^title: (.*)$",header,re.M)[1]);assert title in unescape(html)
        for asset in audit["assets"]:
            assert hashlib.sha256((ROOT/asset["path"]).read_bytes()).hexdigest()==asset["sha256"]
        versions.append({"language":lang,"path":p.relative_to(ROOT).as_posix(),"sha256":digest(p),
          "sourceSha256":digest(source),"texExpressions":18,"diagrams":2,"diagramEdges":[15,0],"pieRatio":[2,1],
          "articleExecutablePrograms":0,"references":len(refs),"datePublished":audit["versions"][lang]["datePublished"],"dateModified":modified_dates[lang],"passed":True})
    result={"version":1,"checkedAt":datetime.now(timezone(timedelta(hours=9))).isoformat(),
      "allPassed":True,"versions":versions,"sharedAuxiliaryChecks":auxiliary(),
      "hindiTaxonomyCorrection":hindi_tag_redirects(args.site) if "hi" in args.languages else None,
      "sourceAuditSha256":hashlib.sha256((D/"batch-028-source-audit.json").read_bytes()).hexdigest(),
      "reviewedTranslationsAdded":0,"limitations":["Selected source/decodedHTML/auxiliary checks do not certify full prose or add ledger records.",
        "No article executable programs;auxiliary calculations distinct.",
        "Not native-language,browser visual/runtime,psychological or universal-policy certification.",
        "Other languages/publication pending;full article goal active."]}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":True,"versions":len(versions),"texEach":18,"diagramsEach":2,"diagramEdges":[15,0],"pieRatio":[2,1],"auxiliary":result["sharedAuxiliaryChecks"]}))
if __name__=="__main__":main()
