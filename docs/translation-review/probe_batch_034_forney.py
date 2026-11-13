from pathlib import Path
from datetime import datetime,timezone,timedelta
import json,re,hashlib,os
root=Path('C:/work/kenji.blog');d=root/'docs/translation-review';out=d/'batch-034-original-forney-probe.json';assert not out.exists()
slug='error-correcting-codes-hamming-reed-solomon-ldpc-shannon-capacity-information-theory'
text=(root/'content/post'/slug/'index.en.md').read_text(encoding='utf-8')
code=re.findall('^'+chr(96)*3+r'python\n(.*?)^'+chr(96)*3,text,re.M|re.S)[0]
ns={'__name__':'forney_auxiliary'};exec(compile(code,'original-en-article','exec'),ns);gf=ns['GF256']()
# Single error: S_j=Y*X^j, j starts at 1; Lambda(z)=1-X*z.
# S(z)=S_1+S_2*z+..., hence Omega(z)=Y*X (constant),
# and Lambda'(z)=-X, equal to X in characteristic two.
checked=wrong=0
for X in range(1,256):
    for Y in range(1,256):
        omega=gf.mul(Y,X);derivative=X
        fixed=gf.div(omega,derivative)
        article=gf.div(gf.mul(X,omega),derivative)
        assert fixed==Y
        wrong+=article!=Y;checked+=1
assert checked==65025 and wrong==64770
doc={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'originalEnSourceSha256':hashlib.sha256(text.encode()).hexdigest(),'singleErrorPairsChecked':checked,'originalExtraXFormulaWrongPairs':wrong,'correctedFormulaMatches':checked,'witness':{'X':2,'Y':3,'S1':6,'omega':6,'lambdaDerivative':2,'originalExtraXResult':gf.div(gf.mul(2,6),2),'withoutExtraXResult':gf.div(6,2)},'reason':'OriginalENexplicitS(z)=sum_{j=1}^{2t}S_j*z^(j-1),S_j=Y*X^j. Foroneerror,Lambda=1-X*z,Omega=YX. Then-YX/(-X)=Y;extraXyieldsXY. Characteristic2negativeequalspositive. Otherfirst-root/syndromeconventionscanlegitimatelychangeXfactor;claimonlythisarticleexplicitconvention.','initialAuxiliaryFailureRetained':'docs/translation-review/probe_batch_034_forney_initial.py','initialFailure':'Assertion expected65535 pairs;actual255*255=65025. Correctedonlyexpectedcasecount;allGFcomputationsand64770mismatchesunchanged. Initialfailedscriptpreserved.','reviewedTranslationsAdded':0,'scope':'IndependentfinitealgebraicwitnessbasedonarticledefinitionsusingoriginalGF256arithmetic,notexecutionofarevisedRSdecoder orcompleteproof/QRimplementation/benchmark.'}
out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(doc,ensure_ascii=False))
