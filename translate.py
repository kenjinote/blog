import re

source_path = r'c:\work\kenji.blog\content\post\physics-superconductivity\index.md'
dest_path = r'c:\work\kenji.blog\content\post\physics-superconductivity\index.ru.md'

with open(source_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
for line in lines:
    if line.startswith('title:'):
        out_lines.append('title: "Физика: Как работает сверхпроводимость - Эффект Мейснера и поезда на магнитной подушке"\n')
    elif line.startswith('# 物理学: 超伝導の仕組み'):
        out_lines.append('# Физика: Как работает сверхпроводимость\n')
    elif line.startswith('超伝導は電気抵抗がゼロになる現象です。'):
        out_lines.append('Сверхпроводимость — это явление, при котором электрическое сопротивление становится равным нулю.\n')
    elif line.startswith('## マイスナー効果'):
        out_lines.append('## Эффект Мейснера\n')
    elif 'A["Normal State' in line:
        out_lines.append('    A["Нормальное состояние (Магнитное поле проникает)"] --> B["Сверхпроводящее состояние (Магнитное поле выталкивается)"]\n')
    elif line.startswith('## ロンドン方程式'):
        out_lines.append('## Уравнение Лондонов\n')
    elif line.startswith('## 追加技術検証パート'):
        part_num = line.strip().split('パート')[-1].strip()
        out_lines.append(f'## Дополнительная техническая проверка, часть {part_num}\n')
    elif line.startswith('このセクションでは、さらなる技術的な詳細とケーススタディについて深く掘り下げます'):
        out_lines.append('В этом разделе мы более подробно рассмотрим технические детали и тематические исследования. Мы оценим производительность в различных условиях и обсудим проблемы и решения, связанные с интеграцией с другими системами. Мы также обсудим будущие перспективы и ограничения.\n')
    else:
        out_lines.append(line)

with open(dest_path, 'w', encoding='utf-8') as f:
    f.writelines(out_lines)

print('Translation complete')
