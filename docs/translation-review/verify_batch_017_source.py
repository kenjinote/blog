"""Reproduce public mathematical counterexamples for the factoring article audit.

No executable article code exists. This performs independent arithmetic and does
not mark any translation reviewed, certify cryptographic security or prove factor primality.
Usage: python docs/translation-review/verify_batch_017_source.py --output NEW.json
"""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from fractions import Fraction
import argparse,json,math

def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def fermat(N):
    x=math.isqrt(N)
    if x*x<N:x+=1
    start=x;count=0
    while True:
        count+=1;y=math.isqrt(x*x-N)
        if y*y==x*x-N:return {'N':N,'start':start,'successX':x,'candidates':count,'factors':[x-y,x+y]}
        x+=1
assert prime(1009) and prime(1013) and prime(104729)
close=fermat(1009*1013);far=fermat(3*104729)
assert close['candidates']==1 and far['candidates']==51806
assert all((1<<(N.bit_length()-1))<=N<(1<<N.bit_length()) for N in range(1,10001))
assert 5>math.sqrt(15) and 15==3*5
assert all(prime(p) for p in (521,523,1019,1021))
products=[{'p':p,'q':q,'primeBits':[p.bit_length(),q.bit_length()],'product':p*q,'productBits':(p*q).bit_length()} for p,q in [(521,523),(1019,1021)]]
assert [v['productBits'] for v in products]==[19,20]
N=21;f=lambda x:(x*x+1)%N;x=f(2);y=f(f(2));d=math.gcd(abs(x-y),N)
assert (x,y,d)==(5,5,21)
N,x,y=1155,76,1;g1,g2=math.gcd(x-y,N),math.gcd(x+y,N)
assert (x*x-y*y)%N==0 and x%N not in (y%N,(-y)%N) and (g1,g2)==(15,77)
assert not prime(g1) and not prime(g2)
c=(64/9)**(1/3);converted=c*math.log(2)**(1/3)
def mul(u,v):return (u[0]*v[0]+5*u[1]*v[1],u[0]*v[1]+u[1]*v[0])
beta=(Fraction(1,2),Fraction(1,2));square=mul(beta,beta)
assert (square[0]-beta[0]-1,square[1]-beta[1])==(0,0)
assert beta[0].denominator==2 and beta[1].denominator==2
P=int('64135289477071580278790190170577389084825014742943447208116859632024532344630238623598752668347708737661925585694639798853367')
Q=int('33372027594978156556226010605355114227940760344767554666784520987023841729210037080257448673296881877565718986258036932062711')
RSA250=int('2140324650240744961264423072839333563008614715144755017797754920881418023447140136643345519095804679610992851872470914587687396261921557363047454770520805119056493106687691590019759405693457452230589325976697471681738069364894699871578494975937497937')
assert P*Q==RSA250 and len(str(RSA250))==250 and RSA250.bit_length()==829
repros={'scope':'Independent public mathematical fixtures; original JA/EN article has no executable code, only2Mermaid blocks. Not cryptographic attacks or an implementation audit.',
'bitLengthBoundsInputs':10000,'exampleN15':{'N':15,'bits':(15).bit_length(),'twoToBits':1<<(15).bit_length(),'largestPrimeFactor':5,'sqrtN':math.sqrt(15)},
'equalPrimeBitLengthExamples':products,'fermatClose':close,'fermatUnbalanced':far,
'rhoFixedPolynomialFailure':{'N':21,'seed':2,'polynomial':'x^2+1 mod N','firstFloydValues':[5,5],'gcd':21,'needsRestart':True},
'congruentSquaresCompositeDivisors':{'N':1155,'x':76,'y':1,'gcdMinus':15,'gcdPlus':77,'bothComposite':True},
'bigOUpperNotTight':'f(b)=1 belongs to O(2^b), yet f(b+1)/f(b)=1, not2.',
'lEndpointCounterexample':'b^(c+o1) can be b^c*ln(b), taking o1=lnln(b)/ln(b); ratio to b^c is unbounded.',
'gnfsNaturalLogConstant':c,'gnfsLeadingConstantWithBinaryBitLength':converted,
'integerRingCounterexample':{'alpha':'sqrt5','betaCoordinatesInQsqrt5':['1/2','1/2'],'betaSatisfiesMonicPolynomial':'beta^2-beta-1=0','integralButNotInZalpha':True,'scope':'Exact rational pair arithmetic for a counterexample; not GNFS implementation.'},
'rsa250Announcement':{'url':'https://caramba.loria.fr/rsa250.txt','announcedAt':'2020-02-28','p':str(P),'q':str(Q),'N':str(RSA250),'productVerified':True,'digits':250,'bits':829,'reportedApproxCoreYears':2700,'claimedCurrentRecord':False,'primalityOfPublishedFactorsIndependentlyCertified':False}}

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
if args.output.exists():
    parser.error('Preserve existing evidence; choose a new output path.')
document={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),
          'scope':'Independent mathematical fixtures for the initial audit, not article-code execution or translation review.',
          'arithmeticReproductions':repros,'allPassed':True}
args.output.write_text(json.dumps(document,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'fermatCandidates':[close['candidates'],far['candidates']],
                  'congruentSquareCompositeDivisors':[g1,g2],'rsa250ProductVerified':True}))
