"""Validate JSON-LD in built HTML, including multilingual and author overrides."""

import json
import sys
from collections import Counter
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.active = False
        self.canonical = None
        self.language = None
        self.redirect = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.language = attrs.get("lang")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.redirect = True
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.active = True
            self.blocks.append("")

    def handle_data(self, data):
        if self.active:
            self.blocks[-1] += data

    def handle_endtag(self, tag):
        if tag == "script":
            self.active = False


def validate(path):
    parser = HeadParser()
    head = ""
    with path.open(encoding="utf-8") as source:
        while "</head>" not in head:
            chunk = source.read(8192)
            if not chunk:
                break
            head += chunk
    parser.feed(head.split("</head>", 1)[0])
    if parser.redirect or path.name == "404.html":
        assert not parser.blocks, "redirect/404 must not describe an article"
        return None
    assert len(parser.blocks) == 1, "expected exactly one JSON-LD block"
    data = json.loads(parser.blocks[0])
    assert isinstance(data, dict), "JSON-LD must be an object, not a quoted string"
    assert data["@context"] == "https://schema.org"
    website, page = data["@graph"]
    assert website["@type"] == "WebSite"
    assert page["isPartOf"]["@id"] == website["@id"]
    assert page["url"] == parser.canonical
    assert page["inLanguage"].lower() == parser.language.lower()
    assert page["name"]
    if page["@type"] == "BlogPosting":
        assert page["headline"] == page["name"]
        assert page["mainEntityOfPage"]["@id"] == parser.canonical
        assert isinstance(page["author"]["name"], str)
        assert page["author"]["name"]
        if page["author"]["name"] != website["publisher"]["name"]:
            assert "url" not in page["author"], "override must not inherit publisher URL"
        for key in ("datePublished", "dateModified"):
            if key in page:
                assert datetime.fromisoformat(page[key]).tzinfo is not None
        for url in page.get("image", []):
            assert url.startswith(("https://", "http://")), "image URL must be absolute"
    else:
        assert page["@type"] in ("WebPage", "CollectionPage", "ProfilePage")
        if page["@type"] == "ProfilePage":
            assert page["mainEntity"]["@type"] == "Person"
            assert page["mainEntity"]["url"] == parser.canonical
        assert "headline" not in page
    return page["@type"], page["inLanguage"]


def published_pages(root):
    """Use current sitemaps, excluding stale files left in a reused output folder."""
    pending = [root / "sitemap.xml"]
    seen = set()
    pages = set()
    while pending:
        sitemap = pending.pop()
        if sitemap in seen:
            continue
        seen.add(sitemap)
        tree = ElementTree.parse(sitemap).getroot()
        is_index = tree.tag.endswith("sitemapindex")
        for loc in tree.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
            path = unquote(urlsplit(loc.text).path).lstrip("/")
            target = root / path
            if is_index:
                pending.append(target)
            else:
                pages.add(target / "index.html" if not Path(path).suffix or path.endswith("/") else target)
    return sorted(pages)


if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
    counts = Counter()
    errors = []
    for path in published_pages(root):
        try:
            result = validate(path)
            if result:
                counts[result] += 1
        except (AssertionError, ValueError, KeyError, TypeError, OSError) as error:
            errors.append(f"{path}: {error}")
    for (kind, language), count in sorted(counts.items()):
        print(f"{language}: {kind}: {count}")
    if errors:
        print("\n".join(errors[:30]), file=sys.stderr)
        print(f"FAILED: {len(errors)} pages", file=sys.stderr)
        sys.exit(1)
    if not counts:
        sys.exit("No JSON-LD pages found")
    print(f"Validated {sum(counts.values())} pages")
