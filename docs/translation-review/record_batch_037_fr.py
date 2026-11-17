from pathlib import Path
from datetime import datetime, timezone, timedelta
import copy, hashlib, json, subprocess, sys

ROOT = Path.cwd()
D = ROOT / 'docs/translation-review'
read = lambda name: json.loads((D / name).read_text(encoding='utf-8'))
digest = lambda name: hashlib.sha256((ROOT / 'content' / name).read_text(encoding='utf-8-sig').encode()).hexdigest()
doc = read('batch-037.json')
assert len(doc['reviews']) == 6
proof = read('batch-037-fr-validation.json')
checks = read('batch-037-fr-checks.json')
assert proof['allPassed'] and checks['allPassed']
assert checks['postSnapshotsExact'] == 494 and checks['actualPreviewBundles'] == 38
assert read('batch-037-fr-original-reading.json')['originalBodyFullyRead']
source = 'post/godels-incompleteness-theorems/index.md'
key = 'post/godels-incompleteness-theorems/index.fr.md'
assert digest(source) == doc['frozenSourceHash']
assert digest(key) == proof['sourceSha256']
notes = {
    'meaning': 'Original and saved revised French whole bodies read and compared with the whole revised Japanese source: introduction, eight chapters, conclusion and references. Replaced absolute unprovability with theory-relative unprovability; restored effective axiomatization and sufficient PA-extension assumptions; distinguished consistency, soundness, completeness and decidability. Clarified Hilbert program, stronger theories and limits of human/AI conclusions.',
    'terminology': 'Distinguished coherence, correction semantique, completude syntaxique and decidabilite. Checked schema d axiomes de recurrence, lemme du point fixe, predicat de demonstrabilite, conditions de derivabilite, corps reels clos and elimination des quantificateurs. Distinguished calculabilite from complexite, finite proof checking from proof-existence search, and omega-coherence from ordinary coherence. French accents retained in article.',
    'mathematics': 'Compared fixed-point and consistency displays exactly with Japanese. Read the finite-proof contradiction argument and external truth argument, explicitly separating failure to prove G from failure to refute G under consistency alone. Checked symbol coding 2,3,2 and positional primes 2,3,5 giving 2700. Qualified real closed fields by first-order language and halting argument by soundness. Static HTML preserves 34 TeX expressions, two displays and all four graphs with 3,5,4,4 edges. No new theorem or full proof certification.',
    'code': 'No executable programs occur in this article. Read all four Mermaid sources and translated labels, compared graph structure with Japanese and checked preservation in HTML. Browser Mermaid execution was not tested.',
    'links': 'Four external references match Japanese; three article links use French routes for Hilbert, Godel and halting-problem. Removed unrelated CAP consistency and Turing-machine targets. Static checks cover title, actual September14 publication date, November17 lastmod, cover, canonical, unique reciprocal hreflang and article-preserving sidebar. Fresh38bundle preview:494posts+1tag,2139 multilingual pages,3898HTTPS HTML and41XML. Primary-source reading limited to previously documented excerpts.'
}
entry = dict(reviewKind='ai', reviewedAt='2026-11-17', reviewer='Codex (AI)', source=source,
    sourceHash=digest(source), translationHash=digest(key),
    checks={k: dict(status='checked', note=v) for k,v in notes.items()},
    summary='Full French comparison with corrected Japanese incompleteness article, including theorem conditions, terminology, coding, diagrams and references.',
    languageSpecificFindings='Removed en japonais literal leftover and maquille suggesting illegitimate arithmetization. Removed repeated Hilbert links and the Japanese Euclide target, corrected CAP and halting links. Replaced postulat absolu and absolutely unprovable framing with theory-relative claims and explicit effectiveness/soundness hypotheses. Corrected same-symbol numbering and factorization scope. Read entire original and saved revised French against Japanese, including all graph labels and formula contexts.',
    validation='docs/translation-review/batch-037-fr-validation.json',
    limitations=['AI review, not human or native-speaker certification.', 'Other5 original translation bodies remain unread.', 'Static HTML only; no browser KaTeX/Mermaid execution.', 'Selected primary-source excerpts only; no full-paper review or theorem certification.', 'Batch037 publication and all-article goal remain pending.'])
ledger = ROOT / 'data/translation_reviews.json'
prior = copy.deepcopy(json.loads(ledger.read_text(encoding='utf-8'))['reviews'])
assert len(prior) == 450 and key not in prior
doc['reviews'][key] = entry
doc['stages'].append(dict(date='2026-11-17', stage='French whole original/revised comparison and static HTML validation', validation=entry['validation'], reviewedTranslationsAdded=1))
doc['scope'] = 'Japanese, English, both Chinese, Spanish, Korean, Portuguese and French whole bodies reviewed;7AI records, other5unread. Static preview passed. Publication037 and full goal pending.'
(D/'batch-037.json').write_text(json.dumps(doc, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
r = subprocess.run([sys.executable,'scripts/translation_reviews.py','record',key,'--source',source,'--reviewer','Codex (AI)','--kind','ai','--evidence','docs/translation-review/batch-037.json','--date','2026-11-17'],capture_output=True,text=True,encoding='utf-8',check=True)
c = subprocess.run([sys.executable,'scripts/translation_reviews.py','check'],capture_output=True,text=True,encoding='utf-8',check=True)
assert json.loads(c.stdout) == dict(current=451, unreviewed=12581)
new = json.loads(ledger.read_text(encoding='utf-8'))['reviews']
assert all(new[k] == v for k,v in prior.items())
receipt = dict(checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(), recordStdout=r.stdout, ledgerStdout=c.stdout, priorEntriesUnchanged=450, sourceHash=digest(source), translationHash=digest(key), newAiReviews=1, humanReviews=0, publicationPending=True)
(D/'batch-037-fr-ledger-validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
goal = ROOT/'docs/translation-review-goal.md'
s = goal.read_text(encoding='utf-8')
assert 'AI校閲済み450、未校閲12,582' in s
s = s.replace('AI校閲済み450、未校閲12,582','AI校閲済み451、未校閲12,581')
s += '\n- 2026-11-17 ゲーデルの不完全性定理のフランス語旧稿・改稿を全文照合。「日本語で」という直訳、符号化を偽装とする表現、無矛盾性と健全性の混同、定理の条件・図・誤リンクを修正。AI校閲累計451／未確認12,581／人0。34TeX・2表示式・4図16辺・79本文断片と38束の静的検査を通過。他5言語と公開確認は未完了。\n'
goal.write_text(s,encoding='utf-8')
print(c.stdout)
