"""Verify Batch 068 after CI deployment and record its public-page receipt."""
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree
import argparse
import json
import re
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
CONTENT = ROOT / "content/post/Edge-AIの未来とIoTデバイスへの実装アプローチ"
LANGS = ["ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id"]
SLUG = "edge-ai-future-iot-implementation"
OFFICIAL_LINKS = {
    "https://www.raspberrypi.com/documentation/accessories/ai-hat-plus.html",
    "https://coral.ai/docs/",
    "https://onnxruntime.ai/docs/reference/high-level-design.html",
    "https://www.nist.gov/blogs/cybersecurity-insights/privacy-attacks-federated-learning",
    "https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd",
    "https://www.tensorflow.org/model_optimization/guide",
}
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
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                raw = response.read().decode("utf-8", "replace")
                page = Page()
                page.feed(raw)
                return response.status, raw, page
        except urllib.error.HTTPError as error:
            if error.code != 503 or attempt == 2:
                raise
            time.sleep(2 ** attempt)


def metadata(lang):
    path = CONTENT / ("index.md" if lang == "ja" else f"index.{lang}.md")
    text = path.read_text(encoding="utf-8")
    values = {}
    for field in ("title", "slug", "description"):
        match = re.search(rf"^{field}:\s*(.*?)\s*$", text, re.M)
        if not match:
            raise SystemExit(f"Missing {field} in {path}")
        value = match.group(1)
        values[field] = json.loads(value) if value.startswith('"') else value
    return values


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
    sitemap = ElementTree.fromstring(response.read())
ja_map = next((e.find("s:loc", NS).text for e in sitemap.findall("s:sitemap", NS) if "/ja/sitemap.xml" in e.find("s:loc", NS).text), None)
if not ja_map:
    raise SystemExit("Japanese sitemap is missing")
with urllib.request.urlopen(ja_map, timeout=45) as response:
    ja_sitemap = ElementTree.fromstring(response.read())
urls = [e.find("s:loc", NS).text for e in ja_sitemap.findall("s:url", NS)]
root_url = next((url for url in urls if f"/p/{SLUG}/" in unquote(url)), None)
if not root_url:
    raise SystemExit("Japanese sitemap is missing the article")
_, _, root_page = fetch(root_url)
targets = set(root_page.hreflang.values())
if len(targets) != 13 or len(root_page.hreflang) != 14:
    raise SystemExit("Unexpected hreflang target count")

results = []
for lang in LANGS:
    url = next((u for u in targets if (lang == "ja" and re.search(r"https://kenji\.blog/p/", u)) or (lang != "ja" and f"/{lang}/p/" in u)), None)
    if not url:
        raise SystemExit(f"Missing {lang} hreflang page")
    status, raw, page = fetch(url)
    meta = metadata(lang)
    resolved = set(page.links)
    checks = {
        "http200": status == 200,
        "canonical": page.canonical == [url],
        "language": page.lang == lang,
        "arabicRtl": lang != "ar" or page.direction == "rtl",
        "title": meta["title"] in "".join(page.titles),
        "description": len(page.descriptions) == 1 and page.descriptions[0].strip() == meta["description"],
        "sourceLinks": OFFICIAL_LINKS.issubset(resolved),
        "hreflangCount": len(page.hreflang) == 14,
        "hreflangTargets": set(page.hreflang.values()) == targets,
        "articleText": SLUG in raw and "FedAvg" in " ".join(page.text) and "ONNX Runtime" in " ".join(page.text),
    }
    results.append({"language": lang, "url": url, "status": status, "checks": checks, "passed": all(checks.values())})

passed = len(results) == 13 and all(row["passed"] for row in results)
receipt = {
    "version": 1,
    "checkedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
    "ciRun": args.ci_run,
    "ciUrl": f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}",
    "deployedCommit": args.commit,
    "allPassed": passed,
    "scope": "Batch 068 Japanese source and twelve translations; thirteen live pages checked for HTTP status, canonical, language/RTL, title, description, six primary-source links, reciprocal hreflang, and Edge AI/federated-learning article text.",
    "pages": results,
    "limitations": ["AI translation review only; no human or native-speaker certification.", "No device model inference or performance benchmark was performed.", "Mermaid structure was checked in source but the diagram was not visually inspected."],
}
(DOCS / "publication-068.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if passed:
    path = DOCS / "batch-068.json"
    batch = json.loads(path.read_text(encoding="utf-8"))
    batch["publicationPending"] = False
    batch["publication"] = {"record": "docs/translation-review/publication-068.json", "ciRun": args.ci_run, "deployedCommit": args.commit, "allPassed": True}
    path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"allPassed": passed, "pages": len(results), "failures": [row for row in results if not row["passed"]]}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
