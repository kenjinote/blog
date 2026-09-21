with open(r'c:\work\kenji.blog\content\post\sorting-algorithms-visualized-bubble-quick-merge\index.es.md', encoding='utf-8') as f:
    text = f.read()
import re
japanese_re = re.compile(r'[ぁ-んァ-ヶ亜-熙]')

lines = text.split('\n')
for i, line in enumerate(lines):
    if japanese_re.search(line):
        print(f'Line {i+1}: {repr(line)}')
