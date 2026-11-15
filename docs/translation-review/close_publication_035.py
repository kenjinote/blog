from pathlib import Path
from datetime import datetime,timezone,timedelta
import copy,hashlib,json
ROOT=Path.cwd();D=ROOT/'docs/translation-review'
p=D/'batch-035.json';doc=json.loads(p.read_text(encoding='utf-8'));old=copy.deepcopy(doc['reviews'])
assert len(old)==12 and 'publicationCheckpoints' not in doc and doc['finalAssembly']['publicationPending']
dispatch=copy.deepcopy(doc['publicationDispatch'])
live=json.loads((D/'publication-035.json').read_text(encoding='utf-8'))
ci=json.loads((D/'batch-035-ci-completion.json').read_text(encoding='utf-8'))
assert live['allPassed'] and len(live['pages'])==468 and len(live['hindiTaxonomyPages'])==3
assert all(page['passed'] and all(page['checks'].values()) for page in live['pages']+live['hindiTaxonomyPages'])
assert live['deployedCommit']==ci['deployedCommit']==dispatch['deployedCommitExpected']=='5477149d4e7216e1cc2909d6d38cf2fe18754946'
assert live['ciRun']==ci['ciRun']==dispatch['ciRun']==43661446242
assert ci['runAttempt']==dispatch['runAttempt']==1 and ci['status']=='completed' and ci['conclusion']=='success'
jobs={j['name']:j for j in ci['jobs']};assert all(jobs[n]['status']=='completed' and jobs[n]['conclusion']=='success' for n in ('build','deploy'))
pages=[page for page in live['pages'] if '/p/'+doc['article']+'/' in page['url']];assert len(pages)==13
for page in pages:
    assert all(page['checks'][key] for key in ('allReviewedTeXPreserved','allKolmogorovDiagramsExact','allEightKolmogorovReferencesPresent','bothKolmogorovPseudocodesExact','allKolmogorovProsePreserved','bothKolmogorovTablesPresent'))
    if page['language']=='ar':assert page['checks']['all7KolmogorovCodeValuesIsolatedLtr'] and page['checks']['rtlPreserved']
ledger=json.loads((ROOT/'data/translation_reviews.json').read_text(encoding='utf-8'))['reviews'];assert len(ledger)==432
digest=lambda path:hashlib.sha256(path.read_text(encoding='utf-8-sig').encode()).hexdigest()
for key,e in old.items():
    assert ledger[key]['sourceHash']==e['sourceHash'] and ledger[key]['translationHash']==e['translationHash']
    assert digest(ROOT/'content'/key)==e['translationHash'] and digest(ROOT/'content'/e['source'])==e['sourceHash']
now=datetime.now(timezone(timedelta(hours=9)))
checkpoint=dict(checkedAt=now.isoformat(),ciRun=ci['ciRun'],ciUrl=ci['ciUrl'],deployedCommit=ci['deployedCommit'],runAttempt=1,ciCompletion='docs/translation-review/batch-035-ci-completion.json',proof='docs/translation-review/publication-035.json',pages=468,passed=468,failed=0,translations=432,japaneseSources=36,mathVersions=273,texExpressions=17156,kolmogorovVersions=13,kolmogorovTeX=2841,kolmogorovDiagrams=26,kolmogorovGraphEdges=143,kolmogorovReferencesEach=8,kolmogorovPseudocodeBlocks=26,kolmogorovProseFragments=3337,arabicKolmogorovLtrValues=7,additionalHindiTaxonomyPages=3,additionalHindiTaxonomyPassed=3,httpPageProbeAttempts=1,httpPageRetries=0,buildCompletedAt=jobs['build']['completed_at'],deployCompletedAt=jobs['deploy']['completed_at'],scope='Actual first live468articles+3Hindi tags after exact CI head/attempt/build/deploy success. Prior455checks retained. New13Kolmogorov versions exact math,graphs,references,pseudocodes,prose,tables,title,dates,navigation;Arabic7LTR/RTL. No native/browser/fullsite certification. Whole goal remains active.')
doc['publicationCheckpoints']=[checkpoint];doc['publicationPending']=False
doc['finalAssembly']['publicationPending']=False;doc['finalAssembly']['publicationVerifiedBy']='docs/translation-review/publication-035.json'
assert doc['reviews']==old and doc['publicationDispatch']==dispatch
p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
note='\n2026-11-15: Batch035 publication closed after exact CI43661446242 attempt1/head5477149d4e7216e1cc2909d6d38cf2fe18754946 success. Actual468article+3Hindi tag HTTP checks all passed first attempt; new13Kolmogorov versions2841TeX/26graphs143edges/3337prose fragments,8refs and2pseudocodes each; Arabic7LTR/RTL. Original12review entries and dispatch preserved. AI432/unreviewed12600/human0. Batch036 source/English work remains unapproved. Full goal active.\n'
for name in ('docs/translation-review-goal.md','docs/translation-review/batch-035-source-notes.md'):
    with (ROOT/name).open('a',encoding='utf-8') as f:f.write(note)
print(json.dumps(checkpoint))
