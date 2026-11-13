from pathlib import Path
import re,hashlib,json
p=Path('C:/work/kenji.blog/content/post/error-correcting-codes-hamming-reed-solomon-ldpc-shannon-capacity-information-theory/index.ja.md')
s=p.read_text(encoding='utf-8');assert hashlib.sha256(s.encode()).hexdigest()=='368b468f84ce3ca93f96e78fa7f6731be837a2e6e728cf78e1d167d5c76b2b54'
t=re.sub(r'(?m)^[ \t]+$','',s);assert re.sub(r'\s+','',s)==re.sub(r'\s+','',t)
p.write_text(t,encoding='utf-8',newline='\n');print(hashlib.sha256(t.encode()).hexdigest())
base=Path(__file__).parent
runner=(base/'check_batch_034_ja_r3.py').read_text(encoding='utf-8')
runner=runner.replace('-r3','-r4')
out=base/'check_batch_034_ja_r4.py';assert not out.exists();out.write_text(runner,encoding='utf-8')
