"""Fresh 36 post-bundle preview, including existing Hindi taxonomy metadata."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json,os,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
base=Path(os.environ['TEMP'])/'kenji-priority-review-20261024'
content=base/'content-36-bundles-kolm-ja-r2';site=base/'public-kolm-ja-r2'
assert not content.exists() and not site.exists() and not (D/'batch-035-ja-r2-checks.json').exists()
slugs={p.name for p in (base/'content-35-bundles-ecc-final-r3/post').iterdir() if p.is_dir()}
slugs.add('kolmogorov-complexity-algorithmic-information-theory-incompressibility-randomness');assert len(slugs)==36
for slug in slugs:shutil.copytree(ROOT/'content/post'/slug,content/'post'/slug)
shutil.copytree(ROOT/'content/tags',content/'tags')
snapshots=[]
for p in content.rglob('*.md'):
    real=ROOT/'content'/p.relative_to(content);assert p.read_bytes()==real.read_bytes()
    snapshots.append(dict(path=real.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
assert len(snapshots)==469 and len(list((content/'post').glob('*/*.md')))==468
cmd=['hugo','--environment','production','--minify','--buildFuture','--baseURL','https://kenji.blog/','--contentDir',str(content),'--destination',str(site)]
r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
(D/'batch-035-ja-r2-build.json').write_text(json.dumps(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');assert r.returncode==0
results=[]
commands=[['docs/translation-review/verify_batch_035_ja_r2.py',str(site),'docs/translation-review/batch-035-ja-r2-validation.json'],['scripts/check_multilingual.py',str(site)],['scripts/check_https_urls.py',str(site)],['scripts/test_multilingual.py'],['scripts/test_math_rendering.py'],['scripts/test_translation_reviews.py'],['scripts/translation_reviews.py','check']]
for cmd in commands:
    r=subprocess.run([sys.executable,*cmd],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
    results.append(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr))
    print(json.dumps(dict(command=cmd[0],exitCode=r.returncode,stdout=r.stdout[-1200:],stderr=r.stderr[-1800:])),flush=True)
receipt=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=all(r['exitCode']==0 for r in results),actualPreviewBundles=36,postSnapshotsExact=468,taxonomySnapshotsExact=1,snapshots=snapshots,unitTestsRerun=17,results=results,reviewedTranslationsAdded=0,publicationPending=True,scope='36-bundle preview; no full-site/browser or publication certification. Build warnings retained; EN remains original; other11 have only recorded mechanical escape restoration and remain unapproved.')
(D/'batch-035-ja-r2-checks.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');assert receipt['allPassed']
