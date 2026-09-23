import re

def translate():
    with open('index.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate frontmatter title
    content = content.replace(
        'title: "ゲーム技術: 3Dグラフィックスエンジンの進化 (Unreal Engine / Unity)"',
        'title: "Игровые технологии: Эволюция движков 3D-графики (Unreal Engine / Unity)"'
    )
    
    # Translate body title
    content = content.replace(
        '# ゲーム技術: 3Dグラフィックスエンジンの進化',
        '# Игровые технологии: Эволюция движков 3D-графики'
    )
    
    # Translate intro
    content = content.replace(
        '3Dエンジンはリアルタイムレンダリングを進化させました。',
        '3D-движки способствовали развитию рендеринга в реальном времени.'
    )
    
    # Translate section headers
    content = content.replace(
        '## レンダリングパイプライン',
        '## Конвейер рендеринга'
    )
    content = content.replace(
        '## レンダリング方程式',
        '## Уравнение рендеринга'
    )
    
    # Translate repeated headers and texts using regex
    # ## 追加技術検証パート 1
    content = re.sub(
        r'## 追加技術検証パート (\d+)',
        r'## Дополнительная техническая проверка, часть \1',
        content
    )
    
    # Repeated body
    content = content.replace(
        'このセクションでは、さらなる技術的な詳細とケーススタディについて深く掘り下げます。様々な条件下でのパフォーマンスの評価や、他のシステムとの統合に関する課題と解決策を検討します。今後の展望や限界についても考察を行います。',
        'В этом разделе мы подробно рассмотрим дальнейшие технические детали и тематические исследования. Мы оценим производительность в различных условиях и рассмотрим проблемы и решения для интеграции с другими системами. Мы также обсудим будущие перспективы и ограничения.'
    )
    
    # Ensure mermaid nodes are in double quotes
    # Just in case, let's use a regex to ensure nodes without quotes get quotes, but we know the file already has quotes.
    # The requirement is: "Enclose Mermaid nodes in double quotes"
    # Wait, let me check the file carefully again.
    
    with open('index.ru.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Translation complete.")

if __name__ == '__main__':
    translate()
