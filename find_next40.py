import os
import glob
import yaml
import json

base_dir = 'c:/work/kenji.blog/content/post'
md_files = []

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file == 'index.md':
            path = os.path.join(root, file)
            md_files.append(path)

def get_date(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        parts = content.split('---')
        if len(parts) >= 3:
            front = yaml.safe_load(parts[1])
            return front.get('date', '')
    except:
        pass
    return ''

files_with_date = []
for f in md_files:
    d = get_date(f)
    if d:
        files_with_date.append((d, f))

# Sort descending by date
files_with_date.sort(key=lambda x: str(x[0]), reverse=True)

target_files = []
for d, f in files_with_date:
    es_file = f.replace('.md', '.es.md')
    ko_file = f.replace('.md', '.ko.md')
    if not os.path.exists(es_file) or not os.path.exists(ko_file):
        target_files.append(f)
    if len(target_files) >= 40:
        break

print(f"Found {len(target_files)} files to translate.")
with open('c:/work/kenji.blog/next40_to_translate.json', 'w', encoding='utf-8') as f:
    json.dump(target_files, f, indent=2, ensure_ascii=False)
