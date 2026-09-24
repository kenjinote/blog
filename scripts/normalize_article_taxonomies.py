"""Copy the Japanese article's canonical taxonomy IDs to its translations.

This utility only validates/repairs frontmatter. It never generates prose.
Usage: python scripts/normalize_article_taxonomies.py <article-slug> [<slug> ...]
"""

import ast
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1] / "content" / "post"


def normalize(slug):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError(f"Invalid article slug: {slug}")
    folder = ROOT / slug
    original = (folder / "index.md").read_text(encoding="utf-8-sig")
    canonical = original.split("---", 2)[1]
    fields = {}
    for field in ("categories", "tags"):
        match = re.search(rf"^{field}:\s*(\[[^\n]+\])\s*$", canonical, re.M)
        if not match:
            raise ValueError(f"Expected inline canonical {field}: {slug}")
        values = ast.literal_eval(match.group(1))
        if not values or not all(
            isinstance(value, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value)
            for value in values
        ):
            raise ValueError(f"Noncanonical {field}: {slug}")
        fields[field] = f"{field}: {match.group(1)}"

    repaired = 0
    translations = sorted(folder.glob("index.*.md"))
    for path in translations:
        text = path.read_text(encoding="utf-8-sig")
        opening, frontmatter, body = text.split("---", 2)
        if opening.strip():
            raise ValueError(f"Unexpected content before frontmatter: {path}")
        for field, line in fields.items():
            pattern = rf"^{field}:[^\n]*(?:\n[ \t]+-[^\n]*)*"
            frontmatter, count = re.subn(pattern, line, frontmatter, flags=re.M)
            if count != 1:
                raise ValueError(f"Expected one {field} field: {path}")
        updated = "---" + frontmatter + "---" + body
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            repaired += 1
    print(f"{slug}: checked {len(translations)} translations; repaired {repaired}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Pass one or more article slugs.")
    for article in sys.argv[1:]:
        normalize(article)
