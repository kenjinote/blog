"""One-time CJK punctuation emphasis fix. Initial source and failed check retained."""
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[2]
p=root/'content/post/error-correcting-codes-hamming-reed-solomon-ldpc-shannon-capacity-information-theory/index.zh-cn.md'
old=p.read_text(encoding='utf-8');assert old==(root/'docs/drafts/ecc034-zh-cn-initial.md').read_text(encoding='utf-8')
f=chr(96)*3;parts=re.split('(^'+f+r'.*?^'+f+r'[^\n]*\n?)',old,flags=re.M|re.S);count=0
def fix(m):
    global count
    count+=1;return '<strong>'+m[1]+'</strong>'
new=''.join(part if i%2 else re.sub(r'\*\*([^\n]+?)\*\*',fix,part) for i,part in enumerate(parts))
assert count>10
assert new.replace('<strong>','**').replace('</strong>','**')==old
p.write_text(new,encoding='utf-8',newline='\n')
print(json.dumps(dict(strongSpans=count,onlyEmphasisMarkupChanged=True,oldSha256=hashlib.sha256(old.encode()).hexdigest(),newSha256=hashlib.sha256(new.encode()).hexdigest())))
