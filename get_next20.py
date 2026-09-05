import glob, os

files = glob.glob(r'c:\work\kenji.blog\content\post\**\index.md', recursive=True)
posts = []

for file in files:
    if file.endswith('.en.md') or file.endswith('.zh-cn.md'): continue
    
    # Check if translation already exists
    dir_name = os.path.dirname(file)
    en_file = os.path.join(dir_name, 'index.en.md')
    zh_file = os.path.join(dir_name, 'index.zh-cn.md')
    if os.path.exists(en_file) and os.path.exists(zh_file):
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

# Sort by date descending
posts.sort(reverse=True, key=lambda x: x[0])

# Get next 20
next20 = [p[1] for p in posts[:20]]
with open('c:/work/kenji.blog/next20.txt', 'w', encoding='utf-8') as f:
    for path in next20:
        f.write(path + '\n')
print(f'Found {len(next20)} articles to translate.')
