from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json,os,shutil,subprocess,sys
root=Path('C:/work/kenji.blog');docs=root/'docs/translation-review'
base=Path(os.environ['TEMP'])/'kenji-priority-review-20261024'
content=base/'content-35-bundles-ecc-ja-r3';site=base/'public-ecc-ja-r3'
assert not content.exists() and not site.exists() and not (docs/'batch-034-ja-checks-r3.json').exists()
slugs={p.name for p in (base/'content-34-bundles-lossless/post').iterdir() if p.is_dir()}
slugs.add('error-correcting-codes-hamming-reed-solomon-ldpc-shannon-capacity-information-theory')
assert len(slugs)==35
for slug in slugs:shutil.copytree(root/'content/post'/slug,content/'post'/slug)
snapshots=[]
for p in (content/'post').glob('*/*.md'):
    real=root/'content/post'/p.relative_to(content/'post');assert p.read_bytes()==real.read_bytes()
    snapshots.append(dict(path=real.relative_to(root).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
assert len(snapshots)==455
cmd=['hugo','--environment','production','--minify','--buildFuture','--baseURL','https://kenji.blog/','--contentDir',str(content),'--destination',str(site)]
r=subprocess.run(cmd,cwd=root,capture_output=True,text=True,encoding='utf-8')
(docs/'batch-034-ja-build-r3.json').write_text(json.dumps(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');assert r.returncode==0
commands=[
 ['docs/translation-review/verify_batch_034_ja.py',str(site),'docs/translation-review/batch-034-ja-validation-r3.json'],
 ['scripts/check_multilingual.py',str(site)],
 ['scripts/check_https_urls.py',str(site)],
 ['scripts/test_multilingual.py'],
 ['scripts/test_math_rendering.py'],
 ['scripts/test_translation_reviews.py'],
 ['scripts/translation_reviews.py','check'],
]
results=[]
for command in commands:
    r=subprocess.run([sys.executable,*command],cwd=root,capture_output=True,text=True,encoding='utf-8')
    results.append(dict(command=command,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr))
    print(json.dumps(dict(command=command[0],exitCode=r.returncode,stdout=r.stdout[-1000:],stderr=r.stderr[-1500:])))
receipt=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=all(r['exitCode']==0 for r in results),
 actualPreviewBundles=35,sourceSnapshotsExact=len(snapshots),snapshots=snapshots,results=results,
 reviewedTranslationsAdded=0,publicationPending=True,
 scope='35-bundle post-only local build; existing warnings retained. JA working draft;12 old translations remain, not review approval or full-site/browser/publication verification.')
(docs/'batch-034-ja-checks-r3.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert receipt['allPassed']
