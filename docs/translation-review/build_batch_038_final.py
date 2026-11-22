"""Build one fresh 39-bundle integration preview and validate every Cantor translation."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json,os,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
base=Path(os.environ['TEMP'])/'kenji-priority-review-20261024'
content=base/'content-39-bundles-diagonal-final';site=base/'public-diagonal-final';receipt_path=D/'batch-038-final-checks.json'
assert not content.exists() and not site.exists() and not receipt_path.exists()
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
(D/'batch-038-final-build.json').write_text(json.dumps(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');assert r.returncode==0
results=[]
commands=[]
for lang,verifier in [('en','verify_batch_038_ja_en.py'),('zh-cn','verify_batch_038_zh_cn.py'),('zh-tw','verify_batch_038_zh_tw.py'),('es','verify_batch_038_es.py'),('ko','verify_batch_038_ko.py'),('pt','verify_batch_038_pt.py'),('fr','verify_batch_038_fr.py'),('de','verify_batch_038_de.py'),('hi','verify_batch_038_hi.py'),('id','verify_batch_038_id.py'),('ar','verify_batch_038_ar.py'),('ru','verify_batch_038_ru.py')]:
    commands.append([verifier,str(site),f'docs/translation-review/batch-038-final-validation-{lang}.json'])
commands += [['scripts/check_multilingual.py',str(site)],['scripts/check_https_urls.py',str(site)],['scripts/translation_reviews.py','check']]
for cmd in commands:
    r=subprocess.run([sys.executable,*cmd],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
    results.append(dict(command=cmd,exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr))
    print(json.dumps(dict(command=cmd[0],exitCode=r.returncode,stdout=r.stdout[-1000:],stderr=r.stderr[-1200:])),flush=True)
assert len(json.loads((D/'batch-038.json').read_text(encoding='utf-8'))['reviews'])==12
receipt=dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),allPassed=all(x['exitCode']==0 for x in results),actualPreviewBundles=39,postSnapshotsExact=507,taxonomySnapshotsExact=1,snapshots=snapshots,languageVerifiers=12,reviewedTranslationsAdded=0,publicationPending=True,unitTestsRerun=0,priorTestsPreviouslyPassedNotRerun=17,priorTests='docs/translation-review/batch-037-final-checks.json',scope='One fresh 39-bundle static production preview with all12 translations checked against frozen Japanese; all12 translation ledger entries registered. No browser KaTeX/Mermaid execution, fullsite validation, publication or live check yet.',results=results)
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');assert receipt['allPassed']
