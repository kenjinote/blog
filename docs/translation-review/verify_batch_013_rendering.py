"""Compare every TeX expression in the reviewed cryptography Markdown and HTML.

Usage: python docs/translation-review/verify_batch_013_rendering.py SITE --output NEW.json
This checks decoded HTML text, not browser layout or native-language fluency.
The source tokenizer is scoped to these reviewed articles, excluding fenced code.
"""

import argparse
import collections
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from translation_reviews import digest

SLUG = "modern-cryptography-public-key-hash-signature"
PATTERN = r"(?s)(?<!\\)\$\$(.*?)\$\$|(?<![\\$])\$(?!\$)(.*?)(?<!\\)\$|\\\((.*?)\\\)|\\\[(.*?)\\\]"


class ArticleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == "section" and "article-content" in dict(attrs).get("class", "").split():
            self.depth = 1
        elif self.depth and tag == "section":
            self.depth += 1

    def handle_endtag(self, tag):
        if self.depth and tag == "section":
            self.depth -= 1

    def handle_data(self, text):
        if self.depth:
            self.parts.append(text)


def expressions(text):
    return collections.Counter(
        next(value for value in match.groups() if value is not None).strip()
        for match in re.finditer(PATTERN, text)
    )


def verify(site):
    files = []
    for path in sorted((ROOT / "content/post" / SLUG).glob("index*.md")):
        language = "ja" if path.name == "index.md" else path.name[6:-3]
        source = re.sub(r"^```.*?^```[^\n]*", "", path.read_text(encoding="utf-8"), flags=re.M | re.S)
        html_path = site / ("" if language == "ja" else language) / "p" / SLUG / "index.html"
        parser = ArticleText()
        parser.feed(html_path.read_text(encoding="utf-8"))
        text = "".join(parser.parts)
        expected, actual = expressions(source), expressions(text)
        checks = {
            "allTeXExpressionsPreserved": expected == actual,
            "rsaConditionPreserved": r"1<e<\phi(N)" in actual,
            "followingEnglishSentencePreserved": language != "en" or "The implementation below uses" in text,
        }
        files.append({
            "language": language, "path": path.relative_to(ROOT / "content").as_posix(),
            "hash": digest(path), "expressions": sum(expected.values()),
            "missing": list((expected - actual).elements()),
            "unexpected": list((actual - expected).elements()),
            "checks": checks, "passed": all(checks.values()),
        })
    return {
        "version": 1, "checkedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
        "site": str(site), "scope": "All thirteen cryptography article versions; exact TeX after HTML entity decoding and outer whitespace stripping.",
        "limitations": "Not a visual browser/KaTeX test. Fenced code excluded; tokenizer scoped to these articles.",
        "files": files, "allPassed": all(item["passed"] for item in files),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output and args.output.exists():
        parser.error("Preserve the existing evidence; choose a new output path.")
    result = verify(args.site)
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"pages": len(result["files"]), "expressions": sum(item["expressions"] for item in result["files"]),
                      "passed": sum(item["passed"] for item in result["files"]),
                      "failures": [item for item in result["files"] if not item["passed"]]}, ensure_ascii=False))
    sys.exit(0 if result["allPassed"] else 1)
