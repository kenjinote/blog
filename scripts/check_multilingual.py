"""Validate hreflang uniqueness, reciprocal canonical URLs and sidebar destinations."""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonical = None
        self.language = None
        self.alternates = {}
        self.options = {}
        self.in_switch = False
        self.status = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.language = attrs.get("lang")
        if tag == "link" and attrs.get("rel") == "canonical":
            assert self.canonical is None, "Duplicate canonical"
            self.canonical = attrs["href"]
        if tag == "link" and "hreflang" in attrs:
            language = attrs["hreflang"]
            assert language not in self.alternates, f"Duplicate hreflang: {language}"
            assert attrs.get("rel") == "alternate"
            self.alternates[language] = attrs["href"]
        if tag == "select" and attrs.get("id") == "language-select":
            self.in_switch = True
        if tag == "option" and self.in_switch:
            language = attrs["data-language"]
            assert language not in self.options, f"Duplicate language option: {language}"
            self.options[language] = attrs.get("value", "")
        if attrs.get("id") == "language-status":
            self.status = bool(attrs.get("data-missing")) and attrs.get("role") == "status"

    def handle_endtag(self, tag):
        if tag == "select":
            self.in_switch = False


def sitemap_urls(root, path=None):
    tree = ElementTree.parse(path or root / "sitemap.xml")
    for location in tree.iter(f"{NS}loc"):
        url = location.text
        if tree.getroot().tag == f"{NS}sitemapindex":
            yield from sitemap_urls(root, root / unquote(urlsplit(url).path).lstrip("/"))
        else:
            yield url


def validate(root):
    pages = {}
    for url in sitemap_urls(root):
        path = root / unquote(urlsplit(url).path).lstrip("/") / "index.html"
        parser = PageParser()
        # Sidebar precedes article text: parsing just through </aside> avoids huge article bodies.
        with path.open(encoding="utf-8") as source:
            prefix = ""
            while "</aside>" not in prefix:
                chunk = source.read(8192)
                if not chunk:
                    break
                prefix += chunk
        try:
            parser.feed(prefix.split("</aside>", 1)[0] + "</aside>")
            assert parser.canonical == url, f"Canonical differs from sitemap: {parser.canonical}"
            assert parser.alternates.get(parser.language) == url, "Missing self hreflang"
            assert parser.status, "Missing untranslated-page notice"
            assert parser.options, "Missing language selector"
            for language, target in parser.options.items():
                assert target == parser.alternates.get(language, ""), f"Sidebar differs from hreflang: {language}"
            assert set(parser.alternates) - {"x-default"} <= set(parser.options), "Translation absent from sidebar"
            expected_default = parser.alternates.get("ja")
            assert parser.alternates.get("x-default") == expected_default, "Incorrect x-default"
        except (AssertionError, KeyError) as error:
            raise AssertionError(f"{url}: {error}") from error
        pages[url] = (parser.language, parser.alternates)
    for url, (_, alternates) in pages.items():
        for language, target in alternates.items():
            assert urlsplit(target).scheme == "https", f"Non-HTTPS alternate: {target}"
            assert target in pages, f"Alternate missing from sitemap: {url} -> {target}"
            target_language, target_alternates = pages[target]
            assert language == "x-default" or target_language == language, f"Wrong target language: {target}"
            assert target_alternates == alternates, f"Non-reciprocal translation group: {url} -> {target}"
    print(f"Multilingual verified: {len(pages)} pages; unique, reciprocal hreflang and matching sidebar URLs")


if __name__ == "__main__":
    try:
        validate(Path(sys.argv[1] if len(sys.argv) > 1 else "public"))
    except (AssertionError, KeyError, OSError, ValueError) as error:
        sys.exit(str(error))
