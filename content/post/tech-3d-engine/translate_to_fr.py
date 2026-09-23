import sys
import re

def translate():
    with open('c:/work/kenji.blog/content/post/tech-3d-engine/index.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Translate Title
    content = content.replace('title: "ゲーム技術: 3Dグラフィックスエンジンの進化 (Unreal Engine / Unity)"', 'title: "Technologie du jeu : L\'évolution des moteurs graphiques 3D (Unreal Engine / Unity)"')
    
    # Translate H1
    content = content.replace('# ゲーム技術: 3Dグラフィックスエンジンの進化', '# Technologie du jeu : L\'évolution des moteurs graphiques 3D')
    
    # Translate Intro
    content = content.replace('3Dエンジンはリアルタイムレンダリングを進化させました。', 'Les moteurs 3D ont fait évoluer le rendu en temps réel.')
    
    # Translate H2
    content = content.replace('## レンダリングパイプライン', '## Pipeline de rendu')
    content = content.replace('## レンダリング方程式', '## Équation de rendu')
    
    # Translate Part Header
    content = re.sub(r'## 追加技術検証パート (\d+)', r'## Partie de validation technique supplémentaire \1', content)
    
    # Translate Paragraph
    content = content.replace('このセクションでは、さらなる技術的な詳細とケーススタディについて深く掘り下げます。様々な条件下でのパフォーマンスの評価や、他のシステムとの統合に関する課題と解決策を検討します。今後の展望や限界についても考察を行います。', 'Dans cette section, nous approfondissons davantage les détails techniques et les études de cas. Nous évaluons les performances dans diverses conditions et examinons les défis ainsi que les solutions liés à l\'intégration avec d\'autres systèmes. Nous discutons également des perspectives futures et des limites.')

    # Mermaid nodes in double quotes
    def add_quotes_to_mermaid(match):
        mermaid_block = match.group(0)
        # Match NodeId[NodeLabel] and add quotes to NodeLabel if they aren't already quoted
        mermaid_block = re.sub(r'([A-Za-z0-9_]+)\[([^"\]]+)\]', r'\1["\2"]', mermaid_block)
        return mermaid_block

    content = re.sub(r'```mermaid.*?```', add_quotes_to_mermaid, content, flags=re.DOTALL)
    
    with open('c:/work/kenji.blog/content/post/tech-3d-engine/index.fr.md', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    translate()
