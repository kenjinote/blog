"""Check the deployed AG03 article pages in all languages over HTTPS."""
import concurrent.futures
import datetime
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs" / "translation-review"
LANGS = ("ja", "en", "zh-cn", "zh-tw", "es", "ko", "pt", "fr", "de", "hi", "id", "ar", "ru")
REFS = (
    "https://jp.yamaha.com/audio/streaming-gaming/products/mixers/ag/ag03/support.html",
    "https://jp.yamaha.com/support/updates/yamaha_steinberg_usb_driver_for_win.html",
    "https://jp.yamaha.com/business/audio/news/2022/defect.html",
    "https://jp.yamaha.com/audio/streaming-gaming/products/mixers/ag/ag03/specs.html",
)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.html_attrs, self.canonical, self.hreflang = {}, [], {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.html_attrs = a
        if tag == "link" and "canonical" in a.get("rel", "").split():
            self.canonical.append(a.get("href"))
        if tag == "link" and a.get("rel") == "alternate" and a.get("hreflang"):
            self.hreflang[a["hreflang"]] = a.get("href")


def check(language, url, urls):
    req = Request(url, headers={"User-Agent": "Codex-publication-check/1.0", "Cache-Control": "no-cache"})
    with urlopen(req, timeout=45) as response:
        status = response.status
        final_url = response.geturl()
        body = response.read().decode("utf-8")
        last_modified = response.headers.get("Last-Modified")
    parser = Page()
    parser.feed(body)
    article = ROOT / "content" / "post" / "AG03ノイズ解消方法" / ("index.md" if language == "ja" else f"index.{language}.md")
    text = article.read_text(encoding="utf-8")
    title = json.loads(re.search(r'^title: (".*")$', text, re.M).group(1))
    checks = {
        "http200": status == 200,
        "finalUrlMatches": final_url == url,
        "canonicalMatches": parser.canonical == [url],
        "languageMatches": parser.html_attrs.get("lang") == language,
        "arabicRtl": language != "ar" or parser.html_attrs.get("dir") == "rtl",
        "titlePresent": html.unescape(title) in html.unescape(body),
        "officialReferencesPresent": all(ref in body for ref in REFS),
        "staleMercariAdRemoved": "m10570024971" not in body,
        "archivedFaqRemoved": "web.archive.org/web/20201003230738" not in body,
        "allLanguageTargetsMatch": all(parser.hreflang.get(lang) == target for lang, target in urls.items()),
        "hreflangCount14": len(parser.hreflang) == 14,
    }
    return {"language": language, "url": url, "status": status, "lastModified": last_modified, "checks": checks, "passed": all(checks.values())}


def main():
    validation = json.loads((DOCS / "batch-039-r2-validation.json").read_text(encoding="utf-8"))
    urls = {p["language"]: p["url"] for p in validation["articlePages"]}
    assert set(urls) == set(LANGS)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        pages = list(pool.map(lambda lang: check(lang, urls[lang], urls), LANGS))
    receipt = {
        "checkedAt": datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat(),
        "allPassed": all(p["passed"] for p in pages),
        "pages": pages,
        "scope": "Post-deployment HTTPS/HTTP verification of Japanese original plus all12 revised AG03 translations. Checks status, final URL, canonical, language/Arabic RTL, title, four official sources, removed obsolete embeds and all14 hreflang destinations. No browser-rendering, hardware-driver execution or human/native-speaker certification.",
    }
    out = DOCS / "batch-039-live-pages.json"
    out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"allPassed": receipt["allPassed"], "pages": len(pages), "failed": [p["language"] for p in pages if not p["passed"]], "receipt": str(out)}, ensure_ascii=False))
    if not receipt["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
