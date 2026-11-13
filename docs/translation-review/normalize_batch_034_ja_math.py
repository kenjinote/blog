"""One-time draft formatting repair; preserved R2 draft and failed build remain."""
from pathlib import Path
import re,hashlib,json
root=Path(__file__).resolve().parents[2]
p=root/'content/post/error-correcting-codes-hamming-reed-solomon-ldpc-shannon-capacity-information-theory/index.ja.md'
old=p.read_text(encoding='utf-8')
preserved=(root/'docs/drafts/ecc034-ja-r2.md').read_text(encoding='utf-8')
assert old==preserved
fence=chr(96)*3
parts=re.split('(^'+fence+r'.*?^'+fence+r'[^\n]*\n?)',old,flags=re.M|re.S)
count=0
def fix(match):
    global count
    count+=1
    before=match.string[:match.start()].rsplit('\n',1)[-1]
    assert not before.strip(),'Display math must begin on its own line'
    indent=before
    inner=' '.join(match[1].split())
    return '\n\n'+indent+'$$\n'+indent+inner+'\n'+indent+'$$\n\n'
new=''.join(part if i%2 else re.sub(r'\$\$(.*?)\$\$',fix,part,flags=re.S) for i,part in enumerate(parts))
assert count>30
# Ignore only formatting whitespace: all prose, TeX characters and code remain.
assert re.sub(r'\s+','',old)==re.sub(r'\s+','',new)
p.write_text(new,encoding='utf-8',newline='\n')
print(json.dumps(dict(displayBlocksReformatted=count,nonWhitespaceCharactersIdentical=True,oldSha256=hashlib.sha256(old.encode()).hexdigest(),newSha256=hashlib.sha256(new.encode()).hexdigest())))
