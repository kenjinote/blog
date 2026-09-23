import re
import os

filepath = r'c:\work\kenji.blog\content\post\physics-superconductivity\index.md'
outpath = r'c:\work\kenji.blog\content\post\physics-superconductivity\index.hi.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace frontmatter title
content = re.sub(r'title: "物理学: 超伝導の仕組み - マイスナー効果とリニアモーターカー"', r'title: "भौतिक विज्ञान: सुपरकंडक्टिविटी कैसे काम करती है - मीस्नर प्रभाव और मैग्लेव"', content)

# Replace headings
content = re.sub(r'# 物理学: 超伝導の仕組み', r'# भौतिक विज्ञान: सुपरकंडक्टिविटी कैसे काम करती है', content)

# Replace paragraph
content = re.sub(r'超伝導は電気抵抗がゼロになる現象です。', r'सुपरकंडक्टिविटी वह घटना है जहां विद्युत प्रतिरोध शून्य हो जाता है।', content)

# Replace Meissner effect heading
content = re.sub(r'## マイスナー効果', r'## मीस्नर प्रभाव', content)

# Replace Mermaid nodes
content = re.sub(r'A\["Normal State \(Magnetic field penetrates\)"\]', r'A["सामान्य स्थिति (चुंबकीय क्षेत्र प्रवेश करता है)"]', content)
content = re.sub(r'B\["Superconducting State \(Magnetic field expelled\)"\]', r'B["सुपरकंडक्टिंग स्थिति (चुंबकीय क्षेत्र बाहर निकल जाता है)"]', content)

# Replace London Equation heading
content = re.sub(r'## ロンドン方程式', r'## लंदन समीकरण', content)

# Replace repetitive sections
content = re.sub(r'## 追加技術検証パート (\d+)', r'## अतिरिक्त तकनीकी सत्यापन भाग \1', content)

para_jp = r'このセクションでは、さらなる技術的な詳細とケーススタディについて深く掘り下げます。様々な条件下でのパフォーマンスの評価や、他のシステムとの統合に関する課題と解決策を検討します。今後の展望や限界についても考察を行います。'
para_hi = r'इस अनुभाग में, हम और अधिक तकनीकी विवरणों और केस स्टडीज में गहराई से जाएंगे। हम विभिन्न परिस्थितियों में प्रदर्शन का मूल्यांकन करेंगे और अन्य प्रणालियों के साथ एकीकरण से संबंधित चुनौतियों और समाधानों की जांच करेंगे। हम भविष्य की संभावनाओं और सीमाओं पर भी विचार करेंगे।'

content = content.replace(para_jp, para_hi)

with open(outpath, 'w', encoding='utf-8') as f:
    f.write(content)
