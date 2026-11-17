from pathlib import Path
from datetime import datetime,timezone,timedelta
import copy,hashlib,json
ROOT=Path.cwd();D=ROOT/'docs/translation-review'
p=D/'batch-036.json';doc=json.loads(p.read_text(encoding='utf-8'));old=copy.deepcopy(doc['reviews'])
assert len(old)==12 and 'publicationCheckpoints' not in doc and doc['publicationPending']
dispatch=copy.deepcopy(doc['publicationDispatch'])
live=json.loads((D/'publication-036.json').read_text(encoding='utf-8'))
ci=json.loads((D/'batch-036-ci-completion.json').read_text(encoding='utf-8'))
assert live['allPassed'] and len(live['pages'])==481 and len(live['hindiTaxonomyPages'])==3
assert all(page['passed'] and all(page['checks'].values()) for page in live['pages']+live['hindiTaxonomyPages'])
assert live['deployedCommit']==ci['deployedCommit']==dispatch['deployedCommitExpected']=='159f7f81ba89e5940d4b1d965b34fa1fb6108057'
assert live['ciRun']==ci['ciRun']==dispatch['ciRun']==43992951343
assert ci['runAttempt']==dispatch['runAttempt']==1 and ci['status']=='completed' and ci['conclusion']=='success'
jobs={j['name']:j for j in ci['jobs']};assert all(jobs[n]['status']=='completed' and jobs[n]['conclusion']=='success' for n in ('build','deploy'))
pages=[page for page in live['pages'] if '/p/'+doc['article']+'/' in page['url']];assert len(pages)==13
for page in pages:
    assert all(page['checks'][key] for key in ('allReviewedTeXPreserved','haltingDiagramExact','haltingReferencesExact','allSixHaltingCodeTextBlocksExact','allHaltingProsePreserved','haltingCaseTablePresent','haltingStrongSpansPreserved','revisedCoverPresent'))
    if page['language']=='ar':assert page['checks']['rtlPreserved']
ledger=json.loads((ROOT/'data/translation_reviews.json').read_text(encoding='utf-8'))['reviews'];assert len(ledger)==444
digest=lambda path:hashlib.sha256(path.read_text(encoding='utf-8-sig').encode()).hexdigest()
for key,e in old.items():
    assert ledger[key]['sourceHash']==e['sourceHash'] and ledger[key]['translationHash']==e['translationHash']
    assert digest(ROOT/'content'/key)==e['translationHash'] and digest(ROOT/'content'/e['source'])==e['sourceHash']
now=datetime.now(timezone(timedelta(hours=9)))
checkpoint=dict(checkedAt=now.isoformat(),ciRun=ci['ciRun'],ciUrl=ci['ciUrl'],deployedCommit=ci['deployedCommit'],runAttempt=1,ciCompletion='docs/translation-review/batch-036-ci-completion.json',proof='docs/translation-review/publication-036.json',pages=481,passed=481,failed=0,translations=444,japaneseSources=37,mathVersions=286,texExpressions=17571,haltingVersions=13,haltingTeX=415,haltingDiagrams=13,haltingGraphEdges=104,haltingExternalReferencesEach=4,haltingInternalReferencesEach=3,haltingCodeTextBlocks=78,haltingProseFragments=989,additionalHindiTaxonomyPages=3,additionalHindiTaxonomyPassed=3,httpPageProbeAttempts=1,httpPageRetries=0,buildCompletedAt=jobs['build']['completed_at'],deployCompletedAt=jobs['deploy']['completed_at'],scope='Actual first live481articles+3Hindi tags after exact CI head/attempt/build/deploy success. Prior468checks retained. New13halting versions exact math,graphs,references,code/text blocks,prose,tables,title,dates,navigation,cover reference;ArabicRTL. No native/browser/fullsite certification. Whole goal remains active.')
doc['publicationCheckpoints']=[checkpoint];doc['publicationPending']=False
doc['publicationVerifiedBy']='docs/translation-review/publication-036.json'
assert doc['reviews']==old and doc['publicationDispatch']==dispatch
p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
note='\n2026-11-17 Batch036 publication closed after exact CI43992951343 attempt1/head159f7f81ba89e5940d4b1d965b34fa1fb6108057 success. Actual481article+3Hindi tag HTTP checks passed first attempt; new13halting versions415TeX/13graphs104edges/989prose fragments,4external3internal refs and6code/text blocks each; ArabicRTL. Original12review entries and dispatch preserved. AI444/unreviewed12588/human0. Full goal active.\n'
for name in ('docs/translation-review-goal.md','docs/translation-review/batch-036-source-notes.md'):
    with (ROOT/name).open('a',encoding='utf-8') as f:f.write(note)
print(json.dumps(checkpoint))
