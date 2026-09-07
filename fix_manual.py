import re
path = 'c:/work/kenji.blog/content/post/「日本人ファースト」について思うこと/index.es.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'^title:\s*.*$', 'title: "Reflexiones sobre el \\"Primero los Japoneses\\""', text, flags=re.MULTILINE)
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

path2 = 'c:/work/kenji.blog/content/post/インターネットの暗号を破る最強の数学「一般数体篩法（GNFS）」とは？/index.es.md'
with open(path2, 'r', encoding='utf-8') as f:
    text2 = f.read()
text2 = re.sub(r'^title:\s*.*$', 'title: "¿Qué es la Criba General del Campo de Números (GNFS)?"', text2, flags=re.MULTILINE)
with open(path2, 'w', encoding='utf-8') as f:
    f.write(text2)
