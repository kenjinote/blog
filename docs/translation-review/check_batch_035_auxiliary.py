"""Finite coding/arithmetic witnesses, not computation of C/K or halting probabilities."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import heapq,json,math

def entropy(ps):return math.fsum(-float(p)*math.log2(float(p)) for p in ps if p)
def huffman(ps):
    heap=[p for p in ps if p];heapq.heapify(heap);cost=F(0)
    while len(heap)>1:
        w=heapq.heappop(heap)+heapq.heappop(heap);cost+=w;heapq.heappush(heap,w)
    return cost
def ceil_surprisal(p):
    k=0
    while p*2**k<1:k+=1
    return k
def sfe(ps):
    cumulative=F(0);words=[]
    for p in ps:
        assert p>0
        length=ceil_surprisal(p)+1;mid=cumulative+p/2
        integer=(mid*2**length).__floor__();word=format(integer,'0'+str(length)+'b')
        lo=F(integer,2**length);hi=F(integer+1,2**length)
        assert cumulative<=lo<hi<=cumulative+p
        assert len(word)<=math.ceil(-math.log2(float(p))-1e-12)+2
        words.append(word);cumulative+=p
    assert cumulative==1
    ordered=sorted(words);assert not any(b.startswith(a) for a,b in zip(ordered,ordered[1:]))
    return words

def run():
    gamma=[];mass=F(0)
    for n in range(1,1024):
        bits=bin(n)[2:];word='0'*(len(bits)-1)+bits
        zeros=len(word)-len(word.lstrip('0'));decoded=int(word[zeros:zeros+zeros+1],2)
        assert decoded==n and len(word)==2*(n.bit_length()-1)+1
        gamma.append(word);mass+=F(1,2**len(word))
    ordered=sorted(gamma);assert not any(b.startswith(a) for a,b in zip(ordered,ordered[1:]))
    assert mass==1-F(1,1024)
    profiles=0;sfe_symbols=0
    for total in range(2,17):
        for a in range(total+1):
            for b in range(total-a+1):
                ps=[F(a,total),F(b,total),F(total-a-b,total)];h=entropy(ps);length=float(huffman(ps))
                assert h-1e-12<=length<h+1
                positive=[p for p in ps if p];words=sfe(positive)
                assert len(set(words))==len(positive);sfe_symbols+=len(words);profiles+=1
    sequential=[]
    for size in range(1,10):
        sequences=list(product((0,1),repeat=size));ps=[]
        for seq in sequences:
            probability=F(1)
            for j,bit in enumerate(seq):
                p1=F(1,3) if j==0 else F(1,4) if seq[j-1]==0 else F(3,4)
                probability*=p1 if bit else 1-p1
            ps.append(probability)
        words=sfe(ps);decode=dict(zip(words,sequences));assert all(decode[w]==s for w,s in zip(words,sequences))
        sequential.append(dict(tokens=size,sequences=len(sequences),sumProbability=str(sum(ps)),prefixFree=True,allDyadicIntervalsContained=True,allCodewordRoundTripsExact=True,entropy=entropy(ps)))
    residual=[]
    for n in range(1,17):
        # A computable illustrative rational, explicitly NOT an actual Omega_U.
        omega=F(1,3);a=F((omega*2**n).__floor__(),2**n)
        q=F((omega*2**(n+3)).__floor__(),2**(n+3))
        assert a<q<=omega<a+F(1,2**n) and omega-q<F(1,2**n)
        # Equality at the lower endpoint is sufficient too: original JA was valid here.
        assert omega-a<F(1,2**n)
        residual.append(dict(bits=n,strictCrossingResidualBoundPassed=True,equalityAtLowerEndpointAlsoSufficient=True))
    return dict(gammaIntegers=1023,gammaKraftMass=str(mass),gammaPrefixFreeAndDecoded=True,
        rationalHuffmanProfiles=profiles,sfeFiniteProfileSymbols=sfe_symbols,sequentialDyadicCodes=sequential,
        sequentialCodewordRoundTrips=sum(x['sequences'] for x in sequential),
        omegaResidualIllustrations=residual,
        scope='Finite exact rational/dyadic codes and selected inequalities. SFE construction is an auxiliary, not an article program or production arithmetic coder. No actual C/K, shortest program, optimal machine, Omega value, ML/Brudno theorem, corpus/LLM, NCD universality or benchmark computed/proved.')

if __name__=='__main__':
    import sys
    out=Path(sys.argv[1]);assert not out.exists()
    result=run();out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
