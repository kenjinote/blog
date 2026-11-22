"""Verify all Nanakusa-gayu pages after a successful Pages deployment."""
from datetime import datetime, timedelta, timezone
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote
import argparse
import json
import re
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / 'docs/translation-review'
BUNDLE = ROOT / 'content/post/七草粥のレシピ'
LANGS = ['ja', 'en', 'zh-cn', 'es', 'ko', 'pt', 'zh-tw', 'hi', 'fr', 'de', 'ar', 'ru', 'id']
REQUIRED_LINKS = [
    'maff.go.jp', 'kinki.env.go.jp', 'sirogohan.com/recipe/nanakusa/',
    'powo.science.kew.org/taxon/urn:lsid:ipni.org:names:981300-1',
]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = ''
        self.direction = ''
        self.canonical = []
        self.hreflang = {}
        self.links = []
        self.text = []
        self.title = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.lang, self.direction = a.get('lang', ''), a.get('dir', '')
        if tag == 'link' and 'canonical' in a.get('rel', '').split():
            self.canonical.append(a.get('href', ''))
        if tag == 'link' and a.get('hreflang'):
            self.hreflang[a['hreflang']] = a.get('href', '')
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.title.append(data)


def metadata(lang):
    path = BUNDLE / ('index.md' if lang == 'ja' else f'index.{lang}.md')
    text = path.read_text(encoding='utf-8')
    def field(name):
        raw = re.search(rf'^{name}:\s*(.*?)\s*$', text, re.M).group(1)
        return json.loads(raw) if raw.startswith('"') else raw.strip('"')
    return field('title'), field('slug')


parser = argparse.ArgumentParser()
parser.add_argument('--ci-run', required=True, type=int)
parser.add_argument('--commit', required=True)
args = parser.parse_args()
try:
    req = urllib.request.Request(
        f'https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}',
        headers={'User-Agent': 'kenji.blog-translation-review/1.0', 'Accept': 'application/vnd.github+json'},
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        run = json.load(response)
    if run.get('conclusion') != 'success' or not run.get('head_sha', '').startswith(args.commit):
        raise SystemExit('CI run is not successful for the specified commit')
except urllib.error.HTTPError as error:
    if error.code != 403:
        raise
    req = urllib.request.Request(
        f'https://github.com/kenjinote/blog/actions/runs/{args.ci_run}?review_check=1',
        headers={'User-Agent': 'Mozilla/5.0 kenji.blog-translation-review/1.0'},
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        page = response.read().decode('utf-8', 'replace')
    if '<span class="h4 color-fg-default">Success</span>' not in page or args.commit[:7] not in page:
        raise SystemExit('GitHub run page does not confirm success for the specified commit')

_, slug = metadata('ja')
ja_url = 'https://kenji.blog/p/' + quote(slug, safe='') + '/'
request = urllib.request.Request(ja_url, headers={'User-Agent': 'kenji.blog-translation-review/1.0'})
with urllib.request.urlopen(request, timeout=30) as response:
    root = Page()
    root.feed(response.read().decode('utf-8', 'replace'))
expected = set(root.hreflang.values())
if len(expected) != 13 or len(root.hreflang) != 14:
    raise SystemExit('Japanese page does not expose the expected 13 hreflang targets')

records = []
for lang in LANGS:
    url = next((u for u in expected if (lang == 'ja' and re.search(r'https://kenji\.blog/p/', u)) or (lang != 'ja' and f'/{lang}/p/' in u)), None)
    if not url:
        raise SystemExit(f'Missing hreflang URL for {lang}')
    title, _ = metadata(lang)
    request = urllib.request.Request(url, headers={'User-Agent': 'kenji.blog-translation-review/1.0'})
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read().decode('utf-8', 'replace')
        page = Page()
        page.feed(raw)
        visible = unescape(' '.join(page.text))
        links = '\n'.join(page.links)
        checks = {
            'http200': response.status == 200,
            'canonical': page.canonical == [url],
            'language': page.lang == lang,
            'arabicRtl': lang != 'ar' or page.direction == 'rtl',
            'title': title in ''.join(page.title),
            'originalDate': '2024-01-06' in raw,
            'lastmod': '2026-11-23' in raw,
            'botanicalIdentity': 'Lapsanastrum apogonoides' in visible,
            'recipeQuantities': '75' in visible and '600' in visible,
            'sourceLinks': all(target in links for target in REQUIRED_LINKS),
            'noJavaArticleLink': not re.search(r'(?:oracle\.com/java|/java(?:/|"|$)|/category/java)', links, re.I),
            'hreflangCount': len(page.hreflang) == 14,
            'hreflangTargets': set(page.hreflang.values()) == expected,
        }
        records.append({'language': lang, 'url': url, 'status': response.status, 'checks': checks, 'passed': all(checks.values())})

passed = len(records) == 13 and all(record['passed'] for record in records)
receipt = {
    'version': 1,
    'checkedAt': datetime.now(timezone(timedelta(hours=9))).isoformat(),
    'ciRun': args.ci_run,
    'ciUrl': f'https://github.com/kenjinote/blog/actions/runs/{args.ci_run}',
    'deployedCommit': args.commit,
    'allPassed': passed,
    'scope': 'Batch 049 Nanakusa-gayu Japanese source plus twelve translations; live HTTP validates canonical, language/RTL, title, publication/update dates, botanical identity, recipe quantities, four source links, removed unrelated Java links, and hreflang targets.',
    'pages': records,
    'limitations': ['AI review only; no human/native-speaker certification.', 'The recipe was not cooked or taste-tested.', 'No rendered browser/device visual QA was performed.'],
}
(DOCS / 'publication-049.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
if passed:
    batch_path = DOCS / 'batch-049.json'
    batch = json.loads(batch_path.read_text(encoding='utf-8'))
    batch['publicationPending'] = False
    batch['publication'] = {'record': 'docs/translation-review/publication-049.json', 'ciRun': args.ci_run, 'deployedCommit': args.commit, 'allPassed': True}
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'allPassed': passed, 'pages': len(records), 'failures': [record for record in records if not record['passed']]}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
