"""Create a fixed, resumable inventory; never infer editorial review from a scan."""
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/article-audit'


def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', *args], cwd=cwd).decode('utf-8')


def main():
    OUT.mkdir(exist_ok=True)
    inventory = OUT / 'inventory.json'
    if inventory.exists():
        raise SystemExit('Inventory already exists: resume it instead of overwriting.')
    listing = subprocess.check_output(['hugo', 'list', 'published'], cwd=ROOT).decode('utf-8-sig')
    rows = list(csv.DictReader(io.StringIO(listing)))
    published = {r['path'].replace('\\', '/'): r['permalink'] for r in rows if r['kind'] == 'page'}
    (OUT / 'published.csv').write_text(listing, encoding='utf-8')
    definitions = {p.name for p in (ROOT / 'content/categories').iterdir() if p.is_dir()}
    articles = []
    for name in git('ls-files', '-z', 'content/post').split('\0'):
        if not name.endswith('.md'):
            continue
        path = ROOT / name
        raw = path.read_bytes()
        source = raw.decode('utf-8-sig')
        match = re.match(r'\A---\s*\r?\n(.*?)\r?\n---(?:\s*\r?\n|$)', source, re.S)
        problem = None
        try:
            data = yaml.safe_load(match[1]) if match else {}
            if not isinstance(data, dict):
                raise ValueError('Frontmatter must be a mapping')
        except (yaml.YAMLError, ValueError) as error:
            data = {}
            problem = str(error)
        categories = data.get('categories') or []
        if isinstance(categories, str):
            categories = [categories]
        articles.append({
            'path': name, 'bundle': path.parent.name,
            'language': path.name.split('.')[-2] if path.name.count('.') > 1 else 'ja',
            'title': data.get('title'), 'source_sha256': hashlib.sha256(raw).hexdigest(),
            'url': published.get(name), 'categories_before': categories,
            'undefined_categories': [c for c in categories if c not in definitions],
            'frontmatter_error': problem,
            'status': 'pending' if name in published and not problem else 'held',
            'hold_reason': problem or (None if name in published else 'Not in Hugo published inventory; inspect draft/date/expiry or auxiliary file'),
            'body_reviewed': False, 'categories_reviewed': False, 'links_reviewed': False,
            'validation': None, 'batch': None,
        })
    original = Path('C:/work/kenji.blog')
    untracked = [p for p in git('ls-files', '--others', '--exclude-standard', '-z', 'content/post', cwd=original).split('\0') if p.endswith('.md')]
    inventory.write_text(json.dumps({
        'started_date_jst': '2026-10-15', 'base_commit': git('rev-parse', 'HEAD').strip(),
        'scope': 'Tracked article Markdown at start; source checkout untracked drafts recorded separately and never edited.',
        'articles': articles,
        'held_untracked': [{'path': p, 'reason': 'Uncommitted article in another active checkout; do not overwrite', 'status': 'held'} for p in untracked],
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'tracked_articles': len(articles), 'published_pending': sum(a['status'] == 'pending' for a in articles), 'held_tracked': sum(a['status'] == 'held' for a in articles), 'held_untracked': len(untracked), 'undefined_category_articles': sum(bool(a['undefined_categories']) for a in articles)}, indent=2))


if __name__ == '__main__':
    main()
