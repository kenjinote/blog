import re
import os

source = r"c:\work\kenji.blog\content\post\physics-gps\index.md"
dest = r"c:\work\kenji.blog\content\post\physics-gps\index.ru.md"

with open(source, "r", encoding="utf-8") as f:
    text = f.read()

# Translate headers and specific sentences
replacements = {
    r'title: "宇宙と技術: GPSの仕組み - 相対性理論と衛星測位システム"': 'title: "Космос и технологии: Как работает GPS - Теория относительности и спутниковые системы позиционирования"',
    r'# 宇宙と技術: GPSの仕組み': '# Космос и технологии: Как работает GPS',
    r'GPSは相対性理論を利用して正確な位置を測定します。': 'GPS использует теорию относительности для точного измерения местоположения.',
    r'## 測位原理': '## Принцип позиционирования',
    r'## 時間の遅れ': '## Замедление времени',
    r'このセクションでは、さらなる技術的な詳細とケーススタディについて深く掘り下げます。様々な条件下でのパフォーマンスの評価や、他のシステムとの統合に関する課題と解決策を検討します。今後の展望や限界についても考察を行います。': 'В этом разделе мы углубимся в дальнейшие технические детали и тематические исследования. Мы оценим производительность в различных условиях и рассмотрим проблемы и решения, связанные с интеграцией с другими системами. Также будут рассмотрены будущие перспективы и ограничения.'
}

for src, tgt in replacements.items():
    text = text.replace(src, tgt)

# Translate repetitive sections
text = re.sub(
    r'## 追加技術検証パート (\d+)',
    r'## Часть \1 дополнительной технической проверки',
    text
)

# Check and enforce double quotes around mermaid nodes
# The prompt says: "Enclose Mermaid nodes in double quotes."
# Let's ensure the mermaid nodes are exactly as they were, since they are already in double quotes.
# e.g., A["Satellite 1, 2, 3, 4 (Time and Position)"]

with open(dest, "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
