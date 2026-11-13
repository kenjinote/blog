"""Finite, reproducible boundary witnesses; never computes Kolmogorov complexity."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from fractions import Fraction
import gzip, hashlib, json, math, random, re, sys

ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
audit=json.loads((D/'batch-035-source-audit.json').read_text(encoding='utf-8'))
originals={}
for lang in ('ja','en'):
    e=audit['versions'][lang];t=(ROOT/e['path']).read_text(encoding='utf-8-sig')
    assert hashlib.sha256(t.encode()).hexdigest()==e['sha256'];originals[lang]=t
checks=[]
for n in range(17):
    for c in range(n+1):
        threshold=n-c;short=sum(2**k for k in range(threshold))
        assert short==2**threshold-1
        lower=2**n-short;assert 1<=lower<=2**n
        checks.append(dict(n=n,c=c,shortPrograms=short,incompressibleCountLowerBound=lower))
counterexamples=[]
for n,c in [(0,1),(1,2),(2,3),(5,8)]:
    old=2**n-Fraction(2)**(n-c)+1
    assert old>2**n
    counterexamples.append(dict(n=n,c=c,claimedLowerBound=str(old),totalStrings=2**n))
# Literal strings/UTF-8 storage, not an allocator memory-footprint benchmark.
text='01'*500_000
assert len(text)==1_000_000 and len(text.encode('ascii'))==1_000_000
assert len(text)//8==125_000
ja_phrase='30文字未満の日本語では定義できない最小の正の整数'
en_phrase='The smallest positive integer not definable in under twenty English words'
# An English-specific correct claim must not inherit the Japanese count error.
assert len(en_phrase.split())==11
# A reproducible long-window counterexample to treating practical NCD as identity.
rng=random.Random(3501);x=bytes(rng.getrandbits(8) for _ in range(65536))
compress=lambda value:gzip.compress(value,mtime=0)
cx=len(compress(x));cxx=len(compress(x+x))
assert gzip.decompress(compress(x+x))==x+x
ncd=Fraction(cxx-cx,cx);assert ncd>Fraction(9,10)
# K(n)=log(n)+O(1) cannot be justified by omitting self-delimiting overhead.
# This is a coding construction only, not an actual K computation.
subsequence=[]
for m in (16,32,64,128,256,1024):
    gamma_bits=2*m.bit_length()-1
    assert gamma_bits<m
    subsequence.append(dict(nDescription='2**'+str(m),binaryLengthOfN=m+1,
        prefixGammaLengthOfExponent=gamma_bits,
        scope='Fixed program can reconstruct n=2**m from gamma(m); fixed interpreter overhead not measured.'))
out=D/'batch-035-original-finite-probe.json';assert not out.exists()
receipt=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),
    originalHashes={l:audit['versions'][l]['sha256'] for l in originals},
    countingCases=checks,unrestrictedCGreaterThanNCounterexamples=counterexamples,
    storage=dict(abstractBits=1_000_000,packedBytes=125_000,asciiUtf8Bytes=len(text.encode('ascii')),
        scope='Packed abstract bits versus one-byte ASCII characters; Python/container overhead not measured.'),
    berryPhrases=dict(japanese=ja_phrase,japaneseUnicodeCodePoints=len(ja_phrase),originalJapaneseClaim=24,
        japaneseClaimMatches=len(ja_phrase)==24,english=en_phrase,englishWhitespaceWords=len(en_phrase.split()),englishClaimMatches=True),
    gzipSameFileNcd=dict(inputBytes=len(x),seed=3501,compressedXBytes=cx,compressedXXBytes=cxx,
        ratio=str(ncd),approx=float(ncd),roundTripExact=True,
        scope='One chosen deterministic input/profile and finite-window gzip. No claim of computing K/NID, all compressors, general metric proof or performance benchmark.'),
    prefixIntegerCodingSubsequence=subsequence,reviewedTranslationsAdded=0,passed=True,
    limitations=['No Kolmogorov complexity or halting oracle implemented/computed.',
        'Finite arithmetic and selected codec examples; no theorem proof, actual million-coin experiment or complete pi-normality test.',
        'Only original JA/EN full bodies read; other11 bodies unread. No source revision,translation approval,build or publication certification.'])
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(countingCases=len(checks),invalidDomainWitnesses=counterexamples,berry=receipt['berryPhrases'],gzip=receipt['gzipSameFileNcd']),ensure_ascii=False))
