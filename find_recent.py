import os, glob

files = glob.glob(r'c:\work\kenji.blog\content\post\**\index.md', recursive=True)
posts = []

for file in files:
    if file.endswith('.en.md') or file.endswith('.zh-cn.md'):
        continue
    try:
        with open(file, 'r', encoding='utf-8') as f:
            date_str = ''
            for line in f:
                if line.startswith('date:'):
                    date_str = line.split('date:', 1)[1].strip().strip('\'\"')
                    break
            if date_str:
                posts.append((date_str, file))
    except Exception as e:
        pass

posts.sort(reverse=True, key=lambda x: x[0])

for p in posts[:12]:
    print(p[1])
