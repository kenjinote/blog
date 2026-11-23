"""Verify the OpenAI curl article after GitHub Pages deployment."""
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree
import argparse
import json
import re
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
BUNDLE = "post/ChatGPT APIをcurlから呼び出す"
LANGS = ["ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id"]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang, self.direction = "", ""
        self.canonical, self.hreflang, self.links = [], {}, []
        self.text, self.title, self.descriptions = [], [], []
        self.in_title = False

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
            self.title.append(data)


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "kenji.blog-translation-review/1.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        raw = response.read().decode("utf-8", "replace")
        page = Page()
        page.feed(raw)
        return response.status, raw, page, " ".join(page.text)


def metadata(lang):
    path = ROOT / "content" / BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    text = path.read_text(encoding="utf-8")
    values = {}
    for field in ("title", "slug", "description"):
        match = re.search(rf"^{field}:\s*(.*?)\s*$", text, re.M)
        if not match:
            raise SystemExit(f"Missing {field} in {path}")
        value = match.group(1)
        if value.startswith('"'):
            values[field] = json.loads(value)
        elif value.startswith("'") and value.endswith("'"):
            values[field] = value[1:-1].replace("''", "'")
        else:
            values[field] = value
    return values


parser = argparse.ArgumentParser()
parser.add_argument("--ci-run", required=True, type=int)
parser.add_argument("--commit", required=True)
args = parser.parse_args()
request = urllib.request.Request(
    f"https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}",
    headers={"User-Agent": "kenji.blog-translation-review/1.0", "Accept": "application/vnd.github+json"},
)
try:
    with urllib.request.urlopen(request, timeout=30) as response:
        run = json.load(response)
    if run.get("conclusion") != "success" or not run.get("head_sha", "").startswith(args.commit):
        raise SystemExit("CI run is not successful for the specified commit")
except urllib.error.HTTPError as error:
    if error.code != 403:
        raise
    request = urllib.request.Request(
        f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}?review_check=1",
        headers={"User-Agent": "Mozilla/5.0 kenji.blog-translation-review/1.0"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        body = response.read().decode("utf-8", "replace")
    if '<span class="h4 color-fg-default">Success</span>' not in body or args.commit[:7] not in body:
        raise SystemExit("GitHub run page does not confirm success for the specified commit")

ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
index = ElementTree.fromstring(urllib.request.urlopen("https://kenji.blog/sitemap.xml", timeout=45).read())
ja_map = next(e.find("s:loc", ns).text for e in index.findall("s:sitemap", ns) if "/ja/sitemap.xml" in e.find("s:loc", ns).text)
ja_sitemap = ElementTree.fromstring(urllib.request.urlopen(ja_map, timeout=45).read())
urls = [e.find("s:loc", ns).text for e in ja_sitemap.findall("s:url", ns)]
root_url = next((url for url in urls if "/p/" in url and "chatgpt-api" in unquote(url).lower()), None)
if not root_url:
    raise SystemExit("Japanese sitemap is missing the article slug")
_, _, root_page, _ = fetch(root_url)
targets = set(root_page.hreflang.values())
if len(targets) != 13 or len(root_page.hreflang) != 14:
    raise SystemExit("Unexpected hreflang target count")

official = [
    "https://developers.openai.com/api/docs/quickstart",
    "https://developers.openai.com/api/docs/guides/text",
    "https://developers.openai.com/api/reference/resources/responses/methods/create",
    "https://developers.openai.com/api/docs/models",
    "https://developers.openai.com/api/docs/pricing",
    "https://developers.openai.com/api/docs/guides/production-best-practices",
    "https://platform.openai.com/api-keys",
    "https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform",
]
results = []
for lang in LANGS:
    url = next((u for u in targets if (lang == "ja" and re.search(r"https://kenji\.blog/p/", u)) or (lang != "ja" and f"/{lang}/p/" in u)), None)
    if not url:
        raise SystemExit(f"Missing {lang} hreflang page")
    status, raw, page, visible = fetch(url)
    meta = metadata(lang)
    compact = re.sub(r"\s+", "", visible)
    checks = {
        "http200": status == 200,
        "canonical": page.canonical == [url],
        "language": page.lang == lang,
        "arabicRtl": lang != "ar" or page.direction == "rtl",
        "title": meta["title"] in "".join(page.title),
        "description": len(page.descriptions) == 1 and page.descriptions[0].strip() == meta["description"],
        "originalDate": "2025-02-01" in raw,
        "lastmod": "2026-11-23" in raw,
        "hreflangCount": len(page.hreflang) == 14,
        "hreflangTargets": set(page.hreflang.values()) == targets,
        "officialReferences": all(link in page.links for link in official),
        "responsesCommand": all(token in compact for token in ("curl.exe", "https://api.openai.com/v1/responses", "--data-binary", "@request.json", "gpt-6.2-sol")),
        "keyUsesEnvironment": "OPENAI_API_KEY" in visible and "Authorization" in visible and "Bearer" in visible,
        "requestHasNoSecretPlaceholder": "sk-proj-XXXXXXXXXXXXXXXXXXXX" not in raw,
        "responseSchema": "output_text" in visible and "type" in visible,
        "errorsAndBilling": "401" in visible and "429" in visible and "ChatGPT" in visible,
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
    "scope": "Batch 061 Japanese source and twelve translations; live HTTP, metadata, canonical, language/RTL, reciprocal hreflang, Responses API request, API-key handling, response shape, billing guidance, and official references.",
    "pages": results,
    "limitations": ["AI translation review only; no human or native-speaker certification.", "No API key was used and no billable API request was made."],
}
(DOCS / "publication-061.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if passed:
    batch_path = DOCS / "batch-061.json"
    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    batch["publicationPending"] = False
    batch["publication"] = {"record": "docs/translation-review/publication-061.json", "ciRun": args.ci_run, "deployedCommit": args.commit, "allPassed": True}
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"allPassed": passed, "pages": len(results), "failures": [row for row in results if not row["passed"]]}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
