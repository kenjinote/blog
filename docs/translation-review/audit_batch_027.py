"""St Petersburg baseline inventory and scoped arithmetic; not review approval."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as Q,localcontext
from datetime import datetime,timezone,timedelta
import json,re,hashlib,os,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/"docs/translation-review"
out=D/"batch-027-source-audit.json";assert not out.exists()
sys.path.insert(0,str(ROOT/"scripts"));from check_multilingual import PageParser
folder=ROOT/"content/post/サンクトペテルブルクのパラドックス"
site=Path(os.environ["TEMP"])/"kenji-priority-review-20261024/public-29-bundles-stp-baseline"
ledger=json.loads((ROOT/"data/translation_reviews.json").read_text(encoding="utf-8"))
assert len(ledger["reviews"])==324 and all(v["reviewKind"]=="ai" for v in ledger["reviews"].values())
versions={};fence=chr(96)*3
for p in sorted(folder.glob("index*.md")):
    lang="ja" if p.name=="index.md" else p.name.split(".")[1]
    assert p.relative_to(ROOT/"content").as_posix() not in ledger["reviews"]
    text=p.read_text(encoding="utf-8-sig");header=text.split("---",2)[1]
    slug=re.search(r"^slug:\s*['\"]([^'\"]+)",header,re.M)[1]
    html=(site/("" if lang=="ja" else lang)/"p"/slug/"index.html").read_text(encoding="utf-8")
    parser=PageParser();parser.feed(html.split("</aside>",1)[0]+"</aside>")
    scripts=re.findall(r"<script\b[^>]*>.*?</script>",html,re.S)
    versions[lang]={"path":p.relative_to(ROOT).as_posix(),"sha256":hashlib.sha256(text.replace("\r\n","\n").encode()).hexdigest(),
      "canonical":parser.canonical,"slug":slug,"datePublished":re.search(r'"datePublished":"([^"]+)"',html)[1],
      "headerDateLines":re.findall(r"^date:.*$",header,re.M),
      "mathFlag":re.findall(r"^math:.*$",header,re.M),"mermaidFlag":re.findall(r"^mermaid:.*$",header,re.M),
      "fenceLanguages":re.findall(r"^"+fence+r"(\w+)\n",text,re.M),
      "explicitKaTeXScriptReference":any("katex" in s for s in scripts),
      "explicitMermaidScriptReference":any("mermaid" in s for s in scripts),
      "fullOriginalMetadataBodyAndDiagramRead":lang in ["ja","en"],"reviewed":False}
assert len(versions)==13
assert all(v["datePublished"]=="2026-09-10T05:00:00+09:00" and len(v["headerDateLines"])==2 for v in versions.values())
assert all(v["fenceLanguages"]==["mermaid"] for v in versions.values())
cases=[]
for k in range(1,65):
    mass=sum((F(1,2**n) for n in range(1,k+1)),F(0))
    partial_money=sum((F(2**n,2**n) for n in range(1,k+1)),F(0))
    partial_log_utility=sum((F(n,2**n) for n in range(1,k+1)),F(0))
    cap_money=sum((F(2**n,2**n) for n in range(1,k)),F(0))+F(2**k,2**(k-1))
    assert mass==1-F(1,2**k) and partial_money==k
    assert partial_log_utility==2-F(k+2,2**k) and cap_money==k+1
    cases.append({"K":k,"firstTailByK":str(mass),"partialUncappedExpectation":str(partial_money),
      "capAt2ToKExpectation":str(cap_money),"partialLog2PrizeUtility":str(partial_log_utility),
      "logUtilityRemainder":str(F(k+2,2**k))})
wealth_cases=[]
with localcontext() as ctx:
    ctx.prec=90;ln2=Q(2).ln();m=128
    def expected_log2(remaining):
        return Q(2)+sum((Q(2)**(-n)*(1+remaining*Q(2)**(-n)).ln()/ln2 for n in range(1,m+1)),Q(0))
    for w in map(Q,[10,100,1000]):
        target=w.ln()/ln2;lo=Q(0);hi=w
        assert expected_log2(w)>target and expected_log2(Q(0))<target
        for _ in range(100):
            mid=(lo+hi)/2
            if expected_log2(w-mid)>target:lo=mid
            else:hi=mid
        assert hi-lo<w/Q(2)**99
        wealth_cases.append({"initialWealth":str(w),"numericalFeeBracket":[str(lo),str(hi)],
          "terms":m,"analyticOmittedPositiveTailBoundAtMost":str(w*Q(4)**(-m)/(3*ln2)),
          "scope":"90-digit Decimal arithmetic/100 bisections,with analytical truncation bound. Not machine-verified floating/Decimal interval-rounding proof or empirical willingness-to-pay."})
input_root=Path(os.environ["TEMP"])/"kenji-priority-review-20261024/content-29-bundles-stp/post"
bundles=len([p for p in input_root.iterdir() if p.is_dir()])
assert bundles==28
image=folder/"img/st_petersburg.jpg"
result={"version":1,"checkedAt":datetime.now(timezone(timedelta(hours=9))).isoformat(),
 "baselineCommit":"03dc2a9279274bd8db955101c882034535d7197e","baselineSite":str(site),
 "actualPreviewBundles":bundles,"previewDirectoryNameIsNotBundleCount":True,
 "versions":versions,"image":{"path":image.relative_to(ROOT).as_posix(),"sha256":hashlib.sha256(image.read_bytes()).hexdigest()},
 "auxiliaryChecks":{"finiteExactCases":cases,"logWealthFeeExamples":wealth_cases,
   "scope":"64 finite exact geometric/utility/cap checks plus three numerical fee examples. Limit arguments and model assumptions require manual review;not game-program execution, a general utility theorem or human-choice certification."},
 "reviewedTranslationsAdded":0,"currentAiTranslations":324,"unreviewedTranslations":12708,"humanReviews":0,
 "limitations":["Pre-audit only;no source edits or review ledger entry.",
  "OnlyJAENoriginal full bodies read;other11metadata/hash/fence/script inventory only.",
  "All13headers contain two dates;effectiveHTML date Sep10 preserved;newer duplicate Sep24 must not silently replace public date.",
  "Directory says29bundles but actual content inventory is28:StPetersburg was already in old28-bundle preview. Do not claim29.",
  "Explicit script references are not browser runtime/visual proof.",
  "Primary-reading scope/history/utility corrections recorded separately;batch026 deployment remains pending."]}
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"versions":13,"originalBodiesRead":["ja","en"],"exactFiniteCases":64,
 "feeExamples":[{"w":v["initialWealth"],"feeApprox":v["numericalFeeBracket"][0][:12]} for v in wealth_cases],
 "actualPreviewBundles":bundles,"reviewedAdded":0},ensure_ascii=False))
if __name__=="__main__":pass
