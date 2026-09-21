with open('translate_search.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
text = re.sub(r'original = line.*', r'original = line.rstrip("\r\n")', text)

with open('translate_search.py', 'w', encoding='utf-8') as f:
    f.write(text)
