with open(r'c:\work\kenji.blog\content\post\search-algorithms-linear-binary-hash-table-principles\index.hi.md', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Match A["\"Text\""] -> A["Text"]
content = re.sub(r'\["\\"([^"]+)\\""\]', r'["\1"]', content)
content = re.sub(r'\{"\\"([^"]+)\\""\}', r'{"\1"}', content)

with open(r'c:\work\kenji.blog\content\post\search-algorithms-linear-binary-hash-table-principles\index.hi.md', 'w', encoding='utf-8') as f:
    f.write(content)
