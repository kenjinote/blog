"""Bayes pre-audit: original metadata and independent arithmetic, not approval."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone,timedelta
import json,re,hashlib,itertools,math,os,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/"docs/translation-review"
out=D/"batch-026-source-audit.json";assert not out.exists()
sys.path.insert(0,str(ROOT/"scripts"));from check_multilingual import PageParser
folder=ROOT/"content/post/bayes-theorem"
site=Path(os.environ["TEMP"])/"kenji-priority-review-20261024/public-28-bundles-two-envelopes-final"
ledger=json.loads((ROOT/"data/translation_reviews.json").read_text(encoding="utf-8"));versions={}
fence=chr(96)*3
for p in sorted(folder.glob("index*.md")):
    lang="ja" if p.name=="index.md" else p.name.split(".")[1]
    key=p.relative_to(ROOT/"content").as_posix();assert key not in ledger["reviews"]
    text=p.read_text(encoding="utf-8-sig");header=text.split("---",2)[1];slug=re.search(r"^slug:\s*['\"]([^'\"]+)",header,re.M)[1]
    html=(site/("" if lang=="ja" else lang)/"p"/slug/"index.html").read_text(encoding="utf-8")
    parser=PageParser();parser.feed(html.split("</aside>",1)[0]+"</aside>")
    scripts=re.findall(r"<script\b[^>]*>.*?</script>",html,re.S)
    versions[lang]={"path":p.relative_to(ROOT).as_posix(),"sha256":hashlib.sha256(text.replace("\r\n","\n").encode()).hexdigest(),"canonical":parser.canonical,"datePublished":re.search(r'"datePublished":"([^"]+)"',html)[1],"slug":slug,"mathFlag":re.findall(r"^math:.*$",header,re.M),"mermaidFlag":re.findall(r"^mermaid:.*$",header,re.M),"explicitKaTeXScriptReference":any("katex" in s for s in scripts),"explicitMermaidScriptReference":any("mermaid" in s for s in scripts),"fullOriginalMetadataBodyAndDiagramsRead":lang in ["ja","en"],"reviewed":False}
assert len(versions)==13 and len(ledger["reviews"])==312 and all(v["reviewKind"]=="ai" for v in ledger["reviews"].values())
for lang in ["ja","en"]:
    s=(ROOT/versions[lang]["path"]).read_text(encoding="utf-8")
    assert re.findall(r"^"+fence+r"(\w+)\n",s,re.M)==["mermaid","mermaid"]
    assert not re.search(r"^(math|mermaid):",s.split("---",2)[1],re.M)

tp,fn,fp,tn=99,1,495,9405;total=tp+fn+fp+tn;assert total==10000
diagnostic={"population":total,"truePositive":tp,"falseNegative":fn,"falsePositive":fp,"trueNegative":tn,"prevalence":F(tp+fn,total),"sensitivity":F(tp,tp+fn),"specificity":F(tn,tn+fp),"falsePositiveRate":F(fp,fp+tn),"positiveProbability":F(tp+fp,total),"positivePredictiveValue":F(tp,tp+fp),"falseDiscoveryProportionAmongPositives":F(fp,tp+fp),"overallAccuracy":F(tp+tn,total)}
assert diagnostic["prevalence"]==F(1,100) and diagnostic["sensitivity"]==F(99,100)
assert diagnostic["positivePredictiveValue"]==F(1,6) and diagnostic["falseDiscoveryProportionAmongPositives"]==F(5,6)
assert diagnostic["overallAccuracy"]==F(594,625)!=diagnostic["sensitivity"]
bayes_cases=0;skipped=0
for a,b,c,d in itertools.product(range(6),repeat=4):
    n=a+b+c+d
    if not n or not a+b or not a+c:skipped+=1;continue
    p_a=F(a+b,n);p_b=F(a+c,n);p_b_a=F(a,a+b)
    assert p_b_a*p_a/p_b==F(a,a+c)==F(a,n)/p_b
    bayes_cases+=1
assert bayes_cases+skipped==1296

joint=[]
for cls in [0,1]:
    q=F(9,10) if cls else F(1,10)
    for f1,f2 in itertools.product([0,1],repeat=2):
        joint.append((cls,f1,f2,F(1,2)*(q if f1 else 1-q)*(q if f2 else 1-q)))
assert sum(w for _,_,_,w in joint)==1
for cls in [0,1]:
    mass=sum(w for c,_,_,w in joint if c==cls)
    p1=sum(w for c,f1,_,w in joint if c==cls and f1)/mass
    p2=sum(w for c,_,f2,w in joint if c==cls and f2)/mass
    assert sum(w for c,f1,f2,w in joint if c==cls and f1 and f2)/mass==p1*p2
p11=sum(w for _,f1,f2,w in joint if f1 and f2)
p1=sum(w for _,f1,_,w in joint if f1);p2=sum(w for _,_,f2,w in joint if f2)
assert p11==F(41,100) and p1*p2==F(1,4)!=p11
xor=[(a,b,a^b) for a,b in itertools.product([0,1],repeat=2)]
for i,j in itertools.combinations(range(3),2):
    assert Counter((row[i],row[j]) for row in xor)==Counter({(0,0):1,(0,1):1,(1,0):1,(1,1):1})
assert (1,1,1) not in xor

coin=[]
for n in range(1,21):
    weights=[F(math.comb(n,k),2**n) for k in range(n+1)]
    assert sum(weights)==1 and sum(F(k,n)*w for k,w in enumerate(weights))==F(1,2)
    exact=weights[n//2] if n%2==0 else F(0);assert exact<1
    coin.append({"tosses":n,"probabilityExactlyHalfHeads":exact})

# Exact polynomial integration of a hand-specified posterior, not CAS/NN execution.
integral=lambda coefficients:sum((F(c,k+1) for k,c in enumerate(coefficients)),F(0))
posterior=[0,0,12,-12];assert integral(posterior)==1
predictive=integral([0]+posterior);mode=F(2,3)
derivative=lambda x:24*x-36*x*x
assert derivative(mode)==0 and predictive==F(3,5)!=mode
assert derivative(F(1,3))>0 and derivative(F(5,6))<0
result={"version":1,"checkedAt":datetime.now(timezone(timedelta(hours=9))).isoformat(),"versions":versions,"image":{"path":"content/post/bayes-theorem/eyecatch.jpg","sha256":hashlib.sha256((folder/"eyecatch.jpg").read_bytes()).hexdigest()},"baselineSite":str(site),"auxiliaryChecks":{"hypotheticalDiagnosticExample":diagnostic,"bayesJointTablesChecked":bayes_cases,"zeroOrUndefinedConditioningTablesSkipped":skipped,"conditionalIndependentButMarginalDependent":{"states":8,"pBothOne":p11,"productMarginals":p1*p2},"pairwiseIndependentButNotJointIndependent":{"xorStates":4,"pairTablesChecked":3,"p111":"0","productMarginals":"1/8"},"finiteCoinCases":coin,"posteriorModeVersusPredictive":{"model":"Uniform prior on[0,1],ordered data1,1,0,posterior12theta^2(1-theta)","normalization":F(1),"mode":mode,"posteriorPredictive":predictive,"scope":"Hand-specified polynomial coefficients integrated by exact rational arithmetic;derivative sign argument separately checked. No general symbolic integration,BNN training,empirical clinical validation or LLN proof."}},"reviewedTranslationsAdded":0,"currentAiTranslations":312,"unreviewedTranslations":12720,"humanReviews":0,"limitations":["Pre-audit only;no article source edits or review entry.","OnlyJAENoriginal full bodies read;other11metadata/hash/HTML inventory only.","Numerical medical example is hypothetical,not measured clinical test performance or advice.","ExplicitKaTeX/Mermaid script references found;presence does not certify browser runtime or visual rendering.","Primary-reading scope and still-unverified history/BO/BNN claims recorded separately."]}
out.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=lambda v:str(v) if isinstance(v,F) else v)+"\n",encoding="utf-8")
print(json.dumps({"versionsInventoried":13,"fullOriginalBodiesRead":["ja","en"],"bayesJointTables":bayes_cases,"skipped":skipped,"diagnosticPPV":str(diagnostic["positivePredictiveValue"]),"accuracy":str(diagnostic["overallAccuracy"]),"posteriorMode":str(mode),"posteriorPredictive":str(predictive),"reviewedAdded":0}))
