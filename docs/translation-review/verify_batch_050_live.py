"""Verify the Hugo raw-HTML configuration article after Pages deployment."""
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
BUNDLE = ROOT / 'content/post/HUGOでHTMLタグを使う'
LANGS = ['ja', 'en', 'zh-cn', 'es', 'ko', 'pt', 'zh-tw', 'hi', 'fr', 'de', 'ar', 'ru', 'id']
SOURCES = ['https://gohugo.io/configuration/markup/', 'https://gohugo.io/about/security/']
WARNINGS = {
    'ja': '信頼できない投稿者', 'en': 'untrusted contributors', 'de': 'nicht vertrauenswürdigen',
    'es': 'no confiables', 'fr': 'non fiables', 'hi': 'अविश्वसनीय', 'id': 'tidak tepercaya',
    'ko': '신뢰할 수 없는', 'pt': 'não confiáveis', 'ru': 'ненадёжных', 'ar': 'غير موثوق',
    'zh-cn': '不可信贡献者', 'zh-tw': '不可信投稿者',
}


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
        self.descriptions = []
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
        if tag == 'meta' and a.get('name', '').lower() == 'description':
            self.descriptions.append(a.get('content', ''))
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
    fields = {}
    for name in ('title', 'slug', 'description'):
        raw = re.search(rf'^{name}:\s*(.*?)\s*$', text, re.M).group(1)
        fields[name] = json.loads(raw)
    return fields


parser = argparse.ArgumentParser()
parser.add_argument('--ci-run', required=True, type=int)
parser.add_argument('--commit', required=True)
args = parser.parse_args()
try:
    request = urllib.request.Request(
        f'https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}',
        headers={'User-Agent': 'kenji.blog-translation-review/1.0', 'Accept': 'application/vnd.github+json'},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        run = json.load(response)
    if run.get('conclusion') != 'success' or not run.get('head_sha', '').startswith(args.commit):
        raise SystemExit('CI run is not successful for the specified commit')
except urllib.error.HTTPError as error:
    if error.code != 403:
        raise
    request = urllib.request.Request(
        f'https://github.com/kenjinote/blog/actions/runs/{args.ci_run}?review_check=1',
        headers={'User-Agent': 'Mozilla/5.0 kenji.blog-translation-review/1.0'},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        ci_page = response.read().decode('utf-8', 'replace')
    if '<span class="h4 color-fg-default">Success</span>' not in ci_page or args.commit[:7] not in ci_page:
        raise SystemExit('GitHub run page does not confirm success for the specified commit')

slug = metadata('ja')['slug']
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
    meta = metadata(lang)
    request = urllib.request.Request(url, headers={'User-Agent': 'kenji.blog-translation-review/1.0'})
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read().decode('utf-8', 'replace')
        page = Page()
        page.feed(raw)
        visible = unescape(' '.join(page.text))
        checks = {
            'http200': response.status == 200,
            'canonical': page.canonical == [url],
            'language': page.lang == lang,
            'arabicRtl': lang != 'ar' or page.direction == 'rtl',
            'title': meta['title'] in ''.join(page.title),
            'description': len(page.descriptions) == 1 and unescape(page.descriptions[0]) == meta['description'],
            'originalDate': '2023-01-17' in raw,
            'lastmod': '2026-11-23' in raw,
            'yamlTomlJsonExamples': all(term in visible for term in ('markup', 'goldmark', 'renderer', 'unsafe: true', '[markup.goldmark.renderer]', '"unsafe": true')),
            'defaultFalse': 'false' in visible,
            'securityWarning': WARNINGS[lang].lower() in visible.lower(),
            'officialReferences': all(source in page.links for source in SOURCES),
            'oldDocumentationUrlAbsent': 'getting-started/configuration-markup' not in raw,
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
    'scope': 'Batch 050 Hugo raw-HTML article Japanese source plus twelve translations; live HTTP validates title/description, canonical, language/RTL, dates, YAML/TOML/JSON setting snippets, default false, localized untrusted-content warning, current Hugo references, and hreflang targets.',
    'pages': records,
    'limitations': ['AI review only; no human/native-speaker certification.', 'No security audit or cross-version Hugo runtime test was performed.', 'No rendered browser/device visual QA was performed.'],
}
(DOCS / 'publication-050.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
if passed:
    batch_path = DOCS / 'batch-050.json'
    batch = json.loads(batch_path.read_text(encoding='utf-8'))
    batch['publicationPending'] = False
    batch['publication'] = {'record': 'docs/translation-review/publication-050.json', 'ciRun': args.ci_run, 'deployedCommit': args.commit, 'allPassed': True}
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'allPassed': passed, 'pages': len(records), 'failures': [record for record in records if not record['passed']]}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
