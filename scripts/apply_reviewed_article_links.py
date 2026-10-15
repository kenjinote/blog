"""Apply an explicit editorial plan to reviewed articles, preserving source bytes.

This is deliberately restricted to simple inline links. Unsupported syntax fails
closed. It does not select articles, terms, destinations or categories itself.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
from internal_links import ROOT, language, link_text, published_pages, protected_ranges

SIMPLE_LINK = re.compile(r'(?<!!)\[([^\[\]\r\n]+)\]\((https?://[^\s()]+|/[^\s()]+)\)')


def protected_material(text):
    # Reviewed inputs must use these conventional fences/math delimiters.
    return (re.match(r'\A---\r?\n.*?\r?\n---', text, re.S)[0],
            re.findall(r'(?ms)^```[^\r\n]*\r?\n.*?^```[^\r\n]*', text),
            re.findall(r'(?s)\$\$.*?\$\$|(?<![\\$])\$(?!\$).*?(?<!\\)\$', text),
            [m[0] for m in re.finditer(r'(?s)(`+).*?\1', text)],
            re.findall(r'(?s)\\\(.*?\\\)|\\\[.*?\\\]', text))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan', type=Path)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text(encoding='utf-8'))
    published = published_pages(ROOT / 'docs/article-audit/published.csv')
    records = {p: row for p, row in published.items()}
    changes, report = [], []
    for item in plan['articles']:
        path = (ROOT / item['path']).resolve()
        if path not in records:
            raise ValueError(f'Unpublished source: {path}')
        raw = path.read_bytes()
        source = raw.decode('utf-8')
        if hashlib.sha256(raw).hexdigest() != item['source_sha256']:
            raise ValueError(f'Source changed since review: {path}')
        own = urlsplit(records[path]['permalink']).path
        protected = protected_ranges(source, protect_paragraphs=False)
        # Hugo includes Markdown link destinations in generated heading IDs.
        # Preserve heading source so existing fragment URLs remain valid.
        protected += [(m.start(), m.end()) for m in re.finditer(r"(?m)^ {0,3}#{1,6} .*$", source)]
        removed = 0
        def remove_self(match):
            nonlocal removed
            if any(a < match.end() and b > match.start() for a, b in protected):
                return match[0]
            url = urlsplit(match[2])
            if url.netloc in ('', 'kenji.blog') and url.path == own and not url.fragment and not url.query:
                removed += 1
                return match[1]
            return match[0]
        updated = SIMPLE_LINK.sub(remove_self, source)
        added = []
        for addition in item['links']:
            target = (ROOT / addition['target']).resolve()
            if target not in records or target == path or language(target) != language(path):
                raise ValueError(f'Invalid target: {target}')
            destination = urlsplit(records[target]['permalink']).path
            if any(urlsplit(m[2]).path == destination for m in SIMPLE_LINK.finditer(updated)):
                continue
            candidate, count = link_text(updated, {addition['term']: destination})
            if count != 1:
                raise ValueError(f'Expected one safe occurrence: {path}: {addition["term"]}: {count}')
            updated = candidate
            added.append({'term': addition['term'], 'url': destination})
        comparison_source = source
        if 'categories' in item:
            before, after = item['categories']['before'], item['categories']['after']
            if len(after) != len(set(after)) or not after:
                raise ValueError('Invalid category list')
            for category in after:
                if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', category):
                    raise ValueError('Invalid category identifier')
                filename = '_index.md' if language(path) == 'ja' else f'_index.{language(path)}.md'
                if not (ROOT / 'content/categories' / category / filename).is_file():
                    raise ValueError(f'Missing localized category: {category}')
            old_field = 'categories: ' + json.dumps(before, ensure_ascii=False)
            new_field = 'categories: ' + json.dumps(after, ensure_ascii=False)
            fm = protected_material(source)[0]
            if fm.count(old_field) != 1:
                raise ValueError('Category field does not match reviewed plan')
            updated = updated.replace(old_field, new_field, 1)
            comparison_source = source.replace(old_field, new_field, 1)
        strip = lambda value: SIMPLE_LINK.sub(lambda m: m[1], value)
        if strip(comparison_source) != strip(updated) or protected_material(comparison_source) != protected_material(updated):
            raise ValueError(f'Non-link content changed: {path}')
        if '\r\n' in source and updated.count('\r\n') != source.count('\r\n'):
            raise ValueError('Line ending change')
        changes.append((path, raw, updated.encode('utf-8')))
        report.append({'path': item['path'], 'removed_self_links': removed, 'added_links': added,
                       'protected_content_unchanged': True, 'visible_source_unchanged': True,
                       'category_change': item.get('categories'),
                       'categories': item['category_decision'],
                       'updated_sha256': hashlib.sha256(updated.encode('utf-8')).hexdigest()})
    if args.write:
        for path, raw, _ in changes:
            if path.read_bytes() != raw:
                raise ValueError(f'Concurrent edit: {path}')
        for path, _, updated in changes:
            path.write_bytes(updated)
        report_path = args.plan.with_name(args.plan.stem + '-source-validation.json')
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
