"""Compile explicitly selected article C blocks; prose review is a separate activity."""
from pathlib import Path
import argparse,hashlib,json,re,subprocess,tempfile,random,math,sys
from datetime import datetime,timezone,timedelta
ROOT=Path(__file__).resolve().parents[2]
FOLDER=ROOT/'content/post/素数を生成するC言語コード'

def digest(p):
    return hashlib.sha256(p.read_text(encoding='utf-8-sig').replace('\r\n','\n').encode()).hexdigest()

def unix(p):
    s=str(p.resolve()).replace('\\','/')
    return '/mnt/'+s[0].lower()+s[2:]

def run(binary,args=(),data=''):
    # Send bytes: Windows text-mode pipes would turn LF into CRLF and alter byte limits.
    r=subprocess.run(['wsl','--exec',unix(binary),*args],input=data.encode('utf-8'),capture_output=True,timeout=30)
    r.stdout=r.stdout.decode('utf-8');r.stderr=r.stderr.decode('utf-8')
    assert not r.stderr or r.returncode!=0,r.stderr
    return r

def compile_code(code,work,name,flags):
    p=work/(name+'.c');p.write_text(code,encoding='utf-8');binary=work/name
    r=subprocess.run(['wsl','--exec','gcc','-std=c17','-Wall','-Wextra',*flags,unix(p),'-o',unix(binary)],capture_output=True,text=True,encoding='utf-8',timeout=60)
    assert r.returncode==0 and not r.stderr,r.stderr
    return binary

