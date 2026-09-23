with open('c:/work/kenji.blog/content/post/history-of-apple/index.zh-cn.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Replace the specific math block containing tabs and form feeds with the properly formatted Chinese string
pattern = "\n\text{Performance per Watt} = \x0crac{\text{Computation Output (FLOPS)}}{\text{Power Consumption (Watts)}}\n"
replacement = "\n\\text{每瓦性能} = \\frac{\\text{计算输出 (FLOPS)}}{\\text{功耗 (瓦特)}}\n"

new_text = text.replace(pattern, replacement)

with open('c:/work/kenji.blog/content/post/history-of-apple/index.zh-cn.md', 'w', encoding='utf-8') as f:
    f.write(new_text)
