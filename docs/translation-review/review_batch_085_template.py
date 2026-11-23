"""Review the template draft and all translations (batch 085)."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content/post/000_テンプレート"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/000_テンプレート/index.md"
EVIDENCE = "docs/translation-review/batch-085.json"
LANGS = ("ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")


def digest(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def split_frontmatter(text):
    require(text.startswith("---\n"), "Missing YAML front matter")
    frontmatter, body = text[4:].split("\n---\n", 1)
    return frontmatter, body


def shape(body):
    return {
        "headings": len(re.findall(r"(?m)^#{1,6}\s", body)),
        "fences": re.findall(r"(?m)^```([^\n]*)$", body),
        "ordered": len(re.findall(r"(?m)^\d+\.\s", body)),
        "unordered": len(re.findall(r"(?m)^-\s", body)),
        "quotes": len(re.findall(r"(?m)^>\s", body)),
        "tables": len(re.findall(r"(?m)^\|", body)),
        "links": re.findall(r"\]\((https?://[^)]+)\)", body),
        "emphasis": re.findall(r"(?m)^(\*\*|\*|~~).+?\1$", body),
        "horizontalRules": len(re.findall(r"(?m)^---$", body)),
    }


source_text = (CONTENT / "index.md").read_text(encoding="utf-8-sig")
source_front, source_body = split_frontmatter(source_text)
require(len(re.findall(r"(?m)^date:", source_front)) == 1, "Japanese draft must have exactly one date")
require("lastmod: 2026-11-24T00:00:00+09:00" in source_front, "Japanese lastmod missing")
require("# ブログタイトル" in source_body and "# プログタイトル" not in source_body, "Japanese title typo remains")
source_shape = shape(source_body)
source_hash = digest(source_text)
reviews = {}

for language in LANGS:
    relative = f"post/000_テンプレート/index.{language}.md"
    text = (ROOT / "content" / relative).read_text(encoding="utf-8-sig")
    front, body = split_frontmatter(text)
    require(len(re.findall(r"(?m)^date:", front)) == 1, f"{language}: duplicate date remains")
    require("date: 2022-01-01T00:00:00+09:00" in front, f"{language}: original draft date changed")
    require("lastmod: 2026-11-24T00:00:00+09:00" in front, f"{language}: lastmod missing")
    require(shape(body) == source_shape, f"{language}: Markdown structure or links differ")
    require("draft: true" in front, f"{language}: draft status changed")
    review = {
        "reviewKind": "ai",
        "reviewedAt": TODAY,
        "reviewer": "Codex (AI)",
        "source": SOURCE,
        "sourceHash": source_hash,
        "translationHash": digest(text),
        "summary": "Compared this complete localized template draft with Japanese: metadata, Markdown syntax examples, placeholders, links, and SEO-related description. Corrected the Japanese heading typo and removed the duplicate date field from all editions.",
        "checks": {
            "meaning": {"status": "checked", "note": "The title and localized descriptions identify this as a reusable article-writing template; examples and placeholders align with the Japanese draft."},
            "terminology": {"status": "checked", "note": "Localized labels for headings, lists, code blocks, links, quotations, and SEO describe the same template elements."},
            "mathematics": {"status": "not_applicable", "note": "The template contains no mathematical claims or formulas."},
            "code": {"status": "checked", "note": "The shell-fenced PowerShell placeholder is present in every edition; it is intentionally illustrative and is not an executable article example."},
            "links": {"status": "checked", "note": "The Google link and two YouTube URLs match the Japanese template in all translations."},
        },
        "limitations": [
            "AI-assisted review; no human or native-speaker certification.",
            "This article is marked draft:true and is excluded from production publication.",
        ],
    }
    reviews[relative] = review

entry = {
    "version": 1,
    "batch": 85,
    "article": "000_テンプレート",
    "reviewedAt": TODAY,
    "sourceHash": source_hash,
    "sources": [],
    "scope": "Read the complete Japanese draft and all twelve complete translations. Compared metadata, title and description meaning, localized labels, Markdown formatting, placeholder code fence, external links, and draft status.",
    "findings": [
        "The Japanese H1 contained a typo (プログタイトル); corrected it to ブログタイトル.",
        "All thirteen editions contained duplicate date keys with conflicting values. Removed the accidental 2026-09-24 duplicate and retained the original 2022-01-01 date; recorded the review date in lastmod.",
        "All translations preserve the same heading, lists, emphasis, table, links, quotation, horizontal rule, and two video URLs.",
        "The fenced PowerShell block contains only a comment placeholder, so it is not presented as executable guidance.",
        "This remains a draft and is not published by the production site.",
    ],
    "publicationPending": False,
    "publicationStatus": "draft excluded from production",
    "reviews": reviews,
}
(DOCS / "batch-085.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = EVIDENCE
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 85, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
