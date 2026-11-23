"""Verify the Go installation article after the Pages workflow deploys it."""
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as ET
import argparse
import json
import re
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
CONTENT = ROOT / "content/post/Goをインストールする方法"
LANGS = ["ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id"]
OFFICIAL = [
    "https://go.dev/doc/install",
    "https://go.dev/doc/tutorial/getting-started",
    "https://go.dev/doc/manage-install",
    "https://go.dev/doc/faq",
    "https://go.dev/play/",
]
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}


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
    source = path.read_text(encoding="utf-8-sig")
    match = re.search(rf"^{key}:\s*(.*?)\s*$", source, re.M)
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

with urllib.request.urlopen(f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}?review_check=1", timeout=45) as response:
    run_html = response.read().decode("utf-8", "replace")
if '<span class="h4 color-fg-default">Success</span>' not in run_html or args.commit[:7] not in run_html:
    raise SystemExit("GitHub run page does not confirm success for the specified commit")

with urllib.request.urlopen("https://kenji.blog/sitemap.xml", timeout=45) as response:
    sitemap = ET.fromstring(response.read())
ja_map = next((e.find("s:loc", NS).text for e in sitemap.findall("s:sitemap", NS) if "/ja/sitemap.xml" in e.find("s:loc", NS).text), None)
if not ja_map:
    raise SystemExit("Japanese sitemap is missing")
with urllib.request.urlopen(ja_map, timeout=45) as response:
    ja_sitemap = ET.fromstring(response.read())
urls = [e.find("s:loc", NS).text for e in ja_sitemap.findall("s:url", NS)]
slug = re.sub(r"\s+", "-", re.sub(r"[()（）]", "", yaml_value(CONTENT / "index.md", "slug"))).casefold()
ja_url = next((url for url in urls if f"/p/{slug}/" in unquote(url).casefold()), None)
if not ja_url:
    raise SystemExit("Japanese sitemap is missing the article")
_, raw = fetch(ja_url)
root = Page(); root.feed(raw.decode("utf-8", "replace"))
targets = set(root.hreflang.values())
if len(targets) != 13 or len(root.hreflang) != 14:
    raise SystemExit("Unexpected hreflang targets")

results = []
for lang in LANGS:
    url = next((u for u in targets if (lang == "ja" and re.search(r"https://kenji\.blog/p/", u)) or (lang != "ja" and f"/{lang}/p/" in u)), None)
    if not url:
        results.append({"language": lang, "passed": False, "failure": "hreflang target missing"})
        continue
    status, raw = fetch(url)
    page = Page(); page.feed(raw.decode("utf-8", "replace"))
    md = CONTENT / ("index.md" if lang == "ja" else f"index.{lang}.md")
    title = yaml_value(md, "title")
    description = yaml_value(md, "description")
    text = re.sub(r"\s+", " ", " ".join(page.text))
    compact_text = re.sub(r"\s+", "", "".join(page.text))
    links = set(page.links)
    checks = {
        "http200": status == 200,
        "canonical": page.canonical == [url],
        "language": page.lang.lower() == lang,
        "arabicRtl": lang != "ar" or page.direction == "rtl",
        "title": title in "".join(page.titles),
        "description": len(page.descriptions) == 1 and page.descriptions[0].strip() == description,
        "hreflangCount": len(page.hreflang) == 14,
        "hreflangTargets": set(page.hreflang.values()) == targets,
        "officialGoReferences": all(link in links for link in OFFICIAL),
        "moduleAndRunCommands": "gomodinitexample/hello" in compact_text and "gorun." in compact_text and "goversion" in compact_text,
        "helloWorldCodeAndOutput": bool(re.search(r'fmt\.Println\("Hello,World!"\)', compact_text)) and "Hello, World!" in text,
        "obsoleteJapaneseDocsRemoved": "go.shibu.jp" not in raw.decode("utf-8", "replace"),
    }
    results.append({"language": lang, "url": url, "status": status, "checks": checks, "passed": all(checks.values())})

passed = len(results) == 13 and all(row["passed"] for row in results)
receipt = {
    "version": 1,
    "batch": 80,
    "verifiedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
    "ciRun": args.ci_run,
    "ciUrl": f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}",
    "sourceCommit": args.commit,
    "deployment": "success" if passed else "verification_failed",
    "pagesVerified": sum(row["passed"] for row in results),
    "allPassed": passed,
    "checks": ["HTTP 200, canonical, language/RTL, title/description, reciprocal 14-label hreflang on all 13 editions", "official Go installation, getting-started, version management, FAQ, and Playground links", "module initialization, run/build instructions, Hello World code/output, and removal of the obsolete Japanese documentation link"],
    "pages": results,
    "limitations": ["AI translation review only; no human or native-speaker certification.", "The Go toolchain was not installed in the review environment, so the sample was checked against the official tutorial but not run locally."],
}
(DOCS / "publication-080.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if passed:
    path = DOCS / "batch-080.json"
    batch = json.loads(path.read_text(encoding="utf-8"))
    batch["publicationPending"] = False
    batch["publication"] = {"record": "docs/translation-review/publication-080.json", "ciRun": args.ci_run, "sourceCommit": args.commit, "allPassed": True}
    path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"allPassed": passed, "pages": len(results), "failures": [row for row in results if not row["passed"]]}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
