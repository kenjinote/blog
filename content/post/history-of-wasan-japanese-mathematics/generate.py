import os
from deep_translator import GoogleTranslator
import time

ja_text = """---
title: "江戸時代の天才たちが挑んだ数学ミステリー：日本独自の数学「和算」と算額の歴史"
description: "鎖国下の日本で独自に発達した高度な数学「和算」。関孝和をはじめとする天才数学者たちの軌跡と、神社仏閣に奉納された「算額」の謎に迫ります。"
date: "2026-09-25T02:00:00+09:00"
categories: ["history", "mathematics"]
tags: ["wasan", "math", "history", "japan"]
slug: "history-of-wasan-japanese-mathematics"
image: "eyecatch.jpg"
---

## 1. 和算（Wasan）とは何か：鎖国が生んだ奇跡の数学

江戸時代（1603年〜1867年）、日本は「鎖国」と呼ばれる対外孤立政策をとっていました。しかし、この文化的・物理的な閉鎖空間のなかで、独自の高度な数学文化が花開きました。それが**和算（Wasan）**です。

当時のヨーロッパでは、ニュートンやライプニッツが微分積分学を創始していましたが、同時期の日本でも、全く別の文脈から微積分に匹敵する概念が生まれていました。和算は、実用的な測量や暦の計算から始まり、次第に純粋な数学的遊戯、あるいは一種の芸術へと昇華していきました。

```mermaid
graph TD
    A["古代中国の数学（九章算術など）"] -- "伝来" --> B["初期の和算（塵劫記など）"]
    B -- "実用から学問へ" --> C["関孝和による代数学の確立（点竄術）"]
    C -- "高度化・遊戯化" --> D["算額奉納の流行"]
    D -- "円理（微積分）の発展" --> E["幕末の超絶技巧数学"]
```

### 1.1 塵劫記のベストセラー化

和算の爆発的な普及のきっかけとなったのは、1627年に出版された吉田光由の『塵劫記（じんこうき）』です。そろばんの使い方から、面積・体積の求め方、さらにはネズミ算のような娯楽的な問題まで、図入りで分かりやすく解説されていました。

```python
# ネズミ算のシミュレーション（Pythonによる実装）
def nezumizan(months):
    # 最初のつがい
    pairs = 1
    for month in range(1, months + 1):
        # 毎月12匹（6つがい）を生むと仮定
        pairs += pairs * 6
    return pairs * 2 # 匹数

print(f"12ヶ月後のネズミの数: {nezumizan(12)}匹")
# 出力: 12ヶ月後のネズミの数: 27682574402匹
```

この本は江戸時代の識字率の高さも相まって空前の大ベストセラーとなり、多くの日本人が数学の魅力に取り憑かれました。

## 2. 天才・関孝和と「点竄術（てんざんじゅつ）」

17世紀後半、和算を世界トップレベルに引き上げたのが**関孝和（Seki Takakazu）**です。彼は「算聖」と称され、日本のニュートンとも呼ばれます。

関孝和の最大の功績は、未知数を記号で表して方程式を立てる「点竄術」を考案したことです。これにより、中国から伝わった算木（さんぎ）という物理的な計算道具の限界を超え、紙の上で複雑な代数計算を行うことが可能になりました。

### 行列式の発見
関孝和はヨーロッパのライプニッツより10年も早く、連立一次方程式の解法として「行列式（Determinant）」の概念を発見していました。彼の著書『解伏題之法』には、現代の行列式展開と本質的に同じ計算手法が記されています。

$$ \\Delta = a_{11}a_{22} - a_{12}a_{21} $$

## 3. 神社仏閣に掲げられた数学の絵馬：「算額（Sangaku）」

和算を語る上で欠かせないのが**算額（Sangaku）**の文化です。算額とは、数学の問題やその解法を美しい図形とともに木の板に描き、神社や寺院に奉納した絵馬の一種です。

### 3.1 神への感謝と、数学者たちの挑戦状

なぜ数学を神社仏閣に奉納したのでしょうか。
1. **感謝の表現**: 「難問が解けたのは神仏の加護のおかげ」という感謝。
2. **自己顕示とコミュニケーション**: 自分の学力を世間に示し、同時に「この問題が解けるか？」という他の数学者への挑戦状（遺題）としての役割。

村の農民から武士、商人、さらには女性や子供に至るまで、身分を問わず多くの人々が算額の作成に参加しました。これは世界でも類を見ない、大衆参加型の数学文化でした。

```mermaid
sequenceDiagram
    participant M["数学者A"]
    participant S["神社 (算額)"]
    participant N["数学者B"]
    
    M->>S: "問題と解答を奉納 (遺題を含む)"
    S-->>N: "参拝時に問題を発見"
    N->>N: "難問に挑戦"
    N->>S: "新たな算額として解答を奉納"
```

### 3.2 算額の典型的な問題（円理）

算額の問題の多くは、幾何学に関するものでした。特に、円の中に複数の円や多角形が接している図形問題が好まれました。

**【代表的な問題の例】**
「外円の中に、互いに接する3つの等しい円（甲円）と、それらに接する小さな円（乙円）がある。甲円の直径が与えられたとき、乙円の直径を求めよ。」

こうした複雑な図形問題を解くために、和算家たちは「**円理（えんり）**」と呼ばれる、現代の積分法に相当する極限計算の手法を発展させました。彼らは円周率 $\\pi$ の値を小数点以下数十桁まで正確に計算し、複雑な曲線の長さや立体図形の体積を求めていました。

## 4. 和算の終焉と近代数学への接続

明治時代（1868年〜）に入ると、日本は急速な近代化（西洋化）を推し進めました。明治政府は教育制度の改革において、実用性に劣り独自の記号体系を持つ和算を廃止し、西洋数学を正式な学問として採用することを決定しました。

これにより和算は急速に衰退しましたが、和算によって培われた「高度な数学的思考力」と「パズルを楽しむような知的好奇心」は、明治以降の日本人が西洋の近代科学や数学を驚異的なスピードで吸収する原動力となりました。

## 5. 現代に生きる和算の精神

現在でも、日本各地の神社仏閣には約900面の算額が現存しており、地域の文化財として大切に保存されています。また、現代の数学教育においても、論理的思考や探求心を育む教材として算額のパズル的な問題が見直されています。

江戸時代の天才たちが木の板に刻んだ数学の謎は、時を超えて現代の私たちにも、数学の美しさと解く喜びを伝えてくれているのです。
"""

