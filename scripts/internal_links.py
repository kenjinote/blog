"""Conservative, source-preserving internal links for Hugo. Python 3.10+."""
from __future__ import annotations

import argparse
import csv
import difflib
import io
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit, quote, unquote, urlunsplit

ROOT = Path(__file__).resolve().parents[1]


def protected_ranges(text: str, protect_paragraphs: bool = True) -> list[tuple[int, int]]:
    """Protect uncertain syntax rather than try to repair or reserialize Markdown."""
    ranges = []
    fm = re.match(r'\ufeff?(---|\+\+\+)\r?\n', text)
    if not fm:
        return [(0, len(text))]
    end = re.search(r'(?m)^' + re.escape(fm[1]) + r'\s*\r?$', text[fm.end():])
    if not end:
        return [(0, len(text))]
    body = fm.end() + end.end()
    ranges.append((0, body))
    # Paired HTML/shortcodes can span paragraphs. Leave such documents untouched.
    if re.search(r'<[A-Za-z/!]|\{\{[<%]', text[body:]):
        return [(0, len(text))]
    fence = None
    offset = body
    for line in text[body:].splitlines(keepends=True):
        # Also recognize fences nested inside lists/quotes; overprotection is safe.
        marker = re.match(r'^[\s>]*(?:[-+*]|\d+[.)])?\s*(`{3,}|~{3,})(.*)', line)
        if fence:
            ranges.append((offset, offset + len(line)))
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
        elif marker:
            fence = (marker[1][0], len(marker[1]))
            ranges.append((offset, offset + len(line)))
        offset += len(line)
    # Headings (anchors/TOC), indented code, quote continuations, references and
    # attributes: skip the whole paragraph, including lazy continuation lines.
    for block in re.finditer(r'[^\r\n].*?(?=\r?\n[ \t]*\r?\n|\Z)', text[body:], re.S):
        if not protect_paragraphs:
            # URL localization may include headings but still excludes code and
            # reference definitions, whose URL syntax is different.
            if re.search(r'(?m)^(?: {4}|\t| {0,3}\[[^\]\r\n]+\]:)', block[0]):
                ranges.append((body + block.start(), body + block.end()))
            continue
        if re.search(r'(?m)^(?: {4}|\t| {0,3}(?:#{1,6}(?:\s|$)|>|\[[^\]\r\n]+\]:|\{|(?:=+|-+)\s*$))', block[0]):
            ranges.append((body + block.start(), body + block.end()))
    return ranges


def balanced_end(text: str, start: int, left: str, right: str) -> int:
    depth, i = 1, start + 1
    while i < len(text):
        if text[i] == '\\':
            i += 2
            continue
        if text[i] == '`' or (left == '(' and text[i] in '\"\''):
            delimiter = re.match(r'`+', text[i:])[0] if text[i] == '`' else text[i]
            stop = text.find(delimiter, i + len(delimiter))
            if stop < 0:
                return len(text)
            i = stop + len(delimiter)
            continue
        if text[i] == left:
            depth += 1
        elif text[i] == right:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return len(text)


def word_character(char: str) -> bool:
    """CJK words accept attached particles; other scripts need word boundaries."""
    code = ord(char)
    if 0x3040 <= code <= 0x30ff or 0x3400 <= code <= 0x9fff or 0xac00 <= code <= 0xd7af or 0x20000 <= code <= 0x3134f:
        return False
    return char == '_' or unicodedata.category(char)[0] in 'LNM'


