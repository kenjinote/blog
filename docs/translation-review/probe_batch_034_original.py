from pathlib import Path
from datetime import datetime,timezone,timedelta
import json,re,hashlib,subprocess,sys,io,contextlib,itertools,os
root=Path('C:/work/kenji.blog');d=root/'docs/translation-review';slug='error-correcting-codes-hamming-reed-solomon-ldpc-shannon-capacity-information-theory';folder=root/'content/post'/slug
out=d/'batch-034-source-audit.json';probe=d/'batch-034-original-code-probe.json';assert not out.exists() and not probe.exists()
scratch=Path(os.environ['TEMP'])/'kenji-priority-review-20261024/ecc-original-034';assert not scratch.exists();scratch.mkdir()
digest=lambda s:hashlib.sha256(s.encode()).hexdigest()
commit=subprocess.run(['git','rev-parse','HEAD'],cwd=root,capture_output=True,text=True,check=True).stdout.strip()
versions={};texts={}
for p in sorted(folder.glob('index*.md')):
    lang=p.name[6:-3];text=p.read_text(encoding='utf-8-sig');rel=p.relative_to(root).as_posix()
    original=subprocess.run(['git','show',commit+':'+rel],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True).stdout;assert original==text
    texts[lang]=text
    versions[lang]={'path':rel,'sha256':digest(text),'lines':len(text.splitlines()),'utf8BytesNormalizedLf':len(text.encode()),'h2Headings':re.findall(r'^## .+$',text,re.M),'fenceLanguages':re.findall('^'+chr(96)*3+r'(\w+)\n',text,re.M),'displayMathDelimiters':text.count('$$'),'fullOriginalMetadataBodyAndDiagramsRead':lang in ('ja','en'),'reviewed':False}
assert len(versions)==13
results=[]
for lang in ('ja','en'):
    text=texts[lang];fence=chr(96)*3
    codes=re.findall('^'+fence+r'python\n(.*?)^'+fence,text,re.M|re.S);assert len(codes)==1
    code=codes[0];p=scratch/(lang+'.py');p.write_text(code,encoding='utf-8')
    run=subprocess.run([sys.executable,str(p)],capture_output=True,text=True,encoding='utf-8',timeout=15)
    shown=re.findall('^'+fence+r'text\n(.*?)^'+fence,text,re.M|re.S);assert len(shown)==1
    result={'language':lang,'sourceSha256':versions[lang]['sha256'],'codeSha256':digest(code),'actualProgramExitCode':run.returncode,'actualStdout':run.stdout,'actualStderr':run.stderr,'displayedTextOutput':shown[0],'displayedOutputMatchesActual':run.stdout.strip()==shown[0].strip()}
    ns={'__name__':'original_probe'}
    exec(compile(code,str(p),'exec'),ns)
    if lang=='ja':
        poly=ns['poly_eval'];add=ns['gf_add'];mul=ns['gf_mul']
        point=list(range(1,16));msg=list(b'VOYAGER-1');cw=[poly(msg,x) for x in point]
        decoder=ns['reed_solomon_berlekamp_welch_decode']
        result['finiteField']='GF(257)';result['byteCoefficientExampleProducesNonByteSymbol']={'message':[255,1],'point':1,'value':poly([255,1],1)}
        result['fixedRadiusErrorCases']=[]
        for count in range(5):
            received=cw[:]
            for i in range(count):received[i]=add(received[i],i+1)
            with contextlib.redirect_stdout(io.StringIO()):
                try:got=decoder(point,received,len(msg),3);case={'actualErrors':count,'result':got,'matches':got==msg}
                except Exception as e:case={'actualErrors':count,'exception':type(e).__name__,'message':str(e)}
            result['fixedRadiusErrorCases'].append(case)
    else:
        gf=ns['GF256']();point=gf.exp[:15];msg=list(b'VOYAGER-1');cw=[gf.poly_eval(msg,x) for x in point]
        result['finiteField']='GF(2^8),polynomial0x11D';result['fixedRadiusLinearSolveCases']=[]
        for count in range(5):
            received=cw[:]
            for i in range(count):received[i]^=i+1
            k=len(msg);t=3
            A=[[gf.power(x,j) for j in range(k+t)]+[gf.mul(y,gf.power(x,j)) for j in range(t)] for x,y in zip(point,received)]
            b=[gf.mul(y,gf.power(x,t)) for x,y in zip(point,received)]
            try:
                sol=gf.solve_linear_system(A,b);E=sol[k+t:]+[1];valid=[(x,y) for x,y in zip(point,received) if gf.poly_eval(E,x)!=0]
                got=gf.solve_linear_system([[gf.power(x,j) for j in range(k)] for x,y in valid[:k]],[y for x,y in valid[:k]])
                case={'actualErrors':count,'result':got,'matches':got==msg}
            except Exception as e:case={'actualErrors':count,'exception':type(e).__name__,'message':str(e)}
            result['fixedRadiusLinearSolveCases'].append(case)
        # Independent shift/XOR reduction oracle for all byte products.
        def oracle(a,b):
            value=0
            for _ in range(8):
                if b&1:value^=a
                b>>=1;a<<=1
                if a&256:a^=0x11d
            return value
        assert all(gf.mul(a,b)==oracle(a,b) for a in range(256) for b in range(256))
        result['independentByteMultiplicationPairs']=65536
        result['inverseCases']=sum(gf.mul(a,gf.inv(a))==1 for a in range(1,256));assert result['inverseCases']==255
    results.append(result)
