import re
import json

with open(r'c:\work\kenji.blog\content\post\sorting-algorithms-visualized-bubble-quick-merge\index.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('translations_dict.json', 'r', encoding='utf-8') as f:
    trans_dict = json.load(f)

def get_trans(t):
    original_t = t
    if t.startswith('# '):
        header_text = t[2:]
        if header_text in trans_dict:
            return '# ' + trans_dict[header_text]
    if t.startswith('## '):
        header_text = t[3:]
        if header_text in trans_dict:
            return '## ' + trans_dict[header_text]
    if t.startswith('### '):
        header_text = t[4:]
        if header_text in trans_dict:
            return '### ' + trans_dict[header_text]
    
    if t in trans_dict:
        return trans_dict[t]
    
    return original_t

new_lines = []
in_frontmatter = False
in_mermaid = False
in_code = False

for i, line in enumerate(lines):
    original = line.strip('\n')
    
    if i == 0 and original == '---':
        in_frontmatter = True
        new_lines.append(original + '\n')
        continue
    
    if in_frontmatter:
        if original == '---':
            in_frontmatter = False
            new_lines.append(original + '\n')
            continue
            
        if original.startswith('slug:') or original.startswith('date:') or original.startswith('image:'):
            new_lines.append(original + '\n')
            continue
            
        if ':' in original:
            key, val = original.split(':', 1)
            key, val = key.strip(), val.strip()
            
            if key in ['title', 'description']:
                val_unquoted = val.strip('"\'')
                translated_val = get_trans(val_unquoted)
                translated_val = translated_val.replace('"', '\\"')
                new_lines.append(f'{key}: "{translated_val}"\n')
                continue
                
            if key in ['categories', 'tags']:
                try:
                    arr = json.loads(val)
                    arr_trans = [get_trans(x) for x in arr]
                    new_lines.append(f'{key}: {json.dumps(arr_trans, ensure_ascii=False)}\n')
                except:
                    new_lines.append(original + '\n')
                continue
                
        new_lines.append(original + '\n')
        continue
        
    if original.startswith('```'):
        if original.startswith('```mermaid'): in_mermaid = True
        elif original == '```': in_mermaid, in_code = False, False
        else: in_code = True
        new_lines.append(original + '\n')
        continue
        
    if in_code:
        if '#' in original:
            idx = original.find('#')
            pre = original[:idx+1]
            comment = original[idx+1:].strip()
            new_lines.append(pre + ' ' + get_trans(comment) + '\n')
        else:
            new_lines.append(original + '\n')
        continue
        
    if in_mermaid:
        if original.strip().startswith('%%'):
            comment = original.strip()[2:].strip()
            new_lines.append(f'%% {get_trans(comment)}\n')
            continue

        m_link = re.search(r'-->\|(.*?)\|', original)
        if m_link:
            link_text = m_link.group(1).strip('"\'')
            original = original.replace(f'|{m_link.group(1)}|', f'|"{get_trans(link_text)}"|')
            
        node_pattern = re.compile(r'([A-Z0-9]+)(\[|\{)(.*?)(\]|\})')
        def replace_node(m):
            id_, open_b, text, close_b = m.group(1), m.group(2), m.group(3).strip('"\''), m.group(4)
            return f'{id_}{open_b}"{get_trans(text)}"{close_b}'
            
        new_lines.append(node_pattern.sub(replace_node, original) + '\n')
        continue
        
    if original:
        if original.startswith('**パス') and '完了後**:' in original:
            m = re.match(r'\*\*パス (\d+) 完了後\*\*:(.*)', original)
            if m:
                new_lines.append(f'**패스 {m.group(1)} 완료 후**:{m.group(2)}\n')
            else:
                new_lines.append(original + '\n')
            continue
        elif original.startswith('**ステップ') and 'を挿入後**:' in original:
            m = re.match(r'\*\*ステップ (\d+) \(要素 (\d+) を挿入後\)\*\*:(.*)', original)
            if m:
                new_lines.append(f'**단계 {m.group(1)} (요소 {m.group(2)} 삽입 후)**:{m.group(3)}\n')
            else:
                new_lines.append(original + '\n')
            continue
        elif original.startswith('**初期状態**: `['):
            new_lines.append(original.replace('**初期状態**:', '**초기 상태**:') + '\n')
            continue
            
        trans = get_trans(original)
        
        # Translate math \text{}
        def translate_text_in_math(m_text):
            return '\\text{' + get_trans(m_text.group(1)) + '}'
        trans = re.sub(r'\\text\{([^}]+)\}', translate_text_in_math, trans)
        
        # Asterisk bolding
        trans = re.sub(r'(?<=[가-힣])\*\*(.*?)\*\*(?=[가-힣])', r' **\1** ', trans)
        trans = re.sub(r'(?<=[가-힣])\*\*(.*?)\*\*', r' **\1**', trans)
        trans = re.sub(r'\*\*(.*?)\*\*(?=[가-힣])', r'**\1** ', trans)
        trans = trans.replace('  **', ' **').replace('**  ', '** ')

        new_lines.append(trans + '\n')
    else:
        new_lines.append('\n')

with open(r'c:\work\kenji.blog\content\post\sorting-algorithms-visualized-bubble-quick-merge\index.ko.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Done!')
