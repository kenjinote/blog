"""Verify Batch 042 pages after a successful GitHub Pages deploy."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from datetime import datetime, timezone, timedelta
import argparse, json, re, urllib.request

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / 'docs' / 'translation-review'
LANGS = ('ja', 'en', 'zh-cn', 'zh-tw', 'es', 'ko', 'pt', 'fr', 'de', 'hi', 'id', 'ar', 'ru')
BUNDLE = ROOT / 'content' / 'post' / 'AI画像生成ツールのローカル環境構築マニュアル'


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
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang', '')
            self.direction = attrs.get('dir', '')
        if tag == 'link' and 'canonical' in attrs.get('rel', '').split():
            self.canonical.append(attrs.get('href', ''))
        if tag == 'link' and attrs.get('hreflang'):
            self.hreflang[attrs['hreflang']] = attrs.get('href', '')
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.title.append(data)


def title_for(lang):
    source = BUNDLE / ('index.md' if lang == 'ja' else f'index.{lang}.md')
    match = re.search(r"^title:\s*['\"]?(.*?)['\"]?\s*$", source.read_text(encoding='utf8'), re.M)
    if not match:
        raise ValueError(f'Missing title in {source}')
    return unescape(match.group(1).replace("''", "'"))


parser = argparse.ArgumentParser()
parser.add_argument('--ci-run', required=True, type=int)
parser.add_argument('--commit', required=True, help='Full deployed Git commit SHA')
args = parser.parse_args()

request = urllib.request.Request(
    f'https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}',
    headers={'User-Agent': 'kenji.blog-translation-review/1.0', 'Accept': 'application/vnd.github+json'},
)
with urllib.request.urlopen(request, timeout=30) as response:
    run = json.load(response)
if run.get('conclusion') != 'success' or not run.get('head_sha', '').startswith(args.commit):
    raise SystemExit('Specified CI run is not a successful run for the deployed commit')

preview = json.loads((DOCS / 'batch-042-preview-validation.json').read_text(encoding='utf8'))
expected = {page['url'] for page in preview['pages']}
results = []
for lang in LANGS:
    url = f'https://kenji.blog/{"p/" if lang == "ja" else lang + "/p/"}local-ai-image-generation-setup/'
    request = urllib.request.Request(url, headers={'User-Agent': 'kenji.blog-translation-review/1.0'})
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode('utf8', 'replace')
        page = Page()
        page.feed(html)
        text = unescape(' '.join(page.text))
        checks = {
            'http200': response.status == 200,
            'finalUrl': response.geturl() == url,
            'canonical': page.canonical == [url],
            'language': page.lang == lang,
            'arabicRtl': lang != 'ar' or page.direction == 'rtl',
            'title': title_for(lang) in ''.join(page.title),
            'fullHreflang': len(page.hreflang) == 14 and set(page.hreflang.values()) == expected,
            'lastmod': '2026-11-23' in html,
            'correctionNote': all(term in text for term in ('ComfyUI', 'Fooocus', 'safetensors', 'ControlNet')),
            'officialLinks': all(
                any(host in link for link in page.links)
                for host in (
                    'docs.comfy.org/installation/comfyui_portable_windows',
                    'github.com/AUTOMATIC1111/stable-diffusion-webui',
                    'github.com/lllyasviel/Fooocus',
                    'docs.comfy.org/registry/claim-my-node',
                )
            ),
        }
        results.append({
            'language': lang,
            'url': url,
            'status': response.status,
            'lastModified': response.headers.get('Last-Modified'),
            'checks': checks,
            'passed': all(checks.values()),
        })

passed = len(results) == 13 and all(page['passed'] for page in results)
receipt = {
    'version': 1,
    'checkedAt': datetime.now(timezone(timedelta(hours=9))).isoformat(),
    'ciRun': args.ci_run,
    'ciUrl': f'https://github.com/kenjinote/blog/actions/runs/{args.ci_run}',
    'deployedCommit': args.commit,
    'allPassed': passed,
    'scope': 'Batch 042: Japanese article and all 12 translations. Live HTTP checks validate status, final URL, canonical, language, Arabic RTL, title, last modification, current correction note, official project links, and all 14 hreflang entries/targets.',
    'pages': results,
    'limitations': [
        'AI review only; no human/native-speaker certification.',
        'No GPU hardware or performance test.',
        'Browser/device visual QA was not performed.',
    ],
}
(DOCS / 'publication-042.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
if passed:
    batch_path = DOCS / 'batch-042.json'
    batch = json.loads(batch_path.read_text(encoding='utf8'))
    batch['publicationPending'] = False
    batch['publication'] = {
        'record': 'docs/translation-review/publication-042.json',
        'ciRun': args.ci_run,
        'deployedCommit': args.commit,
        'allPassed': True,
    }
    batch['scope'] = batch['scope'].replace(
        'CI publication and post-deploy checks remain pending.',
        'CI succeeded and all 13 live pages passed post-deploy checks.',
    )
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n', encoding='utf8')

print(json.dumps({'allPassed': passed, 'pages': len(results), 'failures': [p for p in results if not p['passed']]}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