import re
import json

def translate_markdown(text, target_lang):
    print(f"Translating to {target_lang}...")
    if target_lang == 'zh-cn':
        t_lang = 'zh-CN'
    elif target_lang == 'zh-tw':
        t_lang = 'zh-TW'
    else:
        t_lang = target_lang

    translator = GoogleTranslator(source='auto', target=t_lang)
    
    # Split text to preserve frontmatter structure manually
    parts = text.split('---')
    if len(parts) >= 3:
        frontmatter = parts[1]
        body = '---'.join(parts[2:])
        
        # Parse frontmatter
        lines = frontmatter.strip().split('\n')
        new_lines = []
        for line in lines:
            if line.startswith('title: '):
                val = line[7:].strip('" ')
                val_t = translator.translate(val)
                val_t = val_t.replace('"', '\\"')
                new_lines.append(f'title: "{val_t}"')
            elif line.startswith('description: '):
                val = line[13:].strip('" ')
                val_t = translator.translate(val)
                val_t = val_t.replace('"', '\\"')
                new_lines.append(f'description: "{val_t}"')
            else:
                new_lines.append(line)
        new_frontmatter = '\n'.join(new_lines)
    else:
        new_frontmatter = ""
        body = text

    # Chunk body by empty lines to translate without breaking markdown much
    paragraphs = body.split('\n\n')
    translated_paragraphs = []
    
    for p in paragraphs:
        # Don't translate code blocks or mermaid nodes/links blindly, but we'll do a simple text translation for simplicity
        # To be safe from deep_translator breaking markdown, we skip translation of code blocks
        if p.strip().startswith('```') and not p.strip().endswith('```'):
            translated_paragraphs.append(p)
            continue
        if p.strip() == '':
            translated_paragraphs.append('')
            continue
            
        # skip if it contains only english/symbols/code
        if p.startswith('```') or p.startswith('$$'):
            translated_paragraphs.append(p)
            continue
            
        try:
            t = translator.translate(p)
            translated_paragraphs.append(t if t else p)
        except Exception as e:
            print(f"Error translating chunk: {e}")
            translated_paragraphs.append(p)
            
    translated_body = '\n\n'.join(translated_paragraphs)
    
    return f"---\n{new_frontmatter}\n---\n{translated_body}"

def main():
    base_path = r"C:\work\kenji.blog\content\post\history-of-wasan-japanese-mathematics"
    os.makedirs(base_path, exist_ok=True)
    
    with open(os.path.join(base_path, "index.md"), "w", encoding="utf-8") as f:
        f.write(ja_text)
        
    langs = ["ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw"]
    
    for lang in langs:
        translated = translate_markdown(ja_text, lang)
        
        # fix some translator issues with mermaid syntax if any
        translated = translated.replace("ーー", "--").replace("ー", "-")
        
        filepath = os.path.join(base_path, f"index.{lang}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(translated)
        print(f"Generated {filepath}")
        time.sleep(1) # throttle a bit

if __name__ == "__main__":
    main()
