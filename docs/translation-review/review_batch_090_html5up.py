"""Record evidence for the updated HTML5 UP article (batch 090)."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/かっこいい Web ページテンプレート（html5up）"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/かっこいい Web ページテンプレート（html5up）/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
LINKS = ["https://html5up.net/", "https://html5up.net/license"]
EVIDENCE = "docs/translation-review/batch-090.json"

def require(ok, message):
    if not ok:
        raise SystemExit(message)

def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def read(language):
    path = BUNDLE / ("index.md" if language == "ja" else f"index.{language}.md")
    return path, path.read_text(encoding="utf-8-sig")

def split(text):
    require(text.startswith("---\n"), "Missing front matter")
    return text[4:].split("\n---\n", 1)

source_text = read("ja")[1]
source_front, source_body = split(source_text)
require(len(re.findall(r"(?m)^date:", source_front)) == 1, "Japanese source has duplicate date keys")
require("date: 2023-04-17T00:26:55+09:00" in source_front, "Original date was changed")
require(f"lastmod: {TODAY}T00:00:00+09:00" in source_front, "Source lastmod missing")
source_hash = digest(source_text)
reviews = {}
for language in LANGS[1:]:
    path, text = read(language)
    front, body = split(text)
    require(len(re.findall(r"(?m)^date:", front)) == 1, f"{language}: duplicate date keys")
    require("date: 2023-04-17T00:26:55+09:00" in front, f"{language}: publication date changed")
    require(f"lastmod: {TODAY}T00:00:00+09:00" in front, f"{language}: lastmod missing")
    require("draft: false" in front, f"{language}: publication status changed")
    require(re.findall(r"\]\((https://html5up\.net/[^)]*)\)", body) == LINKS, f"{language}: official links differ")
    require(len(re.findall(r"(?m)^##\s", body)) == 3, f"{language}: section structure differs")
    for marker in ("HTML5", "CSS3", "CC BY 3.0"):
        require(marker in body, f"{language}: missing {marker}")
    review = {
        "reviewKind": "ai", "reviewedAt": TODAY, "reviewer": "Codex (AI)", "source": SOURCE,
        "sourceHash": source_hash, "translationHash": digest(text),
        "summary": "Compared all twelve translations with the complete Japanese article. Verified the current HTML5 UP catalog, responsive HTML5/CSS3 template description, and CC BY 3.0 permissions and attribution requirement against the official site and license page.",
        "checks": {
            "meaning": {"status": "checked", "note": "Each edition preserves the template-selection, download/customization, and license/attribution guidance."},
            "terminology": {"status": "checked", "note": "HTML5, CSS3, template, responsive design, CC BY 3.0, and attribution are represented consistently."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no mathematical claims or formulas."},
            "code": {"status": "not_applicable", "note": "The article contains no code samples."},
            "links": {"status": "checked", "note": "All editions point to the same official template catalog and license page."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "Template availability can change; readers are directed to the current official catalog.", "Separate assets or libraries may have their own licenses, which the article asks readers to check."],
    }
    reviews[f"post/{BUNDLE.name}/{path.name}"] = review

entry = {
    "version": 1, "batch": 90, "article": BUNDLE.name, "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": LINKS,
    "scope": "Read the complete Japanese source and all twelve translations. Checked section coverage, meaning, terminology, metadata, official links, and the current official HTML5 UP and license information.",
    "findings": [
        "Expanded the original one-paragraph bookmark into a practical guide covering template selection, preview, download, customization, and pre-publication review.",
        "Confirmed the official site describes its templates as responsive HTML5/CSS3 templates, and the official license page identifies CC BY 3.0, permits personal/commercial use and modifications, and requests credit for the design.",
        "Localized the complete revised article into twelve languages, preserving the same three sections and official references.",
        "Removed duplicate date metadata, retained the original 2023-04-17 publication date, and set lastmod to 2026-11-24.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-090.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
ledger["reviews"].pop(f"post/{BUNDLE.name}/index.md", None)
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = EVIDENCE
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 90, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
