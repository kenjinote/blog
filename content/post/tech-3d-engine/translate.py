import re

input_file = 'c:/work/kenji.blog/content/post/tech-3d-engine/index.md'
output_file = 'c:/work/kenji.blog/content/post/tech-3d-engine/index.zh-tw.md'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Translate Title in frontmatter
content = re.sub(
    r'title: "ゲーム技術: 3Dグラフィックスエンジンの進化 \(Unreal Engine / Unity\)"',
    r'title: "遊戲技術：3D圖形引擎的進化 (Unreal Engine / Unity)"',
    content
)

# Translate body title
content = content.replace(
    '# ゲーム技術: 3Dグラフィックスエンジンの進化',
    '# 遊戲技術：3D圖形引擎的進化'
)

# Translate first sentence
content = content.replace(
    '3Dエンジンはリアルタイムレンダリングを進化させました。',
    '3D引擎使即時渲染技術得到了進化。'
)

# Translate headers
content = content.replace(
    '## レンダリングパイプライン',
    '## 渲染管線'
)

content = content.replace(
    '## レンダリング方程式',
    '## 渲染方程式'
)

# Translate repeated sections
content = re.sub(
    r'## 追加技術検証パート (\d+)',
    r'## 附加技術驗證部分 \1',
    content
)

content = content.replace(
    'このセクションでは、さらなる技術的な詳細とケーススタディについて深く掘り下げます。様々な条件下でのパフォーマンスの評価や、他のシステムとの統合に関する課題と解決策を検討します。今後の展望や限界についても考察を行います。',
    '本節將深入探討更多的技術細節與案例研究。我們將評估各種條件下的效能，並探討與其他系統整合時的挑戰與解決方案。同時，也會對未來的展望與局限性進行考察。'
)

def add_quotes_to_mermaid(match):
    mermaid_block = match.group(0)
    mermaid_block = re.sub(r'([A-Za-z0-9_]+)\[([^"\]]+)\]', r'\1["\2"]', mermaid_block)
    return mermaid_block

content = re.sub(r'```mermaid.*?```', add_quotes_to_mermaid, content, flags=re.DOTALL)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)
