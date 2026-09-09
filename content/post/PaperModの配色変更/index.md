---
title: 'Hugo PaperModテーマの配色・カラーテーマをCSSで変更する方法'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["ブログ運営"]
description: 'HugoのPaperModテーマにおける全体の配色をカスタマイズする方法を解説します。背景色やテキスト色、コードブロック等のスタイル定義が含まれるCSS（blank.css）を編集し、好みのカラースキームを適用するための具体的な変数の設定例を紹介します。'
---
PaperModテーマの配色を変更しました。変更方法は下記を参考にしました。

https://github.com/adityatelange/hugo-PaperMod/discussions/645

CSSのパスは下記になります。

`themes/PaperMod/assets/css/extended/blank.css`

```
:root {
    --entry: #fbf7ef;
    --primary: rgba(113, 103, 91, 1.00);
    --secondary: rgba(113, 103, 91, 0.95);
    --tertiary: rgba(113, 103, 91, 0.50);
    --content: rgba(113, 103, 91, 0.85);
    --hljs-bg: #34231B;
    --code-bg: #ebe4d7;
    --border: #fdfaf5;
    --theme: #fbf7ef;
}
.dark {
}
```

ダークはいったん変更なしです。