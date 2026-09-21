import re
import json
import time
from deep_translator import GoogleTranslator

with open(r'c:\work\kenji.blog\content\post\sorting-algorithms-visualized-bubble-quick-merge\index.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

translator = GoogleTranslator(source='ja', target='ko')

# 1. Collect all texts to translate
texts_to_translate = set()

in_frontmatter = False
in_mermaid = False
in_code = False

for i, line in enumerate(lines):
    original = line.strip('\n')
    if i == 0 and original == '---':
        in_frontmatter = True
        continue
    
    if in_frontmatter:
        if original == '---':
            in_frontmatter = False
            continue
        if ':' in original and not (original.startswith('slug:') or original.startswith('date:') or original.startswith('image:')):
            key, val = original.split(':', 1)
            key, val = key.strip(), val.strip()
            if key in ['title', 'description']:
                texts_to_translate.add(val.strip('"\''))
            elif key in ['categories', 'tags']:
                try:
                    arr = json.loads(val)
                    for x in arr: texts_to_translate.add(x)
                except:
                    pass
        continue
        
    if original.startswith('```'):
        if original.startswith('```mermaid'):
            in_mermaid = True
        elif original == '```':
            in_mermaid, in_code = False, False
        else:
            in_code = True
        continue
        
    if in_code:
        if '#' in original:
            idx = original.find('#')
            texts_to_translate.add(original[idx+1:])
        continue
        
    if in_mermaid:
        m_link = re.search(r'-->\|(.*?)\|', original)
        if m_link: texts_to_translate.add(m_link.group(1).strip('"\''))
        node_pattern = re.compile(r'([A-Z0-9]+)(\[|\{)(.*?)(\]|\})')
        for m in node_pattern.finditer(original):
            texts_to_translate.add(m.group(3).strip('"\''))
        continue
        
    if original:
        if original.startswith('**パス') and '完了後**:' in original: continue
        elif original.startswith('**ステップ') and 'を挿入後**:' in original: continue
        elif original.startswith('**初期状態**: `['): continue
        
        def hide_math(m): return ' MATH '
        text_to_trans = re.sub(r'\$.*?\$', hide_math, original)
        texts_to_translate.add(text_to_trans)
        
        # Add math translations
        for text in re.findall(r'\\text\{([^}]+)\}', original):
            texts_to_translate.add(text)

texts_list = [t for t in texts_to_translate if t.strip()]

# 2. Batch Translate
trans_dict = {}
chunk_size = 50
print(f"Translating {len(texts_list)} unique strings...")

for i in range(0, len(texts_list), chunk_size):
    chunk = texts_list[i:i+chunk_size]
    try:
        translated = translator.translate_batch(chunk)
        for c, t in zip(chunk, translated):
            trans_dict[c] = t
    except Exception as e:
        print(f"Batch failed, doing one by one: {e}")
        for c in chunk:
            try:
                trans_dict[c] = translator.translate(c)
                time.sleep(0.5)
            except Exception as e2:
                trans_dict[c] = c
                print(f"Failed to translate {c}: {e2}")

# 3. Second pass
new_lines = []
in_frontmatter = False
in_mermaid = False
in_code = False

def get_trans(t):
    return trans_dict.get(t, t)

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
            comment = original[idx+1:]
            new_lines.append(pre + get_trans(comment) + '\n')
        else:
            new_lines.append(original + '\n')
        continue
        
    if in_mermaid:
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
            new_lines.append(f'**패스 {m.group(1)} 완료 후**:{m.group(2)}\n')
            continue
        elif original.startswith('**ステップ') and 'を挿入後**:' in original:
            m = re.match(r'\*\*ステップ (\d+) \(要素 (\d+) を挿入後\)\*\*:(.*)', original)
            new_lines.append(f'**단계 {m.group(1)} (요소 {m.group(2)} 삽입 후)**:{m.group(3)}\n')
            continue
        elif original.startswith('**初期状態**: `['):
            new_lines.append(original.replace('**初期状態**:', '**초기 상태**:') + '\n')
            continue
            
        maths = []
        def hide_math(m):
            maths.append(m.group(0))
            return f' MATH_TOKEN_{len(maths)-1} '
        text_to_trans = re.sub(r'\$.*?\$', hide_math, original)
        
        trans = get_trans(text_to_trans)
        
        for idx, math_txt in enumerate(maths):
            def translate_text_in_math(m_text):
                return '\\text{' + get_trans(m_text.group(1)) + '}'
            translated_math = re.sub(r'\\text\{([^}]+)\}', translate_text_in_math, math_txt)
            trans = trans.replace(f' MATH_TOKEN_{idx} ', translated_math)
            trans = trans.replace(f'MATH_TOKEN_{idx}', translated_math)

        trans = re.sub(r'(?<=[가-힣])\*\*', ' **', trans)
        trans = re.sub(r'\*\*(?=[가-힣])', '** ', trans)
        trans = trans.replace('  **', ' **').replace('**  ', '** ')
        
        new_lines.append(trans.strip() + '\n')
    else:
        new_lines.append('\n')

with open(r'c:\work\kenji.blog\content\post\sorting-algorithms-visualized-bubble-quick-merge\index.ko.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Done!')
