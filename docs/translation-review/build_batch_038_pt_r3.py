"""Fresh 39 post-bundle preview, including existing Hindi taxonomy metadata."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json,os,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
base=Path(os.environ['TEMP'])/'kenji-priority-review-20261024'
content=base/'content-39-bundles-diagonal-pt-r3';site=base/'public-diagonal-pt-r3'
assert not content.exists() and not site.exists() and not (D/'batch-038-pt-r3-checks.json').exists()
prior=json.loads((D/'batch-037-final-checks.json').read_text(encoding='utf-8'))
assert prior['allPassed'] and len(prior['snapshots'])==495
slugs={Path(x['path']).parts[2] for x in prior['snapshots'] if Path(x['path']).parts[:2]==('content','post')};slugs.add('cantors-diagonal-argument');assert len(slugs)==39
for slug in slugs:shutil.copytree(ROOT/'content/post'/slug,content/'post'/slug)
shutil.copytree(ROOT/'content/tags',content/'tags')
snapshots=[]
for p in content.rglob('*.md'):
    real=ROOT/'content'/p.relative_to(content);assert p.read_bytes()==real.read_bytes()
    snapshots.append(dict(path=real.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
assert len(snapshots)==508 and len(list((content/'post').glob('*/*.md')))==507
cmd=['hugo','--environment','production','--minify','--buildFuture','--baseURL','https://kenji.blog/','--contentDir',str(content),'--destination',str(site)]
r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
(D/'batch-038-pt-r3-build.json').write_text(json.dumps(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');assert r.returncode==0
results=[]
commands=[['docs/translation-review/verify_batch_038_pt.py',str(site),'docs/translation-review/batch-038-pt-r3-validation.json'],['scripts/check_multilingual.py',str(site)],['scripts/check_https_urls.py',str(site)],['scripts/translation_reviews.py','check']]
for cmd in commands:
    r=subprocess.run([sys.executable,*cmd],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
    results.append(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr))
    print(json.dumps(dict(command=cmd[0],exitCode=r.returncode,stdout=r.stdout[-1200:],stderr=r.stderr[-1800:])),flush=True)
receipt=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=all(r['exitCode']==0 for r in results),actualPreviewBundles=39,postSnapshotsExact=507,taxonomySnapshotsExact=1,snapshots=snapshots,unitTestsRerun=0,existingTestsPreviouslyPassedNotRerun=17,priorTests="docs/translation-review/batch-037-final-checks.json",results=results,reviewedTranslationsAdded=0,publicationPending=True,scope='39-bundle static preview. Japanese, English and3translations original/revised read;8translations unread; ES registration pending. Prior17tests not rerun; no browser/fullsite/publication approval.')
(D/'batch-038-pt-r3-checks.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');assert receipt['allPassed']
