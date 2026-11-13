"""Fresh post-only35bundle preview for one fully read working translation."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json,os,shutil,subprocess,sys
root=Path(__file__).resolve().parents[2];d=root/'docs/translation-review'
lang=sys.argv[1];assert lang=='zh-cn'
base=Path(os.environ['TEMP'])/'kenji-priority-review-20261024'
content=base/('content-35-bundles-ecc-'+lang+'-r2');site=base/('public-ecc-'+lang+'-r2');stem='batch-034-'+lang+'-r2'
assert not content.exists() and not site.exists() and not (d/(stem+'-checks.json')).exists()
slugs={p.name for p in (base/'content-35-bundles-ecc-ja-en-r2/post').iterdir() if p.is_dir()};assert len(slugs)==35
for slug in slugs:shutil.copytree(root/'content/post'/slug,content/'post'/slug)
snapshots=[]
for p in (content/'post').glob('*/*.md'):
    real=root/'content/post'/p.relative_to(content/'post');assert p.read_bytes()==real.read_bytes()
    snapshots.append(dict(path=real.relative_to(root).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
assert len(snapshots)==455
cmd=['hugo','--environment','production','--minify','--buildFuture','--baseURL','https://kenji.blog/','--contentDir',str(content),'--destination',str(site)]
r=subprocess.run(cmd,cwd=root,capture_output=True,text=True,encoding='utf-8')
(d/(stem+'-build.json')).write_text(json.dumps(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');assert r.returncode==0
commands=[
 ['docs/translation-review/verify_batch_034_language.py',str(site),lang,'docs/translation-review/'+stem+'-validation.json'],
 ['scripts/check_multilingual.py',str(site)],['scripts/check_https_urls.py',str(site)]
]
results=[]
for command in commands:
    r=subprocess.run([sys.executable,*command],cwd=root,capture_output=True,text=True,encoding='utf-8')
    results.append(dict(command=command,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr))
    print(json.dumps(dict(command=command[0],exitCode=r.returncode,stdout=r.stdout[-1200:],stderr=r.stderr[-2000:])))
receipt=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),
 allPassed=all(r['exitCode']==0 for r in results),actualPreviewBundles=35,sourceSnapshotsExact=len(snapshots),
 snapshots=snapshots,results=results,reviewedTranslationsAdded=0,publicationPending=True,
 existingTestsPreviouslyPassedNotRerun=17,priorTests='docs/translation-review/batch-034-ja-en-checks-r2.json',
 scope='Selected translation code/math/prose/HTML and35bundle global checks. Prior17unit tests referenced,not rerun; no whole-site/browser/publication certification.')
(d/(stem+'-checks.json')).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert receipt['allPassed']
