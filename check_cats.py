import os
import yaml

dir_path = r"c:\work\kenji.blog\content\post"
categories = set()

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                parts = content.split('---')
                if len(parts) >= 3:
                    fm_text = parts[1]
                    # Simple regex or yaml load
                    fm = yaml.safe_load(fm_text)
                    if fm and 'categories' in fm:
                        cats = fm['categories']
                        if isinstance(cats, list):
                            for c in cats:
                                categories.add(c)
                        elif isinstance(cats, str):
                            categories.add(cats)
            except Exception:
                pass

# write to file to avoid console encoding issues
with open("categories_list.txt", 'w', encoding='utf-8') as f:
    for c in sorted(list(categories)):
        f.write(c + "\n")
