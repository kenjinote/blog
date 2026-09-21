import re
content = open('c:/work/kenji.blog/content/post/sorting-algorithms-visualized-bubble-quick-merge/index.zh-tw.md', 'r', encoding='utf-8').read()
content = content.replace('E -->|"Yes"| G["ソート完了"]', 'E -->|"Yes"| G["排序完成"]')
content = content.replace('A["將陣列從中央分為兩個"] --> B{"要素数が1以下か"}', 'A["將陣列從中央分為兩個"] --> B{"元素數量是否小於等於1"}')
with open('c:/work/kenji.blog/content/post/sorting-algorithms-visualized-bubble-quick-merge/index.zh-tw.md', 'w', encoding='utf-8') as f:
    f.write(content)
