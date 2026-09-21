with open(r'c:\work\kenji.blog\content\post\search-algorithms-linear-binary-hash-table-principles\index.hi.md', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('[""', '["').replace('""]', '"]').replace('{""', '{"').replace('""}', '"}')

with open(r'c:\work\kenji.blog\content\post\search-algorithms-linear-binary-hash-table-principles\index.hi.md', 'w', encoding='utf-8') as f:
    f.write(content)
