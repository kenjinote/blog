"""One read/revised language's static/finite checks; no automatic semantic approval."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from collections import Counter
from html import unescape
import hashlib,importlib.util,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review';FENCE=chr(96)*3
spec=importlib.util.spec_from_file_location('eccpair',D/'verify_batch_034_ja_en.py');pair=importlib.util.module_from_spec(spec);spec.loader.exec_module(pair)
shared=pair.shared
ANNOTATIONS={'zh-cn':{'だが同時に':'但同时','2元符号では ':'对于二元码：',' の位':' 位'},
             'zh-tw':{'だが同時に':'但同時','2元符号では ':'對二元碼：',' の位':' 位'},
             'es':{'だが同時に':'pero a la vez','2元符号では ':'para códigos binarios: ',' の位':' posición','bits / channel use':'bits / uso de canal','bits / second':'bits / segundo'},
             'ko':{'だが同時に':'그러나 동시에','2元符号では ':'이진 부호에서는 ',' の位':' 자리','bits / channel use':'비트 / 채널 사용','bits / second':'비트 / 초'},
             'pt':{'だが同時に':'mas simultaneamente','2元符号では ':'para códigos binários: ',' の位':' posição','bits / channel use':'bits / uso do canal','bits / second':'bits / segundo'},
             'fr':{'だが同時に':'mais simultanément','2元符号では ':'pour les codes binaires : ',' の位':' position','bits / channel use':'bits / utilisation du canal','bits / second':'bits / seconde'},
             'de':{'だが同時に':'doch gleichzeitig','2元符号では ':'für binäre Codes: ',' の位':' Stelle','bits / channel use':'Bit / Kanalnutzung','bits / second':'Bit / Sekunde'},
             'hi':{'だが同時に':'लेकिन साथ ही','2元符号では ':'द्विआधारी कोड के लिए: ',' の位':' का स्थान','bits / channel use':'बिट / चैनल उपयोग','bits / second':'बिट / सेकंड',' bits':' बिट'},
             'id':{'だが同時に':'tetapi sekaligus','2元符号では ':'untuk kode biner: ',' の位':' posisi','bits / channel use':'bit / penggunaan kanal','bits / second':'bit / detik',' bits':' bit'},
             'ru':{'だが同時に':'но одновременно','2元符号では ':'для двоичных кодов: ',' の位':' разряд','bits / channel use':'бит / использование канала','bits / second':'бит / секунду',' bits':' бит',r'\text{dB}':r'\text{дБ}'}}

def main():
    site=Path(sys.argv[1]);lang=sys.argv[2];out=Path(sys.argv[3]);assert not out.exists() and lang in ANNOTATIONS
    audit=json.loads((D/'batch-034-source-audit.json').read_text(encoding='utf-8'))
    reviews=json.loads((D/'batch-034.json').read_text(encoding='utf-8'))
    source=ROOT/audit['versions']['ja']['path'];ja=source.read_text(encoding='utf-8')
    source_hash=shared.shared.digest(source);assert source_hash==reviews['frozenSourceHash']
    prior={}
    for key,entry in reviews['reviews'].items():
        assert entry['sourceHash']==source_hash and shared.shared.digest(ROOT/'content'/key)==entry['translationHash']
        prior[key]=entry['translationHash']
    urls={}
    for language,entry in audit['versions'].items():
        t=(ROOT/entry['path']).read_text(encoding='utf-8')
        slug=json.loads(re.search(r'^slug: (.*)$',t,re.M)[1])
        urls[language]='https://kenji.blog/'+('' if language=='ja' else language+'/')+'p/'+slug+'/'
    entry=audit['versions'][lang];p=ROOT/entry['path'];text=p.read_text(encoding='utf-8')
    original=subprocess.run(['git','show',audit['baselineCommit']+':'+entry['path']],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
    assert hashlib.sha256(original.encode()).hexdigest()==entry['sha256']
    for key in ('date','slug','image','draft'):
        assert re.findall('^'+key+':.*$',text,re.M)==re.findall('^'+key+':.*$',original,re.M)
    assert shared.shared.taxonomy(text)==shared.shared.taxonomy(original)
    assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,9)))
    assert 'lastmod: "2026-11-13"' in text and 'mermaid: true' in text
    core=[m[1].strip() for m in re.finditer(r'\$\$(.*?)\$\$',ja,re.S)];assert len(core)==47
    translated=[]
    for tex in core:
        for a,b in ANNOTATIONS[lang].items():tex=tex.replace(a,b)
        if lang in ('es','pt','fr','de','id','ru'):
            # Decimal-comma typography must preserve every numeric token's value.
            before=tex
            tex=re.sub(r'(\d+)\.(\d+)',r'\1{,}\2',tex)
            assert tex.replace('{,}','.')==before
        translated.append(tex)
    actual=[m[1].strip() for m in re.finditer(r'\$\$(.*?)\$\$',text,re.S)]
    assert Counter(actual)==Counter(translated) and len(actual)==47
    refs=set(re.findall(r'\]\((https://[^)]+)\)',ja));assert len(refs)==10 and set(re.findall(r'\]\((https://[^)]+)\)',text))==refs
    graphs=shared.shared.graphs(text);assert len(graphs)==4
    shape=lambda g:re.sub(r'"[^"\n]*"','""',g)
    assert list(map(shape,graphs))==list(map(shape,shared.shared.graphs(ja)))
    code=re.search('^'+FENCE+r'python\n(.*?)^'+FENCE,text,re.M|re.S)[1]
    shown=re.search('^'+FENCE+r'text\n(.*?)^'+FENCE,text,re.M|re.S)[1]
    assert code.rstrip()==(D/'ecc034_revised_code.py').read_text(encoding='utf-8').rstrip()
    run=subprocess.run([sys.executable,'-c',code],capture_output=True,text=True,encoding='utf-8')
    assert run.returncode==0 and run.stdout==shown
    ns={'__name__':'article_extra_probe'};exec(compile(code,str(p),'exec'),ns)
    inverse_rejected=False
    try:ns['gf_inv'](0)
    except ZeroDivisionError:inverse_rejected=True
    assert inverse_rejected
    payload=list(b'VOYAGER-1');points=[ns['gf_pow'](2,i) for i in range(15)];cw=ns['rs_encode'](payload,points)
    cases=[]
    for pattern in ('initial','scattered'):
        indices=[0,1,2] if pattern=='initial' else [1,6,13]
        for count in range(4):
            r=cw.copy()
            for index,magnitude in list(zip(indices,[255,165,60]))[:count]:r[index]^=magnitude
            assert ns['rs_decode'](r,points,9,3)==payload;cases.append(dict(pattern=pattern,errors=count))
    html=(site/urls[lang].removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
    a=shared.Article();a.feed(html);tex=shared.source_math(text)
    assert shared.shared.render.expressions(''.join(a.math))==tex
    assert all(g.strip() in unescape(html) for g in graphs) and code in a.codes and shown in a.codes
    assert refs<=set(a.links) and len([row for row in a.rows if len(row)==4])==6
    nav=shared.shared.PageParser();nav.feed(html.split('</aside>',1)[0]+'</aside>')
    assert nav.canonical==urls[lang] and nav.language==lang and nav.alternates==dict(urls,**{'x-default':urls['ja']}) and nav.options==urls
    header=text.split('---',2)[1];published=json.loads(re.search(r'^date: (.*)$',header,re.M)[1])
    assert '"datePublished":"'+published+'"' in html and '"dateModified":"2026-11-13' in html
    assert json.loads(re.search(r'^title: (.*)$',header,re.M)[1]) in unescape(html)
    fragments=pair.prose_fragments(text,html)
    if lang=='zh-cn':
        assert not re.search(r'[\u3040-\u30ff]',text)
        assert '**' not in ''.join(a.math)
        for label in ['逐次消除译码（SC）','逐次消除列表译码（SCL）','错误值：','校验子：']:
            assert '<strong>'+label+'</strong>' in html
        assert all(v in ''.join(a.all) for v in ['校验子','擦除','逐次消除','8比特码字','整个RS码字','[1,0,1,1]','[0,1,1]','[1,6,13]'])
        assert '0\\mapsto00000' in text and '1\\mapsto11111' in text
        probe=json.loads((D/'batch-034-zh-cn-original-code-probe.json').read_text(encoding='utf-8'))
        assert probe['originalSourceSha256']==entry['sha256'] and probe['zeroInverseReturned']==1 and probe['displayedOutputBlocks']==0
    if lang=='zh-tw':
        assert not re.search(r'[\u3040-\u30ff]',text) and '**' not in ''.join(a.math)
        for label in ['逐次消除解碼（SC）','逐次消除清單解碼（SCL）','錯誤值：','伴隨式：','直欄（column）','橫列（row）']:
            assert '<strong>'+label+'</strong>' in html
        assert all(v in ''.join(a.all) for v in ['位元組','抹除','航海家','夏農','摺積碼','內插','概似比','整個RS碼字','[1,0,1,1]','[0,1,1]','[1,6,13]'])
        assert '0\\mapsto00000' in text and '1\\mapsto11111' in text
        probe=json.loads((D/'batch-034-zh-tw-original-code-probe.json').read_text(encoding='utf-8'))
        assert probe['originalSourceSha256']==entry['sha256'] and probe['zeroInverseReturned']==1 and probe['displayedOutputBlocks']==0
    if lang=='es':
        assert not re.search(r'[\u3040-\u30ff\u3400-\u9fff]',text)
        for label in ['síndrome','Valores de error:','cancelación sucesiva (SC)','cancelación sucesiva con lista (SCL)']:
            assert '<strong>'+label+'</strong>' in html
        assert '0<p<1/2' in text and r'p\in(0,0,5)' not in text
        assert all(v in ''.join(a.all) for v in ['borrados','cuerpo finito','[1,0,1,1]','[0,1,1]','[1,6,13]'])
        assert '0\\mapsto00000' in text and '1\\mapsto11111' in text
        assert 'Check -- "Sí" --> Done' in graphs[1]
        probe=json.loads((D/'batch-034-es-original-code-probe.json').read_text(encoding='utf-8'))
        assert probe['originalSourceSha256']==entry['sha256'] and probe['zeroInverseReturned']==1 and probe['displayedOutputBlocks']==0
    if lang=='ko':
        assert not re.search(r'[\u3040-\u30ff\u3400-\u9fff]',text)
        for label in ['신드롬','오류값:','순차 제거 복호(SC)','순차 제거 리스트 복호(SCL)']:
            assert '<strong>'+label+'</strong>' in html
        assert all(v in ''.join(a.all) for v in ['소실','유한체','연판정','랭크 부족','이진 자릿수 순서를 뒤집는 순열','[1,0,1,1]','[0,1,1]','[1,6,13]'])
        assert '0\\mapsto00000' in text and '1\\mapsto11111' in text
        assert 'Check -- "예" --> Done' in graphs[1]
        probe=json.loads((D/'batch-034-ko-original-code-probe.json').read_text(encoding='utf-8'))
        assert probe['originalSourceSha256']==entry['sha256'] and probe['zeroInverseReturned']==1 and probe['displayedOutputBlocks']==0
    if lang=='pt':
        assert not re.search(r'[\u3040-\u30ff\u3400-\u9fff]',text)
        for label in ['síndrome','Valores dos erros:','cancelamento sucessivo (SC)','cancelamento sucessivo com lista (SCL)']:
            assert '<strong>'+label+'</strong>' in html
        assert '0<p<1/2' in text and r'p\in(0,0,5)' not in text
        assert all(v in ''.join(a.all) for v in ['apagamentos','corpo finito','posto da matriz','[1,0,1,1]','[0,1,1]','[1,6,13]'])
        assert '0\\mapsto00000' in text and '1\\mapsto11111' in text
        assert 'Check -- "Sim" --> Done' in graphs[1]
        probe=json.loads((D/'batch-034-pt-original-code-probe.json').read_text(encoding='utf-8'))
        assert probe['originalSourceSha256']==entry['sha256'] and probe['zeroInverseReturned']==1 and probe['displayedOutputBlocks']==0
    if lang=='fr':
        assert not re.search(r'[\u3040-\u30ff\u3400-\u9fff]',text)
        # Same prose-only smart-apostrophe normalization as the prior EN comparison.
        prose_html=unescape(html).replace(chr(0x2019),chr(39)).replace(chr(0x2018),chr(39))
        for label in ['syndrome',"Valeurs d'erreur :",'annulation successive (SC)','annulation successive par liste (SCL)']:
            assert '<strong>'+label+'</strong>' in prose_html
        assert '0<p<1/2' in text and r'p\in(0,0,5)' not in text
        assert all(v in ''.join(a.all) for v in ['effacements','corps fini','octet','rang de la matrice','[1,0,1,1]','[0,1,1]','[1,6,13]'])
        assert '0\\mapsto00000' in text and '1\\mapsto11111' in text
        assert 'Check -- "Oui" --> Done' in graphs[1]
        probe=json.loads((D/'batch-034-fr-original-code-probe.json').read_text(encoding='utf-8'))
        assert probe['originalSourceSha256']==entry['sha256'] and probe['zeroInverseReturned']==1 and probe['displayedOutputBlocks']==0
    if lang=='de':
        assert not re.search(r'[\u3040-\u30ff\u3400-\u9fff]',text)
        for label in ['Syndrom','Fehlerwerte:','Successive Cancellation (SC)','Successive Cancellation List (SCL)']:
            assert '<strong>'+label+'</strong>' in html
        assert all(v in ''.join(a.all) for v in ['Auslöschungen','endlichen Körper','Matrixrang','Leitkoeffizient 1','[1,0,1,1]','[0,1,1]','[1,6,13]'])
        assert '0\\mapsto00000' in text and '1\\mapsto11111' in text and '0<p<1/2' in text
        assert 'Check -- "Ja" --> Done' in graphs[1]
        probe=json.loads((D/'batch-034-de-original-code-probe.json').read_text(encoding='utf-8'))
        assert probe['originalSourceSha256']==entry['sha256'] and probe['zeroInverseReturned']==1 and probe['displayedOutputBlocks']==0
    if lang=='hi':
        assert not re.search(r'[\u3040-\u30ff\u3400-\u9fff]',text)
        for label in ['सिंड्रोम','त्रुटि मान:','क्रमिक निरस्तीकरण (SC)','सूची सहित क्रमिक निरस्तीकरण (SCL)']:
            assert '<strong>'+label+'</strong>' in html
        assert all(v in ''.join(a.all) for v in ['मिटाव','परिमित क्षेत्र','रैंक','गुणनात्मक','अग्रगुणांक 1','[1,0,1,1]','[0,1,1]','[1,6,13]'])
        assert '0\\mapsto00000' in text and '1\\mapsto11111' in text and '0<p<1/2' in text
        assert 'Check -- "हाँ" --> Done' in graphs[1]
        assert 'गुणात्मक' not in text and 'आसन्निक' not in text and 'अतिरिक्त पढ़ाई' not in text
        probe=json.loads((D/'batch-034-hi-original-code-probe.json').read_text(encoding='utf-8'))
        assert probe['originalSourceSha256']==entry['sha256'] and probe['zeroInverseReturned']==1 and probe['displayedOutputBlocks']==0
    if lang=='id':
        assert not re.search(r'[\u3040-\u30ff\u3400-\u9fff\u0400-\u04ff\u0600-\u06ff\u0900-\u097f]',text)
        for label in ['sindrom','Nilai kesalahan:','pembatalan berurutan (SC, successive cancellation)','pembatalan berurutan dengan daftar (SCL)']:
            assert '<strong>'+label+'</strong>' in html
        assert all(v in ''.join(a.all) for v in ['Penghapusan (erasure)','medan hingga','peringkat matriks','defisiensi peringkat','[1,0,1,1]','[0,1,1]','[1,6,13]'])
        assert '0\\mapsto00000' in text and '1\\mapsto11111' in text and '0<p<1/2' in text
        assert 'Check -- "Ya" --> Done' in graphs[1]
        assert 'membulatkan pengamatan' not in text
        probe=json.loads((D/'batch-034-id-original-code-probe.json').read_text(encoding='utf-8'))
        assert probe['originalSourceSha256']==entry['sha256'] and probe['zeroInverseReturned']==1 and probe['displayedOutputBlocks']==0
    if lang=='ru':
        assert not re.search(r'[\u3040-\u30ff\u3400-\u9fff\u0600-\u06ff\u0900-\u097f]',text)
        for label in ['синдром','Значения ошибок:','последовательное исключение (SC)','списочного последовательного исключения (SCL)']:
            assert '<strong>'+label+'</strong>' in html
        assert all(v in ''.join(a.all) for v in ['стирания','конечного поля','ранг матрицы','старшим коэффициентом 1','[1,0,1,1]','[0,1,1]','[1,6,13]'])
        assert '0\\mapsto00000' in text and '1\\mapsto11111' in text and '0<p<1/2' in text
        assert 'Check -- "Да" --> Done' in graphs[1]
        probe=json.loads((D/'batch-034-ru-original-code-probe.json').read_text(encoding='utf-8'))
        assert probe['originalSourceSha256']==entry['sha256'] and probe['zeroInverseReturned']==1 and probe['displayedOutputBlocks']==0
    for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
    v=dict(language=lang,path=entry['path'],sha256=shared.shared.digest(p),sourceSha256=source_hash,
        originalSha256=entry['sha256'],texExpressions=sum(tex.values()),displayMath=47,coreDisplayBlocks=47,
        diagrams=4,diagramEdges=[10,7,9,5],references=10,articleExecutablePrograms=1,
        executableCodeSha256=hashlib.sha256(code.rstrip().encode()).hexdigest(),programExitCode=run.returncode,
        stdout=run.stdout,stderr=run.stderr,displayedOutputExact=True,codeAndOutputHtmlExact=True,mathHtmlExact=True,
        proseFragmentsPreserved=fragments,zeroInverseRejected=True,oldEvaluationPointCases=cases,
        datesTaxonomyImageAndNavigationPassed=True,passed=True)
    doc=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=True,versions=[v],
        frozenSourceUnchanged=True,priorRegisteredTranslationHashesUnchanged=prior,
        priorCandidateFiniteEvidence='docs/translation-review/batch-034-candidate-code-validation.json',
        priorJapaneseArithmeticEvidence='docs/translation-review/batch-034-ja-validation-r4.json',
        priorEnglishAuxiliaryEvidence='docs/translation-review/batch-034-ja-en-validation-r2.json',
        reviewedTranslationsAdded=0,publicationPending=True,
        limitations=['One selected static/finite check,not semantic approval; actual original/revised full reading is separately recorded.',
        'Prior registered source/translation hashes unchanged; earlier full checks referenced,not rerun.',
        'No native-speaker/browser/KaTeX/Mermaid execution,whole-site,hardware,all-input,full QR/LDPC/Polar or benchmark certification.'])
    out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v[k] for k in ('language','texExpressions','displayMath','diagrams','proseFragmentsPreserved','passed')}))
if __name__=='__main__':main()
