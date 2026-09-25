"""Repair unparsed plain-text strong emphasis, with exact Hugo HTML validation.

Dry run by default. Never reserialize Markdown or change renderer settings.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import tempfile
import unicodedata
from collections import Counter
from pathlib import Path

from internal_links import ROOT, balanced_end, protected_ranges


def punctuation(char):
    return bool(char) and (unicodedata.category(char)[0] in 'PS')


def flanking(before, after):
    bw, aw = not before or before.isspace(), not after or after.isspace()
    return (not aw and (not punctuation(after) or bw or punctuation(before)),
            not bw and (not punctuation(before) or aw or punctuation(after)))


def candidates(text):
    protected = bytearray(len(text))
    for a, b in protected_ranges(text):
        protected[a:b] = b'\1' * (b-a)
    i = 0
    while i < len(text):
        if protected[i]:
            i += 1
            continue
        end = i + 1
        if text.startswith(('\\(', '\\['), i) or text[i] in '$`':
            if text[i] == '\\':
                opening = text[i:i+2]
                closing = '\\)' if opening == '\\(' else '\\]'
            else:
                opening = re.match(re.escape(text[i]) + '+', text[i:])[0]
                closing = opening
            match = re.search(r'(?<![\\' + re.escape(closing[-1]) + '])'
                              + re.escape(closing) + r'(?!' + re.escape(closing[-1]) + ')',
                              text[i+len(opening):])
            end = i + len(opening) + match.end() if match else len(text)
        elif text[i] == '\\':
            end = min(i+2, len(text))
        elif text[i] == '[' or text.startswith('![', i):
            end = balanced_end(text, i + (text[i] == '!'), '[', ']')
            following = re.match(r'\s*([\[(])', text[end:])
            if following:
                start = end + following.end() - 1
                end = balanced_end(text, start, text[start], ']' if text[start] == '[' else ')')
        elif text[i] == '{':
            end = balanced_end(text, i, '{', '}')
        if end > i+1:
            protected[i:end] = b'\1' * (end-i)
        i = end
    found = []
    # Deliberately exclude nested Markdown, entities, multiline spans and escapes.
    for match in re.finditer(r'(?<!\*)\*\*([^*\r\n]+)\*\*(?!\*)', text):
        a, b = match.span()
        value = match[1]
        if any(protected[a:b]) or value != value.strip() or re.search(r'[\[\]<>`$\\_&{}]', value):
            continue
        opening, _ = flanking(text[a-1:a] if a else '', value[0])
        _, closing = flanking(value[-1], text[b:b+1])
        if not opening or not closing:
            found.append((a, b, value))
    return found


def replace(text, spans):
    for a, b, value in reversed(spans):
        text = text[:a] + '<strong>' + value + '</strong>' + text[b:]
    return text


def body(text):
    match = re.match(r'\ufeff?(---|\+\+\+)\r?\n', text)
    closing = re.search(r'(?m)^' + re.escape(match[1]) + r'[ \t]*\r?$', text[match.end():])
    return text[match.end()+closing.end():]


def run_hugo(args):
    result = subprocess.run(['hugo', *args], cwd=ROOT, capture_output=True, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(result.stderr + result.stdout)
    return result.stdout


def validate(pages, retry=True):
    """Render both versions; accept only the exact expected strong-tag changes."""
    config = json.loads(run_hugo(['config', '--format', 'json']))
    if not config['markup']['goldmark']['renderer']['unsafe']:
        raise RuntimeError('This repair requires the existing unsafe=true renderer setting.')
    accepted, rejected = [], []
    with tempfile.TemporaryDirectory(prefix='kenji-emphasis-') as directory:
        root = Path(directory)
        (root/'content').mkdir()
        (root/'layouts/_default').mkdir(parents=True)
        (root/'layouts/_default/single.html').write_text('{{ .Content }}', encoding='utf-8')
        (root/'hugo.json').write_text(json.dumps({'markup': config['markup'],
            'disableKinds': ['home', 'taxonomy', 'term', 'RSS', 'sitemap']}), encoding='utf-8')
        for index, (_, original, updated, _) in enumerate(pages):
            for version, value in [('before', original), ('after', updated)]:
                (root/'content'/f'{index}-{version}.md').write_bytes(
                    ('---\ntitle: test\n---\n' + body(value)).encode('utf-8'))
        if not pages:
            return accepted, rejected
        run_hugo(['--source', str(root), '--quiet'])
        for index, page in enumerate(pages):
            before = (root/'public'/f'{index}-before/index.html').read_bytes()
            after = (root/'public'/f'{index}-after/index.html').read_bytes()
            expected = before
            valid = True
            for value, count in Counter(span[2] for span in page[3]).items():
                escaped = html.escape(value, quote=False).encode('utf-8')
                needle = b'**' + escaped + b'**'
                # Ambiguous duplicates, nested markup, or renderer transformations: skip.
                if expected.count(needle) != count:
                    valid = False
                    break
                expected = expected.replace(needle, b'<strong>' + escaped + b'</strong>')
            (accepted if valid and expected == after else rejected).append(page)
    # One ambiguous span must not prevent independent safe repairs on that page.
    if retry and any(len(p[3]) > 1 for p in rejected):
        singles = [(p, old, replace(old, [span]), [span])
                   for p, old, _, spans in rejected for span in spans]
        safe, _ = validate(singles, retry=False)
        by_path = {}
        for p, old, _, spans in safe:
            by_path.setdefault(p, (old, []))[1].extend(spans)
        combined = [(p, old, replace(old, sorted(spans)), sorted(spans))
                    for p, (old, spans) in by_path.items()]
        extra, _ = validate(combined, retry=False)
        accepted.extend(extra)
        counts = {p: len(spans) for p, _, _, spans in extra}
        rejected = [page for page in rejected if counts.get(page[0], 0) < len(page[3])]
    return accepted, rejected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--report', type=Path, default=ROOT/'docs/emphasis-report.json')
    args = parser.parse_args()
    pages, scanned = [], 0
    # Freeze the inventory and snapshot source bytes; do not overwrite concurrent edits.
    for path in sorted((ROOT/'content/post').glob('*/index*.md')):
        scanned += 1
        text = path.read_bytes().decode('utf-8')
        spans = candidates(text)
        if spans:
            pages.append((path, text, replace(text, spans), spans))
    accepted, rejected = validate(pages)
    for path, original, _, _ in accepted:
        if path.read_bytes() != original.encode('utf-8'):
            raise RuntimeError(f'Concurrent edit detected; no files written: {path}')
    if args.write:
        for path, _, updated, _ in accepted:
            path.write_bytes(updated.encode('utf-8'))
    report = {'mode': 'write' if args.write else 'dry-run', 'scanned': scanned,
              'changed_articles': len(accepted), 'replacements': sum(len(p[3]) for p in accepted),
              'validation': 'Exact rendered HTML equality except the listed strong emphasis',
              'articles': [{'path': p.relative_to(ROOT).as_posix(),
                            'changes': [{'line': original[:a].count('\n')+1, 'text': value}
                                        for a, _, value in spans]}
                           for p, original, _, spans in accepted],
              'skipped_render_mismatch': [p.relative_to(ROOT).as_posix() for p, *_ in rejected]}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k not in ('articles', 'skipped_render_mismatch')}, ensure_ascii=False))
    print(f'Skipped ambiguous renderings: {len(rejected)}')


if __name__ == '__main__':
    main()