def reference(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--languages',nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    assert not a.output.exists(),'Preserve previous validation results'
    original=json.loads((ROOT/'docs/translation-review/batch-019-source-audit.json').read_text(encoding='utf-8'))
    flags=bytearray(b'\1')*50001;flags[:2]=b'\0\0'
    for p in range(2,math.isqrt(50000)+1):
        if flags[p]:flags[p*p::p]=b'\0'*((50000-p*p)//p+1)
    rng=random.Random(19019)
    extra=[-2147483648,-100,-1,2147483647,2147483646,2147395600,2146654199]+[rng.randrange(50001,2147483648) for _ in range(160)]
    nums=list(range(50001))+extra;expected=list(map(int,flags))+[int(reference(n)) for n in extra]
    harness=r'''
#include <limits.h>
int main(int argc,char **argv) {
    if (argc>1 && argv[1][0]=='r') {
        int n=-123;bool ok=readLimit(&n);printf("%d %d\n",ok,n);return 0;
    }
    if (argc>1 && argv[1][0]=='p') {printPrimes(atoi(argv[2]));return 0;}
    int n;while(scanf("%d",&n)==1) printf("%d\n",isPrime(n));return 0;
}
'''
    valid=[('0\n',0),('1\n',1),('2\n',2),('30\n',30),(' \t+30 \t\n',30),('0002',2),('-0\n',0),('2147483647\n',2147483647),('0'*126+'2\n',2),('0'*126+'2',2),('2\nabc\n',2)]
    invalid=['','\n',' \t\n','abc\n','-1\n','+\n','1.5\n','0x10\n','2 junk\n','2 3\n','2147483648\n','-2147483649\n','9'*126+'\n','0'*127+'2\n','0'*126+'2x\n','0'*128+'\n','é\n']
    print_bounds=[-2147483648,-1,0,1,2,3,4,5,10,30,100,1000]
    versions=[];ja=(FOLDER/'index.md').read_text(encoding='utf-8');source_code=re.findall(r'^```c\n(.*?)^```',ja,re.M|re.S)[0]
    normalize=lambda s:re.sub(r'"(?:[^"\\]|\\.)*"','"STRING"',s)
    for lang in a.languages:
        p=FOLDER/('index.md' if lang=='ja' else 'index.'+lang+'.md');text=p.read_text(encoding='utf-8')
        codes=re.findall(r'^```c\n(.*?)^```',text,re.M|re.S);assert len(codes)==1
        code=codes[0];assert normalize(code)==normalize(source_code)
        assert len(re.findall(r'^## ',text,re.M))==4
        assert text.count('\ndate: ')==1 and 'date: 2024-08-24T09:38:10+09:00' in text
        assert 'lastmod: 2026-10-28' in text
        assert 'image: "img.webp"' in text and (FOLDER/'img.webp').exists()
        slug=original['versions'][lang]['slug'];assert 'slug: "'+slug+'"' in text
        canonical=original['versions'][lang]['canonical']
        from urllib.parse import unquote,urlsplit
        html=(a.site/unquote(urlsplit(canonical).path).lstrip('/')/'index.html').read_text(encoding='utf-8')
        assert re.search(r'<link rel=canonical href=["\']?'+re.escape(canonical),html)
        assert '"datePublished":"2024-08-24T09:38:10+09:00"' in html
        assert '"dateModified":"2026-10-28' in html
        assert '6k - 1' in html and '127' in html and 'strtol' in html
        assert 'https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf' in text
        target='https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/cpp-fast-prime-testing-miller-rabin/'
        assert target in text and target in html
        assert re.findall(r'^```text\n(.*?)^```',text,re.M|re.S)==['2 3 5 7 11 13 17 19 23 29\n']
        work=Path(tempfile.mkdtemp(prefix='kenji-prime-c-'+lang+'-'));results=[]
        for mode,opts in [('optimized',['-O2']),('ubsan',['-O0','-fsanitize=undefined','-fno-sanitize-recover=undefined'])]:
            full=compile_code(code,work,'article-'+mode,opts)
            helper=compile_code(code.replace('int main(void)','int article_main(void)')+harness,work,'harness-'+mode,opts)
            r=run(helper,data='\n'.join(map(str,nums))+'\n');assert r.returncode==0 and not r.stderr
            assert list(map(int,r.stdout.split()))==expected
            for data,n in valid:
                r=run(helper,['r'],data);assert r.returncode==0 and r.stdout==f'1 {n}\n' and not r.stderr,(lang,mode,data,r)
            for data in invalid:
                r=run(helper,['r'],data);assert r.returncode==0 and r.stdout=='0 -123\n' and not r.stderr,(lang,mode,data,r)
            for n in print_bounds:
                r=run(helper,['p',str(n)]);want=' '.join(str(i) for i in range(2,max(2,n+1)) if flags[i])+'\n'
                assert r.returncode==0 and not r.stderr and r.stdout==want,(lang,mode,n,r.stdout,want)
            for n in [0,1,2,3,10,30]:
                r=run(full,data=str(n)+'\n');want=' '.join(str(i) for i in range(2,max(2,n+1)) if flags[i])+'\n'
                assert r.returncode==0 and not r.stderr and r.stdout.endswith(want)
                assert r.stdout.count('\n')==2
            for data in ['','abc\n','-1\n','2147483648\n','2x\n']:
                r=run(full,data=data);assert r.returncode!=0 and r.stderr and 'runtime error:' not in r.stderr
            results.append({'mode':mode,'primeClassifications':len(nums),'validInputCases':len(valid),'invalidInputCases':len(invalid),'printerCases':len(print_bounds),'completeProgramValidCases':6,'completeProgramInvalidCases':5})
        versions.append({'language':lang,'sha256':digest(p),'canonicalPreserved':canonical,'datePublishedPreserved':'2024-08-24T09:38:10+09:00','codeBlocks':1,'sampleBlocks':1,'sections':4,'mathDelimiters':0,'diagrams':0,'executions':results})
        print(json.dumps({'language':lang,'passed':True,'primeCasesPerMode':len(nums)}),flush=True)
    result={'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),'compiler':subprocess.check_output(['wsl','--exec','gcc','--version'],text=True).splitlines()[0],'versions':versions,'limitations':['Finite tests under Ubuntu GCC13.3 with32bit int; not every C implementation.','Full enumeration to INT_MAX is deliberately not executed.','No browser visual audit, native-speaker certification, binary/NUL input or stream-output failure audit.','Prose, trial-division proof, portable bound argument and primary-source reading recorded separately; this script does not approve translations.']}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
