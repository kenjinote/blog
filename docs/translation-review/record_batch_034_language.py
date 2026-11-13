"""Register one actually read translation from explicit notes and passing scoped evidence."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import copy,hashlib,json,subprocess,sys
root=Path(__file__).resolve().parents[2];d=root/'docs/translation-review'
lang,notes_path,stem=sys.argv[1:4]
assert (lang,stem) in [('zh-cn','batch-034-zh-cn-r2'),('zh-tw','batch-034-zh-tw'),('es','batch-034-es-r2')]
notes=json.loads(Path(notes_path).read_text(encoding='utf-8'))
assert notes['allOriginalAndRevisedBodiesRead'] and set(notes['checks'])=={'meaning','terminology','mathematics','code','links'}
assert all(len(v)>60 for v in notes['checks'].values())
p=d/'batch-034.json';doc=json.loads(p.read_text(encoding='utf-8'));old=copy.deepcopy(doc['reviews'])
slug=doc['article'];source='post/'+slug+'/index.ja.md';key='post/'+slug+'/index.'+lang+'.md'
assert key not in old
proof=json.loads((d/(stem+'-validation.json')).read_text(encoding='utf-8'))
checks=json.loads((d/(stem+'-checks.json')).read_text(encoding='utf-8'))
assert proof['allPassed'] and checks['allPassed'] and checks['sourceSnapshotsExact']==455 and checks['actualPreviewBundles']==35
assert len(checks['results'])==3 and all(r['exitCode']==0 for r in checks['results'])
assert '1983 pages' in checks['results'][1]['stdout'] and "'html': 3616" in checks['results'][2]['stdout']
v=proof['versions'][0];assert v['language']==lang and v['passed'] and v['displayMath']==47 and v['diagramEdges']==[10,7,9,5] and v['articleExecutablePrograms']==1 and v['references']==10
digest=lambda p:hashlib.sha256(p.read_text(encoding='utf-8-sig').encode()).hexdigest()
assert digest(root/'content'/source)==v['sourceSha256']==doc['frozenSourceHash']
assert digest(root/'content'/key)==v['sha256'] and all(e['sourceHash']==v['sourceSha256'] for e in old.values())
lp=root/'data/translation_reviews.json';prior=copy.deepcopy(json.loads(lp.read_text(encoding='utf-8'))['reviews'])
assert len(prior)==408+len(old) and key not in prior
today=datetime.now(timezone(timedelta(hours=9))).date().isoformat();assert today=='2026-11-13'
total=len(prior)+1;other=11-len(old)
entry=dict(reviewKind='ai',reviewedAt=today,reviewer='Codex (AI)',source=source,sourceHash=v['sourceSha256'],translationHash=v['sha256'],
 checks={k:dict(status='checked',note=n) for k,n in notes['checks'].items()},summary=notes['summary'],
 languageSpecificFindings=notes['languageSpecificFindings'],validation='docs/translation-review/'+stem+'-validation.json',
 limitations=['AI review,not human/native-speaker certification.',str(other)+' other translations remain unreviewed; reading status is recorded separately.',
 'Finite educational code/math checks,not all-input theorem proofs,real hardware/spacecraft,full QR/LDPC/Polar software or benchmarks.',
 'Primary reading limited to separately documented selected pages/abstracts,no new full-paper/browser/KaTeX/Mermaid runtime certification.',
 'Batch034publication andwholegoal pending;earlier17unit tests referenced,not rerun for this language.'])
doc['reviews'][key]=entry;p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
r=subprocess.run([sys.executable,'scripts/translation_reviews.py','record',key,'--source',source,'--reviewer','Codex (AI)','--kind','ai','--evidence','docs/translation-review/batch-034.json','--date',today],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True)
c=subprocess.run([sys.executable,'scripts/translation_reviews.py','check'],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True)
assert json.loads(c.stdout)=={'current':total,'unreviewed':13032-total}
new=json.loads(lp.read_text(encoding='utf-8'))['reviews'];assert all(new[k]==e for k,e in prior.items())
receipt=d/('batch-034-'+lang+'-ledger-validation.json');assert not receipt.exists()
receipt.write_text(json.dumps(dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),
 recordStdout=r.stdout,ledgerStdout=c.stdout,priorEntriesUnchanged=len(prior),priorBatchEvidenceEntriesUnchanged=len(old),
 sourceHash=v['sourceSha256'],translationHash=v['sha256'],newAiReviews=1,humanReviews=0,
 scope='Only the fully read selected translation added;priorledger/evidenceentries unchanged,publicationpending.'),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
doc['stages'].append(dict(date=today,languagesRead=[lang],allOriginalAndRevisedBodiesRead=True,
 sourceHash=v['sourceSha256'],validation=entry['validation'],checks='docs/translation-review/'+stem+'-checks.json',
 ledgerValidation=receipt.relative_to(root).as_posix(),texExpressions=v['texExpressions'],displayMath=47,coreDisplayBlocks=47,
 diagramsEach=4,diagramEdgesEach=[10,7,9,5],articleExecutableProgramsEach=1,proseFragmentsPreserved=v['proseFragmentsPreserved'],
 sourceFrozenForFollowingTranslations=True,actualPreviewBundles=35,sourceSnapshotsExact=455,multilingualPages=1983,
 httpsHtmlPages=3616,httpsXmlFiles=41,existingTestsPreviouslyPassedNotRerun=17,
 priorTests='docs/translation-review/batch-034-ja-en-checks-r2.json',reviewedTranslationsTotal=total,
 unreviewedTranslations=13032-total,humanReviews=0,otherTranslationsUnreviewed=other,publicationPending=True))
assert all(doc['reviews'][k]==e for k,e in old.items());p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
goal=root/'docs/translation-review-goal.md';text=goal.read_text(encoding='utf-8')
previous=f'- 全記事の編集キュー13,032行のうち、AI校閲済み{total-1}、未校閲{13032-total+1:,}。未確認の翻訳を校閲済みにはしない。'
assert previous in text
text=text.replace(previous,f'- 全記事の編集キュー13,032行のうち、AI校閲済み{total}、未校閲{13032-total:,}。未確認の翻訳を校閲済みにはしない。')
text+='\n- '+today+' バッチ034の'+lang+'を旧稿・改稿とも本文全体で照合。'+notes['goalNote']+f' {v["texExpressions"]}TeX／47表示式・4図31辺・10参照・実コード出力と説明文{v["proseFragmentsPreserved"]}断片を確認。35束455原稿一致、1983多言語頁／HTTPS3616HTML41XML。既存17テストは日英成功を参照し未再実行。原文・先行校閲エントリ不変、AI{total}／未確認{13032-total:,}／人0、他{other}翻訳本文と034公開・全記事goal継続。\n'
goal.write_text(text,encoding='utf-8');print(r.stdout.strip());print(c.stdout.strip())
