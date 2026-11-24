"""Verify publication of the refreshed IntelliJ translation batches."""
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
LANGS = ("ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id")
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
ARTICLES = {
    87: {
        "bundle": ROOT / "content/post/IntelliJ IDEAでGitHub Copilotを使う",
        "slug": "IntelliJ IDEAでGitHub Copilotを使う",
        "links": [
            "https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension",
            "https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions",
            "https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer",
        ],
        "markers": ["CopyandOpen", "LogintoGitHub", "AuthorizeGitHubCopilotPlugin", "CopilotFree", "GitHubCopilotChat"],
        "date": "2022-09-10",
    },
    88: {
        "bundle": ROOT / "content/post/IntelliJ IDEAで日付を貼り付けるコマンドを追加する",
        "slug": "IntelliJ IDEAで日付を貼り付けるコマンドを追加する",
        "links": [
            "https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html",
            "https://www.jetbrains.com/help/idea/template-variables.html",
            "https://www.jetbrains.com/help/idea/settings-live-templates.html",
        ],
        "markers": ["yyyy-MM-dd'T'HH:mm:ssXXX", "Skipifdefined", "Tab", "Everywhere", "+09:00"],
        "date": "2022-09-04",
    },
    89: {
        "bundle": ROOT / "content/post/LoadIconはDestroyIconを呼び出す必要はない",
        "slug": "LoadIconはDestroyIconを呼び出す必要はない",
        "links": [
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex",
        ],
        "markers": ["LoadIcon", "LoadImage", "LR_SHARED", "LR_COPYRETURNORG", "CopyIcon", "CreateIconFromResourceEx", "DestroyIcon"],
        "date": "2024-04-19",
    },
    90: {
        "bundle": ROOT / "content/post/かっこいい Web ページテンプレート（html5up）",
        "slug": "かっこいい Web ページテンプレート（html5up）",
        "links": ["https://html5up.net/", "https://html5up.net/license"],
        "markers": ["HTML5", "CSS3", "CCBY3.0", "FreeDownload"],
        "date": "2023-04-17",
    },
}


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
        raise ValueError(f"Missing {key}: {path}")
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
    sitemap = ET.fromstring(response.read())
all_urls = [item.find("s:loc", NS).text for item in sitemap.findall("s:url", NS)]

results = {}
for batch_number, article in ARTICLES.items():
    bundle = article["bundle"]
    slug = re.sub(r"\s+", "", article["slug"]).casefold()
    japanese_url = next((url for url in all_urls if f"/p/{slug}/" in unquote(url).casefold()), None)
    if not japanese_url:
        raise SystemExit(f"Batch {batch_number}: Japanese article missing from sitemap")
    _, raw = fetch(japanese_url)
    root_page = Page()
    root_page.feed(raw.decode("utf-8", "replace"))
    targets = set(root_page.hreflang.values())
    if len(targets) != 13 or len(root_page.hreflang) != 14:
        raise SystemExit(f"Batch {batch_number}: unexpected hreflang targets")
    pages = []
    for language in LANGS:
        url = next((value for value in targets if (language == "ja" and re.search(r"https://kenji\.blog/p/", value)) or (language != "ja" and f"/{language}/p/" in value)), None)
        if not url:
            pages.append({"language": language, "passed": False, "failure": "hreflang target missing"})
            continue
        status, raw = fetch(url)
        page = Page()
        html = raw.decode("utf-8", "replace")
        page.feed(html)
        path = bundle / ("index.md" if language == "ja" else f"index.{language}.md")
        title = yaml_value(path, "title")
        description = yaml_value(path, "description")
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
            "officialReferences": all(link in page.links for link in article["links"]),
            "articleInstructions": all(marker in compact for marker in article["markers"]),
            "dates": yaml_value(path, "date").startswith(article["date"]) and yaml_value(path, "lastmod").startswith("2026-11-24"),
        }
        pages.append({"language": language, "url": url, "status": status, "checks": checks, "passed": all(checks.values())})
    results[batch_number] = {"pages": pages, "allPassed": len(pages) == 13 and all(page["passed"] for page in pages)}

passed = len(results) == len(ARTICLES) and all(result["allPassed"] for result in results.values())
receipt = {
    "version": 1,
    "batches": list(ARTICLES),
    "verifiedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
    "ciRun": args.ci_run,
    "ciUrl": f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}",
    "sourceCommit": args.commit,
    "deployment": "success" if passed else "verification_failed",
    "pagesVerified": sum(sum(page["passed"] for page in result["pages"]) for result in results.values()),
    "allPassed": passed,
    "results": results,
    "limitations": ["AI-assisted translation reviews only; no human or native-speaker certification.", "IDE menus and account plan details can change; each article links to current official references."],
}
(DOCS / "publication-087-090.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if passed:
    for batch_number in ARTICLES:
        path = DOCS / f"batch-{batch_number}.json"
        entry = json.loads(path.read_text(encoding="utf-8"))
        entry["publicationPending"] = False
        entry["publication"] = {"record": "docs/translation-review/publication-087-090.json", "ciRun": args.ci_run, "sourceCommit": args.commit, "allPassed": True}
        path.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"allPassed": passed, "pages": receipt["pagesVerified"], "failures": {batch: [page for page in value["pages"] if not page["passed"]] for batch, value in results.items()}}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
