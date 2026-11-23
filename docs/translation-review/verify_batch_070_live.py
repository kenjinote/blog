"""Verify the calendar template editions and workbook after GitHub Pages deploy."""
from __future__ import annotations

from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin
from xml.etree import ElementTree as ET
import argparse
import json
import re
import time
import urllib.error
import urllib.request
import zipfile
from io import BytesIO

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
CONTENT = ROOT / "content/post/Excelのカレンダーテンプレート（休日対応版）"
LANGS = ["ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id"]
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9", "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = self.direction = ""
        self.canonical = []
        self.hreflang = {}
        self.links = []
        self.descriptions = []
        self.titles = []
        self.in_title = False
        self.text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang, self.direction = attrs.get("lang", ""), attrs.get("dir", "")
        elif tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonical.append(attrs.get("href", ""))
        elif tag == "link" and attrs.get("hreflang"):
            self.hreflang[attrs["hreflang"]] = attrs.get("href", "")
        elif tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        elif tag == "meta" and attrs.get("name", "").lower() == "description":
            self.descriptions.append(attrs.get("content", ""))
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.titles.append(data)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "kenji.blog-translation-review/1.0", "Cache-Control": "no-cache"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                return response.status, response.read()
        except urllib.error.HTTPError as error:
            if error.code != 503 or attempt == 3:
                raise
            time.sleep(2 ** attempt)


def yaml_value(path: Path, key: str) -> str:
    text = path.read_text(encoding="utf-8-sig")
    match = re.search(rf"^{key}:\s*(.*?)\s*$", text, re.M)
    if not match:
        raise SystemExit(f"Missing {key} in {path}")
    value = match.group(1)
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


parser = argparse.ArgumentParser()
parser.add_argument("--ci-run", required=True, type=int)
parser.add_argument("--commit", required=True)
args = parser.parse_args()
api = urllib.request.Request(
    f"https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}?nocache={int(datetime.now().timestamp())}",
    headers={"User-Agent": "kenji.blog-translation-review/1.0", "Accept": "application/vnd.github+json", "Cache-Control": "no-cache"},
)
try:
    with urllib.request.urlopen(api, timeout=30) as response:
        run = json.load(response)
    if run.get("conclusion") != "success" or not run.get("head_sha", "").startswith(args.commit):
        raise SystemExit("CI run is not successful for the specified commit")
except urllib.error.HTTPError as error:
    if error.code != 403:
        raise
    req = urllib.request.Request(f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}?review_check=1", headers={"User-Agent": "Mozilla/5.0 kenji.blog-translation-review/1.0"})
    with urllib.request.urlopen(req, timeout=45) as response:
        body = response.read().decode("utf-8", "replace")
    if '<span class="h4 color-fg-default">Success</span>' not in body or args.commit[:7] not in body:
        raise SystemExit("GitHub run page does not confirm success for the specified commit")

with urllib.request.urlopen("https://kenji.blog/sitemap.xml", timeout=45) as response:
    sitemap = ET.fromstring(response.read())
ja_map = next((e.find("s:loc", NS).text for e in sitemap.findall("s:sitemap", NS) if "/ja/sitemap.xml" in e.find("s:loc", NS).text), None)
if not ja_map:
    raise SystemExit("Japanese sitemap is missing")
with urllib.request.urlopen(ja_map, timeout=45) as response:
    ja_sitemap = ET.fromstring(response.read())
all_urls = [e.find("s:loc", NS).text for e in ja_sitemap.findall("s:url", NS)]
ja_slug = yaml_value(CONTENT / "index.md", "slug")
ja_url = next((u for u in all_urls if f"/p/{ja_slug}/" in unquote(u)), None)
if not ja_url:
    raise SystemExit("Japanese sitemap is missing the article")
_, root_raw = fetch(ja_url)
root_page = Page(); root_page.feed(root_raw.decode("utf-8", "replace"))
targets = set(root_page.hreflang.values())
if len(targets) != 13 or len(root_page.hreflang) != 14:
    raise SystemExit("Unexpected hreflang targets for the article")
records = []
for lang in LANGS:
    article_url = next((u for u in targets if (lang == "ja" and re.search(r"https://kenji\.blog/p/", u)) or (lang != "ja" and f"/{lang}/p/" in u)), None)
    if not article_url:
        records.append({"language": lang, "passed": False, "failure": "hreflang target missing"})
        continue
    md = CONTENT / ("index.md" if lang == "ja" else f"index.{lang}.md")
    status, raw = fetch(article_url)
    html = raw.decode("utf-8", "replace")
    page = Page(); page.feed(html)
    mdtext = md.read_text(encoding="utf-8-sig")
    title = yaml_value(md, "title")
    description = yaml_value(md, "description")
    all_langs = set(LANGS) | {"x-default"}
    download = next((urljoin(article_url, href) for href in page.links if unquote(href).endswith("カレンダー.xlsx")), None)
    checks = {
        "http200": status == 200,
        "canonical": page.canonical == [article_url],
        "language": page.lang.lower() == lang,
        "arabicRtl": lang != "ar" or page.direction == "rtl",
        "title": title in "".join(page.titles),
        "description": bool(page.descriptions) and page.descriptions[0] == description,
        "allHreflangTargets": len(page.hreflang) == 14 and set(page.hreflang.values()) == targets,
        "compatibilityNote": "ExcelAPI" in "".join(page.text) and "Mac" in "".join(page.text),
        "microsoftReference": any("support.microsoft.com" in href for href in page.links),
        "holidayApiReference": any("excelapi.org" in href for href in page.links),
        "downloadLink": download is not None,
    }
    if download:
        xstatus, xbytes = fetch(download)
        try:
            with zipfile.ZipFile(BytesIO(xbytes)) as book:
                sheet = book.read("xl/worksheets/sheet2.xml")
                refs_ok = b"http://api.excelapi.org" not in sheet and b"https://api.excelapi.org" in sheet
        except Exception:
            refs_ok = False
        checks["workbookHttp200"] = xstatus == 200
        checks["publicWorkbookUsesHttps"] = refs_ok
    else:
        checks["workbookHttp200"] = False
        checks["publicWorkbookUsesHttps"] = False
    records.append({"language": lang, "url": article_url, "status": status, "checks": checks, "passed": all(checks.values())})

passed = len(records) == len(LANGS) and all(r["passed"] for r in records)
receipt = {
    "version": 1,
    "batch": 70,
    "verifiedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
    "ciRun": args.ci_run,
    "deployedCommit": args.commit,
    "allPassed": passed,
    "scope": "Thirteen public article pages and their language switch metadata, compatibility/source links, downloadable XLSX response, and embedded API scheme.",
    "pages": records,
    "limitations": ["AI translation review only; no human or native-speaker certification.", "Public workbook formulas were inspected; no live Excel recalculation was performed."],
}
(DOCS / "publication-070.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if passed:
    path = DOCS / "batch-070.json"
    batch = json.loads(path.read_text(encoding="utf-8"))
    batch["publicationPending"] = False
    batch["publication"] = {"record": "docs/translation-review/publication-070.json", "ciRun": args.ci_run, "deployedCommit": args.commit, "allPassed": True}
    path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"allPassed": passed, "pages": len(records), "failures": [r for r in records if not r["passed"]]}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
