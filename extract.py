import os
import re
import json
import yaml

def extract_japanese_terms():
    base_dir = r'c:\work\kenji.blog\content\post'
    jp_regex = re.compile(r'[ぁ-んァ-ヶ亜-熙]')
    unique_categories = set()
    unique_tags = set()

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file == 'index.md':
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                parts = content.split('---')
                if len(parts) >= 3:
                    frontmatter_text = parts[1]
                    try:
                        fm = yaml.safe_load(frontmatter_text)
                        if fm:
                            cats = fm.get('categories', [])
                            tags = fm.get('tags', [])
                            
                            if isinstance(cats, list):
                                for c in cats:
                                    if c and jp_regex.search(str(c)):
                                        unique_categories.add(str(c))
                            elif isinstance(cats, str) and jp_regex.search(cats):
                                unique_categories.add(cats)

                            if isinstance(tags, list):
                                for t in tags:
                                    if t and jp_regex.search(str(t)):
                                        unique_tags.add(str(t))
                            elif isinstance(tags, str) and jp_regex.search(tags):
                                unique_tags.add(tags)
                    except Exception as e:
                        pass

    out = {
        'categories': sorted(list(unique_categories)),
        'tags': sorted(list(unique_tags))
    }
    with open('extracted_terms.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

extract_japanese_terms()
