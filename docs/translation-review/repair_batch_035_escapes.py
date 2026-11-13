"""Restore explicitly read damaged TeX escapes only; does not approve translations."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
audit=json.loads((D/'batch-035-source-audit.json').read_text(encoding='utf-8'))
out=D/'batch-035-escape-repair.json';assert not out.exists()
replacements=[(chr(7)+'pprox',r'\approx'),(chr(12)+'rac',r'\frac'),(chr(9)+'ext',r'\text'),(chr(9)+'heta',r'\theta'),(chr(9)+'o',r'\to')]
versions=[]
for lang,e in audit['versions'].items():
    if lang in ('ja','en'):continue
    p=ROOT/e['path'];old=p.read_text(encoding='utf-8-sig');assert hashlib.sha256(old.encode()).hexdigest()==e['sha256']
    new=old;changes=[]
    for damaged,restored in replacements:
        n=new.count(damaged)
        if n:changes.append(dict(damaged=damaged,restored=restored,occurrences=n));new=new.replace(damaged,restored)
    assert new!=old and not any(ord(c)<32 and c not in '\n\r' for c in new)
    # The full result must be exactly the deterministic transformation of the original.
    expected=old
    for damaged,restored in replacements:expected=expected.replace(damaged,restored)
    assert expected==new
    p.write_text(new,encoding='utf-8')
    versions.append(dict(language=lang,path=e['path'],originalSha256=e['sha256'],repairedSha256=hashlib.sha256(new.encode()).hexdigest(),changes=changes,reviewedTranslationsAdded=0))
assert len(versions)==11
doc=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),versions=versions,
    repairedCommands=sum(c['occurrences'] for v in versions for c in v['changes']),
    originalFullBodiesPreviouslyRead=True,changedEscapeContextsRead=True,otherTextAndMetadataUnchanged=True,
    reviewedTranslationsAdded=0,publicationPending=True,
    scope='Restore only BEL+pprox, form-feed+rac and TAB+ext/heta/o to TeX escapes after full original reading and explicit context inspection. Does not approve meanings, full formulas, translations, HTML or publication. Original hashes/audit preserved; semantic rewrites remain pending.')
out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(languages=len(versions),repairedCommands=doc['repairedCommands'],reviewedTranslationsAdded=0)))
