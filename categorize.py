import os, glob, re

def get_category(tags, title):
    tags_str = ' '.join(tags).lower()
    title_lower = title.lower()
    
    if any(k in tags_str or k in title_lower for k in ['gnfs', 'shor', 'rsa', 'pqc', '量子', '暗号', '数学', '素因数', 'アインシュタイン']):
        return '数学・暗号・量子'
    if any(k in tags_str or k in title_lower for k in ['hugo', 'ブログ', 'papermod', 'ウェブ', 'web', 'seo', 'アナリティクス', 'analytics']):
        return 'ブログ運営'
    if any(k in tags_str or k in title_lower for k in ['vscode', 'visual studio', 'git', 'github', 'vim', 'wsl', 'エディタ', 'ターミナル', 'docker', 'winget', 'micro']):
        return 'ツール・開発環境'
    if any(k in tags_str or k in title_lower for k in ['c++', 'python', 'rust', 'go', 'html', 'css', 'javascript', 'powershell', 'api', 'プログラミング', 'wxwidgets', 'win32', 'プログラマ', 'コーディング']):
        return 'プログラミング'
    if any(k in tags_str or k in title_lower for k in ['windows', 'mac', 'ios', 'pc', 'スマホ', 'マウス', 'キーボード', 'ハードウェア', 'デバイス', 'wi-fi', 'ルーター', 'pixel', 'iphone', 'android']):
        return 'PC・ガジェット'
    if any(k in tags_str or k in title_lower for k in ['ai', 'chatgpt', 'gemini', 'copilot', 'stable diffusion']):
        return 'AI・テクノロジー'
    if any(k in tags_str or k in title_lower for k in ['ビジネス', '生活', '趣味', 'エンタメ', '読書', '音楽', '映画', '思考', '健康', '書籍']):
        return 'ライフスタイル・雑記'
        
    return 'IT・テクノロジー'

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    if len(lines) < 2 or lines[0] != '---':
        return False
        
    fm_lines = []
    fm_end_idx = -1
    
    for i in range(1, len(lines)):
        line = lines[i]
        if line == '---':
            fm_end_idx = i
            break
        fm_lines.append(line)
        
    if fm_end_idx == -1:
        return False
        
    body_lines = lines[fm_end_idx+1:]
    tags = []
    title = ''
    has_categories = False
    
    for line in fm_lines:
        if line.startswith('title:'):
            title = line.split('title:', 1)[1].strip().strip('\'\"')
        elif line.startswith('tags:'):
            val = line.split('tags:', 1)[1].strip()
            if val.startswith('['):
                items = val.strip('[]').split(',')
                tags = [item.strip().strip('\'\"') for item in items]
        elif line.startswith('categories:'):
            has_categories = True
            
    if has_categories:
        cat_line = [l for l in fm_lines if l.startswith('categories:')][0]
        if '[]' not in cat_line.replace(' ', ''):
            return False 
            
    category = get_category(tags, title)
    
    new_fm_lines = []
    for line in fm_lines:
        if line.startswith('categories:'):
            continue 
        new_fm_lines.append(line)
        
    new_fm_lines.append(f'categories: [\"{category}\"]')
    
    new_content = '---\n' + '\n'.join(new_fm_lines) + '\n---\n' + '\n'.join(body_lines)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    return True

files = glob.glob(r'c:\work\kenji.blog\content\post\**\index.md', recursive=True)
count = 0
for f in files:
    if process_file(f):
        count += 1
        
print(f'Categorized {count} files.')
