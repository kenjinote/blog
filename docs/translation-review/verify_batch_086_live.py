"""Verify the current Hugo command guide after GitHub Pages deployment."""
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as ET
import argparse
import json
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
CONTENT = ROOT / "content/post/Hugoコマンド一覧"
LANGS = ("ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id")
OFFICIAL = (
    "https://gohugo.io/commands/hugo_new_project/",
    "https://gohugo.io/commands/hugo_new_content/",
    "https://gohugo.io/commands/hugo_deploy/",
    "https://gohugo.io/commands/hugo_list_all/",
    "https://gohugo.io/installation/macos/",
)
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = self.direction = ""
        self.canonical = []
        self.hreflang = {}
        self.links = []
        self.text = []
        self.title = []
        self.description = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "html":
            self.lang, self.direction = values.get("lang", ""), values.get("dir", "")
        elif tag == "link" and "canonical" in values.get("rel", "").split():
            self.canonical.append(values.get("href", ""))
        elif tag == "link" and values.get("hreflang"):
            self.hreflang[values["hreflang"]] = values.get("href", "")
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"])
        elif tag == "meta" and values.get("name", "").lower() == "description":
            self.description.append(values.get("content", ""))
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.title.append(data)


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "kenji.blog-translation-review/1.0", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.status, response.read()


def yaml_value(path, key):
    match = re.search(rf"^{key}:\s*(.*?)\s*$", path.read_text(encoding="utf-8-sig"), re.M)
    if not match:
        raise ValueError(f"Missing {key} in {path}")
    value = match.group(1)
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


parser = argparse.ArgumentParser()
parser.add_argument("--ci-run", type=int, required=True)
parser.add_argument("--commit", required=True)
args = parser.parse_args()
with urllib.request.urlopen(f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}", timeout=45) as response:
    run = response.read().decode("utf-8", "replace")
if '<span class="h4 color-fg-default">Success</span>' not in run or args.commit[:7] not in run:
    raise SystemExit("Specified GitHub run does not confirm success for this commit")

with urllib.request.urlopen("https://kenji.blog/sitemap.xml", timeout=45) as response:
    sitemap = ET.fromstring(response.read())
japanese_map = next((item.find("s:loc", NS).text for item in sitemap.findall("s:sitemap", NS) if "/ja/sitemap.xml" in item.find("s:loc", NS).text), None)
if not japanese_map:
    raise SystemExit("Japanese sitemap is missing")
with urllib.request.urlopen(japanese_map, timeout=45) as response:
    article_map = ET.fromstring(response.read())
urls = [item.find("s:loc", NS).text for item in article_map.findall("s:url", NS)]
slug = yaml_value(CONTENT / "index.md", "slug").casefold()
japanese_url = next((url for url in urls if f"/p/{slug}/" in unquote(url).casefold()), None)
if not japanese_url:
    raise SystemExit("Japanese sitemap is missing the article")
_, raw = fetch(japanese_url)
japanese = Page()
japanese.feed(raw.decode("utf-8", "replace"))
targets = set(japanese.hreflang.values())
if len(targets) != 13 or len(japanese.hreflang) != 14:
    raise SystemExit("Unexpected hreflang targets")

results = []
for language in LANGS:
    url = next((value for value in targets if (language == "ja" and re.search(r"https://kenji\.blog/p/", value)) or (language != "ja" and f"/{language}/p/" in value)), None)
    if not url:
        results.append({"language": language, "passed": False, "failure": "hreflang target missing"})
        continue
    status, raw = fetch(url)
    page = Page()
    page.feed(raw.decode("utf-8", "replace"))
    file = CONTENT / ("index.md" if language == "ja" else f"index.{language}.md")
    title = yaml_value(file, "title")
    description = yaml_value(file, "description")
    compact = re.sub(r"\s+", "", "".join(page.text))
    checks = {
        "http200": status == 200,
        "canonical": page.canonical == [url],
        "language": page.lang.lower() == language,
        "arabicRtl": language != "ar" or page.direction == "rtl",
        "title": title in "".join(page.title),
        "description": len(page.description) == 1 and page.description[0].strip() == description,
        "hreflangCount": len(page.hreflang) == 14,
        "hreflangTargets": set(page.hreflang.values()) == targets,
        "officialReferences": all(link in page.links for link in OFFICIAL),
        "currentCommandsAndCaveats": all(token.replace(" ", "") in compact for token in ["hugo new project", "hugo new content", "hugo deploy", "hugo list all", "0.159.2", "GitHub Pages", "Deploy"]),
        "dates": yaml_value(file, "date").startswith("2024-05-31") and yaml_value(file, "lastmod").startswith("2026-11-24"),
    }
    results.append({"language": language, "url": url, "status": status, "checks": checks, "passed": all(checks.values())})

passed = len(results) == 13 and all(result["passed"] for result in results)
receipt = {
    "version": 1,
    "batch": 86,
    "verifiedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
    "ciRun": args.ci_run,
    "ciUrl": f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}",
    "sourceCommit": args.commit,
    "deployment": "success" if passed else "verification_failed",
    "pagesVerified": sum(result["passed"] for result in results),
    "allPassed": passed,
    "pages": results,
    "limitations": ["AI-assisted translation review only; no human or native-speaker certification.", "Hugo command availability and edition requirements can change in future releases."],
}
(DOCS / "publication-086.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if passed:
    path = DOCS / "batch-086.json"
    batch = json.loads(path.read_text(encoding="utf-8"))
    batch["publicationPending"] = False
    batch["publication"] = {"record": "docs/translation-review/publication-086.json", "ciRun": args.ci_run, "sourceCommit": args.commit, "allPassed": True}
    path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"allPassed": passed, "pages": len(results), "failures": [result for result in results if not result["passed"]]}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
