"""Build a reviewable multilingual term dictionary from published Hugo articles."""
import json
import re
import argparse
from collections import defaultdict, Counter
from pathlib import Path

from internal_links import ROOT, language, published_pages, valid_keyword

# A tool mentioned in a how-to title is not the subject's general reference page.
# Keep the full title of such articles, without turning C++/CLI/UTC into aliases.
PROCEDURAL = re.compile(
    r'方法|手順|コマンド|使って|設定する|自動生成|一括削除|ツール開発|導入する|安装|安装|使用|指令|步骤|步驟|命令|설치|사용법|사용하여|명령|하는 방법|'
    r'\b(?:how to|steps? to|using|download|command|commands|comment |wie man |anleitung|cara |como |comando|comandos|cómo |pasos|как |команд|كيفية|خطوات|أوامر|باستخدام|कैसे|कमांड)\b',
    re.IGNORECASE)
GENERIC = {
    'easy', 'simple', 'introduction', 'overview', 'complete guide', 'path', 'cli', 'utc', 'c++', 'todo', 'tree', 'os史', '기업사',
    'history', 'histoire', 'geschichte', '歴史', '历史', '歷史', '人物伝', '传记', '傳記', 'biography', 'biographie', 'biografía', 'biografia', 'биография', 'история', '역사', '전기', 'تاريخ', 'سيرة', 'इतिहास', 'जीवनी', 'sejarah', 'biografi',
    'physics', 'physique', 'physik', 'física', 'fisica', 'физика', 'الفيزياء', 'भौतिकी', 'fisika', '물리학', '物理', '物理学', '物理學',
    'mathematics', 'mathématiques', 'mathematik', 'matemáticas', 'matemática', 'математика', 'गणित', 'الرياضيات', 'matematika', '수학', '数学', '數學',
}


def plain(text):
    text = re.sub(r'\[([^\]\n]+)\]\([^\n]+?\)', r'\1', text)
    return text.replace('**', '').strip()


def valid(term):
    return (3 <= len(term) <= 240 and valid_keyword(term)
            and any(c.isalpha() for c in term) and not term.isdigit())


def candidates(title, source):
    title = plain(title)
    # Editorial badges are not part of the topic (e.g. [Biography] Ada Lovelace).
    title = re.sub(r'^(?:\[[^\]]+\]|【[^】]+】)\s*(?=\S)', '', title)
    if title.startswith('[') and title.endswith(']'):
        title = title[1:-1]
    title = re.sub(r'\s*\[[^\]]+\]', '', title)
    title = title.strip()
    terms = {title}
    if PROCEDURAL.search(title):
        title = re.split(r'[|｜]', title, maxsplit=1)[0].strip()
        return [title] if valid(title) else []
    lead = re.split(r'[:：|｜]|\s[–—\-]\s', title, maxsplit=1)[0].strip()
    terms.add(lead)
    # Parenthetical translations/acronyms are only taken from the topic portion.
    topic = re.split(r'[（(]', lead, maxsplit=1)[0].strip()
    terms.add(topic)
    for alias in re.findall(r'[（(]([^()（）]+)[）)]', lead):
        if len(alias) >= 4 or re.fullmatch(r'[A-Z][A-Z0-9]{2,}', alias):
            terms.add(alias.strip())
    # Ignore headings; the first bold term in prose often gives the actual noun
    # without an editorial title prefix. Require evidence in the title itself.
    body = re.split(r'(?m)^---\s*$', source, maxsplit=2)
    if len(body) == 3:
        prose = '\n'.join(line for line in body[2].splitlines() if not line.startswith('#'))[:1800]
        bold = re.search(r'\*\*(.+?)\*\*', prose)
        if bold:
            term = plain(bold[1])
            if bold.start() < 80 and term.casefold() in lead.casefold():
                terms.add(term)
    # Drop common editorial affixes, only where the remaining noun is explicit.
    for term in list(terms):
        shortened = re.sub(r'(?:入門|の仕組み|の基礎|とは[？?]?|基础|入门|入門)$', '', term).strip()
        terms.add(shortened)
    return sorted(t for t in terms if valid(t) and (t == title or t.casefold() not in GENERIC))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory', type=Path, help='hugo list published の保存済みCSV')
    args = parser.parse_args()
    published = published_pages(args.inventory)
    pages = {path: row for path, row in published.items()
             if path.is_relative_to(ROOT / 'content/post') and row['kind'] == 'page' and path.suffix == '.md'}
    owners = defaultdict(set)
    per_page = {}
    for path, row in sorted(pages.items()):
        terms = candidates(row['title'], path.read_text(encoding='utf-8-sig'))
        per_page[path] = terms
        for term in terms:
            owners[(language(path), term.casefold())].add(path)
    articles, excluded, uncovered = [], [], []
    counts = Counter()
    for path, terms in per_page.items():
        unique = {}
        for term in terms:
            if len(owners[(language(path), term.casefold())]) == 1:
                unique.setdefault(term.casefold(), term)
        if unique:
            articles.append({'article': path.relative_to(ROOT).as_posix(), 'keywords': sorted(unique.values())})
            counts[language(path)] += len(unique)
        else:
            uncovered.append(path.relative_to(ROOT).as_posix())
    for (lang, term), targets in sorted(owners.items()):
        if len(targets) > 1:
            excluded.append({'language': lang, 'term': term, 'articles': sorted(p.relative_to(ROOT).as_posix() for p in targets)})
    output = ROOT / 'scripts/internal-links.generated.json'
    output.write_text(json.dumps({'version': 1, 'articles': articles}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    report = {'published_articles': len(pages), 'articles_with_terms': len(articles),
              'terms_by_language': dict(sorted(counts.items())),
              'ambiguous_terms': excluded, 'articles_without_safe_terms': uncovered}
    (ROOT / 'docs/internal-links-extraction-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k not in ('ambiguous_terms', 'articles_without_safe_terms')}, ensure_ascii=False))
    print(f'Ambiguous terms: {len(excluded)}; articles without safe terms: {len(uncovered)}')


if __name__ == '__main__':
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
