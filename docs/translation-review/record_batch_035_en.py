"""Append the actually completed English review; never infer reading from static tests."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import copy,hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
p=D/'batch-035.json';doc=json.loads(p.read_text(encoding='utf-8'));old=copy.deepcopy(doc['reviews']);assert not old
notes=json.loads((D/'batch-035-en-reading-notes.json').read_text(encoding='utf-8'))
assert notes['allOriginalAndRevisedBodiesRead'] and set(notes['checks'])=={'meaning','terminology','mathematics','code','links'}
assert all(len(s)>60 for s in notes['checks'].values())
proof=json.loads((D/'batch-035-en-validation.json').read_text(encoding='utf-8'))
checks=json.loads((D/'batch-035-en-checks.json').read_text(encoding='utf-8'))
assert proof['allPassed'] and checks['allPassed'] and checks['postSnapshotsExact']==468 and checks['taxonomySnapshotsExact']==1
assert checks['actualPreviewBundles']==36 and checks['unitTestsRerun']==0 and checks['existingTestsPreviouslyPassedNotRerun']==17
assert len(checks['results'])==4 and all(r['exitCode']==0 for r in checks['results'])
assert '2035 pages' in checks['results'][1]['stdout'] and "'html': 3709" in checks['results'][2]['stdout']
v=next(v for v in proof['versions'] if v['language']=='en')
assert v['passed'] and v['displayMath']==39 and v['coreDisplayBlocks']==38 and v['diagramEdges']==[6,5] and v['pseudocodeBlocks']==2 and v['articleExecutablePrograms']==0 and v['references']==8
source='post/'+doc['article']+'/index.ja.md';key='post/'+doc['article']+'/index.en.md'
digest=lambda path:hashlib.sha256(path.read_text(encoding='utf-8-sig').encode()).hexdigest()
assert digest(ROOT/'content'/source)==v['sourceSha256']==doc['frozenSourceHash']
assert digest(ROOT/'content'/key)==v['sha256']
ledger_path=ROOT/'data/translation_reviews.json';prior=copy.deepcopy(json.loads(ledger_path.read_text(encoding='utf-8'))['reviews']);assert len(prior)==420 and key not in prior
today=datetime.now(timezone(timedelta(hours=9))).date().isoformat()
entry=dict(reviewKind='ai',reviewedAt=today,reviewer='Codex (AI)',source=source,sourceHash=v['sourceSha256'],translationHash=v['sha256'],
    checks={k:dict(status='checked',note=n) for k,n in notes['checks'].items()},summary=notes['summary'],languageSpecificFindings=notes['languageSpecificFindings'],validation='docs/translation-review/batch-035-en-validation.json',
    limitations=['AI review, not human or native-speaker certification.',
        'Other11 original bodies have been read but their semantic revisions remain pending;117 mechanical escape repairs are not approval.',
        'Two proof pseudocodes, zero executable article programs. No true C/K/Omega oracle, general theorem or full compressor/LLM/corpus/benchmark certification.',
        'Primary research restricted to documented selected pages/abstracts/returned passages, not full-paper reading or experimental reproduction.',
        'Selected36-bundle static HTML; no browser/KaTeX/Mermaid execution or full-site certification. Prior17tests referenced, not rerun for English.',
        'Batch035 publication and the complete all-article goal remain pending.'])
doc['reviews'][key]=entry;p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
r=subprocess.run([sys.executable,'scripts/translation_reviews.py','record',key,'--source',source,'--reviewer','Codex (AI)','--kind','ai','--evidence','docs/translation-review/batch-035.json','--date',today],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True)
c=subprocess.run([sys.executable,'scripts/translation_reviews.py','check'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True)
assert json.loads(c.stdout)=={'current':421,'unreviewed':12611}
new=json.loads(ledger_path.read_text(encoding='utf-8'))['reviews'];assert all(new[k]==e for k,e in prior.items())
out=D/'batch-035-en-ledger-validation.json';assert not out.exists()
out.write_text(json.dumps(dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),recordStdout=r.stdout,ledgerStdout=c.stdout,priorEntriesUnchanged=420,sourceHash=v['sourceSha256'],translationHash=v['sha256'],newAiReviews=1,humanReviews=0,scope='Only fully read/revised EN added; frozen JA and prior420 entries unchanged. Publication pending.'),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
doc['stages'].append(dict(date=today,stage='Full English original/revised semantic comparison and static validation',languagesRead=['en'],allOriginalAndRevisedBodiesRead=True,revisedReadingRanges=['1–280','281–557','three final wording replacements'],sourceHash=v['sourceSha256'],translationHash=v['sha256'],validation='docs/translation-review/batch-035-en-validation.json',checks='docs/translation-review/batch-035-en-checks.json',reading='docs/translation-review/batch-035-en-reading-notes.json',ledgerValidation='docs/translation-review/batch-035-en-ledger-validation.json',texExpressions=219,displayMath=39,coreDisplayBlocks=38,diagrams=2,diagramEdges=[6,5],references=8,pseudocodeBlocks=2,articleExecutablePrograms=0,proseFragmentsPreserved=281,strongSpans=21,actualPreviewBundles=36,postSnapshotsExact=468,taxonomySnapshotsExact=1,multilingualPages=2035,httpsHtmlPages=3709,httpsXmlFiles=41,existingTestsPreviouslyPassedNotRerun=17,priorTests='docs/translation-review/batch-035-ja-r2-checks.json',reviewedTranslationsAdded=1,reviewedTranslationsTotal=421,unreviewedTranslations=12611,humanReviews=0,otherTranslationsSemanticallyUnreviewed=11,publicationPending=True))
doc['scope']='All13 original bodies read. Frozen Japanese and English full revisions read; English1AI registered. Other11 only117 mechanical escape repairs, not full revised semantic review. Prior420 entries unchanged. Publication and whole goal pending.'
p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
goal=ROOT/'docs/translation-review-goal.md';s=goal.read_text(encoding='utf-8')
before='- 全記事の編集キュー13,032行のうち、AI校閲済み420、未校閲12,612。未確認の翻訳を校閲済みにはしない。';assert before in s
s=s.replace(before,'- 全記事の編集キュー13,032行のうち、AI校閲済み421、未校閲12,611。未確認の翻訳を校閲済みにはしない。')
s+='\n- '+today+' バッチ035英語を旧稿537行・改稿557行とも全文照合しAI校閲を1件記録。'+notes['goalNote']+' 219TeX／39表示式（共通38＋英語固有1）、2図11辺・8参照・2擬似コード（掲載実行0）、281本文断片・21強調を実HTMLで確認。36束468post＋タグ1原稿一致、2035多言語／HTTPS3709HTML41XML。既存17テストはJA R2成功を参照、未再実行。原文と先行420記録不変、AI421／未確認12,611／人0。他11翻訳の改稿全文照合・公開・全記事goal継続。\n'
goal.write_text(s,encoding='utf-8');print(r.stdout.strip());print(c.stdout.strip())
