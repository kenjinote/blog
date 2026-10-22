"""Reject insecure first-party publication metadata before deploying Hugo output.

Article prose and external URLs are intentionally outside this check.
Uses only the Python standard library.
"""

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree


def check_url(value, source):
    if not isinstance(value, str):
        return
    url = urlsplit(value.strip())
    if url.hostname in {"kenji.blog", "www.kenji.blog"} and url.scheme != "https":
        raise ValueError(f"{source}: insecure publication URL: {value}")


def check_json(value, source):
    if isinstance(value, dict):
        for item in value.values():
            check_json(item, source)
    elif isinstance(value, list):
        for item in value:
            check_json(item, source)
    elif isinstance(value, str) and value.startswith(("http:", "https:", "//")):
        check_url(value, source)


class HeadParser(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.source = source
        self.json_ld = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link":
            check_url(attrs.get("href"), self.source)
        elif tag == "meta":
            if attrs.get("property", "").startswith("og:"):
                check_url(attrs.get("content"), self.source)
            if attrs.get("name", "").startswith("twitter:"):
                check_url(attrs.get("content"), self.source)
            if attrs.get("http-equiv", "").lower() == "refresh":
                _, separator, target = attrs.get("content", "").partition("url=")
                if separator:
                    check_url(target, self.source)
        elif tag == "script" and attrs.get("type") == "application/ld+json":
            self.json_ld = ""

    def handle_data(self, data):
        if self.json_ld is not None:
            self.json_ld += data

    def handle_endtag(self, tag):
        if tag == "script" and self.json_ld is not None:
            check_json(json.loads(self.json_ld), self.source)
            self.json_ld = None


def validate(root):
    for required in ("index.html", "sitemap.xml", "robots.txt"):
        if not (root / required).is_file():
            raise ValueError(f"Missing build output: {root / required}")
    counts = {"html": 0, "xml": 0, "search": 0}
    for path in root.rglob("*.html"):
        with path.open(encoding="utf-8") as source:
            chunks = []
            while True:
                chunk = source.read(8192)
                chunks.append(chunk)
                if "</head>" in chunk or not chunk:
                    break
        HeadParser(path).feed("".join(chunks).split("</head>", 1)[0])
        counts["html"] += 1
    for path in root.rglob("*.xml"):
        for element in ElementTree.parse(path).iter():
            if element.tag.rsplit("}", 1)[-1] in {"loc", "link", "id", "url"}:
                check_url(element.text, path)
            for key in ("href", "url"):
                check_url(element.get(key), path)
        counts["xml"] += 1
    for path in root.glob("**/search/index.json"):
        for entry in json.loads(path.read_text(encoding="utf-8")):
            for key in ("permalink", "image"):
                check_url(entry.get(key), path)
        counts["search"] += 1
    for line in (root / "robots.txt").read_text(encoding="utf-8").splitlines():
        if line.lower().startswith("sitemap:"):
            check_url(line.split(":", 1)[1], root / "robots.txt")
    return counts


if __name__ == "__main__":
    try:
        counts = validate(Path(sys.argv[1] if len(sys.argv) > 1 else "public"))
    except (ValueError, OSError, ElementTree.ParseError) as error:
        sys.exit(str(error))
    print(f"HTTPS publication URLs verified: {counts}")
