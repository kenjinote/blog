"""Verify that every searchable article is indexed in its own language."""

import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


LANGUAGES = {"ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id"}
NAMESPACE = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def validate(root):
    bundle = root / "pagefind"
    entry = json.loads((bundle / "pagefind-entry.json").read_text(encoding="utf-8"))
    assert set(entry["languages"]) == LANGUAGES, "Search languages differ from site languages"
    expected = Counter()
    for sitemap in ElementTree.parse(root / "sitemap.xml").iter(f"{NAMESPACE}loc"):
        sitemap_path = root / unquote(urlsplit(sitemap.text).path).lstrip("/")
        for location in ElementTree.parse(sitemap_path).iter(f"{NAMESPACE}loc"):
            path = unquote(urlsplit(location.text).path)
            if not re.match(r"^/(?:[a-z-]+/)?p/[^/]+/$", path):
                continue
            html = (root / path.lstrip("/") / "index.html").read_text(encoding="utf-8")
            if "data-pagefind-body" not in html:
                continue
            language = re.search(r"<html\b[^>]*\blang=[\"']?([\w-]+)", html).group(1)
            expected[language] += 1
    for language in sorted(LANGUAGES):
        details = entry["languages"][language]
        assert expected[language] > 0, f"No published articles found for {language}"
        assert details["page_count"] == expected[language], (
            f"{language}: indexed {details['page_count']}, expected {expected[language]}"
        )
        assert (bundle / f"pagefind.{details['hash']}.pf_meta").is_file(), f"Missing {language} metadata"
        search_dir = root / ("" if language == "ja" else language) / "search"
        page = (search_dir / "index.html").read_text(encoding="utf-8")
        assert 'data-module="/pagefind/pagefind.js"' in page or 'data-module=/pagefind/pagefind.js' in page
        assert "data-json=" not in page, f"{language} still loads the old full-text JSON"
        assert not (search_dir / "index.json").exists(), f"{language} still publishes the old full-text JSON"
        print(f"{language}: {expected[language]} articles indexed")
    assert (bundle / "pagefind.js").is_file(), "Missing browser search module"
    print(f"Search verified: {sum(expected.values())} articles across {len(LANGUAGES)} languages")


if __name__ == "__main__":
    try:
        validate(Path(sys.argv[1] if len(sys.argv) > 1 else "public"))
    except (AssertionError, OSError, ValueError, AttributeError, KeyError) as error:
        sys.exit(str(error))
