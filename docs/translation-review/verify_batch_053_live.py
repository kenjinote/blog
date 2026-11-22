"""Verify acoustic-levitation article pages after the successful Pages deployment."""
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
BUNDLE = ROOT / 'content/post/acoustic-levitation-standing-waves-radiation-force-ultrasonic-physics'
LANGS = ['ja', 'en', 'zh-cn', 'es', 'ko', 'pt', 'zh-tw', 'hi', 'fr', 'de', 'ar', 'ru', 'id']
SOURCES = [
    'https://cir.nii.ac.jp/crid/1570291226443959680',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC10716583/',
    'https://doi.org/10.1017/jfm.2024.523',
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
    path = BUNDLE / ('index.ja.md' if lang == 'ja' else f'index.{lang}.md')
    text = path.read_text(encoding='utf-8')
    fields = {}
    for name in ('title', 'slug', 'description'):
        match = re.search(rf'^{name}:\s*(.*?)\s*$', text, re.M)
        if not match:
            raise SystemExit(f'Missing {name} in {path}')
        fields[name] = json.loads(match.group(1))
    return fields

parser = argparse.ArgumentParser()
parser.add_argument('--ci-run', required=True, type=int)
parser.add_argument('--commit', required=True)
args = parser.parse_args()
request = urllib.request.Request(
    f'https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}',
    headers={'User-Agent': 'kenji.blog-translation-review/1.0', 'Accept': 'application/vnd.github+json'},
)
try:
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
        page = response.read().decode('utf-8', 'replace')
    if '<span class="h4 color-fg-default">Success</span>' not in page or args.commit[:7] not in page:
        raise SystemExit('GitHub run page does not confirm success for the specified commit')

slug = metadata('ja')['slug'].lower()
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
            'originalDate': '2026-10-14' in raw,
            'lastmod': '2026-11-23' in raw,
            'bibliography': all(source in page.links for source in SOURCES),
            'oldForceCoefficientAbsent': '5/6' not in visible and r'\frac{5}{6}' not in raw,
            'correctedForceCoefficientPresent': '5/2' in visible or r'\frac{5}{2}' in raw or r'\left( \frac{5}{2} \right)' in raw,
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
    'scope': 'Batch 053 acoustic-levitation Japanese source plus twelve translations; live HTTP validates title/description, canonical, language/RTL, dates, four primary references, corrected 5/2 force coefficient, absence of 5/6 and hreflang targets.',
    'pages': records,
    'limitations': ['AI review only; no human/native-speaker certification.', 'No experimental replication or device-specific measurement was performed.', 'No rendered browser/device visual QA was performed.'],
}
(DOCS / 'publication-053.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
if passed:
    batch_path = DOCS / 'batch-053.json'
    batch = json.loads(batch_path.read_text(encoding='utf-8'))
    batch['publicationPending'] = False
    batch['publication'] = {'record': 'docs/translation-review/publication-053.json', 'ciRun': args.ci_run, 'deployedCommit': args.commit, 'allPassed': True}
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'allPassed': passed, 'pages': len(records), 'failures': [record for record in records if not record['passed']]}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
