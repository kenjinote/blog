"""Close batch034 only after matching CI and actual live publication evidence."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import copy,hashlib,json

ROOT=Path(__file__).resolve().parents[2];D=ROOT/'docs/translation-review'
p=D/'batch-034.json';doc=json.loads(p.read_text(encoding='utf-8'));old=copy.deepcopy(doc['reviews'])
assert len(old)==12 and 'publicationCheckpoints' not in doc and doc['finalAssembly']['publicationPending']
dispatch=copy.deepcopy(doc['publicationDispatch'])
live=json.loads((D/'publication-034.json').read_text(encoding='utf-8'))
ci=json.loads((D/'batch-034-ci-completion.json').read_text(encoding='utf-8'))
assert live['allPassed'] and len(live['pages'])==455 and len(live['hindiTaxonomyPages'])==3
assert all(page['passed'] and all(page['checks'].values()) for page in live['pages']+live['hindiTaxonomyPages'])
assert live['deployedCommit']==ci['deployedCommit']==dispatch['deployedCommitExpected']=='2739fdd698dab528d8ca5b047b1e126be8c180f2'
assert live['ciRun']==ci['ciRun']==dispatch['ciRun']==43439178526
assert ci['runAttempt']==dispatch['runAttempt']==1 and ci['status']=='completed' and ci['conclusion']=='success'
jobs={j['name']:j for j in ci['jobs']};assert all(jobs[n]['status']=='completed' and jobs[n]['conclusion']=='success' for n in ('build','deploy'))
pages=[page for page in live['pages'] if '/p/'+doc['article']+'/' in page['url']];assert len(pages)==13
for page in pages:
    assert all(page['checks'][key] for key in ('allReviewedTeXPreserved','allFourEccDiagramsExact','allTenEccReferencesPresent','completeEccProgramAndActualOutputExact','allReviewedEccProsePreserved','eccComparisonTablePresent'))
    if page['language']=='ar':assert page['checks']['all16EccCodeValuesIsolatedLtr'] and page['checks']['rtlPreserved']
ledger=json.loads((ROOT/'data/translation_reviews.json').read_text(encoding='utf-8'))['reviews'];assert len(ledger)==420
digest=lambda path:hashlib.sha256(path.read_text(encoding='utf-8-sig').encode()).hexdigest()
for key,e in old.items():
    assert ledger[key]['sourceHash']==e['sourceHash'] and ledger[key]['translationHash']==e['translationHash']
    assert digest(ROOT/'content'/key)==e['translationHash'] and digest(ROOT/'content'/e['source'])==e['sourceHash']
now=datetime.now(timezone(timedelta(hours=9)));today=now.date().isoformat()
checkpoint=dict(checkedAt=now.isoformat(),ciRun=ci['ciRun'],ciUrl=ci['ciUrl'],deployedCommit=ci['deployedCommit'],runAttempt=1,ciCompletion='docs/translation-review/batch-034-ci-completion.json',proof='docs/translation-review/publication-034.json',pages=455,passed=455,failed=0,translations=420,japaneseSources=35,mathVersions=260,texExpressions=14315,eccVersions=13,eccTeX=3522,eccDiagrams=52,eccGraphEdges=403,eccReferencesEach=10,eccArticlePrograms=13,eccProseFragments=3918,arabicEccLtrValues=16,additionalHindiTaxonomyPages=3,additionalHindiTaxonomyPassed=3,httpPageProbeAttempts=1,httpPageRetries=0,buildCompletedAt=jobs['build']['completed_at'],deployCompletedAt=jobs['deploy']['completed_at'],scope='Actual first live455article+3Hindi tag checks after matching CI head/attempt/build/deploy success. Prior442 article checks retained; new13 ECC versions exact math/graphs/references/full reviewed program and displayed output/prose/table/title/dates/navigation, Arabic16 LTR and RTL. Program execution local only. No native-speaker/browser/fullsite/full QR-LDPC-Polar/hardware/all-input/benchmark certification. Whole goal remains active.')
doc['publicationCheckpoints']=[checkpoint];doc['publicationPending']=False
doc['finalAssembly']['publicationPending']=False;doc['finalAssembly']['publicationVerifiedBy']='docs/translation-review/publication-034.json'
assert doc['reviews']==old and doc['publicationDispatch']==dispatch
p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (ROOT/'docs/translation-review-goal.md').open('a',encoding='utf-8') as f:
    f.write('\n- '+today+' バッチ034公開確認完了。CI43439178526 attempt1、対象2739fdd698dab528d8ca5b047b1e126be8c180f2に一致し、build '+jobs['build']['completed_at']+'／deploy '+jobs['deploy']['completed_at']+'成功を確認後、455記事URL＋ヒンディー語タグ3URLが実HTTP初回すべて成功、再試行0。新規誤り訂正13版3522TeX／52図403辺／各10参照・掲載コードと実行出力・本文3918断片・表・日付・全言語リンク、アラビア語16LTRとRTLも一致。12校閲エントリと初回dispatch不変。AI420／未確認12,612／人0。次のコルモゴロフ複雑性は原文と英語の予備調査のみで加算0、全記事goal継続。\n')
with (D/'batch-034-source-notes.md').open('a',encoding='utf-8') as f:
    f.write('\nPublication034 closure '+today+': matching CI43439178526 attempt1/head2739fdd698dab528d8ca5b047b1e126be8c180f2 build/deploy success, then actual first live455articles+3Hindi tags all pass, retries0. New13 ECC versions exact3522TeX/52graphs403edges/10refs each/full program and actual output/prose3918/table/title/dates/navigation; Arabic16LTR/RTL. Prior442checks retained. Source and12entries/initial dispatch unchanged; historical failures and pending stages retained. Current publication pending cleared; full goal active,035 preliminary audit adds0.\n')
print(json.dumps(checkpoint))
