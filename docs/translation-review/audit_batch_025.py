"""Pre-review evidence: metadata plus exact auxiliary arithmetic, not article approval."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from datetime import datetime,timezone,timedelta
import json,re,hashlib,os,sys
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'scripts'));from check_multilingual import PageParser
folder=ROOT/'content/post/2つの封筒のパラドックス';out=ROOT/'docs/translation-review/batch-025-source-audit.json';assert not out.exists();site=Path(os.environ['TEMP'])/'kenji-priority-review-20261024/public-26-bundles-two-envelopes-before'
versions={};fence=chr(96)*3
for p in sorted(folder.glob('index*.md')):
 lang='ja' if p.name=='index.md' else p.name.split('.')[1];s=p.read_text(encoding='utf-8-sig');slug=re.search(r'^slug:\s*[\'"]([^\'"]+)',s,re.M)[1];prefix='' if lang=='ja' else lang+'/'
 html=(site/(prefix+'p/'+slug)/'index.html').read_text(encoding='utf-8');parser=PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>');date=re.search(r'"datePublished":"([^"]+)"',html)[1]
 versions[lang]={'path':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(s.replace('\r\n','\n').encode()).hexdigest(),'slug':slug,'canonical':parser.canonical,'datePublished':date,'fullOriginalBodyMetadataAndDiagramsRead':lang in ['ja','en'],'reviewed':False}
assert len(versions)==13
for lang in ['ja','en']:
 s=(folder/('index.md' if lang=='ja' else 'index.en.md')).read_text(encoding='utf-8');assert len(re.findall(r'^'+fence+r'mermaid\n(.*?)^'+fence,s,re.M|re.S))==2
 assert not re.findall(r'^'+fence+r'(python|cpp|c|rust|javascript)\n',s,re.M)

def table(prior):
 assert sum(prior.values())==1 and all(s>0 and w>0 for s,w in prior.items());joint=[]
 for s,p in prior.items():joint.extend([(F(s),F(2*s),p/2),(F(2*s),F(s),p/2)])
 grouped=defaultdict(list)
 for x,y,p in joint:grouped[x].append((y,p))
 rows=[]
 for x,items in sorted(grouped.items()):
  px=sum(p for _,p in items);mean=sum(y*p for y,p in items)/px;q=sum(p for y,p in items if y==2*x)/px
  rows.append({'x':x,'probability':px,'probabilityOtherDouble':q,'expectedOther':mean,'conditionalGain':mean-x})
 assert sum(r['probability'] for r in rows)==1
 assert sum(r['probability']*r['conditionalGain'] for r in rows)==0
 assert sum(x*p for x,_,p in joint)==sum(y*p for _,y,p in joint)
 return rows

fixed=[]
for s in [1,2,10,10000]:
 rows=table({s:F(1)});stay=F(3*s,2);assert sum(r['x']*r['probability'] for r in rows)==stay
 fixed.append({'s':s,'expectedStay':stay,'expectedSwitch':stay})
finite=[table({1:F(1)}),table({5000:F(1,2),10000:F(1,2)}),table({1:F(49,100),2:F(1,100),4:F(1,2)})]
middle={r['x']:r for r in finite[1]};assert middle[10000]['probabilityOtherDouble']==F(1,2) and middle[10000]['expectedOther']==12500
nonmonotone={r['x']:r for r in finite[2]};assert nonmonotone[4]['probabilityOtherDouble']>nonmonotone[2]['probabilityOtherDouble']
r=F(2,3);normalization_cases=0
for n in range(101):
 prefix=sum((1-r)*r**j for j in range(n+1));tail=r**(n+1);assert prefix+tail==1;normalization_cases+=1
posteriors=[]
for n in range(1,101):
 x=F(2**n);low=(1-r)*r**n/2;high=(1-r)*r**(n-1)/2;q=low/(low+high);mean=(low*2*x+high*x/2)/(low+high)
 assert q==F(2,5) and mean==F(11,10)*x and mean>x
 if n in [1,2,10,100]:posteriors.append({'n':n,'x':x,'probabilityOtherDouble':q,'expectedOther':mean})
truncations=[]
for n in range(33):
 prior={2**j:(1-r)*r**j/(1-r**(n+1)) for j in range(n+1)};rows=table(prior);assert rows[-1]['conditionalGain']==-F(2**n)
 if n in [0,1,2,5,10,20,32]:truncations.append({'maximumExponent':n,'mass':sum(prior.values()),'largestObservation':rows[-1],'weightedMeanGain':sum(a['probability']*a['conditionalGain'] for a in rows)})
positive_negative_partials=[]
for n in [0,1,2,10,32]:
 partial=sum(F(2**j)*(1-r)*r**j for j in range(n+1));positive_negative_partials.append({'maximumExponent':n,'partialExpectedS':partial,'partialPositiveGain':partial/2,'partialNegativeGain':partial/2})
ratio=F(5,4);ratio_result={'meanYOverX':ratio,'meanXOverY':ratio,'meanProductOfReciprocalRatios':F(1),'productOfMeans':ratio**2};assert ratio**2!=1
grid=sorted({F(j,8) for j in range(1,257)}|{F(2)**j for j in range(-8,13)});f=lambda x:1/(1+x)**2
for x in grid:
 low=f(x)/2;high=f(x/2)/4;q=low/(low+high);mean=(low*2*x+high*x/2)/(low+high)
 assert mean>x and mean==x*(2*f(x)+f(x/2)/4)/(f(x)+f(x/2)/2)
proof={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'versions':versions,'image':{'path':'content/post/2つの封筒のパラドックス/img/two_envelopes.jpg','sha256':hashlib.sha256((folder/'img/two_envelopes.jpg').read_bytes()).hexdigest()},'scope':'Original JA/EN complete metadata/body/twoMermaid diagrams read. Other11translations only metadata/hash/baselineHTMLdate inventoried,not manually read or reviewed. No executable article code in JA/EN. All arithmetic below is auxiliary exact Fraction verification,not article-program execution.','auxiliary':{'fixedSmallerAmounts':fixed,'finitePriors':finite,'normalizationPrefixTailCases':normalization_cases,'geometricProperPrior':'P(S=2^n)=(1/3)(2/3)^n,n>=0. Sum=1 because prefix=1-r^(N+1),r=2/3<1 and tail tends0.','possiblePositiveProbabilityObservations':'X=2^n,n>=0 only;conditioning outside support not claimed.','geometricPosteriorCases':100,'geometricPosteriorExamples':posteriors,'xEquals1ExpectedOther':2,'finiteTruncationsChecked':33,'finiteTruncationExamples':truncations,'divergenceArgument':'E[S]=(1/3)sum(4/3)^n=+infinity. Positive and negative parts of Y-X each have expectation(1/2)E[S]=infinity;unconditional signed gain undefined. Nonnegative tower identity remains valid with infinite values;do not subtract infinity-infinity.','positiveNegativePartialExamples':positive_negative_partials,'ratioExpectations':ratio_result,'continuousDensity':'f(s)=1/(1+s)^2,s>0. Integral0toL=1-1/(1+L),tending1;mean infinite. Conditional densities use1/2 and1/4 mixture/Jacobian factors.','continuousRationalSubstitutionCases':len(grid),'continuousScope':'Exact rational substitution against derived conditional-density formula;no numerical quadrature or symbolic integration execution claimed.'},'reviewedTranslationsAdded':0,'publicationPending':True,'limitations':['Finite exact checks supplement explicit geometric/analytic arguments,not a universal proof.','No native-language or browser/diagram visual certification.','Original article remains unmodified;no AI review entry recorded by this audit.']}
out.write_text(json.dumps(proof,ensure_ascii=False,indent=2,default=lambda v:str(v) if isinstance(v,F) else v)+'\n',encoding='utf-8');print(json.dumps({'languagesInventoried':13,'fullOriginalBodiesRead':['ja','en'],'auxiliaryGeometricPosteriorCases':100,'finiteTruncations':33,'continuousSubstitutionCases':len(grid),'reviewedAdded':0}))
