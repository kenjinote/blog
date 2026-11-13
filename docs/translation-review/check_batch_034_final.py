"""Fresh assembled 35-bundle check; semantic reading remains separate evidence."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from html import unescape
import hashlib, importlib.util, json, os, re, shutil, subprocess, sys

ROOT=Path(__file__).resolve().parents[2]; D=ROOT/'docs/translation-review'
base=Path(os.environ['TEMP'])/'kenji-priority-review-20261024'
content=base/'content-35-bundles-ecc-final'; site=base/'public-ecc-final'
assert not content.exists() and not site.exists() and not (D/'batch-034-final-checks.json').exists()
doc=json.loads((D/'batch-034.json').read_text(encoding='utf-8')); assert len(doc['reviews'])==12
prior=base/'content-35-bundles-ecc-ar/post'
slugs={p.name for p in prior.iterdir() if p.is_dir()}; assert len(slugs)==35
for slug in slugs: shutil.copytree(ROOT/'content/post'/slug,content/'post'/slug)
snapshots=[]
for p in (content/'post').glob('*/*.md'):
    q=ROOT/'content/post'/p.relative_to(content/'post'); assert p.read_bytes()==q.read_bytes()
    snapshots.append(dict(path=q.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(q.read_bytes()).hexdigest()))
assert len(snapshots)==455
cmd=['hugo','--environment','production','--minify','--buildFuture','--baseURL','https://kenji.blog/','--contentDir',str(content),'--destination',str(site)]
r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
(D/'batch-034-final-build.json').write_text(json.dumps(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr),ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); assert r.returncode==0
spec=importlib.util.spec_from_file_location('language',D/'verify_batch_034_language.py'); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
audit=json.loads((D/'batch-034-source-audit.json').read_text(encoding='utf-8')); versions=[]
for lang,e in audit['versions'].items():
    if lang not in ('ja','en'):continue
    p=ROOT/e['path'];text=p.read_text(encoding='utf-8');sha=m.shared.shared.digest(p)
    expected=doc['frozenSourceHash'] if lang=='ja' else doc['reviews'][p.relative_to(ROOT/'content').as_posix()]['translationHash']
    assert sha==expected
    slug=json.loads(re.search(r'^slug: (.*)$',text,re.M)[1]);url='https://kenji.blog/'+('' if lang=='ja' else lang+'/')+'p/'+slug+'/'
    html=(site/url.removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
    a=m.shared.Article();a.feed(html);tex=m.shared.source_math(text)
    assert m.shared.shared.render.expressions(''.join(a.math))==tex
    graphs=m.shared.shared.graphs(text);assert len(graphs)==4 and [g.count('-->') for g in graphs]==[10,7,9,5]
    assert all(g.strip() in unescape(html) for g in graphs)
    code=re.search('^'+m.FENCE+r'python\n(.*?)^'+m.FENCE,text,re.M|re.S)[1]
    shown=re.search('^'+m.FENCE+r'text\n(.*?)^'+m.FENCE,text,re.M|re.S)[1]
    assert code.rstrip()==(D/'ecc034_revised_code.py').read_text(encoding='utf-8').rstrip()
    r=subprocess.run([sys.executable,'-c',code],capture_output=True,text=True,encoding='utf-8');assert r.returncode==0 and r.stdout==shown
    assert code in a.codes and shown in a.codes
    refs=set(re.findall(r'\]\((https://[^)]+)\)',text));assert len(refs)==10 and refs<=set(a.links)
    assert len([row for row in a.rows if len(row)==4])==6
    assert '"datePublished":"2026-10-18T08:00:00+09:00"' in html and '"dateModified":"2026-11-13' in html
    assert json.loads(re.search(r'^title: (.*)$',text,re.M)[1]) in unescape(html)
    versions.append(dict(language=lang,path=e['path'],sha256=sha,texExpressions=sum(tex.values()),displayMath=len(re.findall(r'\$\$(.*?)\$\$',text,re.S)),diagrams=4,diagramEdges=[10,7,9,5],references=10,articleExecutablePrograms=1,proseFragmentsPreserved=m.pair.prose_fragments(text,html),passed=True))
results=[]
for lang in m.ANNOTATIONS:
    output=D/('batch-034-final-'+lang+'-validation.json')
    cmd=['docs/translation-review/verify_batch_034_language.py',str(site),lang,str(output)]
    r=subprocess.run([sys.executable,*cmd],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
    results.append(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr))
    print(json.dumps(dict(language=lang,exitCode=r.returncode,stdout=r.stdout[-500:],stderr=r.stderr[-1000:])),flush=True)
    if r.returncode==0:versions.extend(json.loads(output.read_text(encoding='utf-8'))['versions'])
for cmd in [['scripts/check_multilingual.py',str(site)],['scripts/check_https_urls.py',str(site)],['scripts/test_multilingual.py'],['scripts/test_math_rendering.py'],['scripts/test_translation_reviews.py'],['scripts/translation_reviews.py','check']]:
    r=subprocess.run([sys.executable,*cmd],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
    results.append(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr));print(json.dumps(results[-1]),flush=True)
spec=importlib.util.spec_from_file_location('tags',D/'verify_batch_028.py');tags=importlib.util.module_from_spec(spec);spec.loader.exec_module(tags)
aliases=tags.hindi_tag_redirects(site)
passed=all(r['exitCode']==0 for r in results) and len(versions)==13
receipt=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=passed,actualPreviewBundles=35,sourceSnapshotsExact=455,snapshots=snapshots,unitTestsRerun=17,priorHindiTaxonomyAliases=aliases,results=results,reviewedTranslationsAdded=0,publicationPending=True,scope='Fresh assembled 35-bundle static/finite preview. Full original/revised reading separately recorded. Prior finite arithmetic evidence referenced, not rerun. No whole-site, native-speaker, browser/runtime, hardware, benchmark or full QR/LDPC/Polar certification. Build warnings retained.')
(D/'batch-034-final-checks.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(D/'batch-034-final-validation.json').write_text(json.dumps(dict(version=1,allPassed=passed,versions=versions,reviewedTranslationsAdded=0,publicationPending=True),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert passed
print(json.dumps(dict(passed=True,versions=len(versions),texExpressions=sum(v['texExpressions'] for v in versions),proseFragments=sum(v['proseFragmentsPreserved'] for v in versions))))
