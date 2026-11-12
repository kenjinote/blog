"""Selected lossless article source/decoded-HTML checks, not prose approval."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from html.parser import HTMLParser
from html import unescape
import argparse,hashlib,importlib.util,json,re,subprocess,math
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
spec=importlib.util.spec_from_file_location('shared',D/'verify_batch_028.py');shared=importlib.util.module_from_spec(spec);spec.loader.exec_module(shared)
FENCE=chr(96)*3;TICK=chr(96)

class Article(HTMLParser):
    def __init__(self):super().__init__();self.depth=0;self.skip=0;self.math=[];self.all=[];self.codes=[];self.active_code=False;self.links=[];self.rows=[];self.cell=None;self.row=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='section' and 'article-content' in a.get('class','').split():self.depth=1
        elif self.depth and tag=='section':self.depth+=1
        if not self.depth:return
        if tag in ('pre','code'):self.skip+=1
        if tag=='code':assert not self.active_code;self.active_code=True;self.codes.append('')
        if tag=='a':self.links.append(a.get('href',''))
        if tag=='tr':self.row=[]
        if tag in ('td','th'):self.cell=''
    def handle_data(self,data):
        if not self.depth:return
        self.all.append(data)
        if not self.skip:self.math.append(data)
        if self.active_code:self.codes[-1]+=data
        if self.cell is not None:self.cell+=data
    def handle_endtag(self,tag):
        if not self.depth:return
        if tag in ('td','th') and self.cell is not None:self.row.append(self.cell.strip());self.cell=None
        if tag=='tr' and self.row is not None:self.rows.append(self.row);self.row=None
        if tag=='code':assert self.active_code;self.active_code=False
        if tag in ('pre','code'):self.skip-=1;assert self.skip>=0
        if tag=='section':self.depth-=1

def source_math(text):
    text=shared.strip(text)
    text=re.sub(re.escape(TICK)+r'[^'+TICK+r']*'+re.escape(TICK),'',text)
    return shared.render.expressions(text)

def auxiliary():
    cases=[(b'A',1,99,b'A'*100),(b'XY',2,5,b'XYXYXYX')]
    for value,distance,length,expected in cases:
        output=bytearray(value)
        for _ in range(length):output.append(output[-distance])
        assert bytes(output)==expected
    for value,distance in [(b'std::vector<int>',200),(b'content/post/index',412)]:
        output=bytearray(value+b'.'*(distance-len(value)))
        for _ in range(len(value)):output.append(output[-distance])
        assert bytes(output[-len(value):])==value
    probabilities=[.5,.99,.01,1/256]
    bits=-sum(math.log2(p) for p in probabilities)
    nll=-sum(math.log(p) for p in probabilities)/len(probabilities)
    assert abs(bits+math.log2(math.prod(probabilities)))<1e-12
    assert abs(nll-math.log(2)*bits/len(probabilities))<1e-12
    entropy=-.99*math.log2(.99)-.01*math.log2(.01)
    assert abs(entropy-.080793)<1e-6 and abs(1/entropy-12.4)<.1
    io=[]
    for U,C,vio,vdec in [(10**6,250000,10**8,2*10**8),(10**6,250000,10**9,10**7),(10**6,10**6,10**8,10**8)]:
        raw=U/vio;compressed=C/vio+U/vdec;io.append({'inputBytes':U,'compressedBytes':C,'ioBytesPerSecond':vio,'decodedBytesPerSecond':vdec,'rawSeconds':raw,'serialCompressedSeconds':compressed})
    assert io[0]['serialCompressedSeconds']<io[0]['rawSeconds'] and all(v['serialCompressedSeconds']>v['rawSeconds'] for v in io[1:])
    large_bound=2.0**(-99);assert math.isclose(large_bound,1.58e-30,rel_tol=.002)
    return {'lzForwardCopyExamples':4,'nllBaseAndAveragingExample':True,'binaryEntropyAt099':entropy,'ioModelExamples':io,'largeCountingExample':{'c':100,'requiresNAtLeast':100,'strictFractionUpperBound':large_bound,'scope':'Fixedinjectiveencoder,uniformnbitinput;notallcompressorssimultaneously.'},'scope':'Finite auxiliary arithmetic/copy checks,not article-program execution,benchmark or full compressor.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--languages',nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--expected-modified',action='append',default=[])
    args=ap.parse_args();assert not args.output.exists()
    audit=json.loads((D/'batch-033-source-audit.json').read_text(encoding='utf-8'));source=ROOT/audit['versions']['ja']['path'];ja=source.read_text(encoding='utf-8');tex=source_math(ja);assert sum(tex.values())==29
    refs=set(re.findall(r'\]\((https://[^)]+)\)',ja));assert len(refs)==11
    urls={l:v['canonical'] for l,v in audit['versions'].items()};dates=dict.fromkeys(urls,'2026-11-12')
    for value in args.expected_modified:
        lang,day=value.split('=',1);assert lang in args.languages;datetime.strptime(day,'%Y-%m-%d');dates[lang]=day
    graph_source=shared.graphs(ja);assert len(graph_source)==2 and [g.count('-->') for g in graph_source]==[8,6]
    expected_rows=[['0','$banana','$','a'],['1','a$banan','a','n'],['2','ana$ban','a','n'],['3','anana$b','a','b'],['4','banana$','b','$'],['5','na$bana','n','a'],['6','nana$ba','n','a']]
    versions=[]
    for lang in args.languages:
        v=audit['versions'][lang];p=ROOT/v['path'];text=p.read_text(encoding='utf-8');header=text.split('---',2)[1]
        original=subprocess.run(['git','show',audit['baselineCommit']+':'+v['path']],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
        assert hashlib.sha256(original.encode()).hexdigest()==v['sha256'] and shared.taxonomy(text)==shared.taxonomy(original)
        for key in ('date','slug','image','draft'):assert re.findall(r'^'+key+r':.*$',header,re.M)==re.findall(r'^'+key+r':.*$',original.split('---',2)[1],re.M)
        assert re.findall(r'^lastmod:.*$',header,re.M)==['lastmod: "'+dates[lang]+'"']
        assert re.findall(r'^(?:math|mermaid): true$',header,re.M)==['math: true','mermaid: true']
        assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,7)))
        assert re.findall('^'+FENCE+r'(\w+)\n',text,re.M)==['mermaid','mermaid'] and source_math(text)==tex
        graphs=shared.graphs(text);assert len(graphs)==2 and [g.count('-->') for g in graphs]==[8,6]
        assert [re.sub(r'"[^"\n]*"','""',g) for g in graphs]==[re.sub(r'"[^"\n]*"','""',g) for g in graph_source]
        assert set(re.findall(r'\]\((https://[^)]+)\)',text))==refs
        page=(args.site/urls[lang].removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
        navigation=shared.PageParser();navigation.feed(page.split('</aside>',1)[0]+'</aside>')
        assert navigation.canonical==urls[lang] and navigation.language==lang and navigation.alternates==dict(urls,**{'x-default':urls['ja']}) and navigation.options==urls
        article=Article();article.feed(page)
        assert shared.render.expressions(''.join(article.math))==tex and article.skip==0
        assert all(g.strip() in unescape(page) for g in graphs)
        assert {'std::vector<int>','banana$','annb$aa'}<=set(article.codes)
        assert [row for row in article.rows if len(row)==4 and row[0] in list(map(str,range(7)))]==expected_rows
        assert refs<=set(article.links)
        assert '"datePublished":"'+v['datePublished']+'"' in page and '"dateModified":"'+dates[lang] in page
        assert json.loads(re.search(r'^title: (.*)$',header,re.M)[1]) in unescape(page) and 'katex.min.js' in page and 'mermaid' in page
        for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
        versions.append({'language':lang,'path':v['path'],'sha256':shared.digest(p),'sourceSha256':shared.digest(source),'texExpressions':29,'diagrams':2,'diagramEdges':[8,6],'articleExecutablePrograms':0,'references':11,'literalDollarAndAngleBracketCodePreserved':True,'bwtTableAll7RowsExact':True,'datePublished':v['datePublished'],'dateModified':dates[lang],'passed':True})
        if lang in ('zh-cn','zh-tw'):
            assert all(value in ''.join(article.all) for value in ['c=100','n≥100','2^(-99)','1.58×10^(-30)'])
            versions[-1]['originalC100CountingExamplePreservedWithConditions']=True
        if lang=='de':
            assert all(value in ''.join(article.all) for value in ['c=100','n≥100','2^(-99)','1,58×10^(-30)','1 MB','n=8.000.000','12,5 Byte'])
            versions[-1]['originalC100CountingExamplePreservedWithConditions']=True
            versions[-1]['decimalMegabyteAndBitByteExamplesPreserved']=True
        if lang=='id':
            assert 'строго' in original and 'ตาม' in original
            assert not re.search(r'[\u0400-\u052f\u0e00-\u0e7f]',text+''.join(article.all))
            versions[-1]['originalRussianAndThaiIntrusionsRemoved']=True
    doc={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'allPassed':True,'versions':versions,'priorIndependentAuxiliaryChecks':'docs/translation-review/batch-033-original-math-probe.json','auxiliaryChecks':auxiliary(),'reviewedTranslationsAdded':0,'limitations':['Selected source/decodedHTML checks only;not prose approval or review ledger certification.','No executable articleprograms;independent finite auxiliary experiments are separately scoped.','Not browser/KaTeX/Mermaid execution or native-language/full-site/benchmarks/completecompressor certification.','Draft source can still change until reviewed translations registered;source hash recorded per actualcheck.']}
    args.output.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':True,'versions':len(versions),'texEach':29,'graphEdges':[8,6],'referencesEach':11,'articlePrograms':0}))

if __name__=='__main__':main()
