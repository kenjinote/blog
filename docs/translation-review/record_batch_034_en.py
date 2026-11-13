from pathlib import Path
from datetime import datetime,timezone,timedelta
import copy,hashlib,json,subprocess,sys
root=Path('C:/work/kenji.blog');d=root/'docs/translation-review'
slug='error-correcting-codes-hamming-reed-solomon-ldpc-shannon-capacity-information-theory'
source='post/'+slug+'/index.ja.md';key='post/'+slug+'/index.en.md'
out=d/'batch-034.json';assert not out.exists()
proof=json.loads((d/'batch-034-ja-en-validation-r2.json').read_text(encoding='utf-8'))
checks=json.loads((d/'batch-034-ja-en-checks-r2.json').read_text(encoding='utf-8'))
assert proof['allPassed'] and checks['allPassed'] and checks['actualPreviewBundles']==35 and checks['sourceSnapshotsExact']==455
assert len(checks['results'])==7 and all(r['exitCode']==0 for r in checks['results'])
assert '1983 pages' in checks['results'][1]['stdout'] and "'html': 3616" in checks['results'][2]['stdout']
versions={v['language']:v for v in proof['versions']};ja=versions['ja'];en=versions['en']
assert ja['texExpressions']==435 and en['texExpressions']==272 and en['displayMath']==55 and en['coreDisplayBlocks']==47
assert all(v['articleExecutablePrograms']==1 and v['displayedOutputExact'] and v['diagramEdges']==[10,7,9,5] and v['references']==10 for v in versions.values())
assert en['proseFragmentsPreserved']==324 and ja['proseFragmentsPreserved']==371
digest=lambda p:hashlib.sha256(p.read_text(encoding='utf-8-sig').encode()).hexdigest()
assert digest(root/'content'/source)==ja['sha256']==en['sourceSha256']=='371d428b34995ba3dcbb39f9aa0e35db27a6bdda9a92840815fc1c9b690041da'
assert digest(root/'content'/key)==en['sha256']
ledger_path=root/'data/translation_reviews.json'
prior=copy.deepcopy(json.loads(ledger_path.read_text(encoding='utf-8'))['reviews'])
assert len(prior)==408 and key not in prior and not any(slug in k for k in prior)
today=datetime.now(timezone(timedelta(hours=9))).date().isoformat();assert today=='2026-11-13'
notes={
 'meaning':'Read actual complete original JA/EN including all8sections,4Mermaid diagrams,mathematical derivations/comparison tables,entire Python and displayed outputs. Reread current old EN lines1–170,171–435,436–end and actual revised EN1–330,331–660,661–898 plus final editorial patch. Compared against complete revised JA, whose unchanged LFhash matches prior R4. Retained all8themes and added JA applications/perfect-code scope omitted in oldEN. Corrected guaranteed-radius versus asymptotic reliability,QR codewords versus arbitrary area,spacecraft history/power units,noise/input constraints,and unqualified universal architecture/performance claims. Preserved useful EN-specific proof and examples rather than replacing them with a shortened summary.',
 'terminology':'Compared error versus known-position erasure,codeword/symbol/byte versus image area,code rate bits/use versus information rate bits/s,received Eb/N0 versus S/N,infimum versus positive-efficiency bound,systematic H versus binary column ordering,evaluation message coefficients versus cyclic codeword coefficients,prime GF257 versus extension GF256,rank versus row count,intrinsic/equal-prior/extrinsic LLR,symmetric capacity I(W) versus optimized C,SC versus list-dependent SCL. Retained English Hamming message1011/syndrome011,nonadjacent indices1/6/13,primitive-power example,and corrected Vandermonde independence wording from scalar coordinates to matrix columns.',
 'mathematics':'Read and compared all47shared display blocks,with only three Japanese annotation translations,plus eight EN display additions: natural-log Chernoff bound,asymptotic typical-set counting heuristic,triangle inequality,byte polynomial,Vandermonde determinant,characteristic2formal derivative,and two polarization limits with0<delta<1. Corrected arbitrary radius to t<=floor((d-1)/2),zero syndrome interpretation,Forney extraX for explicitly j=1 syndrome convention,AWGN ln2 as wideband infimum,LDPC k=n-rankH/iteration and cycle limits,and finite versus asymptotic Polar guarantees. English finite auxiliary checks784Chernoff model cases,100independent GF256Vandermonde determinants,2^500approximation,99.94percent sparse example,alpha^8 andHamming example pass. Earlier independent320multi-errorForney magnitudes/65025one-errorcounterexamples retained;finite evidence is not a theorem proof or hardware benchmark.',
 'code':'Read both complete old JA/EN implementations,whose failures and mismatched displayed outputs remain preserved. Read actual revised full GF256code in both bodies and ran each extracted program as a standalone subprocess;exit0/stdout exactly match displayed output and decodedHTML. Rank-aware rectangular Gaussian solving,degrees0..t,Q/Edivision/remainder/degree validation,re-encoding/distance verification,and explicit beyond-radius miscorrection example reviewed. Shared actual code supports zero/fewer-than-t errors and zero evaluation point;byte validation and evaluation code versus full QR format distinguished. Existing independent65536fieldproducts/255inverses/full65536wordn4k2codebook against256receivedvectors/3828single-error cases/144seededcases/24invalidcases referenced byte-identical candidate. Newly exercised oldENalpha-power evaluation points and0–3oforiginalindices1,6,13;codeword matches old actual stdout,not its wrong displayed output. Four complete Mermaid graphs/31edges andcomparison table retained. No full QR/spacecraft/LDPC/Polar implementation,performance or all-input execution claim.',
 'links':'Ten primary/official references match JA/source and actualHTML;their limited actual page/abstract reading scopes remain in source notes,not full-paper certification. OriginalEN had no external reference list and no invented broken-link removal is claimed. Publication date2026-10-18T08:00:00+09:00,slug,imagehash andEnglish taxonomy preserved;actualNov13lastmod andexplicitmermaidflag. Current source/HTML272ENand435JATeX,all47coreblocks,8graphs62edges,allcode/output and324EN/371JAprosefragments verified. First prose check failed on Hugo smart apostrophes;initial receipt/helper retained,only prose apostrophes normalized in successful freshR2,math/code remain exact.35bundle455snapshot/1983multilingualpage/3616HTTPSHTML41XML and17unit tests pass. Publication034pending;other11bodies unread.'
}
entry=dict(reviewKind='ai',reviewedAt=today,reviewer='Codex (AI)',source=source,sourceHash=ja['sha256'],translationHash=en['sha256'],
 checks={k:dict(status='checked',note=n) for k,n in notes.items()},
 summary='Complete English error-correcting-code comparison with corrected guarantees,convention-specific algebra,and executed educational GF256 decoder.',
 languageSpecificFindings='OldENalreadyallowednonnegativecapacity;didnotassignJapanesealways-positivewordingtothisversion. Corrected capacityfromnoisealone,exactdisjointtypicalballpacking,systematicHsyndromenumberinterpretation,Vandermondescalarindependence,extraXForneywithitsownexplicitS(z),unqualified0.0045dB/allSSD/allcontrolclaims,anddisplayedstdoutmismatch. Retained Chernoff/natural-log condition,2^500example,Hamming1011,GFzero-divisor16x16/alpha8,Vandermonde/derivative/polar-limits,99.94percentexamplewithrankcondition,andoldalpha-pointnonadjacenterrorcase. Shared newdemo usesbytepoints1..15andexplains changedcodeword.',
 validation='docs/translation-review/batch-034-ja-en-validation-r2.json',
 limitations=['AI review,not human or native-speaker certification.','Other11translation bodies remain unread andunreviewed.','Finite arithmetic and execution evidence,not all-input theorem proof,real hardware/spacecraft tests,full QR/LDPC/Polar software or speed benchmarks.','Primary reading limited to documented selected pages/abstracts;no entire papers/standard or browser/KaTeX/Mermaid runtime certification.','Batch034publication andwholegoal remain pending.'])
