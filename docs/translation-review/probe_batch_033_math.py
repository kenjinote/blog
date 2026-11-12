from pathlib import Path
from datetime import datetime,timezone,timedelta
from fractions import Fraction
from itertools import product
import json,math
root=Path('C:/work/kenji.blog');out=root/'docs/translation-review/batch-033-original-math-probe.json';assert not out.exists()
counts=[]
for n in range(1,17):
    for c in range(1,n+1):
        shorter=sum(2**k for k in range(n-c+1));assert shorter==2**(n-c+1)-1 and Fraction(shorter,2**n)<Fraction(1,2**(c-1))
        counts.append({'n':n,'c':c,'maxCandidateShortOutputs':shorter})
toy_cases=0
for n in range(1,9):
    universe=[''.join(v) for length in range(n+1) for v in product('01',repeat=length)]
    for value in product('01',repeat=n):
        chosen=''.join(value)
        def swap(s):return chosen if s=='' else '' if s==chosen else s
        outputs=[swap(s) for s in universe]
        assert len(set(outputs))==len(universe) and all(swap(swap(s))==s for s in universe)
        assert swap(chosen)=='' and swap('')==chosen
        toy_cases+=1
def bwt(s):
    rows=sorted(s[i:]+s[:i] for i in range(len(s)))
    return ''.join(row[-1] for row in rows),rows.index(s),rows
def inverse(last,index):
    first=sorted(last);ranks={};lf=[];starts={c:first.index(c) for c in set(first)}
    for c in last:
        rank=ranks.get(c,0);lf.append(starts[c]+rank);ranks[c]=rank+1
    chars=[];row=index
    for _ in last:chars.append(last[row]);row=lf[row]
    return ''.join(reversed(chars))
bwt_cases=0
for n in range(7):
    for chars in product('abc',repeat=n):
        s=''.join(chars)+'$';last,index,rows=bwt(s);assert inverse(last,index)==s and sorted(last)==sorted(s);bwt_cases+=1
last,index,rows=bwt('banana$');assert last=='annb$aa' and index==4
assert rows==['$banana','a$banan','ana$ban','anana$b','banana$','na$bana','nana$ba']
def compositions(total,parts):
    if parts==1:yield (total,);return
    for head in range(1,total-parts+2):
        for tail in compositions(total-head,parts-1):yield (head,)+tail
profiles=pairs=inverses=0
for M in [2,4,8,16]:
    for m in range(1,min(4,M)+1):
        for freq in compositions(M,m):
            starts=[sum(freq[:i]) for i in range(m)]
            def encode(x,s):return (x//freq[s])*M+x%freq[s]+starts[s]
            def decode(y):
                slot=y%M;s=next(i for i in range(m) if starts[i]<=slot<starts[i]+freq[i])
                return freq[s]*(y//M)+slot-starts[s],s
            seen=set()
            for x in range(128):
                for s in range(m):
                    y=encode(x,s);assert decode(y)==(x,s) and y not in seen;seen.add(y);pairs+=1
            for y in range(256):
                x,s=decode(y);assert encode(x,s)==y;inverses+=1
            profiles+=1
arithmetic_cases=0
for n in range(9):
    for symbols in product('01',repeat=n):
        low=Fraction(0);high=Fraction(1);probability=Fraction(1)
        for s in symbols:
            width=high-low
            if s=='0':high=low+width/3;probability/=3
            else:low=low+width/3;probability*=Fraction(2,3)
        width=high-low;assert width==probability
        K=0
        while Fraction(1,2**K)>width/2:K+=1
        scaled=low*2**K;j=-(-scaled.numerator//scaled.denominator)
        assert low<=Fraction(j,2**K) and Fraction(j+1,2**K)<=high
        assert K < -math.log2(float(probability))+2+1e-12
        arithmetic_cases+=1
L=2;H=1;Z=Fraction(1,2);normalized_kl=0;raw_q_expression=1
assert L==H+normalized_kl+math.log2(1/Z)
assert H+raw_q_expression+math.log2(1/Z)==3!=L
interval_counts=[{'L':L,'oldHalfOpenIntegerStates':len(range(L,2*L-1)),'correctHalfOpenIntegerStates':len(range(L,2*L))} for L in [2,4,1024,4096]]
assert all(v['oldHalfOpenIntegerStates']==v['L']-1 and v['correctHalfOpenIntegerStates']==v['L'] for v in interval_counts)
doc={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'allPassed':True,'countingCases':len(counts),'countingCaseScope':'n1through16,c1throughn,exactfinitegeometriccounts;not exhaustiveallinjectivecompressors','fileSpecificSwapEncoderExamples':toy_cases,'quantifierCounterexample':'For each chosen nonempty x use a different fixed injective swap E_x interchanging x and empty,otherwiseidentity. Every chosen x compresses under its own E_x but emptyexpands;decoderdescription/sharedalgorithmcost isnot included. This refutes movingforallx outsideforallE;not a universalcompressor orKolmogorovcomplexityproof.','tansIntervalIntegerCounts':interval_counts,'bwtRoundTripsWithUniqueSentinel':bwt_cases,'bananaExample':{'lastColumn':last,'primaryIndex':index,'sortedRows':rows},'ransFrequencyProfiles':profiles,'ransStateSymbolRoundTrips':pairs,'ransStateInverseChecks':inverses,'ransScope':'PositivecompositionsofM2,4,8,16 over1through4symbols;statex0through127 andencodedstatey0through255. Formula-bijectionfinitechecks,notrenormalizedbitstream/serializedANScompressor.','exactRationalArithmeticIntervalExamples':arithmetic_cases,'arithmeticScope':'FixedbinarymodelP0=1/3,P1=2/3,allstringslength0through8,knownlengthandmodel;dyadiccontainedintervalexists. No precision/framing/modelcost orcompleteencoder/decoder implementation.','englishKlCounterexample':{'P':[0.5,0.5],'lengths':[2,2],'Z':0.5,'normalizedQ':[0.5,0.5],'L':2,'H':1,'normalizedKL':0,'slackBits':1,'wrongUnnormalizedQExpression':1,'wrongDoubleCountedTotal':3},'byteUnitExample':{'oneMiBBits':8*2**20,'oneDecimalMBBits':8*10**6},'exampleAsciiLengths':{'std::vector<int>':len('std::vector<int>'),'content/post/index':len('content/post/index')},'articleExecutablePrograms':0,'reviewedTranslationsAdded':0,'limitations':['Independentfiniteauxiliarychecks derivedfromreadJAENoldmath,notexecutionofnonexistentarticleprograms.','Notfullmathematicalproof,nobenchmarks/LLMexperiments/thirdpartycompressorimplementation.','Noarticlecorrectionsorreviewledgerrecords added;other11translationbodiesunread.']}
out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(doc,ensure_ascii=False))
