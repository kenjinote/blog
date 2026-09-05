import os, glob

tags = set()
for file in glob.glob(r'c:\work\kenji.blog\content\post\**\index.md', recursive=True):
    with open(file, 'r', encoding='utf-8') as f:
        in_fm = False
        for line in f:
            line = line.strip()
            if line == '---':
                if not in_fm: in_fm = True
                else: break
            elif in_fm and line.startswith('tags:'):
                val = line.split(':', 1)[1].strip()
                if val.startswith('['):
                    items = val.strip('[]').split(',')
                    for item in items:
                        tags.add(item.strip().replace('"', '').replace("'", ""))

print(', '.join(sorted(list(tags))))
