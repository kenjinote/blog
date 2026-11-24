"""Review the refreshed GitHub Copilot and IntelliJ guide (batch 087)."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/IntelliJ IDEAでGitHub Copilotを使う"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/IntelliJ IDEAでGitHub Copilotを使う/index.md"
EVIDENCE = "docs/translation-review/batch-087.json"
LANGS = ("ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
OFFICIAL = [
    "https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension",
    "https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions",
    "https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer",
]


def digest(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def require(ok, message):
    if not ok:
        raise SystemExit(message)


def parts(text):
    require(text.startswith("---\n"), "Missing front matter")
    return text[4:].split("\n---\n", 1)


files = {"ja": BUNDLE / "index.md"}
files.update({language: BUNDLE / f"index.{language}.md" for language in LANGS})
source_text = files["ja"].read_text(encoding="utf-8-sig")
source_front, source_body = parts(source_text)
require(len(re.findall(r"(?m)^date:", source_front)) == 1, "Source has duplicate date keys")
require("lastmod: 2026-11-24T00:00:00+09:00" in source_front, "Source lastmod missing")
require(not re.search(r"!\[[^\]]*\]\(", source_body), "Old UI screenshots remain embedded")
source_hash = digest(source_text)
reviews = {}

for language in LANGS:
    relative = f"post/IntelliJ IDEAでGitHub Copilotを使う/index.{language}.md"
    text = files[language].read_text(encoding="utf-8-sig")
    front, body = parts(text)
    require(len(re.findall(r"(?m)^date:", front)) == 1, f"{language}: duplicate date keys")
    require("date: 2022-09-10T09:44:55+09:00" in front, f"{language}: original date changed")
    require("lastmod: 2026-11-24T00:00:00+09:00" in front, f"{language}: lastmod missing")
    require("draft: false" in front, f"{language}: draft status changed")
    require(not re.search(r"!\[[^\]]*\]\(", body), f"{language}: outdated screenshots remain embedded")
    links = re.findall(r"\]\((https?://[^)]+)\)", body)
    require(links == OFFICIAL, f"{language}: official link set differs")
    require(len(re.findall(r"(?m)^##\s", body)) == 5, f"{language}: section structure differs")
    for token in ("Copy and Open", "Login to GitHub", "Authorize GitHub Copilot Plugin", "Tab", "Copilot Free"):
        require(token in body, f"{language}: missing verified flow detail {token}")
    review = {
        "reviewKind": "ai",
        "reviewedAt": TODAY,
        "reviewer": "Codex (AI)",
        "source": SOURCE,
        "sourceHash": source_hash,
        "translationHash": digest(text),
        "summary": "Compared the complete localized guide with current GitHub installation, authentication, account access, IDE compatibility, code suggestion, and JetBrains Marketplace guidance. Replaced outdated UI screenshots with version-aware text instructions.",
        "checks": {
            "meaning": {"status": "checked", "note": "Prerequisites, installation, device-code sign-in, authorization, code suggestions, and Copilot Chat are aligned across all editions with current GitHub documentation."},
            "terminology": {"status": "checked", "note": "GitHub Copilot, IntelliJ IDEA, plugin/Marketplace, device code, authorization, inline suggestions, Chat, and the English UI labels remain distinct and consistent."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no mathematical claims or formulas."},
            "code": {"status": "not_applicable", "note": "The guide contains UI steps rather than code samples; the Tab shortcut for accepting a suggestion matches GitHub documentation."},
            "links": {"status": "checked", "note": "All editions point to the current official GitHub install guide, official JetBrains code-suggestion instructions, and GitHub's JetBrains Marketplace listing."},
        },
        "limitations": [
            "AI-assisted review; no human or native-speaker certification.",
            "IDE menus and GitHub Copilot plan details can change; the guide links to current official references and advises readers to verify them.",
        ],
    }
    reviews[relative] = review

entry = {
    "version": 1,
    "batch": 87,
    "article": "IntelliJ IDEAでGitHub Copilotを使う",
    "reviewedAt": TODAY,
    "sourceHash": source_hash,
    "sources": OFFICIAL,
    "scope": "Read the full Japanese article and all twelve translations. Checked current GitHub account access, supported IDEs, Marketplace installation, device-code authorization flow, inline suggestions, acceptance shortcut, Copilot Chat entry, metadata, and language parity.",
    "findings": [
        "Replaced the old bottom-right icon authentication path with the current Tools > GitHub Copilot > Login to GitHub flow, followed by Copy and Open, device-code authorization, and the IDE confirmation.",
        "Added Copilot access prerequisites and a note that plan limits, IDE compatibility, and UI labels can change.",
        "Updated code suggestion guidance to say Tab accepts the inline suggestion and readers should review it before use.",
        "Removed the old version-specific UI screenshots and their alt text from the article body so they no longer conflict with current UI instructions.",
        "Removed duplicate date fields from all editions, retained the 2022-09-10 publication date, and set lastmod to 2026-11-24.",
    ],
    "publicationPending": True,
    "reviews": reviews,
}
(DOCS / "batch-087.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = EVIDENCE
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 87, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
