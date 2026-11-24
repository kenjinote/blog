"""Record the full source/translation review for the LogicPad story (batch 091)."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/LogicPad 開発秘話"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/LogicPad 開発秘話/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
EVIDENCE = "docs/translation-review/batch-091.json"

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
require(len(re.findall(r"(?m)^date:", source_front)) == 1, "Source has duplicate date keys")
require("date: 2025-07-30T23:51:35+09:00" in source_front, "Source publication date changed")
require(f"lastmod: {TODAY}T00:00:00+09:00" in source_front, "Source lastmod missing")
source_hash = digest(source_text)
reviews = {}
for language in LANGS[1:]:
    path, text, front, body = load(language)
    require(len(re.findall(r"(?m)^date:", front)) == 1, f"{language}: duplicate date keys")
    require("date: 2025-07-30T23:51:35+09:00" in front, f"{language}: publication date changed")
    require(f"lastmod: {TODAY}T00:00:00+09:00" in front, f"{language}: lastmod missing")
    require("draft: false" in front, f"{language}: publication status changed")
    require(len(re.findall(r"(?m)^#{1,3}\s", body)) == 11, f"{language}: article section structure differs")
    require("2025" in body, f"{language}: historical timeframe note missing")
    require("https://logicpad.org" in body, f"{language}: current product reference missing")
    require("👇" in body, f"{language}: historical feature-list heading missing")
    require("kubernetes-k8s-architecture-pod-service-ingress" not in body, f"{language}: unrelated Kubernetes link remains")
    require("logicpad-windows-app-development-journey" not in body, f"{language}: incorrect Hindi internal link remains")
    if language == "es":
        require("[Pod]" not in body, "Spanish text still splits 'Podían' into a link")
    require(len(re.findall(r"\]\(https://logicpad\.org\)", body)) >= 2, f"{language}: product links missing")
    review = {
        "reviewKind": "ai", "reviewedAt": TODAY, "reviewer": "Codex (AI)", "source": SOURCE,
        "sourceHash": source_hash, "translationHash": digest(text),
        "summary": "Compared the complete personal-history article with the Japanese source. Preserved the author's first-person timeline and section sequence; corrected malformed product links and the Spanish mid-word Kubernetes link; dated the beta and feature claims to the July 2025 publication context and linked to current product information.",
        "checks": {
            "meaning": {"status": "checked", "note": "The account of the author's motivation, prior CAD and programming experience, first user feedback, goals, and feature list remains in the same sequence."},
            "terminology": {"status": "checked", "note": "LogicPad, low-code, GUI/CAD, Blueprint, beta, and product features retain their intended meaning; the feature list is explicitly historical."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no mathematical claims or formulas."},
            "code": {"status": "not_applicable", "note": "The article contains no executable code samples."},
            "links": {"status": "checked", "note": "Product references point to logicpad.org; removed an unrelated Spanish Kubernetes link and corrected erroneous Hindi links to a different LogicPad article."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "The author's personal recollections and historical feature claims are not independently audited.", "Current product status and availability are referred to the official LogicPad site."],
    }
    reviews[f"post/{BUNDLE.name}/{path.name}"] = review

entry = {
    "version": 1, "batch": 91, "article": BUNDLE.name, "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": ["https://logicpad.org/"],
    "scope": "Read the complete Japanese source and all twelve translations. Compared narrative sequence, personal timeline, product terminology and links; checked current product information against the official site.",
    "findings": [
        "Removed the duplicate future date from all thirteen editions, retained the original 2025-07-30 publication date, and set lastmod to 2026-11-24.",
        "Fixed a Spanish link inserted into the middle of 'Podían' that pointed to an unrelated Kubernetes article.",
        "Corrected repeated Hindi links that pointed to a different LogicPad article; they now point to the product site.",
        "Changed five titles that incorrectly used passive or plural wording to match the author's first-person account.",
        "Reframed beta status and the adjacent feature list as information from July 2025, and linked readers to the official site for current features and availability.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-091.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = EVIDENCE
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 91, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
