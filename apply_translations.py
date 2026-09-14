import os
import json
import sys

def replace_front_matter():
    lang_code = sys.argv[1]
    with open(f'translations_{lang_code}.json', 'r', encoding='utf-8') as f:
        mapping = json.load(f)
        
    updated_count = 0
    for root, dirs, files in os.walk(r'c:\work\kenji.blog\content\post'):
        for file in files:
            if file == f'index.{lang_code}.md':
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    fm = parts[1]
                    original_fm = fm
                    # Sort mapping by length of Japanese string (descending) to avoid partial replacement of compound words
                    sorted_mapping = sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True)
                    for jp, trans in sorted_mapping:
                        if jp in fm:
                            fm = fm.replace(jp, trans)
                    
                    if fm != original_fm:
                        parts[1] = fm
                        new_content = '---'.join(parts)
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        updated_count += 1

    print(f"[{lang_code}] Updated {updated_count} files.")

if __name__ == '__main__':
    replace_front_matter()
