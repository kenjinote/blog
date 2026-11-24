"""Review Windows icon-handle ownership guidance (batch 089)."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/LoadIconはDestroyIconを呼び出す必要はない"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/LoadIconはDestroyIconを呼び出す必要はない/index.md"
EVIDENCE = "docs/translation-review/batch-089.json"
LANGS = ("ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
OFFICIAL = [
    "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon",
    "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw",
    "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew",
    "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon",
    "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage",
    "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource",
    "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex",
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
    relative = f"post/LoadIconはDestroyIconを呼び出す必要はない/index.{language}.md"
    text = files[language].read_text(encoding="utf-8-sig")
    front, body = split(text)
    require(len(re.findall(r"(?m)^date:", front)) == 1, f"{language}: duplicate date keys")
    require("date: 2024-04-19T01:55:17+09:00" in front, f"{language}: original date changed")
    require("lastmod: 2026-11-24T00:00:00+09:00" in front, f"{language}: lastmod missing")
    require("draft: false" in front, f"{language}: publication status changed")
    links = re.findall(r"\]\((https://learn\.microsoft\.com/[^)]+)\)", body)
    require(links == OFFICIAL, f"{language}: Microsoft reference set differs")
    require(len(re.findall(r"(?m)^##\s", body)) == 4, f"{language}: section structure differs")
    for marker in ("LoadIcon", "LoadImage", "LR_SHARED", "LR_COPYRETURNORG", "CopyIcon", "CreateIconFromResourceEx", "DestroyIcon"):
        require(marker in body, f"{language}: missing API detail {marker}")
    review = {
        "reviewKind": "ai",
        "reviewedAt": TODAY,
        "reviewer": "Codex (AI)",
        "source": SOURCE,
        "sourceHash": source_hash,
        "translationHash": digest(text),
        "summary": "Compared all localized guidance with current Microsoft Learn pages for DestroyIcon, LoadIcon, LoadImage, CopyIcon, CopyImage, and CreateIconFromResource APIs. Clarified shared versus caller-owned icon handles and explicitly noted conflicting ownership instructions in the CreateIconFromResource documentation.",
        "checks": {
            "meaning": {"status": "checked", "note": "All editions distinguish shared LoadIcon/LR_SHARED handles from caller-owned icons and preserve the same caveat about contradictory CreateIconFromResource documentation."},
            "terminology": {"status": "checked", "note": "Icon handle ownership, shared resources, caller-owned resources, DestroyIcon, LR_SHARED, and LR_COPYRETURNORG remain distinct across translations."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no mathematical claims or formulas."},
            "code": {"status": "not_applicable", "note": "The article contains API names and flags but no executable code sample."},
            "links": {"status": "checked", "note": "All seven Microsoft Learn references match across editions and support the ownership statements, including the documented inconsistency."},
        },
        "limitations": [
            "AI-assisted review; no human or native-speaker certification.",
            "Microsoft Learn pages conflict on CreateIconFromResource and CreateIconFromResourceEx ownership guidance; the article flags this and does not assert a universal rule for those APIs.",
        ],
    }
    reviews[relative] = review

entry = {
    "version": 1,
    "batch": 89,
    "article": "LoadIconはDestroyIconを呼び出す必要はない",
    "reviewedAt": TODAY,
    "sourceHash": source_hash,
    "sources": OFFICIAL,
    "scope": "Read the complete Japanese source and all twelve translations. Compared ownership and cleanup guidance for LoadIcon, LoadImage with and without LR_SHARED, CopyImage with LR_COPYRETURNORG, CopyIcon, CreateIconIndirect, and CreateIconFromResource APIs with Microsoft Learn.",
    "findings": [
        "Clarified that LoadIcon handles are shared and must not be passed to DestroyIcon; added the corresponding LoadImage LR_SHARED rule and the caller-owned LR_SHARED-absent rule.",
        "Added CopyImage LR_COPYRETURNORG and CopyIcon ownership details from their function-specific documentation.",
        "Found contradictory Microsoft documentation: the DestroyIcon overview lists CreateIconFromResource among shared-icon sources, while the individual CreateIconFromResource page says to call DestroyIcon; the Ex page also conflicts with LR_SHARED semantics. The article explicitly flags this rather than giving a false universal rule.",
        "Replaced the single DestroyIcon citation with seven direct Microsoft Learn references in all editions.",
        "Removed duplicate date metadata in all editions, retained the 2024-04-19 publication date, and set lastmod to 2026-11-24.",
    ],
    "publicationPending": True,
    "reviews": reviews,
}
(DOCS / "batch-089.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = EVIDENCE
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 89, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
