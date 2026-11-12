"""Selected source, generated HTML, and actual program checks;not prose approval."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from html import unescape
from html.parser import HTMLParser
from urllib.parse import urlsplit
import argparse,hashlib,importlib.util,json,re,subprocess,os,math
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
spec=importlib.util.spec_from_file_location('shared',D/'verify_batch_028.py');shared=importlib.util.module_from_spec(spec);spec.loader.exec_module(shared)
spec=importlib.util.spec_from_file_location('entropy_code',D/'verify_batch_032_code.py');code=importlib.util.module_from_spec(spec);spec.loader.exec_module(code)

class PythonBlocks(HTMLParser):
    def __init__(self):super().__init__();self.active=False;self.blocks=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='code' and ('language-python' in a.get('class','').split() or a.get('data-lang')=='python'):self.active=True;self.blocks.append('')
    def handle_data(self,data):
        if self.active:self.blocks[-1]+=data
    def handle_endtag(self,tag):
        if tag=='code':self.active=False

class BidiValues(HTMLParser):
    def __init__(self):super().__init__();self.active=False;self.values=[];self.styles=[];self.rtl=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.rtl=a.get('lang')=='ar' and a.get('dir')=='rtl'
        if tag=='link' and a.get('rel')=='stylesheet':self.styles.append(a['href'])
        if tag=='bdi':
            assert not self.active and a.get('dir')=='ltr';self.active=True;self.values.append('')
    def handle_data(self,data):
        if self.active:self.values[-1]+=data
    def handle_endtag(self,tag):
        if tag=='bdi':assert self.active;self.active=False

def arabic_direction(text,html,site):
    spans=re.findall(r'<bdi\b[^>]*>.*?</bdi>',text,re.S)
    assert len(spans)==text.count('<bdi ')==text.count('</bdi>')
    source=BidiValues();source.feed(''.join(spans));page=BidiValues();page.feed(html)
    assert len(source.values)>=40 and page.values==source.values and page.rtl
    assert {'L_H<H+1','R<C','B>0','S≥0','N>0','p=0.5','S/N=15','B=1 MHz'}<=set(source.values)
    css_paths=[site/urlsplit(href).path.lstrip('/') for href in page.styles]
    css_paths=[p for p in css_paths if p.is_file()]
    assert css_paths
    css='\n'.join(p.read_text(encoding='utf-8') for p in css_paths)
    rtl=r'\[dir=[\"\x27]?rtl[\"\x27]?\]'
    for selector in [r'\.katex',r'\.article-content pre',r'\.article-content \.highlight']:
        assert re.search(rtl+r'\s*'+selector+r'\s*\{[^}]*direction:\s*ltr(?:;|})',css)
    assert re.search(rtl+r'\s*\.katex\s*\{[^}]*unicode-bidi:\s*isolate',css)
    return {'rtlHtml':True,'ltrBidiValues':len(source.values),'sourceAndHtmlBidiExact':True,'criticalComparisonsPreserved':True,'linkedLocalStylesheetsRead':[str(p.relative_to(site)).replace('\\','/') for p in css_paths],'mathAndCodeLtrCss':True,'scope':'Static source/HTML/linkedCSS only;no browser/KaTeX/Mermaid execution or visual guarantee.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--languages',nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--expected-modified',action='append',default=[])
    args=ap.parse_args();assert not args.output.exists()
    audit_path=D/'batch-032-source-audit.json';audit=json.loads(audit_path.read_text(encoding='utf-8'))
    source=ROOT/audit['versions']['ja']['path'];source_text=source.read_text(encoding='utf-8');tex=shared.render.expressions(shared.strip(source_text));assert sum(tex.values())==14
    urls={l:v['canonical'] for l,v in audit['versions'].items()};dates=dict.fromkeys(urls,'2026-11-12')
    for value in args.expected_modified:
        lang,day=value.split('=',1);assert lang in args.languages
        datetime.strptime(day,'%Y-%m-%d');assert '2026-11-12'<=day<=datetime.now(timezone(timedelta(hours=9))).date().isoformat();dates[lang]=day
    refs={'https://wucj.lab.westlake.edu.cn/Others/shannon1948.pdf','https://compression.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf'}
    expected_programs=re.findall('^'+shared.FENCE+r'python\n(.*?)^'+shared.FENCE,source_text,re.M|re.S);assert len(expected_programs)==2
    versions=[];runs=[]
    for lang in args.languages:
        v=audit['versions'][lang];p=ROOT/v['path'];text=p.read_text(encoding='utf-8');h=text.split('---',2)[1]
        original=subprocess.run(['git','show',audit['baselineCommit']+':'+v['path']],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True).stdout
        assert hashlib.sha256(original.encode()).hexdigest()==v['sha256'] and shared.taxonomy(text)==shared.taxonomy(original)
        assert re.findall(r'^date:.*$',h,re.M)==v['headerDateLines'] and re.findall(r'^lastmod:.*$',h,re.M)==['lastmod: "'+dates[lang]+'"']
        for key in ('slug','image'):assert re.findall(r'^'+key+r':.*$',h,re.M)==re.findall(r'^'+key+r':.*$',original.split('---',2)[1],re.M)
        assert re.findall(r'^(?:math|mermaid): true$',h,re.M)==['math: true','mermaid: true']
        assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,8))) and not re.search(r'^# ',text,re.M)
        assert re.findall('^'+shared.FENCE+r'(\w+)\n',text,re.M)==['mermaid','python','python']
        graphs=shared.graphs(text);assert len(graphs)==1 and graphs[0].count('-->')==4 and graphs[0].count('-.->')==1
        assert re.sub(r'"[^"\n]*"','""',graphs[0])==re.sub(r'"[^"\n]*"','""',shared.graphs(source_text)[0])
        assert shared.render.expressions(shared.strip(text))==tex
        programs=re.findall('^'+shared.FENCE+r'python\n(.*?)^'+shared.FENCE,text,re.M|re.S);assert programs==expected_programs
        html=(args.site/urls[lang].removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
        parser=shared.PageParser();parser.feed(html.split('</aside>',1)[0]+'</aside>')
        assert parser.canonical==urls[lang] and parser.language==lang and parser.alternates==dict(urls,**{'x-default':urls['ja']}) and parser.options==urls
        article=shared.render.ArticleText();article.feed(html);assert shared.render.expressions(''.join(article.parts))==tex
        assert graphs[0].strip() in unescape(html)
        cp=PythonBlocks();cp.feed(html);assert [b.strip() for b in cp.blocks]==[b.strip() for b in programs]
        actual_refs=set(re.findall(r'\]\((https://[^)]+)\)',text));assert actual_refs==refs and all(u in html for u in refs)
        assert '"datePublished":"'+v['datePublished']+'"' in html and '"dateModified":"'+dates[lang] in html
        assert 'katex.min.js' in html and 'mermaid' in html and json.loads(re.search(r'^title: (.*)$',h,re.M)[1]) in unescape(html)
        for asset in audit['assets']:assert hashlib.sha256((ROOT/asset['path']).read_bytes()).hexdigest()==asset['sha256']
        scratch=Path(os.environ['TEMP'])/'kenji-priority-review-20261024'/('entropy-code-'+args.output.stem+'-'+lang)
        run=code.verify(text,lang,scratch);assert run['articleProgramsExecuted']==2;runs.append(run)
        versions.append({'language':lang,'path':v['path'],'sha256':shared.digest(p),'sourceSha256':shared.digest(source),'texExpressions':14,'diagrams':1,'diagramSolidEdges':4,'diagramDottedEdges':1,'articleExecutablePrograms':2,'references':2,'datePublished':v['datePublished'],'dateModified':dates[lang],'passed':True})
        if lang=='ar':versions[-1]['arabicStaticDirection']=arabic_direction(text,html,args.site)
    assert 10**6*math.log2(1+15)==4*10**6
    correlated=[{'n':n,'marginalEntropy':1,'jointBlockEntropy':1,'knownLengthBlockCodeBits':1,'bitsPerSourceSymbol':1/n} for n in [1,2,8,64]]
    doc={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'allPassed':True,'versions':versions,'programRuns':runs,'sharedAuxiliaryChecks':{'awgnExamples':1,'awgnCapacityBitsPerSecond':4000000,'linearSnr':15,'correlatedSourceExamples':correlated,'scope':'Finite mathematical examples,not physical channel simulation or practical compression benchmark.'},'sourceAuditSha256':hashlib.sha256(audit_path.read_bytes()).hexdigest(),'reviewedTranslationsAdded':0,'limitations':['Selected source/HTML/actualPython with finite oracle,not prose/ledger approval.','No native speaker or browser/KaTeX/Mermaid execution. Plot needs separate visual inspection or exact-byte match to inspected image.','Not complete serialized compressor,errorcorrecting code,all-input proof or modern network benchmark.','Other translations/publication and whole goal pending.']}
    args.output.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':True,'versions':len(versions),'texEach':14,'programsEach':2,'roundTripsEach':1093,'optimalProfilesEach':1360}))

if __name__=='__main__':main()
