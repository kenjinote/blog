import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
split_pattern = re.compile(r'(!?\[[^\]]*\]\([^\)]+\)|```.*?```|`[^`]+`)', re.DOTALL)

count = 0
for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file.endswith('.md'):
            parts_file = file.split('.')
            if len(parts_file) == 3 and parts_file[2] == 'md':
                lang_prefix = "/" + parts_file[1]
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        front_matter = '---' + parts[1] + '---'
                        body = parts[2]
                    else:
                        front_matter = ''
                        body = content
                    
                    tokens = split_pattern.split(body)
                    
                    changed = False
                    for i in range(1, len(tokens), 2):
                        text = tokens[i]
                        if text.startswith('[') or text.startswith('!['):
                            old_url = "https://kenji.blog/p/"
                            new_url = f"https://kenji.blog{lang_prefix}/p/"
                            if old_url in text and new_url not in text:
                                tokens[i] = text.replace(old_url, new_url)
                                changed = True
                    
                    if changed:
                        new_body = "".join(tokens)
                        new_content = front_matter + new_body
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
                except Exception:
                    pass

print(f"Fixed {count} markdown files.")
