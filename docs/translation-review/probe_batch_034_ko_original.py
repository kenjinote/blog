from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json,re,subprocess,sys
root=Path(__file__).resolve().parents[2];d=root/'docs/translation-review'
audit=json.loads((d/'batch-034-source-audit.json').read_text(encoding='utf-8'))
entry=audit['versions']['ko'];p=root/entry['path'];text=p.read_text(encoding='utf-8')
assert hashlib.sha256(text.encode()).hexdigest()==entry['sha256']
out=d/'batch-034-ko-original-code-probe.json';assert not out.exists()
f=chr(96)*3;code=re.search('^'+f+r'python\n(.*?)^'+f,text,re.M|re.S)[1]
run=subprocess.run([sys.executable,'-c',code],capture_output=True,text=True,encoding='utf-8',timeout=15)
assert run.returncode==0
ns={'__name__':'original_ko_probe'};exec(compile(code,str(p),'exec'),ns)
gf=ns['GF256']();msg=list(b'VOYAGER-1');pts=gf.exp[:15];cw=[gf.eval_poly(msg,x) for x in pts];cases=[]
for count in range(5):
    received=cw[:]
    for i in range(count):received[i]^=i+1
    k=len(msg);t=3
    a=[[gf.power(x,j) for j in range(k+t)]+[gf.mul(y,gf.power(x,j)) for j in range(t)] for x,y in zip(pts,received)]
    b=[gf.mul(y,gf.power(x,t)) for x,y in zip(pts,received)]
    try:
        solved=gf.solve(a,b);locator=solved[k+t:]+[1]
        pairs=[(x,y) for x,y in zip(pts,received) if gf.eval_poly(locator,x)!=0][:k]
        recovered=gf.solve([[gf.power(x,j) for j in range(k)] for x,y in pairs],[y for x,y in pairs])
        result=dict(errors=count,recovered=recovered,matches=recovered==msg)
    except Exception as e:result=dict(errors=count,exception=type(e).__name__,message=str(e))
    cases.append(result)
inverses=sum(gf.mul(x,gf.inv(x))==1 for x in range(1,256));assert inverses==255
doc=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),
    originalSourcePath=entry['path'],originalSourceSha256=entry['sha256'],originalCodeSha256=hashlib.sha256(code.encode()).hexdigest(),
    actualProgramExitCode=run.returncode,actualStdout=run.stdout,actualStderr=run.stderr,
    displayedOutputBlocks=len(re.findall('^'+f+r'text\n',text,re.M)),
    zeroInverseReturned=gf.inv(0),nonzeroInverseCases=inverses,fixedRadiusCases=cases,
    fullOriginalBodyRead=True,reviewedTranslationsAdded=0,
    scope='Unmodified original KO program run; direct GF class calls/RS linear reconstruction follow the original steps for selected inputs. No new Hamming decoder API invented, no displayed-output mismatch claim because KO has no output block. Not full QR/hardware/all-input or prose approval.')
assert doc['zeroInverseReturned']==1
assert all(cases[i].get('exception')=='StopIteration' for i in range(3)) and cases[3]['matches'] and not cases[4]['matches']
out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(exitCode=run.returncode,zeroInverseReturned=doc['zeroInverseReturned'],cases=cases),ensure_ascii=False))