assets=[{'path':p.relative_to(root).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in folder.rglob('*') if p.is_file() and p.suffix!='.md']
audit={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'baselineCommit':commit,'article':slug,'versions':versions,'assets':assets,'manualReadingScope':'JAandEN completeoriginalmetadata,all8sections/equations/4Mermaidgraphs/Pythonprogram/displayedoutput/comparisontablesread. Other11bodiesnotread;structureinventoryonly. No revisedbody orreviewrecord yet.','reviewedTranslationsAdded':0,'currentAiTranslations':408,'unreviewedTranslations':12624,'humanReviews':0,'initialFindings':['10^-16W equals100aW,not0.1aW;receivedpower/23Wdistance/imagehistoryneedprimaryverification. Voyager1and2notbothallplanetflybys.','QRerrorcorrectionpercentagesarenotunconditionalimagearea/logocoverage/10msguarantees;functionalpatterns/blockdistribution/unknownerrorsversuserasuresmatter.','JAeverymemorylesschannelstrictlypositivecapacityfalse;ENnonnegativecorrectbutcapacitynotnoisealone,continuouschannelinputconstraintsandunitsmustbespecified. Asymptoticallysmallerrornotfinitezeroerror;AWGNln2infimumnotuniverseconstant/equalitywithpositiverate.','JA2t+1<=d iff t=floor((d-1)/2) shouldboundt,notarbitraryt equality. Mixederror/erasureguaranteesquantifiedoverallpatterns,notallreceivedwordsuniquelydecodableexactlyunderbound.','JAperfectcodeclassificationovergeneralallcodesandVoyagerbinary/ternaryGolayclaimsneedverification;ENomitsparagraph. Zero syndromeiscodewordmembership,notproofnochannelerrors.','Hbinarysyndromenumberonlyforbinarycolumnorder;systematicHrequireslookup. GeneralHammingcomputationalcomplexitynotuniversallyO1;SECDEDnoteveryECCDRAMarchitecture.','RSrootboundisfactor-theoremoverfield,notFundamentalTheoremofAlgebra. Evaluationn<=qversuscyclicn=q-1/shortened,QRrootindexconventionsmustseparate. JAsection4.5omittedEN.','ForneyformulaextraXfactorappearsinconsistentwithENexplicitS(x)=sumS_j*x^(j-1),jstarts1;reproduceandverifyprimary.','JAactualcodeGF257butENGF256;notdirecttranslationofsameprogram;captions/proseclaimdifferentfields. FixedtGaussianeliminationassumesuniquefullranksquarematrix,likelyfailsfewerthantradius. Actualrunsandboundarycasesseparatelyrecorded.','JAcode3of15symbols=20percent,not30percent;nonadjacentdamagedindicesnotcontiguousburst. GF257evaluationsarenotallbytes. NoQ/Edivisionorpostdecodereencoding/distanceverification.','Sparsitydoesnotguaranteenosmallcycles;LDPCdimensionn-rankHnotn-numberrowsunlessindependent. LLR2y/sigma2requiresequallylikelyBPSK. LDPCthreshold0.0045dBisnotuniversalultimate-1.59norfiniteperformanceguarantee.','PolarI(W)uniforminput=symmetriccapacity,notgeneralasymmetriccapacity;finiteNnotexactcapacity/zeroerrorfloor. SCversusSCLlistfactor/5GshortUCIexceptions/productadoptionclaimsmustverify.'],'primaryReadingToDate':[],'originalCodeProbe':'docs/translation-review/batch-034-original-code-probe.json','limitations':['Pre-audit only;other11bodiesnotread,nobodycertified.','No current034primarysourcebodyreadyet;initialsourceconcernsarenotallconfirmedfacts.','No rewrittenarticle/completecompressor-or-ECCimplementation/benchmark/browser/nativecertification.','033matchingCI43229194255successverified;live442article+3tagprobecurrentlyrunning,separatelyrecorded.']}
out.write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
probe.write_text(json.dumps({'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'actualOriginalProgramsRun':2,'results':results,'reviewedTranslationsAdded':0,'scope':'OriginalJA/ENcompletePythonprogramrunandfiniteboundary/fieldoraclechecks;notrevisedcode/proseapproval,allinputproof,QRdecoder/spacecraftimplementation/benchmark.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'versions':13,'programsRun':2,'results':[{k:r[k] for k in r if k in ('language','actualProgramExitCode','displayedOutputMatchesActual','fixedRadiusErrorCases','fixedRadiusLinearSolveCases','independentByteMultiplicationPairs')} for r in results]},ensure_ascii=False))
