import json
import re
import time
from deep_translator import GoogleTranslator
from deep_translator.exceptions import TooManyRequests

with open('unique_ja.json', 'r', encoding='utf-8') as f:
    unique_lines = json.load(f)

translator = GoogleTranslator(source='ja', target='de')
translations = {}

def translate_with_retry(text, retries=5):
    for i in range(retries):
        try:
            return translator.translate(text)
        except Exception as e:
            if 'TooManyRequests' in str(type(e)):
                time.sleep(2 ** i)
            else:
                raise e
    return text

def translate_line(line):
    if line.startswith('categories: ') or line.startswith('tags: '):
        return line

    if re.search(r'-->\|"(.*?)"\|', line):
        def rep(m):
            t = translate_with_retry(m.group(1))
            return f'-->|"{t}"|'
        return re.sub(r'-->\|"(.*?)"\|', rep, line)

    if re.search(r'^[ \t]*[A-Z0-9]+[\[\{\(]".*?"[\]\}\)]', line):
        def rep(m):
            t = translate_with_retry(m.group(3))
            return f'{m.group(1)}{m.group(2)}"{t}"{m.group(4)}'
        line = re.sub(r'([A-Z0-9]+)([\[\{\(])"(.*?)"([\]\}\)])', rep, line)
        return line

    m = re.match(r'^\*\*パス (\d+) 完了後\*\*: `(.*)`', line)
    if m:
        return f'**Durchgang {m.group(1)} abgeschlossen**: `{m.group(2)}`'
    
    m = re.match(r'^\*\*ステップ (\d+) \(.*?(\d+).*?\)\*\*: `(.*)`', line)
    if m:
        inner = re.search(r'\((.*?)\)', line).group(1)
        inner_t = translate_with_retry(inner)
        return f'**Schritt {m.group(1)} ({inner_t})**: `{m.group(3)}`'

    m = re.match(r'^\*\*初期状態\*\*: `(.*)`', line)
    if m:
        return f'**Anfangszustand**: `{m.group(1)}`'

    if line.startswith('title: '):
        t = translate_with_retry(line[7:].strip('"'))
        return f'title: "{t}"'
    if line.startswith('description: '):
        t = translate_with_retry(line[13:].strip('"'))
        return f'description: "{t}"'
    
    math_patterns = re.findall(r'\$.*?\$', line)
    tmp_line = line
    for i, mp in enumerate(math_patterns):
        tmp_line = tmp_line.replace(mp, f'__MATH_{i}__')
    
    t_line = translate_with_retry(tmp_line)
    
    for i, mp in enumerate(math_patterns):
        def rep_text(m):
            inner = m.group(1)
            if re.search(r'[ぁ-んァ-ン一-龥]', inner):
                inner = translate_with_retry(inner)
            return f'\\text{{{inner}}}'
        new_mp = re.sub(r'\\text\{(.*?)\}', rep_text, mp)
        t_line = t_line.replace(f'__MATH_{i}__', new_mp)
        
    t_line = re.sub(r'(\S)\*\*', r'\1 **', t_line)
    t_line = re.sub(r'\*\*(\S)', r'** \1', t_line)
    t_line = t_line.replace('**  ', '** ').replace('  **', ' **')

    m = re.match(r'^([ \t]*#\s*)(.*)', line)
    if m:
        t = translate_with_retry(m.group(2))
        return f'{m.group(1)}{t}'

    return t_line

print("Translating unique lines with retry...")
for i, line in enumerate(unique_lines):
    if re.search(r'[ぁ-んァ-ン一-龥]', line):
        try:
            translations[line] = translate_line(line)
        except Exception as e:
            print("Failed to translate:", line[:20], e)
            translations[line] = line
    else:
        translations[line] = line
    print(f"Done {i+1}/{len(unique_lines)}")

with open(r'c:\work\kenji.blog\content\post\sorting-algorithms-visualized-bubble-quick-merge\index.md', 'r', encoding='utf-8') as f:
    full_text = f.read()

lines = full_text.splitlines()
new_lines = []
for l in lines:
    if l in translations:
        new_lines.append(translations[l])
    else:
        if re.search(r'[ぁ-んァ-ン一-龥]', l):
            try:
                new_lines.append(translate_line(l))
            except:
                new_lines.append(l)
        else:
            new_lines.append(l)

with open(r'c:\work\kenji.blog\content\post\sorting-algorithms-visualized-bubble-quick-merge\index.de.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Translation complete!")
