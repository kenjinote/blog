"""Validate shared category IDs and localized titles (requires PyYAML)."""

from pathlib import Path
import re
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r"\A\ufeff?---[^\S\n]*\n(.*?)\n---[^\S\n]*(?:\n|$)", re.S)
CATEGORIES = re.compile(r"^categories:[^\n]*(?:\n[ \t]+-[^\n]*)*", re.M)


def category_field(text):
    frontmatter = FRONTMATTER.match(text)
    if not frontmatter:
        return None, []
    match = CATEGORIES.search(frontmatter.group(1))
    if not match:
        return None, []
    values = yaml.safe_load(match.group())['categories'] or []
    if isinstance(values, str):
        values = [values]
    return match, values


def main():
    languages = yaml.safe_load((ROOT / 'hugo.yaml').read_text(encoding='utf-8'))['languages']
    category_root = ROOT / 'content/categories'
    definitions = {p.name: p for p in category_root.iterdir() if p.is_dir()}
    errors = []
    routes = {}
    aliases = []
    for category, folder in sorted(definitions.items()):
        for language in languages:
            filename = '_index.md' if language == 'ja' else f'_index.{language}.md'
            path = folder / filename
            if not path.exists():
                errors.append(f'Missing localized category: {path.relative_to(ROOT)}')
                continue
            match = FRONTMATTER.match(path.read_text(encoding='utf-8-sig'))
            data = yaml.safe_load(match.group(1)) if match else {}
            prefix = '' if language == 'ja' else f'/{language}'
            routes[f'{prefix}/categories/{category}/'] = category
            aliases.extend((alias, category) for alias in data.get('aliases', []))
            if not isinstance(data.get('title'), str) or not data['title'].strip():
                errors.append(f'Missing title: {path.relative_to(ROOT)}')
        if (folder / '_index.ja.md').exists():
            errors.append(f'Duplicate Japanese definition: {folder.relative_to(ROOT)}')

    for alias, category in aliases:
        if alias in routes and routes[alias] != category:
            errors.append(f'Conflicting category URL: {alias} ({routes[alias]}, {category})')
        routes[alias] = category

    checked = 0
    for path in sorted((ROOT / 'content').rglob('*.md')):
        _, values = category_field(path.read_text(encoding='utf-8-sig'))
        if not values:
            continue
        checked += 1
        for category in values:
            if category not in definitions:
                errors.append(f'{path.relative_to(ROOT)}: undefined category {category!r}')
        if len(values) != len(set(values)):
            errors.append(f'{path.relative_to(ROOT)}: duplicate categories')

    for error in errors:
        print(error)
    print(f'Checked {checked} pages, {len(definitions)} categories, {len(languages)} languages; {len(errors)} errors.')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
