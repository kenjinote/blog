"""Build a fresh 40-article-bundle preview and verify all AG03 translations."""
from __future__ import annotations

import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs" / "translation-review"
ARTICLE = "AG03ノイズ解消方法"
LANGS = ("ja", "en", "zh-cn", "zh-tw", "es", "ko", "pt", "fr", "de", "hi", "id", "ar", "ru")
REFS = (
    "https://jp.yamaha.com/audio/streaming-gaming/products/mixers/ag/ag03/support.html",
    "https://jp.yamaha.com/support/updates/yamaha_steinberg_usb_driver_for_win.html",
    "https://jp.yamaha.com/business/audio/news/2022/defect.html",
    "https://jp.yamaha.com/audio/streaming-gaming/products/mixers/ag/ag03/specs.html",
)
TEMP = Path(os.environ["TEMP"]) / "kenji-priority-review-20261024"
CONTENT = TEMP / "content-40-bundles-ag03-r2"
SITE = TEMP / "public-40-bundles-ag03-r2"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.html_attrs = {}
        self.canonical = []
        self.hreflang = {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.html_attrs = a
        if tag == "link" and "canonical" in a.get("rel", "").split():
            self.canonical.append(a.get("href"))
        if tag == "link" and a.get("hreflang"):
            self.hreflang[a["hreflang"]] = a.get("href")


def run(args):
    p = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    return {"command": args, "exitCode": p.returncode, "stdout": p.stdout, "stderr": p.stderr}


def main():
    assert not CONTENT.exists() and not SITE.exists()
    prior = json.loads((DOCS / "batch-038-final-checks.json").read_text(encoding="utf-8"))
    prior_paths = [Path(x["path"]) for x in prior["snapshots"]]
    slugs = {p.parts[2] for p in prior_paths if p.parts[:2] == ("content", "post")}
    assert len(slugs) == 39 and ARTICLE not in slugs
    (CONTENT / "post").mkdir(parents=True)
    for slug in slugs | {ARTICLE}:
        shutil.copytree(ROOT / "content" / "post" / slug, CONTENT / "post" / slug)
    shutil.copytree(ROOT / "content" / "tags", CONTENT / "tags")
    snapshots = []
    for p in sorted(CONTENT.rglob("*.md")):
        real = ROOT / "content" / p.relative_to(CONTENT)
        assert p.read_bytes() == real.read_bytes(), f"Snapshot differs: {real}"
        snapshots.append({"path": real.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
    assert len(snapshots) == 521, len(snapshots)
    assert len(list((CONTENT / "post").glob("*/*.md"))) == 520

    build = ["hugo", "--environment", "production", "--minify", "--buildFuture", "--baseURL", "https://kenji.blog/", "--contentDir", str(CONTENT), "--destination", str(SITE)]
    build_result = run(build)
    (DOCS / "batch-039-r2-build.json").write_text(json.dumps(build_result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    assert build_result["exitCode"] == 0, build_result["stderr"]

    pages = []
    for lang in LANGS:
        name = "index.md" if lang == "ja" else f"index.{lang}.md"
        source = ROOT / "content" / "post" / ARTICLE / name
        text = source.read_text(encoding="utf-8")
        title = re.search(r'^title: "(.*)"$', text, re.M).group(1)
        slug = re.search(r'^slug: "(.*)"$', text, re.M).group(1)
        assert len(re.findall(r"^date:", text, re.M)) == 1
        assert 'lastmod: "2026-11-23"' in text
        path = SITE / ("" if lang == "ja" else lang) / "p" / slug / "index.html"
        body = path.read_text(encoding="utf-8")
        page = Page()
        page.feed(body)
        canonical = "https://kenji.blog/" + ("" if lang == "ja" else f"{lang}/") + f"p/{slug}/"
        checks = {
            "htmlExists": path.is_file(),
            "languageMatches": page.html_attrs.get("lang") == lang,
            "arabicRtl": lang != "ar" or page.html_attrs.get("dir") == "rtl",
            "canonicalMatches": len(page.canonical) == 1 and unquote(page.canonical[0]).casefold() == unquote(canonical).casefold(),
            "titlePresent": html.unescape(title) in html.unescape(body),
            "officialReferencesPresent": all(url in body for url in REFS),
            "staleMercariAdRemoved": "m10570024971" not in body,
            "archivedFaqRemoved": "web.archive.org/web/20201003230738" not in body,
            "lastmodPresent": "2026-11-23" in body,
            "hreflangCount": len(page.hreflang) == 14,
        }
        pages.append({"language": lang, "url": page.canonical[0] if page.canonical else canonical, "checks": checks, "passed": all(checks.values())})

    checks = [
        run([sys.executable, "scripts/check_multilingual.py", str(SITE)]),
        run([sys.executable, "scripts/check_https_urls.py", str(SITE)]),
        run([sys.executable, "scripts/translation_reviews.py", "check"]),
    ]
    metadata = json.loads((DOCS / "batch-039.json").read_text(encoding="utf-8"))
    assert len(metadata["reviews"]) == 12
    receipt = {
        "version": 1,
        "checkedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
        "allPassed": all(p["passed"] for p in pages) and all(c["exitCode"] == 0 for c in checks),
        "previewBundles": 40,
        "postSnapshotsExact": 520,
        "taxonomySnapshotsExact": 1,
        "snapshots": snapshots,
        "articlePages": pages,
        "siteChecks": checks,
        "priorTestsPreviouslyPassedNotRerun": 17,
        "priorTests": "docs/translation-review/batch-037-final-checks.json",
        "scope": "Fresh 40-article-bundle static production preview. Read and revised the full Japanese source and all12 translations; exact article HTML, date metadata, four official references, removed obsolete ad/archive URL, language/canonical/14 hreflang and Arabic RTL checked. Global multilingual and HTTPS checks run. No browser/device rendering, driver execution, human/native-speaker review or hardware diagnosis.",
        "publicationPending": True,
    }
    (DOCS / "batch-039-r2-validation.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"allPassed": receipt["allPassed"], "pages": len(pages), "failedPages": [p["language"] for p in pages if not p["passed"]], "checks": [{"command": c["command"][1:], "exitCode": c["exitCode"], "stdout": c["stdout"].strip()} for c in checks]}, ensure_ascii=False))
    if not receipt["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
