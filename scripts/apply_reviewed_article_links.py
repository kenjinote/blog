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



def link_reviewed_context(source, term, context, destination, math_literals=(), probe_padding=False):
    """Validate one editor-selected text span even in simple inline-HTML articles."""
    if source.count(context) != 1 or context.count(term) != 1:
        raise ValueError('Reviewed context must identify exactly one term')
    start = source.index(context) + context.index(term)
    end = start + len(term)
    # Only mask known inline tags for the existing conservative scanner. Unknown
    # HTML and shortcodes still cause a refusal. Never edit tag text/attributes.
    tags = list(re.finditer(r'</?(?:strong|br)\b[^>]*>', source, re.I))
    if any(m.start() < end and m.end() > start for m in tags):
        raise ValueError('Reviewed term overlaps HTML markup')
    masked = re.sub(r'</?(?:strong|br)\b[^>]*>', lambda m: ''.join('\n' if c == '\n' else ' ' for c in m[0]), source, flags=re.I)
    # The generic scanner protects a whole block beginning with a heading.
    # For an explicitly reviewed body span, isolate the heading in the probe
    # without permitting changes to the heading itself or to fenced content.
    heading_pattern = r'(?m)^ {0,3}#{1,6}[ \t]+[^\r\n]*'
    if any(m.start() < end and m.end() > start for m in re.finditer(heading_pattern, source)):
        raise ValueError('Reviewed term overlaps a heading')
    masked = re.sub(heading_pattern, lambda m: '\n' * len(m[0]), masked)
    # An explicit reviewed math literal may resemble a dollar-denominated price.
    # Keep its delimiters and length, and prohibit edits inside the literal.
    for literal in math_literals:
        if not re.fullmatch(r'\$[^$\r\n]+\$', literal) or literal not in source:
            raise ValueError('Invalid reviewed math literal')
        for match in re.finditer(re.escape(literal), source):
            if match.start() < end and match.end() > start:
                raise ValueError('Reviewed term overlaps math')
        masked = masked.replace(literal, '$' + 'x' * (len(literal) - 2) + '$')
    token = 'AUDITREVIEWEDTEXTTOKEN'
    if token in source:
        raise ValueError('Probe token collision')
    probe = masked[:start] + (' ' + token + ' ' if probe_padding else token) + masked[end:]
    _, count = link_text(probe, {token: destination})
    if count != 1:
        raise ValueError('Reviewed span is protected Markdown, math, code or HTML')
    return source[:start] + f'[{term}]({destination})' + source[end:], 1


def unwrap_reviewed_link(source, item, allowed_paths):
    """Remove only an explicitly reviewed link wrapper in ordinary body text."""
    raw_link, context = item['link'], item['context']
    match = SIMPLE_LINK.fullmatch(raw_link)
    if not match or item['reason'] not in ('duplicate', 'misleading'):
        raise ValueError('Invalid reviewed link removal')
    url = urlsplit(match[2])
    if url.netloc not in ('', 'kenji.blog') or url.query or url.fragment or url.path not in allowed_paths:
        raise ValueError('Removal target must be a same-language published article')
    # Probe the whole wrapper, so the scanner still rejects math, code, HTML,
    # headings and enclosing links. Discard the probe result; keep the label.
    link_reviewed_context(source, raw_link, context, url.path, probe_padding=True)
    if item['reason'] == 'duplicate' and sum(
        urlsplit(m[2]).netloc in ('', 'kenji.blog') and urlsplit(m[2]).path == url.path
        for m in SIMPLE_LINK.finditer(source)
    ) < 2:
        raise ValueError('Duplicate removal would remove the only target link')
    start = source.index(context) + context.index(raw_link)
    return source[:start] + match[1] + source[start + len(raw_link):]


