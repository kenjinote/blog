"""Execute the reviewed cryptography article's Python examples and offline fixtures.

Run from this repository with Python and cryptography (reviewed with 3.12.14/50.0.2).
Use --output NEW.json to preserve a new result; existing files are never overwritten.
Without --output, print the complete result. No ledger or article files are changed.
This verifies code/math fixtures and structure, not translation meaning, native
fluency, production security or publication. Ephemeral keys remain in memory.
"""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import argparse, ast, contextlib, hashlib, io, json, math, re, sys
import cryptography
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root/'scripts'))
from translation_reviews import digest
slug='modern-cryptography-public-key-hash-signature'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,help='Write a new validation JSON; never overwrite an existing result.')
args=parser.parse_args()
out=args.output
if out is not None: assert not out.exists(), 'Keep historical validation; use a new output path.'
files=[]; programs=[]; formulas=[]
def rejects(expected, fn):
    try: fn()
    except expected: return
    raise AssertionError('Expected '+expected.__name__)
def computation_ast(body):
    tree=ast.parse(body)
    for statement in ast.walk(tree):
        if isinstance(statement,ast.Assign) and len(statement.targets)==1 and isinstance(statement.targets[0],ast.Name) and statement.targets[0].id in {'message','doc_message'}:
            value=statement.value
            if isinstance(value,ast.Constant) and isinstance(value.value,bytes): pass
            elif isinstance(value,ast.Call) and isinstance(value.func,ast.Attribute) and value.func.attr=='encode' and isinstance(value.func.value,ast.Constant) and isinstance(value.func.value.value,str) and len(value.args)==1 and isinstance(value.args[0],ast.Constant) and value.args[0].value=='utf-8' and not value.keywords: pass
            else: raise AssertionError('Unexpected localized input expression')
            statement.value=ast.Constant(value=b'LOCALIZED_SAMPLE_MESSAGE')
    for node in ast.walk(tree):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='print':
            for arg in node.args:
                if isinstance(arg,ast.Constant) and isinstance(arg.value,str): arg.value='LOCALIZED_PRINT_LABEL'
    return ast.dump(tree,include_attributes=False)
expected_by_language={'ko': ['이것은 현대 암호학에 대한 매우 기밀성이 높은 메시지입니다.', '현대 암호학은 안전한 해시 함수에 크게 의존합니다.', '계약서: A는 B에게 1000달러를 지불하는 데 동의합니다.'], 'fr': ['Ceci est un message hautement confidentiel sur la cryptographie moderne.', "La cryptographie moderne s'appuie fortement sur des fonctions de hachage sécurisées.", 'Document contractuel : la partie A accepte de payer 1000 $ à la partie B.'], 'ar': ['هذه رسالة سرية للغاية حول التشفير الحديث.', 'يعتمد التشفير الحديث بشكل كبير على دوال التجزئة الآمنة.', 'وثيقة عقد: يوافق الطرف أ على دفع 1000 دولار للطرف ب.']}
for lang in ['ja','en','zh-cn','es','ko','pt','zh-tw','hi','fr','de','ar','ru','id']:
    path=root/'content/post'/slug/('index.md' if lang=='ja' else 'index.'+lang+'.md')
    text=path.read_text(encoding='utf-8')
    blocks=re.findall(r'^```python\n(.*?)^```',text,re.M|re.S)
    graphs=re.findall(r'^```mermaid\n(.*?)^```',text,re.M|re.S)
    displays=re.findall(r'^\$\$(.*?)\$\$$',text,re.M|re.S)
    assert len(blocks)==3 and len(graphs)==3 and len(displays)==10
    assert [g.count('-->')+g.count('-.->') for g in graphs]==[7,8,5]
    scope=[]
    for i,body in enumerate(blocks):
        env={}
        with contextlib.redirect_stdout(io.StringIO()): exec(compile(body,str(path)+f'#block{i+1}','exec'),env)
        scope.append(env)
    encryption, hashing, signing=scope
    if lang in expected_by_language:
        expected=expected_by_language[lang]
        for sample,key,content in zip(scope,['message','message','doc_message'],expected):
            assert sample[key]==content.encode('utf-8')
        assert len(encryption['message'])<=190

    assert encryption['decrypted_message']==encryption['message']
    pub=encryption['public_key']; priv=encryption['private_key']
    def oaep(label=None): return padding.OAEP(mgf=padding.MGF1(hashes.SHA256()),algorithm=hashes.SHA256(),label=label)
    payloads=[b'',b'x',b'x'*189,b'x'*190,'暗号🔑'.encode('utf-8')]
    for message in payloads:
        ciphertext=pub.encrypt(message,oaep())
        assert priv.decrypt(ciphertext,oaep())==message
    rejects(ValueError,lambda:pub.encrypt(b'x'*191,oaep()))
    ciphertext=encryption['ciphertext']
    rejects(ValueError,lambda:priv.decrypt(ciphertext,oaep(b'wrong-label')))
    altered=bytes([ciphertext[0]^1])+ciphertext[1:]
    rejects(ValueError,lambda:priv.decrypt(altered,oaep()))
    wrong=rsa.generate_private_key(public_exponent=65537,key_size=2048)
    rejects(ValueError,lambda:wrong.decrypt(ciphertext,oaep()))
    for name,func in [('sha256',hashlib.sha256),('sha3',hashlib.sha3_256)]:
        assert hashing['hash_result_'+name]==func(hashing['message']).digest()
    vectors=[(hashes.SHA256,hashlib.sha256,'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'),(hashes.SHA3_256,hashlib.sha3_256,'3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532')]
    for alg,func,abc in vectors:
        for message in [b'',b'abc',b'x'*55,b'x'*56,b'x'*64,b'x'*136,'暗号🔑'.encode()]:
            h=hashes.Hash(alg()); h.update(message[:1]); h.update(message[1:])
            assert h.finalize()==func(message).digest()
        assert func(b'abc').hexdigest()==abc
    sk=signing['signing_key']; vk=signing['verification_key']; pss=signing['pss']
    assert sk.private_numbers().p != priv.private_numbers().p
    for message in [b'', signing['doc_message'], '署名🔑'.encode()]:
        sig=sk.sign(message,pss,hashes.SHA256()); vk.verify(sig,message,pss,hashes.SHA256())
    sig=signing['signature']; doc=signing['doc_message']
    rejects(InvalidSignature,lambda:vk.verify(sig,doc+b'!',pss,hashes.SHA256()))
    rejects(InvalidSignature,lambda:wrong.public_key().verify(sig,doc,pss,hashes.SHA256()))
    rejects(InvalidSignature,lambda:vk.verify(bytes([sig[0]^1])+sig[1:],doc,pss,hashes.SHA256()))
    rejects(InvalidSignature,lambda:vk.verify(sig[:-1],doc,pss,hashes.SHA256()))
    rejects(InvalidSignature,lambda:vk.verify(sig,doc,padding.PKCS1v15(),hashes.SHA256()))
    rejects(InvalidSignature,lambda:vk.verify(sig,doc,padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=0),hashes.SHA256()))
    urls=re.findall(r'\]\((https://[^)]+)\)',text)
    assert len(urls)==9 and len(set(urls))==9
    for target in ['euclidean-algorithm','楕円曲線暗号の数学的基礎とcppでの実装']:
        assert (root/'content/post'/target/('index.md' if lang=='ja' else 'index.'+lang+'.md')).exists()
    assert (path.parent/'eyecatch.jpg').exists()
    assert 'date: "2026-09-22T08:00:00+09:00"' in text and 'lastmod: "2026-10-27"' in text
    programs.append([computation_ast(b) for b in blocks]); formulas.append(displays)
    files.append({'language':lang,'path':path.relative_to(root/'content').as_posix(),'hash':digest(path),'standalonePythonBlocksPassed':3,'localizedMessageByteLengths':[len(scope[0]['message']),len(scope[1]['message']),len(scope[2]['doc_message'])],'oaepRoundtripPayloads':len(payloads),'oaepInvalidCasesRejected':4,'hashExampleDigestsMatched':2,'hashStreamingCasesMatched':14,'abcKnownDigestsMatched':2,'pssValidMessages':3,'pssInvalidCasesRejected':6,'separateEncryptionAndSigningKeys':True,'displayMath':len(displays),'mermaidEdgeCounts':[7,8,5],'primaryReferenceUrls':urls})
