from pathlib import Path
from datetime import datetime, timezone, timedelta
import copy, hashlib, json, subprocess, sys

ROOT = Path.cwd()
D = ROOT / 'docs/translation-review'
read = lambda name: json.loads((D / name).read_text(encoding='utf-8'))
digest = lambda name: hashlib.sha256((ROOT / 'content' / name).read_text(encoding='utf-8-sig').encode()).hexdigest()
doc = read('batch-037.json')
assert len(doc['reviews']) == 4
proof = read('batch-037-ko-validation.json')
checks = read('batch-037-ko-checks.json')
assert proof['allPassed'] and checks['allPassed']
assert checks['postSnapshotsExact'] == 494 and checks['actualPreviewBundles'] == 38
assert read('batch-037-ko-original-reading.json')['originalBodyFullyRead']
source = 'post/godels-incompleteness-theorems/index.md'
key = 'post/godels-incompleteness-theorems/index.ko.md'
assert digest(source) == doc['frozenSourceHash']
assert digest(key) == proof['sourceSha256']
notes = {
    'meaning': 'Original and saved revised Korean whole bodies read and compared with the whole revised Japanese source: introduction, eight chapters, conclusion and references. Replaced absolute unprovability with theory-relative unprovability; restored effective axiomatization and sufficient PA-extension assumptions; distinguished consistency, soundness, completeness and decidability. Clarified Hilbert program, stronger theories and limits of human/AI conclusions.',
    'terminology': 'Distinguished 무모순성 from 건전성 and 구문적 완전성. Used 괴델 번호화 and 부호화 rather than unclear 괴델 수화, and checked 고정점 보조정리, 귀납법 공리 도식, 증명 가능성 술어, 유도 가능성 조건, 실폐체, 양화사 제거, 계산 가능성 and 계산 복잡도. Distinguished ordinary consistency from omega-consistency and sufficient PA-extension assumptions from weakest possible assumptions.',
    'mathematics': 'Compared fixed-point and consistency displays exactly with Japanese. Read the finite-proof contradiction argument and external truth argument, explicitly separating failure to prove G from failure to refute G under consistency alone. Checked symbol coding 2,3,2 and positional primes 2,3,5 giving 2700. Qualified real closed fields by first-order language and halting argument by soundness. Static HTML preserves 34 TeX expressions, two displays and all four graphs with 3,5,4,4 edges. No new theorem or full proof certification.',
    'code': 'No executable programs occur in this article. Read all four Mermaid sources and translated labels, compared graph structure with Japanese and checked preservation in HTML. Browser Mermaid execution was not tested.',
    'links': 'Four external references match Japanese; three article links use Korean routes for Hilbert, Godel and halting-problem. Removed unrelated CAP consistency and Turing-machine targets. Static checks cover title, actual September14 publication date, November17 lastmod, cover, canonical, unique reciprocal hreflang and article-preserving sidebar. Fresh38bundle preview:494posts+1tag,2139 multilingual pages,3898HTTPS HTML and41XML. Primary-source reading limited to previously documented excerpts.'
}
entry = dict(reviewKind='ai', reviewedAt='2026-11-17', reviewer='Codex (AI)', source=source,
    sourceHash=digest(source), translationHash=digest(key),
    checks={k: dict(status='checked', note=v) for k,v in notes.items()},
    summary='Full Korean comparison with corrected Japanese incompleteness article, including theorem conditions, terminology, coding, diagrams and references.',
    languageSpecificFindings='Repaired spaced bold delimiters with six explicit strong spans. Removed 수법/바꿔치기 suggesting a trick, the literal Korean-sentence framing and claims of absolute unprovability. Distinguished symbol codes from positional primes and corrected the 0 code duplication. Replaced physical-machine and unlimited human/AI claims with stated hypotheses; corrected CAP and halting links. Read complete original and saved revised body against Japanese.',
    validation='docs/translation-review/batch-037-ko-validation.json',
    limitations=['AI review, not human or native-speaker certification.', 'Other7 original translation bodies remain unread.', 'Static HTML only; no browser KaTeX/Mermaid execution.', 'Selected primary-source excerpts only; no full-paper review or theorem certification.', 'Batch037 publication and all-article goal remain pending.'])
ledger = ROOT / 'data/translation_reviews.json'
prior = copy.deepcopy(json.loads(ledger.read_text(encoding='utf-8'))['reviews'])
assert len(prior) == 448 and key not in prior
doc['reviews'][key] = entry
doc['stages'].append(dict(date='2026-11-17', stage='Korean whole original/revised comparison and static HTML validation', validation=entry['validation'], reviewedTranslationsAdded=1))
doc['scope'] = 'Japanese, English, both Chinese, Spanish and Korean whole bodies reviewed;5AI records, other7unread. Static preview passed. Publication037 and full goal pending.'
(D/'batch-037.json').write_text(json.dumps(doc, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
r = subprocess.run([sys.executable,'scripts/translation_reviews.py','record',key,'--source',source,'--reviewer','Codex (AI)','--kind','ai','--evidence','docs/translation-review/batch-037.json','--date','2026-11-17'],capture_output=True,text=True,encoding='utf-8',check=True)
c = subprocess.run([sys.executable,'scripts/translation_reviews.py','check'],capture_output=True,text=True,encoding='utf-8',check=True)
assert json.loads(c.stdout) == dict(current=449, unreviewed=12583)
new = json.loads(ledger.read_text(encoding='utf-8'))['reviews']
assert all(new[k] == v for k,v in prior.items())
receipt = dict(checkedAt=datetime.now(timezone(timedelta(hours=9))).isoformat(), recordStdout=r.stdout, ledgerStdout=c.stdout, priorEntriesUnchanged=448, sourceHash=digest(source), translationHash=digest(key), newAiReviews=1, humanReviews=0, publicationPending=True)
(D/'batch-037-ko-ledger-validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
goal = ROOT/'docs/translation-review-goal.md'
s = goal.read_text(encoding='utf-8')
assert 'AI校閲済み448、未校閲12,584' in s
s = s.replace('AI校閲済み448、未校閲12,584','AI校閲済み449、未校閲12,583')
s += '\n- 2026-11-17 ゲーデルの不完全性定理の韓国語旧稿・改稿を全文照合。무모순성と건전성、괴델 번호화、定理の前提・図の符号・誤リンク・強調記法を修正。AI校閲累計449／未確認12,583／人0。34TeX・2表示式・4図16辺・69本文断片と38束の静的検査を通過。他7言語と公開確認は未完了。\n'
goal.write_text(s,encoding='utf-8')
print(c.stdout)
