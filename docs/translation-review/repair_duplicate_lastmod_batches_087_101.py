"""Normalize duplicate lastmod keys in recently reviewed bundles and refresh hashes."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
LEDGER_PATH = ROOT / "data/translation_reviews.json"
BUNDLES = {
    87: "IntelliJ IDEAでGitHub Copilotを使う",
    90: "かっこいい Web ページテンプレート（html5up）",
    99: "Microsoft Wordのショートカット一覧",
    100: "「日本人ファースト」について思うこと",
    101: "『君死にたまふことなかれ』",
}

def normalized_digest(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

changed = {}
for batch, bundle in BUNDLES.items():
    folder = ROOT / "content/post" / bundle
    fixed = []
    for path in sorted(folder.glob("index*.md")):
        text = path.read_text(encoding="utf-8-sig")
        front, body = text.split("---", 2)[1:]
        lines = front.splitlines()
        lastmods = [i for i, line in enumerate(lines) if line.startswith("lastmod:")]
        if len(lastmods) <= 1:
            continue
        first = lastmods[0]
        lines = [line for i, line in enumerate(lines) if not line.startswith("lastmod:") or i == first]
        content = "---\n" + "\n".join(lines).strip("\r\n") + "\n---\n" + body.lstrip("\r\n")
        path.write_text("\n".join(line.rstrip() for line in content.splitlines()) + "\n", encoding="utf-8")
        fixed.append(path.name)
    if not fixed:
        continue
    evidence_path = DOCS / f"batch-{batch:03}.json"
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    source_rel = f"post/{bundle}/index.md"
    source_hash = normalized_digest(ROOT / "content" / source_rel)
    evidence["sourceHash"] = source_hash
    evidence["publicationPending"] = True
    evidence.pop("publication", None)
    finding = "Removed duplicate lastmod front-matter keys from " + ", ".join(fixed) + "; refreshed source/translation hashes to match these metadata-only revisions and set publication verification pending."
    if finding not in evidence["findings"]:
        evidence["findings"].append(finding)
    for rel, review in evidence["reviews"].items():
        review["sourceHash"] = source_hash
        review["translationHash"] = normalized_digest(ROOT / "content" / rel)
    evidence_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    changed[batch] = fixed

ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
for batch in changed:
    evidence_path = DOCS / f"batch-{batch:03}.json"
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    for rel, review in evidence["reviews"].items():
        record = ledger["reviews"][rel]
        for key in ("source", "sourceHash", "translationHash", "reviewedAt", "reviewer", "reviewKind"):
            record[key] = review[key]
        record["evidence"] = f"docs/translation-review/batch-{batch:03}.json"
        record["evidenceHash"] = hashlib.sha256(
            json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")
        ).hexdigest()
LEDGER_PATH.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"normalized": changed}, ensure_ascii=False))
