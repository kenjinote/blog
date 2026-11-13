from pathlib import Path
from datetime import datetime,timezone,timedelta
from itertools import product,combinations
import importlib.util,json,hashlib,random,sys,io,contextlib
root=Path('C:/work/kenji.blog');out=root/'docs/translation-review/batch-034-candidate-code-validation.json';assert not out.exists()
p=Path(__file__).parent/'ecc034_revised_code.py'
s=importlib.util.spec_from_file_location('candidate',p);v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
def carryless(a,b):
    raw=0
    for bit in range(8):
        if b&(1<<bit):raw^=a<<bit
    for degree in range(14,7,-1):
        if raw&(1<<degree):raw^=0x11d<<(degree-8)
    return raw
assert all(v.gf_mul(a,b)==carryless(a,b) for a in range(256) for b in range(256))
assert all(v.gf_mul(a,v.gf_inv(a))==1 for a in range(1,256))
G=v.G;H=v.H
assert all(sum(G[i][j]*H[r][j] for j in range(7))%2==0 for i in range(4) for r in range(3))
words=[]
for m in product((0,1),repeat=4):words.append((list(m),v.hamming_encode(m)))
assert min(sum(a!=b for a,b in zip(x,y)) for i,(_,x) in enumerate(words) for _,y in words[i+1:])==3
hc=0
for m,c in words:
    for index in range(-1,7):
        r=c[:]
        if index>=0:r[index]^=1
        assert v.hamming_decode(r)==m;hc+=1
# Full independent GF256 degree<2 codebook, including coefficients outside
# the tested received alphabet. Direct sum evaluation, not candidate Horner.
points=[0,1,2,3]
products=[[carryless(a,x) for x in points] for a in range(256)]
book=[([a,b],[a^z for z in products[b]]) for a in range(256) for b in range(256)]
assert min(sum(z!=0 for z in c) for m,c in book if any(m))==3
received_cases=accepted=rejected=0
for r in product(range(4),repeat=4):
    expected=[]
    for m,c in book:
        distance=0
        for a,b in zip(r,c):
            distance+=a!=b
            if distance>1:break
        if distance<=1:expected.append(m)
    assert len(expected)<=1
    try:
        got=v.rs_decode(r,points,2,1)
        assert expected==[got];accepted+=1
    except ValueError:
        assert not expected;rejected+=1
    received_cases+=1
assert received_cases==256
# Enumerate every one-symbol position and nonzero error magnitude for 3
# messages, covering 0, a degree<k-1 polynomial and an ordinary payload.
patterns=0
for msg in ([0,0,0],[0,1,0],[255,17,9]):
    pts=[0,1,2,3,4];cw=v.rs_encode(msg,pts)
    assert v.rs_decode(cw,pts,3,1)==msg;patterns+=1
    for i in range(5):
        for error in range(1,256):
            r=cw[:];r[i]^=error
            assert v.rs_decode(r,pts,3,1)==msg;patterns+=1
# Seeded finite coverage of all weights up to radius, rectangular systems,
# zero evaluation point, zero polynomial, and zero padding of coefficients.
rng=random.Random(340013);random_cases=0
for n,k,t in [(15,9,3),(17,9,3),(7,3,2),(6,2,2),(8,4,1),(1,1,0),(256,1,0)]:
    pts=list(range(n))
    for trial in range(8):
        msg=[rng.randrange(256) for _ in range(k)]
        if trial==0:msg=[0]*k
        if trial==1:msg[-1]=0
        cw=v.rs_encode(msg,pts)
        for weight in range(t+1):
            r=cw[:]
            for i in rng.sample(range(n),weight):r[i]^=rng.randrange(1,256)
            assert v.rs_decode(r,pts,k,t)==msg;random_cases+=1
assert v.solve_linear_system([[1,1],[1,1]],[3,3],2)==[3,0]
assert v.solve_linear_system([[1,1],[1,1]],[3,4],2) is None
invalid=[
    lambda:v.rs_encode([], [1]),
    lambda:v.rs_encode([1,2],[1]),
    lambda:v.rs_encode([256],[1]),
    lambda:v.rs_encode([True],[1]),
    lambda:v.rs_encode([1],[]),
    lambda:v.rs_encode([1],[0,0]),
    lambda:v.rs_encode([1],[256]),
    lambda:v.rs_encode([1],[True]),
    lambda:v.rs_decode([1],[0,1],1,0),
    lambda:v.rs_decode([1],[0],0,0),
    lambda:v.rs_decode([1],[0],True,0),
    lambda:v.rs_decode([1],[0],1,True),
    lambda:v.rs_decode([1],[0],1,-1),
    lambda:v.rs_decode([1],[0],1,1),
    lambda:v.rs_decode([-1],[0],1,0),
    lambda:v.rs_decode([1.0],[0],1,0),
    lambda:v.gf_mul(-1,1),
    lambda:v.gf_mul(1,256),
    lambda:v.gf_inv(0),
    lambda:v.gf_pow(1,-1),
    lambda:v.gf_pow(1,True),
    lambda:v.hamming_encode([1,0,1]),
    lambda:v.hamming_decode([True]*7),
    lambda:v.poly_divmod([1],[])
]
for f in invalid:
    try:f()
    except (ValueError,ZeroDivisionError):pass
    else:raise AssertionError('Invalid example accepted')
doc={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'candidatePath':str(p),'candidateSha256':hashlib.sha256(p.read_bytes()).hexdigest(),'allPassed':True,'fieldProductPairs':65536,'nonzeroInverses':255,'hammingCases':hc,'hammingMinimumDistance':3,'independentRsCodebookWords':len(book),'rsCodebookParameters':{'n':4,'k':2,'q':256,'distance':3},'fullCodebookReceivedVectors':received_cases,'oracleAccepted':accepted,'oracleRejected':rejected,'allSingleErrorMagnitudesAndPositionsCases':patterns,'seededRadiusCases':random_cases,'rankDeficientConsistentAndInconsistentSystems':2,'invalidCases':len(invalid),'reviewedTranslationsAdded':0,'scope':'Unpublishedcandidatecodeonly. Independentcarrylessfieldoracle/full65536worddegree<2codebookoracle for256receivedvectors,finiteposition/magnitude/seededcases,notall-inputproof,completeQRformat/hardware/spacecraftimplementation/benchmark. Articlebodyandtranslationreviewpending.'}
out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(doc))
