"""Verify the Teams Graph API article after its successful Pages deployment."""
from datetime import datetime, timedelta, timezone
from html import unescape
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
BUNDLE = ROOT / "content/post/C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
LANGS = ["ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id"]
REFERENCES = [
    "https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0",
    "https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0",
    "https://learn.microsoft.com/en-us/graph/permissions-reference",
    "https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code",
    "https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0",
]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = ""
        self.direction = ""
        self.canonical = []
        self.hreflang = {}
        self.links = []
        self.text = []
        self.title = []
        self.descriptions = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang, self.direction = attrs.get("lang", ""), attrs.get("dir", "")
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonical.append(attrs.get("href", ""))
        if tag == "link" and attrs.get("hreflang"):
            self.hreflang[attrs["hreflang"]] = attrs.get("href", "")
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "meta" and attrs.get("name", "").lower() == "description":
            self.descriptions.append(attrs.get("content", ""))
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.title.append(data)


def metadata(lang):
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    text = path.read_text(encoding="utf-8")
    values = {}
    for name in ("title", "slug", "description"):
        match = re.search(rf"^{name}:\s*(.*?)\s*$", text, re.M)
        if not match:
            raise SystemExit(f"Missing {name} in {path}")
        value = match.group(1)
        if value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        elif value.startswith('"'):
            value = json.loads(value)
        values[name] = value
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
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8", "replace")
    if '<span class="h4 color-fg-default">Success</span>' not in body or args.commit[:7] not in body:
        raise SystemExit("GitHub run page does not confirm success for the specified commit")

namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap_index = ElementTree.fromstring(urllib.request.urlopen("https://kenji.blog/sitemap.xml", timeout=30).read())
ja_sitemap = next(
    entry.find("s:loc", namespace).text
    for entry in sitemap_index.findall("s:sitemap", namespace)
    if "/ja/sitemap.xml" in entry.find("s:loc", namespace).text
)
ja_pages = ElementTree.fromstring(urllib.request.urlopen(ja_sitemap, timeout=30).read())
root_url = next(
    entry.find("s:loc", namespace).text
    for entry in ja_pages.findall("s:url", namespace)
    if "/p/" in entry.find("s:loc", namespace).text
    and "winhttp--graph-api" in unquote(entry.find("s:loc", namespace).text).lower()
)
request = urllib.request.Request(root_url, headers={"User-Agent": "kenji.blog-translation-review/1.0"})
with urllib.request.urlopen(request, timeout=30) as response:
    root = Page()
    root.feed(response.read().decode("utf-8", "replace"))
expected = set(root.hreflang.values())
if len(expected) != 13 or len(root.hreflang) != 14:
    raise SystemExit("Japanese page does not expose the expected 13 hreflang targets")

records = []
for lang in LANGS:
    url = next((value for value in expected if (lang == "ja" and re.search(r"https://kenji\.blog/p/", value)) or (lang != "ja" and f"/{lang}/p/" in value)), None)
    if not url:
        raise SystemExit(f"Missing hreflang URL for {lang}")
    meta = metadata(lang)
    request = urllib.request.Request(url, headers={"User-Agent": "kenji.blog-translation-review/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read().decode("utf-8", "replace")
        page = Page()
        page.feed(raw)
        visible = unescape(" ".join(page.text))
        checks = {
            "http200": response.status == 200,
            "canonical": page.canonical == [url],
            "language": page.lang == lang,
            "arabicRtl": lang != "ar" or page.direction == "rtl",
            "title": meta["title"] in "".join(page.title),
            "description": len(page.descriptions) == 1 and unescape(page.descriptions[0]).strip() == meta["description"],
            "originalDate": "2025-07-14" in raw,
            "lastmod": "2026-11-23" in raw,
            "leastPrivilegePermissions": all(name in visible for name in ("ChatMessage.Send", "Chat.ReadBasic", "ChannelMessage.Send", "Teamwork.Migrate.All")),
            "deviceCodeAndRefreshScope": "offline_access" in visible and "device code" in visible.lower(),
            "utf8JsonAndHttpStatus": "EscapeJsonString" in visible and "charset=utf-8" in raw.lower() and "201" in visible and "statusBytes" in visible,
            "winHttpHandleCleanup": "WinHttpCloseHandle" in visible and "WinHttpHandle" in visible,
            "officialReferences": all(link in page.links for link in REFERENCES),
            "hreflangCount": len(page.hreflang) == 14,
            "hreflangTargets": set(page.hreflang.values()) == expected,
        }
        records.append({"language": lang, "url": url, "status": response.status, "checks": checks, "passed": all(checks.values())})

passed = len(records) == 13 and all(record["passed"] for record in records)
receipt = {
    "version": 1,
    "checkedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
    "ciRun": args.ci_run,
    "ciUrl": f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}",
    "deployedCommit": args.commit,
    "allPassed": passed,
    "scope": "Batch 054 Japanese source plus twelve translations; live HTTP validates status, canonical, locale/RTL, metadata and dates, least-privilege Graph permissions, device-code and refresh-token notes, UTF-8 JSON and HTTP status handling, WinHTTP handle cleanup, official references, and hreflang targets.",
    "pages": records,
    "limitations": ["AI review only; no human/native-speaker certification.", "No C++ compilation or Microsoft 365 tenant integration was performed.", "No rendered browser/device visual QA was performed."],
}
(DOCS / "publication-054.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if passed:
    batch_path = DOCS / "batch-054.json"
    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    batch["publicationPending"] = False
    batch["publication"] = {"record": "docs/translation-review/publication-054.json", "ciRun": args.ci_run, "deployedCommit": args.commit, "allPassed": True}
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"allPassed": passed, "pages": len(records), "failures": [record for record in records if not record["passed"]]}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
