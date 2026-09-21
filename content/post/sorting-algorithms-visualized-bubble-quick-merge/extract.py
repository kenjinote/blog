import json, re
lines = json.load(open('ja_lines.json', encoding='utf-8'))
texts = set()
for l in lines:
    l = re.sub(r'`\[.*?\]`', '', l)
    texts.add(l.strip())
with open('ja_texts.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(texts)))
