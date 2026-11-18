from pathlib import Path
from datetime import datetime, timezone, timedelta
import copy, hashlib, json, subprocess, sys

ROOT = Path.cwd()
D = ROOT / 'docs/translation-review'
read = lambda name: json.loads((D / name).read_text(encoding='utf-8'))
digest = lambda name: hashlib.sha256((ROOT / 'content' / name).read_text(encoding='utf-8-sig').encode()).hexdigest()
doc = read('batch-037.json')
assert len(doc['reviews']) == 10
proof = read('batch-037-ru-validation.json')
checks = read('batch-037-ru-checks.json')
assert proof['allPassed'] and checks['allPassed']
assert checks['postSnapshotsExact'] == 494 and checks['actualPreviewBundles'] == 38
assert read('batch-037-ru-original-reading.json')['originalBodyFullyRead']
source = 'post/godels-incompleteness-theorems/index.md'
key = 'post/godels-incompleteness-theorems/index.ru.md'
assert digest(source) == doc['frozenSourceHash']
assert digest(key) == proof['sourceSha256']
notes = {
    'meaning': 'Original and saved revised Russian whole bodies read and compared with the whole revised Japanese source: introduction, eight chapters, conclusion and references. Replaced absolute unprovability with theory-relative unprovability; restored effective axiomatization and sufficient PA-extension assumptions; distinguished consistency, soundness, completeness and decidability. Clarified Hilbert program, stronger theories and limits of human/AI conclusions.',
    'terminology': 'Distinguished непротиворечивость, семантическая корректность, синтаксическая полнота and разрешимость. Checked эффективная аксиоматизация, схема аксиом индукции, лемма о неподвижной точке, предикат доказуемости, условия выводимости, вещественно замкнутые поля and элиминация кванторов. Distinguished вычислимость from сложность and ordinary consistency from omega-consistency; explicitly included zero in natural numbers.',
    'mathematics': 'Compared fixed-point and consistency displays exactly with Japanese. Read the finite-proof contradiction argument and external truth argument, explicitly separating failure to prove G from failure to refute G under consistency alone. Checked symbol coding 2,3,2 and positional primes 2,3,5 giving 2700. Qualified real closed fields by first-order language and halting argument by soundness. Static HTML preserves 34 TeX expressions, two displays and all four graphs with 3,5,4,4 edges. No new theorem or full proof certification.',
    'code': 'No executable programs occur in this article. Read all four Mermaid sources and translated labels, compared graph structure with Japanese and checked preservation in HTML. Browser Mermaid execution was not tested.',
    'links': 'Four external references match Japanese; three article links use Russian routes for Hilbert, Godel and halting-problem. Removed unrelated CAP consistency and Turing-machine targets. Static checks cover title, actual September14 publication date, November19 lastmod, cover, canonical, unique reciprocal hreflang and article-preserving sidebar. Fresh38bundle preview:494posts+1tag,2139 multilingual pages,3898HTTPS HTML and41XML. Primary-source reading limited to previously documented excerpts.'
}
entry = dict(reviewKind='ai', reviewedAt='2026-11-19', reviewer='Codex (AI)', source=source,
    sourceHash=digest(source), translationHash=digest(key),
    checks={k: dict(status='checked', note=v) for k,v in notes.items()},
    summary='Full Russian comparison with corrected Japanese incompleteness article, including theorem conditions, terminology, coding, diagrams and references.',
    languageSpecificFindings='Read entire original and saved revised Russian; subsequently read final changed coding sentence and graph label. Removed literal здравый смысл and самодоказать phrasing and absolute-unprovability framing. Distinguished own correctness from consistency, fixed same-zero codes and factorization domain, clarified finite formula sequences constituting proofs. Corrected CAP and Turing-machine targets and removed self-links. Final punctuation and lastmod updated November19; original reading receipt remains November17.',
    validation='docs/translation-review/batch-037-ru-validation.json',
    limitations=['AI review, not human or native-speaker certification.', 'Arabic original body remains unread.', 'Static HTML only; no browser KaTeX/Mermaid execution.', 'Selected primary-source excerpts only; no full-paper review or theorem certification.', 'Batch037 publication and all-article goal remain pending.'])
ledger = ROOT / 'data/translation_reviews.json'
prior = copy.deepcopy(json.loads(ledger.read_text(encoding='utf-8'))['reviews'])
assert len(prior) == 454 and key not in prior
doc['reviews'][key] = entry
doc['stages'].append(dict(date='2026-11-19', stage='Russian whole original/revised comparison and static HTML validation', validation=entry['validation'], reviewedTranslationsAdded=1))
doc['scope'] = 'Japanese and11translations whole bodies reviewed;11AI records, Arabic unread. Static preview passed. Publication037 and full goal pending.'
(D/'batch-037.json').write_text(json.dumps(doc, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
r = subprocess.run([sys.executable,'scripts/translation_reviews.py','record',key,'--source',source,'--reviewer','Codex (AI)','--kind','ai','--evidence','docs/translation-review/batch-037.json','--date','2026-11-19'],capture_output=True,text=True,encoding='utf-8',check=True)
c = subprocess.run([sys.executable,'scripts/translation_reviews.py','check'],capture_output=True,text=True,encoding='utf-8',check=True)
assert json.loads(c.stdout) == dict(current=455, unreviewed=12577)
new = json.loads(ledger.read_text(encoding='utf-8'))['reviews']
assert all(new[k] == v for k,v in prior.items())
receipt = dict(checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(), recordStdout=r.stdout, ledgerStdout=c.stdout, priorEntriesUnchanged=454, sourceHash=digest(source), translationHash=digest(key), newAiReviews=1, humanReviews=0, publicationPending=True)
(D/'batch-037-ru-ledger-validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
goal = ROOT/'docs/translation-review-goal.md'
s = goal.read_text(encoding='utf-8')
assert 'AI校閲済み454、未校閲12,578' in s
s = s.replace('AI校閲済み454、未校閲12,578','AI校閲済み455、未校閲12,577')
s += '\n- 2026-11-19 ゲーデルの不完全性定理のロシア語旧稿・改稿を全文照合し最終修正を検証。無矛盾性と意味論的健全性、定理の条件、証明列と図の符号、直訳表現・誤リンクを訂正。AI校閲累計455／未確認12,577／人0。数式・図・本文と38束の静的検査を通過。アラビア語と公開確認は未完了。\n'
goal.write_text(s,encoding='utf-8')
print(c.stdout)
