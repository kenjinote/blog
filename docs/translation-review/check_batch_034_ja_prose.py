"""Guard against loss of explanatory prose around display math; static comparison only."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from html import unescape
import importlib.util,json,re,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
spec=importlib.util.spec_from_file_location('eccja',D/'verify_batch_034_ja.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
site=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
p=ROOT/'content/post/error-correcting-codes-hamming-reed-solomon-ldpc-shannon-capacity-information-theory/index.ja.md'
source=p.read_text(encoding='utf-8')
title=json.loads(re.search(r'^title: (.*)$',source,re.M)[1])
text=source.split('---',2)[2]
text=v.shared.shared.strip(text)
text=re.sub(v.shared.shared.render.PATTERN,'@MATHCUT@',text)
text=re.sub(r'<[^>]+>','',text)
text=re.sub(r'\[([^\]]+)\]\(https://[^)]+\)',r'\1',text)
text=text.replace(chr(96),'')
h=(site/'p/error-correcting-codes-hamming-reed-solomon-ldpc-shannon-capacity-information-theory/index.html').read_text(encoding='utf-8')
assert title in unescape(h)
parsed=v.shared.Article();parsed.feed(h)
def norm(s):return re.sub(r'\s+','',unescape(s))
actual=norm(''.join(parsed.all));pieces=[]
for line in text.splitlines():
    line=re.sub(r'^\s*(?:#{1,6}|[-*>]|\d+\.)\s*','',line)
    for piece in re.split(r'@MATHCUT@|\|',line):
        piece=norm(piece)
        if len(piece)>=12 and not re.fullmatch(r'[:\-]+',piece):pieces.append(piece)
missing=[piece for piece in pieces if piece not in actual]
doc=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),
    sourceSha256=v.shared.shared.digest(p),titleMatchesSource=True,fragmentsChecked=len(pieces),missing=missing,allPassed=not missing,
    source='Japanese prose outside metadata/fenced code/math, split at math and table cells, fragments at least12non-whitespace characters.',
    limitation='Static output-retention guard, not semantic approval, browser layout, whole-prose token equality or translation review.')
out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(allPassed=doc['allPassed'],fragmentsChecked=len(pieces),missing=missing),ensure_ascii=False))
assert not missing
