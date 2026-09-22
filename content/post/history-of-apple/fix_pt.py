import re

filepath = r'c:\work\kenji.blog\content\post\history-of-apple\index.pt.md'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'(\s*- "innovation"\n){2,}', '\n    - "innovation"\n', text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
