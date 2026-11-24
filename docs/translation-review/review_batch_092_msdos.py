"""Record evidence for the updated MS-DOS 4.00 translation batch."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/MS-DOS 4.0 のオープンソース化"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/MS-DOS 4.0 のオープンソース化/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
BLOG = "https://opensource.microsoft.com/blog/2024/04/25/open-sourcing-ms-dos-4-0/"
REPO = "https://github.com/microsoft/MS-DOS"
LICENSE = "https://github.com/microsoft/MS-DOS/blob/main/v4.0/LICENSE"
LINKS = [BLOG, REPO, LICENSE]
EVIDENCE = "docs/translation-review/batch-092.json"

def require(ok, message):
    if not ok:
        raise SystemExit(message)

def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def load(language):
    path = BUNDLE / ("index.md" if language == "ja" else f"index.{language}.md")
    text = path.read_text(encoding="utf-8-sig")
    require(text.startswith("---\n"), f"{language}: missing front matter")
    front, body = text[4:].split("\n---\n", 1)
    return path, text, front, body

source_path, source_text, source_front, source_body = load("ja")
require(len(re.findall(r"(?m)^date:", source_front)) == 1, "Source has duplicate dates")
require("date: 2024-05-05T16:44:28+09:00" in source_front, "Original date changed")
require(f"lastmod: {TODAY}T00:00:00+09:00" in source_front, "Source lastmod missing")
source_hash = digest(source_text)
reviews = {}
for language in LANGS[1:]:
    path, text, front, body = load(language)
    require(len(re.findall(r"(?m)^date:", front)) == 1, f"{language}: duplicate dates")
    require("date: 2024-05-05T16:44:28+09:00" in front, f"{language}: original date changed")
    require(f"lastmod: {TODAY}T00:00:00+09:00" in front, f"{language}: lastmod missing")
    require("draft: false" in front, f"{language}: publication status changed")
    require(len(re.findall(r"(?m)^##\s", body)) == 3, f"{language}: section structure differs")
    body_links = re.findall(r"\]\((https://[^)]+)\)", body)
    require(all(link in body_links for link in LINKS), f"{language}: official source links differ")
    for marker in ("2024", "8086", "MIT"):
        require(marker in body, f"{language}: missing {marker}")
    review = {
        "reviewKind": "ai", "reviewedAt": TODAY, "reviewer": "Codex (AI)", "source": SOURCE,
        "sourceHash": source_hash, "translationHash": digest(text),
        "summary": "Compared the complete translated article with the Japanese source and checked the April 2024 announcement, repository contents, MIT license, and archived read-only status against Microsoft's official announcement and the Microsoft GitHub repository.",
        "checks": {
            "meaning": {"status": "checked", "note": "Every edition distinguishes the 2024 release event, the historical source/binary/docs material, and the repository's current archived state."},
            "terminology": {"status": "checked", "note": "MS-DOS 4.00, IBM, Microsoft, 8086 assembly, MIT License, binaries, and read-only archive are consistently identified."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no mathematical claims or formulas."},
            "code": {"status": "not_applicable", "note": "The article discusses historical source code but contains no executable code sample."},
            "links": {"status": "checked", "note": "All editions include the Microsoft announcement, official repository, and v4.0 license file."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "This is a historical article; release dates and repository archive status are stated explicitly.", "The linked repository's MIT terms apply as described by its license file."],
    }
    reviews[f"post/{BUNDLE.name}/{path.name}"] = review

entry = {
    "version": 1, "batch": 92, "article": BUNDLE.name, "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": LINKS,
    "scope": "Read the complete Japanese source and all twelve translations. Compared the release date, IBM collaboration, source language, repository contents, MIT license, and archived status with Microsoft's official announcement and repository files.",
    "findings": [
        "Replaced the ambiguous 'nearly 40 years old' framing with the exact 2024 publication date and MS-DOS 4.00 version.",
        "Clarified the IBM partnership, 8086 assembly, repository contents, and previously unreleased beta binaries described in Microsoft's announcement.",
        "Added the MIT license and the repository's archived, read-only status, with direct links to the official license and repository.",
        "Removed duplicate future date metadata, retained the original 2024-05-05 publication date, and set lastmod to 2026-11-24.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-092.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = EVIDENCE
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 92, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
