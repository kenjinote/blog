"""Verify the deployed AI-era programmer article bundle and save publication evidence."""
import json
import re
import urllib.request
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs" / "translation-review"
LANGS = ("ja", "en", "zh-cn", "zh-tw", "es", "ko", "pt", "fr", "de", "hi", "id", "ar", "ru")
ARTICLE = "AI時代のプログラマーはどう生き残るべきか"
RUN = 45049913673
COMMIT = "14e655cd6"
SOURCES = (
    "https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/",
    "https://arxiv.org/abs/2507.09089",
)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = ""
        self.direction = ""
        self.canonical = []
        self.hreflang = {}
        self.links = []
        self.text = []
        self.in_title = False
        self.title = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang", "")
            self.direction = attrs.get("dir", "")
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonical.append(attrs.get("href", ""))
        if tag == "link" and attrs.get("hreflang"):
            self.hreflang[attrs["hreflang"]] = attrs.get("href", "")
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.title.append(data)


def title_from(path):
    match = re.search(r"^title:\s*[\"']?(.*?)[\"']?\s*$", path.read_text(encoding="utf-8-sig"), re.M)
    if not match:
        raise ValueError(f"Missing title: {path}")
    return unescape(match.group(1))


preview = json.loads((DOCS / "batch-041-preview-validation.json").read_text(encoding="utf-8"))
pages = [p for p in preview["pages"] if p.get("batch") == "batch-041"]
if len(pages) != len(LANGS):
    raise SystemExit(f"Expected 13 preview URLs, got {len(pages)}")

bundle = ROOT / "content" / "post" / ARTICLE
records = []
for item in pages:
    lang = item["lang"]
    source = bundle / ("index.md" if lang == "ja" else f"index.{lang}.md")
    title = title_from(source)
    req = urllib.request.Request(item["url"], headers={"User-Agent": "kenji.blog-translation-review/1.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        html = response.read().decode("utf-8", "replace")
        page = Page()
        page.feed(html)
        text = " ".join(page.text)
        targets = set(page.hreflang.values())
        checks = {
            "http200": response.status == 200,
            "finalUrlMatches": response.geturl() == item["url"],
            "canonicalMatches": page.canonical == [item["url"]],
            "languageMatches": page.lang == lang,
            "arabicRtl": lang != "ar" or page.direction == "rtl",
            "titlePresent": title in "".join(page.title),
            "allLanguageTargetsMatch": targets == {p["url"] for p in pages},
            "hreflangCount14": len(page.hreflang) == 14,
            "primaryResearchReferences": all(any(source in link for link in page.links) for source in SOURCES),
            "recentUpdateVisible": "2026-11-23" in text,
        }
        records.append({"language": lang, "url": item["url"], "status": response.status,
                        "lastModified": response.headers.get("Last-Modified"), "checks": checks,
                        "passed": all(checks.values())})

receipt = {
    "version": 1,
    "checkedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
    "ciRun": RUN,
    "ciUrl": f"https://github.com/kenjinote/kenji.blog/actions/runs/{RUN}",
    "deployedCommit": COMMIT,
    "scope": "Batch041: Japanese AI-era programmer article and all 12 translations. Post-deploy HTTP checks validate all 13 pages, canonical, language, Arabic RTL, title, both primary research links, and the full 14-entry hreflang set.",
    "allPassed": len(records) == 13 and all(record["passed"] for record in records),
    "pages": records,
    "limitations": ["Static HTTP checks only; no browser/device rendering.", "The DORA source is survey/qualitative evidence and the METR trial is narrow in participants, tasks, and tool vintage.", "AI review only; no human/native-speaker certification."],
}
(DOCS / "publication-041.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
batch_path = DOCS / "batch-041.json"
batch = json.loads(batch_path.read_text(encoding="utf-8"))
batch["publicationPending"] = not receipt["allPassed"]
batch["publication"] = {"record": "docs/translation-review/publication-041.json", "ciRun": RUN, "deployedCommit": COMMIT, "allPassed": receipt["allPassed"]}
batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"allPassed": receipt["allPassed"], "pages": len(records), "failures": [r for r in records if not r["passed"]]}, ensure_ascii=False, indent=2))
if not receipt["allPassed"]:
    raise SystemExit(1)
