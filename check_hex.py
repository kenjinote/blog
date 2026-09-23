import re
with open('c:/work/kenji.blog/content/post/history-of-apple/index.zh-cn.md', 'r', encoding='utf-8') as f:
    text = f.read()

math_block = re.search(r'\$\$(.*?)\$\$', text, re.DOTALL)
if math_block:
    print(' '.join(hex(ord(c)) for c in math_block.group(1)))
