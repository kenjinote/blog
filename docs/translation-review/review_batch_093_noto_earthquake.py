"""Record the Noto earthquake article's source and translation review."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/日本の災害"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/日本の災害/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
JMA = "https://www.jma.go.jp/jma/menu/20240101_noto_jishin.html"
FDMA = "https://www.fdma.go.jp/disaster/info/items/b055402cefac7721623c30034b25489118dbec38.pdf"
LINKS = [JMA, FDMA]
EVIDENCE = "docs/translation-review/batch-093.json"

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
require("date: 2024-01-07T00:50:09+09:00" in source_front, "Source publication date changed")
require(f"lastmod: {TODAY}T00:00:00+09:00" in source_front, "Source lastmod missing")
source_hash = digest(source_text)
reviews = {}
for language in LANGS[1:]:
    path, text, front, body = load(language)
    require(len(re.findall(r"(?m)^date:", front)) == 1, f"{language}: duplicate dates")
    require("date: 2024-01-07T00:50:09+09:00" in front, f"{language}: publication date changed")
    require(f"lastmod: {TODAY}T00:00:00+09:00" in front, f"{language}: lastmod missing")
    require("draft: false" in front, f"{language}: publication state changed")
    require(len(re.findall(r"(?m)^##\s", body)) == 2, f"{language}: section structure differs")
    body_links = re.findall(r"\]\((https://[^)]+)\)", body)
    require(all(link in body_links for link in LINKS), f"{language}: official references missing")
    for marker in ("2024", "720", "492"):
        require(marker in body, f"{language}: missing verified data marker {marker}")
    magnitude = "7,6" if language in ("de", "es", "fr", "id", "pt", "ru") else "7.6"
    require(magnitude in body, f"{language}: magnitude formatting is missing")
    require(re.search(r"165[,. ]?813", body) is not None, f"{language}: housing-damage figure is missing")
    require("img.webp" in body, f"{language}: earthquake photo missing")
    review = {
        "reviewKind": "ai", "reviewedAt": TODAY, "reviewer": "Codex (AI)", "source": SOURCE,
        "sourceHash": source_hash, "translationHash": digest(text),
        "summary": "Compared the complete translation with the Japanese source and verified the earthquake time, magnitude, maximum intensity, report date, casualty and housing-damage snapshot against JMA and Fire and Disaster Management Agency primary sources.",
        "checks": {
            "meaning": {"status": "checked", "note": "Every edition separates the earthquake overview from the explicitly dated preliminary damage snapshot."},
            "terminology": {"status": "checked", "note": "Magnitude, Japan's seismic intensity scale, disaster-related deaths, missing persons, and residential-building damage are distinguished."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no mathematical formulas."},
            "code": {"status": "not_applicable", "note": "The article contains no code samples."},
            "links": {"status": "checked", "note": "Every edition links directly to the Japan Meteorological Agency and the dated FDMA situation report."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "FDMA report 123 is explicitly marked preliminary; its figures may change.", "The photograph is contextual and is not presented as a statistical or location-specific record."],
    }
    reviews[f"post/{BUNDLE.name}/{path.name}"] = review

entry = {
    "version": 1, "batch": 93, "article": BUNDLE.name, "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": LINKS,
    "scope": "Read the complete Japanese source and all twelve translations. Verified the event's time, magnitude, maximum intensity, and dated casualty/housing snapshot against the JMA and FDMA primary sources.",
    "findings": [
        "Replaced a title-only placeholder with a concise event overview, a dated damage snapshot, and direct primary-source references in all thirteen editions.",
        "Confirmed the JMA event data: January 1, 2024 at 16:10 JST, magnitude 7.6, maximum intensity 7.",
        "Recorded the FDMA report 123 snapshot as of March 31, 2026: 720 deaths including 492 disaster-related deaths, 2 missing persons, and 165,813 residential buildings damaged; retained the source's preliminary-data caveat.",
        "Improved the image alternative text, removed duplicate future date metadata, retained the original 2024-01-07 publication date, and set lastmod to 2026-11-24.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-093.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = EVIDENCE
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 93, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
