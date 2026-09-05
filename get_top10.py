import glob

files = glob.glob(r'c:\work\kenji.blog\content\post\**\index.md', recursive=True)
posts = []

for file in files:
    if file.endswith('.en.md') or file.endswith('.zh-cn.md'): continue
    if 'Google Pixel' in file: continue # already translated
    if 'gnfs-to-shors' in file: continue # already translated? No, wait, I didn't translate gnfs-to-shors-algorithm-math-deepdive.
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

# Get top 10
top10 = [p[1] for p in posts[:10]]
with open('c:/work/kenji.blog/top10.txt', 'w', encoding='utf-8') as f:
    for path in top10:
        f.write(path + '\n')
