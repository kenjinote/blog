import os
import yaml

dir_path = r"c:\work\kenji.blog\content\post"
file_path = os.path.join(dir_path, "fermat", "index.md")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

parts = content.split('---')
if len(parts) >= 3:
    print(parts[1].strip())