def link_text(text: str, keywords: dict[str, str], localizer=None) -> tuple[str, int]:
    """One pass over original source; never run replacements on generated links."""
    if not keywords and not localizer:
        return text, 0
    protected = bytearray(len(text))
    for start, end in protected_ranges(text, protect_paragraphs=localizer is None):
        protected[start:end] = b'\1' * (end - start)
    destinations = {key.casefold(): value for key, value in keywords.items()}
    # Acronyms such as RAM/WHO/TODO must not match ordinary lowercase words.
    alternatives = [('(?-i:' + re.escape(k) + ')') if re.fullmatch(r'[A-Z][A-Z0-9]{2,7}', k) else re.escape(k)
                    for k in sorted(keywords, key=len, reverse=True)]
    pattern = re.compile('|'.join(alternatives), re.IGNORECASE) if keywords else None
    output, count, i = [], 0, 0
    while i < len(text):
        end = i + 1
        if protected[i]:
            while end < len(text) and protected[end]:
                end += 1
        elif text.startswith(('\\(', '\\['), i) or text[i] in '$`':
            if text[i] == '\\':
                opening, closing = text[i:i+2], '\\)' if text[i+1] == '(' else '\\]'
            else:
                opening = re.match(re.escape(text[i]) + '+', text[i:])[0]
                closing = opening
            # Exact delimiter runs; an unmatched delimiter protects the remainder.
            close = re.compile(r'(?<![\\' + re.escape(closing[-1]) + '])' + re.escape(closing) + r'(?!' + re.escape(closing[-1]) + ')')
            match = close.search(text, i + len(opening))
            end = match.end() if match else len(text)
        elif text[i] == '\\':
            end = min(i + 2, len(text))
        elif text[i] == '[' or text.startswith('![', i):
            end = balanced_end(text, i + (text[i] == '!'), '[', ']')
            following = re.match(r'\s*([\[(])', text[end:])
            if following:
                start = end + following.end() - 1
                end = balanced_end(text, start, text[start], ']' if text[start] == '[' else ')')
                if localizer and text[i] != '!' and text[start] == '(' and text[end-1:end] == ')':
                    destination = re.match(r'\(\s*(<?)([^\s<>]+?)(>?)(?=\s|\))', text[start:end])
                    if destination and destination[1] == ('<' if destination[3] else ''):
                        url = destination[2]
                        # Parenthesized/escaped URLs require a fuller parser.
                        if not re.search(r'[()\\]', url):
                            replacement = localizer(url)
                            if replacement != url:
                                a, b = start + destination.start(2), start + destination.end(2)
                                output.append(text[i:a] + replacement + text[b:end])
                                count += 1
                                i = end
                                continue
        elif text[i] == '{':
            end = balanced_end(text, i, '{', '}')
        elif re.match(r'(?:https?://|www\.|mailto:)', text[i:i+10]):
            end = i + len(re.match(r'\S+', text[i:])[0])
        elif text[i] == '&' and re.match(r'&(?:#\d+|#x[0-9a-fA-F]+|[A-Za-z]+);', text[i:]):
            end = i + len(re.match(r'&[^;]+;', text[i:])[0])
        else:
            match = pattern.match(text, i) if pattern else None
            if match and not any(protected[i:match.end()]):
                keyword = match[0]
                left_ok = not (word_character(keyword[0]) and i and word_character(text[i-1]))
                right_ok = not (word_character(keyword[-1]) and match.end() < len(text) and word_character(text[match.end()]))
                destination = destinations.get(keyword.casefold())
                if left_ok and right_ok and destination:
                    output.append(f'[{keyword}]({destination})')
                    count += 1
                    i = match.end()
                    continue
        output.append(text[i:end])
        i = end
    return ''.join(output), count


def language(path: Path) -> str:
    parts = path.name.split('.')
    return 'ja' if len(parts) == 2 else parts[-2]


def valid_keyword(keyword):
    return (isinstance(keyword, str) and len(keyword.strip()) >= 2 and keyword == keyword.strip()
            and not re.search(r'[\[\]\\`$<>\r\n*{}|]', keyword.replace('A*', 'A'))
            and not re.search(r'(?<!\w)_|_(?!\w)', keyword))


def localizers(published):
    """Resolve translated siblings by source bundle, never by invented URL paths."""
    routes, bundles = {}, {}
    for path, row in published.items():
        if row['kind'] != 'page' or not path.is_relative_to(ROOT / 'content/post'):
            continue
        url = urlsplit(row['permalink'])
        routes[unquote(url.path)] = path
        bundles.setdefault(path.parent, {})[language(path)] = url.path
    hosts = {urlsplit(row['permalink']).netloc for row in published.values()}

    def for_language(lang):
        def localize(value):
            url = urlsplit(value)
            if (url.netloc and url.netloc not in hosts) or url.scheme not in ('', 'http', 'https') or not url.path.startswith('/'):
                return value
            path = routes.get(unquote(url.path))
            if not path or language(path) == lang:
                return value
            target = bundles[path.parent].get(lang)
            if not target:
                return value
            return urlunsplit((url.scheme, url.netloc, quote(unquote(target), safe='/-%._~'), url.query, url.fragment))
        return localize
    return for_language


def load_rules(config: Path, root: Path, published: dict) -> dict:
    data = json.loads(config.read_text(encoding='utf-8-sig'))
    if data.get('version') != 1 or not isinstance(data.get('articles'), list):
        raise ValueError('設定には version: 1 と articles 配列が必要です')
    result = {}
    for entry in data['articles']:
        target = (root / entry['article']).resolve()
        if not target.is_relative_to(root / 'content' / 'post') or not target.is_file():
            raise ValueError(f'記事が存在しないか対象外です: {target}')
        row = published.get(target)
        if not row or row['kind'] != 'page':
            raise ValueError(f'Hugo の公開対象にリンク先がありません: {target}')
        url = urlsplit(row['permalink'])
        if url.scheme not in ('http', 'https') or not url.netloc or not url.path.startswith('/'):
            raise ValueError(f'無効な公開URL: {row["permalink"]}')
        destination = quote(url.path, safe='/-%._~')
        lang = language(target)
        rules = result.setdefault(lang, {})
        if not isinstance(entry['keywords'], list) or not entry['keywords']:
            raise ValueError('keywords は空でない配列にしてください')
        for keyword in entry['keywords']:
            if not valid_keyword(keyword):
                raise ValueError(f'キーワードには2文字以上の通常の文言を指定してください: {keyword!r}')
            if keyword.casefold() in {key.casefold() for key in rules}:
                raise ValueError(f'同じ言語のキーワードが重複しています: {keyword}')
            rules[keyword] = (target, destination)
    return result


