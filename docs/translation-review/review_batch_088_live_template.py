"""Review the IntelliJ IDEA timestamp live-template guide (batch 088)."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/IntelliJ IDEAで日付を貼り付けるコマンドを追加する/index.md"
EVIDENCE = "docs/translation-review/batch-088.json"
LANGS = ("ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
OFFICIAL = [
    "https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html",
    "https://www.jetbrains.com/help/idea/template-variables.html",
    "https://www.jetbrains.com/help/idea/settings-live-templates.html",
]


def digest(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def require(ok, message):
    if not ok:
        raise SystemExit(message)


def split(text):
    require(text.startswith("---\n"), "Missing front matter")
    return text[4:].split("\n---\n", 1)


files = {"ja": BUNDLE / "index.md"}
files.update({language: BUNDLE / f"index.{language}.md" for language in LANGS})
source_text = files["ja"].read_text(encoding="utf-8-sig")
source_front, source_body = split(source_text)
require(len(re.findall(r"(?m)^date:", source_front)) == 1, "Source has duplicate date keys")
require("lastmod: 2026-11-24T00:00:00+09:00" in source_front, "Source lastmod missing")
source_hash = digest(source_text)
reviews = {}

for language in LANGS:
    relative = f"post/IntelliJ IDEAで日付を貼り付けるコマンドを追加する/index.{language}.md"
    text = files[language].read_text(encoding="utf-8-sig")
    front, body = split(text)
    require(len(re.findall(r"(?m)^date:", front)) == 1, f"{language}: duplicate date keys")
    require("date: 2022-09-04T05:59:04+09:00" in front, f"{language}: original date changed")
    require("lastmod: 2026-11-24T00:00:00+09:00" in front, f"{language}: lastmod missing")
    require("draft: false" in front, f"{language}: publication status changed")
    require(not re.search(r"!\[[^\]]*\]\(", body), f"{language}: old screenshots remain embedded")
    links = re.findall(r"\]\((https://www\.jetbrains\.com/[^)]+)\)", body)
    require(links == OFFICIAL, f"{language}: official references differ")
    require(len(re.findall(r"(?m)^##\s", body)) == 3, f"{language}: section structure differs")
    for marker in ('date("yyyy-MM-dd\'T\'HH:mm:ssXXX")', "Skip if defined", "Tab", "+09:00", "XXX"):
        require(marker in body, f"{language}: missing verified date-template detail {marker}")
    review = {
        "reviewKind": "ai",
        "reviewedAt": TODAY,
        "reviewer": "Codex (AI)",
        "source": SOURCE,
        "sourceHash": source_hash,
        "translationHash": digest(text),
        "summary": "Compared the full localized guide with current JetBrains documentation for creating live templates, variables, date formatting, and expansion keys. Corrected the UI path and default Tab key and replaced the fixed Japan offset with a local ISO 8601 offset.",
        "checks": {
            "meaning": {"status": "checked", "note": "All language editions explain the same IntelliJ settings path, abbreviation, template variable expression, use context, Tab expansion, local timestamp, and timezone behavior."},
            "terminology": {"status": "checked", "note": "Live Template, variable, expression, abbreviation, expansion key, and ISO 8601 time-zone offset remain distinct in each language."},
            "mathematics": {"status": "not_applicable", "note": "No mathematical claims or calculations are present."},
            "code": {"status": "checked", "note": "The exact date expression `date(\"yyyy-MM-dd'T'HH:mm:ssXXX\")` is present in every edition and follows JetBrains' SimpleDateFormat-based date function."},
            "links": {"status": "checked", "note": "All editions use the same three current JetBrains official pages for creating templates, variables, and expansion settings."},
        },
        "limitations": [
            "AI-assisted review; no human or native-speaker certification.",
            "Settings labels can vary by IDE version and operating system; the article links directly to current JetBrains documentation.",
        ],
    }
    reviews[relative] = review

entry = {
    "version": 1,
    "batch": 88,
    "article": "IntelliJ IDEAで日付を貼り付けるコマンドを追加する",
    "reviewedAt": TODAY,
    "sourceHash": source_hash,
    "sources": OFFICIAL,
    "scope": "Read the entire Japanese article and all twelve translations. Verified the current Live Templates settings path, date expression format, time-zone behavior, Skip if defined, context selection, default Tab expansion key, metadata and official references.",
    "findings": [
        "Updated the settings path to Editor > Live Templates and the group/add-template flow to match current JetBrains guidance.",
        "Corrected the expansion key from Enter to the default Tab key and documented that users can configure a different key.",
        "Replaced the fixed +09:00 suffix with SimpleDateFormat's XXX time-zone offset so generated timestamps use the computer's local zone.",
        "Removed outdated UI screenshots and replaced the old Stack Overflow citation with three direct JetBrains references.",
        "Removed duplicate date metadata in all editions, retained the original 2022-09-04 publication date, and set lastmod to 2026-11-24.",
    ],
    "publicationPending": True,
    "reviews": reviews,
}
(DOCS / "batch-088.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = EVIDENCE
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 88, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
