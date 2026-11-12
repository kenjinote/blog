"""Execute article-extracted scalar entropy/Huffman examples with finite oracles."""
from pathlib import Path
from contextlib import redirect_stdout
from functools import lru_cache
from itertools import product
import os,runpy,math,json,hashlib,io,sys,warnings,re

@lru_cache(None)
def depths(leaves):
    if leaves==1:return {(0,)}
    return {tuple(sorted(d+1 for d in left+right)) for nleft in range(1,leaves) for left in depths(nleft) for right in depths(leaves-nleft)}

def verify(text,lang,scratch):
    os.environ['MPLBACKEND']='Agg'
    scratch.mkdir(parents=True,exist_ok=False)
    blocks=re.findall('^'+chr(96)*3+r'python\n(.*?)^'+chr(96)*3,text,re.M|re.S)
    assert len(blocks)==2
    plot=scratch/'plot.py';program=scratch/'huffman.py'
    for path,block in zip([plot,program],blocks):path.write_text(block.strip()+'\n',encoding='utf-8',newline='\n')
    b=runpy.run_path(str(plot));h=runpy.run_path(str(program))
    entropy=b['binary_entropy'];build=h['build_huffman_tree'];codes_for=h['generate_huffman_codes'];encode=h['encode'];decode=h['decode']
    for k in range(1001):
        p=k/1000;value=entropy(p)
        assert math.isfinite(value) and -1e-14<=value<=1+1e-14 and abs(value-entropy(1-p))<1e-12
    assert entropy(0)==entropy(1)==0 and entropy(.5)==1
    for p in [-.1,1.1,float('nan'),float('inf'),-float('inf')]:
        try:entropy(p)
        except ValueError:pass
        else:raise AssertionError(p)
    roundtrips=0
    for size in range(7):
        for chars in product('abc',repeat=size):
            text_value=''.join(chars);tree=build(text_value);codes=codes_for(tree);payload=encode(text_value,codes)
            assert decode(payload,tree)==text_value and set(codes)==set(text_value)
            assert codes==codes_for(build(text_value[::-1]))
            assert all(not y.startswith(x) for a,x in codes.items() for c,y in codes.items() if a!=c)
            if len(codes)==1:assert list(codes.values())==['0'] and len(payload)==len(text_value)
            roundtrips+=1
    unicode_cases=['ああいうえお','مرحبا🙂مرحبا','कखक','e\u0301é','\0a\0','aaaa']
    for text_value in unicode_cases:
        tree=build(text_value);assert decode(encode(text_value,codes_for(tree)),tree)==text_value
    localized_examples=[]
    for text_value in {'zh-tw':['夏農熵與資訊理論']}.get(lang,[]):
        tree=build(text_value);payload=encode(text_value,codes_for(tree));assert decode(payload,tree)==text_value
        assert len(text_value)==len(set(text_value))==8 and len(payload)==24
        localized_examples.append({'text':text_value,'codePoints':len(text_value),'logicalPayloadBits':len(payload),'roundTrip':True})
    first=codes_for(build('ab'));second=codes_for(build('cd'))
    assert first is not second and set(second)==set('cd') and set(first)==set('ab')
    for value in [None,123,b'abc',['a']]:
        try:build(value)
        except TypeError:pass
        else:raise AssertionError(value)
    tree=build('aaaabbc');single=build('aaaa')
    bad_payloads=[('2',tree),('10x',tree),('0',None),('1',single),('01',single)]
    long_code=next(c for c in codes_for(tree).values() if len(c)>1);bad_payloads.append((long_code[:-1],tree))
    for bits,t in bad_payloads:
        try:decode(bits,t)
        except ValueError:pass
        else:raise AssertionError(bits)
    try:encode('z',codes_for(tree))
    except ValueError:pass
    else:raise AssertionError('unknown symbol accepted')
    optimal_profiles=0
    for size in range(2,6):
        for weights in product(range(1,5),repeat=size):
            text_value=''.join(chr(65+i)*w for i,w in enumerate(weights));codes=codes_for(build(text_value))
            actual=sum(w*len(codes[chr(65+i)]) for i,w in enumerate(weights))
            best=min(sum(w*d for w,d in zip(sorted(weights,reverse=True),shape)) for shape in depths(size))
            assert actual==best
            total=sum(weights);H=-sum((w/total)*math.log2(w/total) for w in weights);L=actual/total
            assert H<=L+1e-12 and L<H+1
            optimal_profiles+=1
    buffer=io.StringIO()
    with redirect_stdout(buffer):runpy.run_path(str(program),run_name='__main__')
    assert 'Logical payload bits: 140\nRound trip: True' in buffer.getvalue()
    import matplotlib.pyplot as plt
    plt.close('all')
    with warnings.catch_warnings(record=True) as plot_warnings:
        warnings.simplefilter('always');runpy.run_path(str(plot),run_name='__main__')
    xs,ys=plt.gca().lines[0].get_data()
    assert len(xs)==len(ys)==101 and xs[50]==.5 and ys[50]==1 and ys[0]==ys[-1]==0
    png=scratch/'binary-entropy.png';plt.gcf().savefig(png,dpi=160,bbox_inches='tight');plt.close('all')
    return {'language':lang,'articleProgramsExecuted':2,'extractedProgramSha256':[hashlib.sha256(p.read_bytes()).hexdigest() for p in [plot,program]],'pythonVersion':sys.version,'binaryEntropyValidPoints':1001,'binaryEntropyInvalidPointsRejected':5,'exhaustiveAbcRoundTripsLength0through6':roundtrips,'unicodeRoundTrips':len(unicode_cases),'localizedOriginalExampleRoundTrips':localized_examples,'repeatedCallNoStaleCodebook':True,'equalFrequenciesDeterministicAcrossInputOrder':True,'nonStringBuildInputsRejected':4,'invalidOrTruncatedPayloadCasesRejected':len(bad_payloads),'unknownSymbolRejected':True,'independentFullBinaryTreeShapeOptimalProfiles':optimal_profiles,'optimalProfileScope':'2through5symbols,eachpositiveintegerweight1through4;allfullbinaryleafdepthmultisets,largestweightstoshortestdepths. Finite independent oracle,not all-input proof.','singleSymbolConvention':'Nonempty0code,L=1,H=0;strictL<H+1notclaimedforthisimplementationcase.','sampleStdout':buffer.getvalue(),'plot':{'path':str(png),'sha256':hashlib.sha256(png.read_bytes()).hexdigest(),'points':101,'peakAtHalf':True,'warnings':[str(w.message) for w in plot_warnings],'visuallyInspectedByThisCode':False},'scope':'Actual article-extracted standalone programs plus finite oracles. No serialized-file format,errorcorrection,all-input proof or native/browser/ledger certification.'}