def published_pages() -> dict:
    process = subprocess.run(['hugo', 'list', 'published'], cwd=ROOT, capture_output=True, encoding='utf-8', check=True)
    rows = list(csv.DictReader(io.StringIO(process.stdout)))
    if not rows or not {'path', 'permalink', 'kind'} <= rows[0].keys():
        raise ValueError('hugo list published のCSVを読み取れませんでした')
    return {(ROOT / row['path']).resolve(): row for row in rows}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=ROOT / 'scripts/internal-links.json')
    parser.add_argument('--write', action='store_true', help='実際にファイルを書き換える（既定は差分表示のみ）')
    parser.add_argument('--generated', type=Path, default=ROOT / 'scripts/internal-links.generated.json')
    parser.add_argument('--quiet', action='store_true', help='記事ごとのdiffを省略し集計だけ表示')
    parser.add_argument('--report', type=Path, help='言語別・記事別の処理結果をJSONに保存')
    parser.add_argument('--localize-existing', action='store_true', help='既存リンクも公開済みの同じ言語の対応記事へ修正')
    args = parser.parse_args()
    published = published_pages()
    rules = load_rules(args.generated, ROOT, published) if args.generated.exists() else {}
    for lang, manual in load_rules(args.config, ROOT, published).items():
        overrides = {key.casefold() for key in manual}
        rules[lang] = {key: value for key, value in rules.get(lang, {}).items() if key.casefold() not in overrides}
        rules[lang].update(manual)
    changes = []
    scanned, protected_files, changed_files, link_counts, localized_counts = Counter(), Counter(), Counter(), Counter(), Counter()
    localizer_for = localizers(published)
    article_results = []
    skipped_articles = []
    for path in sorted((ROOT / 'content/post').rglob('*.md')):
        resolved = path.resolve()
        if resolved not in published:
            continue
        lang = language(path)
        scanned[lang] += 1
        if sum(scanned.values()) % 1000 == 0:
            print(f'Scanned {sum(scanned.values())} articles...', file=sys.stderr, flush=True)
        original = path.read_bytes()
        source = original.decode('utf-8')
        if protected_ranges(source) == [(0, len(source))]:
            protected_files[lang] += 1
            skipped_articles.append({'article': path.relative_to(ROOT).as_posix(),
                                     'reason': 'HTML/shortcode or missing/unclosed frontmatter'})
            continue
        localize = localizer_for(lang)
        needs_localization = args.localize_existing and any(
            localize(match[1]) != match[1]
            for match in re.finditer(r'\]\(\s*<?((?:https?://|/)[^\s<>)]+)', source))
        localized, localized_count = link_text(source, {}, localize) if needs_localization else (source, 0)
        folded = localized.casefold()
        keywords = {k: url for k, (target, url) in rules.get(lang, {}).items() if target != resolved and k.casefold() in folded}
        updated, count = link_text(localized, keywords)
        if updated == source:
            continue
        verified, _ = link_text(updated, {}, localize) if localized_count else (updated, 0)
        if link_text(verified, keywords)[0] != updated:
            raise ValueError(f'再実行時の安全性検証に失敗: {path}')
        changes.append((path, original, updated.encode('utf-8'), count))
        changed_files[lang] += 1
        link_counts[lang] += count
        localized_counts[lang] += localized_count
        name = path.relative_to(ROOT).as_posix()
        article_results.append({'article': name, 'added_links': count, 'localized_links': localized_count})
        if not args.quiet:
            sys.stdout.writelines(difflib.unified_diff(source.splitlines(True), updated.splitlines(True), fromfile=name, tofile=name))
    # Validate every change before the first write, preserving encoding/newlines.
    if args.write:
        for path, original, _, _ in changes:
            if path.read_bytes() != original:
                raise ValueError(f'実行中に記事が更新されました: {path}')
        for path, _, updated, _ in changes:
            path.write_bytes(updated)
    print(f'\n{"更新" if args.write else "変更予定"}: {len(changes)} 記事 / {sum(c[3] for c in changes)} 追加リンク / {sum(localized_counts.values())} 言語修正')
    report = {'mode': 'write' if args.write else 'dry-run', 'scanned': sum(scanned.values()),
              'changed_articles': len(changes), 'added_links': sum(link_counts.values()), 'localized_links': sum(localized_counts.values()),
              'languages': {lang: {'scanned': scanned[lang], 'protected_articles': protected_files[lang],
                                   'changed_articles': changed_files[lang], 'added_links': link_counts[lang], 'localized_links': localized_counts[lang]}
                            for lang in sorted(scanned)},
              'articles': article_results, 'protected_articles': skipped_articles}
    print(json.dumps(report['languages'], ensure_ascii=False))
    if args.report:
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print(f'エラー: {error}', file=sys.stderr)
        raise SystemExit(1)