assert all(p==programs[0] for p in programs)
assert all(f==formulas[0] for f in formulas)
p,q,e=61,53,17; n=p*q; phi=(p-1)*(q-1); d=pow(e,-1,phi)
assert d==2753 and pow(61,phi,n)==1220
for m in range(n):
    assert pow(pow(m,e,n),d,n)==m
    for r in [p,q]: assert pow(m,e*d,r)==m%r
assert (e*d-1)%math.lcm(p-1,q-1)==0
assert 256-2*32-2==190
# Small curve group illustrates the stated scalar range; not a production curve or security proof.
def add(a,b):
    if a is None:return b
    if b is None:return a
    x,y=a; X,Y=b
    if x==X and (y+Y)%17==0:return None
    slope=((3*x*x+2)*pow(2*y,-1,17) if a==b else (Y-y)*pow(X-x,-1,17))%17
    u=(slope*slope-x-X)%17
    return u,(slope*(x-u)-y)%17
g=(5,1); pt=None; points=[]
for k in range(1,20):
    pt=add(pt,g)
    if k<19:
        assert pt is not None and (pt[1]**2-pt[0]**3-2*pt[0]-2)%17==0
        points.append(pt)
    else:assert pt is None
assert len(set(points))==18 and (4*2**3+27*2**2)%17!=0
v={'version':1,'checkedAt':datetime.now(ZoneInfo('Asia/Tokyo')).isoformat(),'runtime':{'python':sys.version.split()[0],'cryptography':cryptography.__version__},'files':files,'crossLanguage':{'pythonComputationAstEqualIgnoringPrintLabelsAndLocalizedSampleMessages':True,'allTenDisplayFormulasEqual':True},'mathematics':{'rsaToyMessagesPassed':3233,'nonCoprimeEulerCounterexample':{'M':61,'N':3233,'phi':3120,'eulerPowerModN':1220,'rsaRoundtrip':61},'crtResiduesCheckedForEveryToyMessage':True,'lambdaInverseConditionPassed':True,'oaepBoundBytes':190,'eccToyCurve':'p=17,a=2,b=2,G=(5,1),order=19; 18 distinct nonidentity public points; 19G=infinity','limitations':'Finite examples support the explanations; they are not general correctness/security proofs or production parameter recommendations.'},'limitations':['Offline fixtures only; no side-channel analysis or formal proof.','No live TLS/CA, certificate-chain conformance, penetration or native-speaker human review.','Mermaid source edges checked, not visual rendering.'],'buildPending':True,'publicationPending':True}
if out is not None:
    out.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'versions':len(files),'pythonBlocksPassed':sum(f['standalonePythonBlocksPassed'] for f in files),'displayMath':sum(f['displayMath'] for f in files),'mermaidEdges':sum(sum(f['mermaidEdgeCounts']) for f in files),'rsaToyMessages':v['mathematics']['rsaToyMessagesPassed'],'validation':str(out)},ensure_ascii=False))
else:
    print(json.dumps(v,ensure_ascii=False,indent=2))