doc=dict(version=1,article=slug,sourceAudit='docs/translation-review/batch-034-source-audit.json',
 sourceNotes='docs/translation-review/batch-034-source-notes.md',
 sourceFrozenForFollowingTranslations=True,frozenSourceHash=ja['sha256'],reviews={key:entry},stages=[],
 publicationPending=True)
out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
record=subprocess.run([sys.executable,'scripts/translation_reviews.py','record',key,'--source',source,'--reviewer','Codex (AI)','--kind','ai','--evidence','docs/translation-review/batch-034.json','--date',today],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True)
check=subprocess.run([sys.executable,'scripts/translation_reviews.py','check'],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True)
assert json.loads(check.stdout)=={'current':409,'unreviewed':12623}
current=json.loads(ledger_path.read_text(encoding='utf-8'))['reviews'];assert all(current[k]==v for k,v in prior.items())
lp=d/'batch-034-en-ledger-validation.json';assert not lp.exists()
lp.write_text(json.dumps(dict(version=1,checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(),
 recordStdout=record.stdout,ledgerStdout=check.stdout,priorEntriesUnchanged=408,newAiReviews=1,humanReviews=0,
 sourceHash=ja['sha256'],translationHash=en['sha256'],
 scope='Only fully read/revised English registered. Other11unread,publicationpending. Allprior408ledger/evidence entries retained.'),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
doc['stages'].append(dict(date=today,languagesRead=['ja','en'],allOriginalAndRevisedBodiesRead=True,
 sourceHash=ja['sha256'],validation=entry['validation'],checks='docs/translation-review/batch-034-ja-en-checks-r2.json',
 ledgerValidation=lp.relative_to(root).as_posix(),sourceFrozenForFollowingTranslations=True,
 texExpressions={'ja':435,'en':272},displayMath={'ja':47,'en':55},sharedCoreDisplayBlocks=47,
 diagramsEach=4,diagramEdgesEach=[10,7,9,5],articleExecutableProgramsEach=1,actualPreviewBundles=35,
 sourceSnapshotsExact=455,multilingualPages=1983,httpsHtmlPages=3616,httpsXmlFiles=41,existingTestsRerun=17,
 reviewedTranslationsTotal=409,unreviewedTranslations=12623,humanReviews=0,otherTranslationsUnreviewed=11,publicationPending=True))
assert doc['reviews'][key]==entry
out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
goal=root/'docs/translation-review-goal.md';text=goal.read_text(encoding='utf-8')
old='- 全記事の編集キュー13,032行のうち、AI校閲済み408、未校閲12,624。未確認の翻訳を校閲済みにはしない。'
assert old in text;text=text.replace(old,'- 全記事の編集キュー13,032行のうち、AI校閲済み409、未校閲12,623。未確認の翻訳を校閲済みにはしない。')
text+='\n- '+today+' バッチ034の英語旧稿・改稿を全8章・数式・4図・掲載Python・出力まで通読し、日本語修正版と照合。共通47表示式と英語独自8表示式を確認し、誤り訂正半径、Forney規約、典型集合の厳密な球充填という誤解、Vandermonde独立性、LDPC階数・Polar有限長・用途断定を訂正。英語272TeX／55表示式・4図31辺・10参照・説明文324断片と日435TeX・371断片、実コード2本と出力一致を確認。784Chernoff例・100独立Vandermonde行列・旧英評価点と0～3誤り例も成功。初回のスマート引用符による照合失敗を保存し文章のアポストロフィだけを正規化、新規R2で35束455原稿・1983多言語頁／HTTPS3616HTML41XML／既存17テスト成功。日本語SHA371d428b34995ba3dcbb39f9aa0e35db27a6bdda9a92840815fc1c9b690041daを後続用に固定。AI409／未確認12,623／人0、他11本文は未読、034公開と全記事goalは継続。\n'
goal.write_text(text,encoding='utf-8')
print(record.stdout.strip());print(check.stdout.strip())