def unwrap_reviewed_heading(source, item, allowed_paths):
    """Keep a reviewed rendered anchor when removing one misleading heading link.

    The plan supplies the old ID from the baseline HTML. A subsequent browser
    comparison must confirm that the actual heading IDs remain unchanged.
    """
    heading, raw_link, old_id = item['heading'], item['link'], item['old_id']
    match = re.fullmatch(r'(#{1,6}) ([^\r\n]+)', heading)
    if (not match or source.splitlines().count(heading) != 1 or source.count(heading) != 1
            or not re.fullmatch(r'[\w-]+', old_id)
            or any(c in match[2] for c in '`$<>{}\\')
            or heading.count(raw_link) != 1
            or heading[heading.index(raw_link)-1:heading.index(raw_link)] in ('!', '\\')):
        raise ValueError('Invalid reviewed heading or baseline anchor')
    # Temporarily remove the heading marker to run the ordinary protected-span
    # check. Fences, frontmatter and enclosing Markdown still stay protected.
    probe = source.replace(heading, match[2], 1)
    removal = {'link': raw_link, 'context': match[2], 'reason': 'misleading'}
    unwrap_reviewed_link(probe, removal, allowed_paths)
    link = SIMPLE_LINK.fullmatch(raw_link)
    updated_heading = heading.replace(raw_link, link[1], 1) + ' {#' + old_id + '}'
    return source.replace(heading, updated_heading, 1), updated_heading


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
        if item.get('pending_unwrap'):
            raise ValueError('Unresolved link review in plan')
        broken_self_links = item.get('broken_self_links', [])
        for raw_link in broken_self_links:
            match = SIMPLE_LINK.fullmatch(raw_link)
            if not match or source.count(raw_link) != 1:
                raise ValueError('Broken self-link must identify one exact link')
            url = urlsplit(match[2])
            if url.netloc not in ('', 'kenji.blog') or url.fragment or url.query or url.path == own or url.path.replace("'", '') != own:
                raise ValueError('Reviewed broken link is not a quoted self-link')
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
            if match[0] in broken_self_links:
                removed += 1
                return match[1]
            if url.netloc in ('', 'kenji.blog') and url.path == own and not url.fragment and not url.query:
                removed += 1
                return match[1]
            return match[0]
        updated = SIMPLE_LINK.sub(remove_self, source)
        if any(raw_link in updated for raw_link in broken_self_links):
            raise ValueError('Broken self-link lies in protected content')
        unwrapped = item.get('unwrap_links', [])
        allowed_paths = {urlsplit(row['permalink']).path for p, row in records.items()
                         if language(p) == language(path) and p != path}
        for removal in unwrapped:
            updated = unwrap_reviewed_link(updated, removal, allowed_paths)
        added = []
        for addition in item['links']:
            target = (ROOT / addition['target']).resolve()
            if target not in records or target == path or language(target) != language(path):
                raise ValueError(f'Invalid target: {target}')
            destination = urlsplit(records[target]['permalink']).path
            if any(urlsplit(m[2]).path == destination for m in SIMPLE_LINK.finditer(updated)):
                continue
            if 'context' in addition:
                candidate, count = link_reviewed_context(updated, addition['term'], addition['context'], destination, item.get('math_literals', []))
            else:
                candidate, count = link_text(updated, {addition['term']: destination})
            if count != 1:
                raise ValueError(f'Expected one safe occurrence: {path}: {addition["term"]}: {count}')
            updated = candidate
            added.append({'term': addition['term'], 'url': destination})
        comparison_source = source
        heading_repairs = []
        for heading_item in item.get('heading_unwraps', []):
            updated, new_heading = unwrap_reviewed_heading(updated, heading_item, allowed_paths)
            comparison_source = comparison_source.replace(
                heading_item['heading'], heading_item['heading'] + ' {#' + heading_item['old_id'] + '}', 1)
            heading_repairs.append({'before': heading_item['heading'], 'after': new_heading,
                                    'preserved_id': heading_item['old_id']})
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
            old_field = item['categories'].get('source_field', 'categories: ' + json.dumps(before, ensure_ascii=False))
            import yaml
            if yaml.safe_load(old_field) != {'categories': before}:
                raise ValueError('Category source field differs from planned values')
            if '\r\n' in source:
                old_field = old_field.replace('\r\n', '\n').replace('\n', '\r\n')
            new_field = 'categories: ' + json.dumps(after, ensure_ascii=False)
            fm = protected_material(source)[0]
            if fm.count(old_field) != 1:
                raise ValueError('Category field does not match reviewed plan')
            updated = updated.replace(old_field, new_field, 1)
            comparison_source = comparison_source.replace(old_field, new_field, 1)
        repairs = []
        for old_edge in item.get('mermaid_edge_labels', []):
            match = re.fullmatch(r'( +)([A-Za-z][A-Za-z0-9_]*) -->\|([^|"\r\n]+)\| ([A-Za-z][A-Za-z0-9_]*)', old_edge)
            if not match or source.count(old_edge) != 1:
                raise ValueError('Invalid reviewed Mermaid edge')
            if not any(old_edge in block for block in re.findall(r'(?ms)^```mermaid\r?\n.*?^```', source)):
                raise ValueError('Reviewed edge is not in a Mermaid fence')
            new_edge = f'{match[1]}{match[2]} -- "{match[3]}" --> {match[4]}'
            updated = updated.replace(old_edge, new_edge, 1)
            comparison_source = comparison_source.replace(old_edge, new_edge, 1)
            repairs.append({'before': old_edge, 'after': new_edge})
        strip = lambda value: SIMPLE_LINK.sub(lambda m: m[1], value)
        if strip(comparison_source) != strip(updated) or protected_material(comparison_source) != protected_material(updated):
            raise ValueError(f'Non-link content changed: {path}')
        if re.findall(r'</?[A-Za-z][^>]*>', source) != re.findall(r'</?[A-Za-z][^>]*>', updated):
            raise ValueError('HTML markup changed')
        if '\r\n' in source and '\n' in updated.replace('\r\n', ''):
            raise ValueError('Line ending change')
        changes.append((path, raw, updated.encode('utf-8')))
        report.append({'path': item['path'], 'removed_self_links': removed, 'added_links': added,
                       'protected_content_unchanged': not bool(repairs), 'visible_source_unchanged': not bool(repairs),
                       'prose_unchanged': True, 'protected_content_unchanged_except_reviewed_repairs': True,
                       'mermaid_label_repairs': repairs,
                       'reviewed_unwrapped_links': unwrapped,
                       'heading_link_repairs': heading_repairs,
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
