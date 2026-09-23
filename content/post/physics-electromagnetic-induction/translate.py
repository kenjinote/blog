import re

with open(r'c:\work\kenji.blog\content\post\physics-electromagnetic-induction\index.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Translate frontmatter
text = re.sub(r'title: ".*?"', 'title: "物理学：电磁感应与电机原理 - 从法拉第的发现到电动汽车"', text, count=1)

# Translate headings
text = text.replace('# 物理学: 電磁誘導とモーターの仕組み', '# 物理学：电磁感应与电机原理')
text = text.replace('電磁誘導は発電機やモーターの基礎です。', '电磁感应是发电机和电机的基础。')
text = text.replace('## ファラデーの法則', '## 法拉第定律')
text = text.replace('## ファラデーの電磁誘導の法則', '## 法拉第电磁感应定律')

# Translate repeated sections
text = re.sub(r'## 追加技術検証パート (\d+)', r'## 附加技术验证部分 \1', text)
text = text.replace('このセクションでは、さらなる技術的な詳細とケーススタディについて深く掘り下げます。様々な条件下でのパフォーマンスの評価や、他のシステムとの統合に関する課題と解決策を検討します。今後の展望や限界についても考察を行います。', '本节深入探讨了进一步的技术细节和案例研究。我们将评估各种条件下的性能，并探讨与其他系统集成的挑战和解决方案。我们还将讨论未来的前景和局限性。')

with open(r'c:\work\kenji.blog\content\post\physics-electromagnetic-induction\index.zh-cn.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Translation completed.')
