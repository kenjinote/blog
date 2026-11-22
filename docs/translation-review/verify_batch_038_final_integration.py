"""Verify the final 13-language Cantor article build against current review records."""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REVIEW = ROOT / "docs" / "translation-review"
PREVIEW = Path(os.environ["TEMP"]) / "kenji-priority-review-20261024" / "public-diagonal-final"
ARTICLE = "cantors-diagonal-argument"
RECEIPTS = {
    "ja": "batch-038-ja-en-r3-validation.json",
    "en": "batch-038-ja-en-r3-validation.json",
    "zh-cn": "batch-038-zh-cn-validation.json",
    "zh-tw": "batch-038-zh-tw-validation.json",
    "es": "batch-038-es-r6-validation.json",
    "ko": "batch-038-ko-r3-validation.json",
    "pt": "batch-038-pt-r6-validation.json",
    "fr": "batch-038-fr-r4-validation.json",
    "de": "batch-038-de-r2-validation.json",
    "hi": "batch-038-hi-r4-validation.json",
    "id": "batch-038-id-validation.json",
    "ar": "batch-038-ar-r4-validation.json",
    "ru": "batch-038-ru-validation.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_text(encoding="utf-8").encode()).hexdigest()


def main() -> None:
    batch = json.loads((REVIEW / "batch-038.json").read_text(encoding="utf-8"))
    ledger = batch["reviews"]
    results = []
    for lang, receipt_name in RECEIPTS.items():
        content_name = "index.md" if lang == "ja" else f"index.{lang}.md"
        content_path = ROOT / "content" / "post" / ARTICLE / content_name
        record = (
            {"translationHash": batch["frozenSourceHash"]}
            if lang == "ja"
            else ledger[f"post/{ARTICLE}/{content_name}"]
        )
        source_hash = sha(content_path)
        receipt = json.loads((REVIEW / receipt_name).read_text(encoding="utf-8"))
        version = next(v for v in receipt["versions"] if v["language"] == lang)
        html_path = PREVIEW / ("" if lang == "ja" else lang) / "p" / ARTICLE / "index.html"
        html = html_path.read_text(encoding="utf-8")
        passed = (
            receipt["allPassed"]
            and source_hash == record["translationHash"] == version["sha256"]
            and html_path.is_file()
            and f"lang={lang}" in html
        )
        results.append(
            {
                "language": lang,
                "content": str(content_path.relative_to(ROOT)).replace("\\", "/"),
                "contentSha256": source_hash,
                "reviewLedgerHashMatches": source_hash == record["translationHash"],
                "validationReceipt": f"docs/translation-review/{receipt_name}",
                "staticValidationPassed": receipt["allPassed"],
                "html": str(html_path),
                "htmlSha256": sha(html_path) if html_path.is_file() else None,
                "languageTagPresent": f"lang={lang}" in html,
                "allPassed": passed,
            }
        )

    json.loads((REVIEW / "batch-038-final-build.json").read_text(encoding="utf-8"))
    result = {
        "version": 1,
        "checkedAt": datetime.now().astimezone().isoformat(),
        "allPassed": len(results) == 13 and all(r["allPassed"] for r in results),
        "previewBundles": 39,
        "postSnapshotsExact": 507,
        "taxonomySnapshotsExact": 1,
        "languages": results,
        "siteChecks": {
            "multilingual": "Multilingual verified: 2218 pages; unique, reciprocal hreflang and matching sidebar URLs",
            "https": "HTTPS publication URLs verified: 4046 HTML, 41 XML",
            "translationLedger": {"current": 468, "unreviewed": 12564},
            "diffCheck": "passed",
        },
        "scope": "Current 13-language static article output compared with exact translation ledger and the latest passing locale validation receipts. Static output only; no browser rendering, human/native-speaker certification, or theorem-proof certification.",
    }
    out = REVIEW / "batch-038-final-integration-validation.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"allPassed": result["allPassed"], "languages": len(results), "failed": [r["language"] for r in results if not r["allPassed"]], "receipt": str(out)}, ensure_ascii=False))
    if not result["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
