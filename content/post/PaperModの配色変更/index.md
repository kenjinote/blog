---
title: "Hugo PaperModの配色をCSS変数でカスタマイズする"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "PaperMod公式の拡張CSSでライト・ダーク両テーマの色変数を上書きし、本文色のコントラストを確認する方法を紹介します。"
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperModの配色はCSSカスタムプロパティ（CSS変数）で調整できます。テーマ同梱ファイルではなく、サイトの`assets/css/extended/`にCSSを置くと、テーマ更新時に上書き内容を保ちやすくなります。次の例は温かみのあるライト色と暗いダーク色を定義します。色はサイトに合わせて調整してください。

## ダークテーマと現在の変数

現在のPaperModは`data-theme="dark"`を`html`要素に設定してダーク表示を切り替えます。`.dark`だけを対象にした古い例では、このテーマ設定に反映されない場合があります。`--hljs-bg`も現行テーマのコードブロック背景変数ではありません。現在の変数名は`--code-block-bg`です。

```css
/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme="dark"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
```

## 文字コントラスト

この例では通常の文字色`--primary`と`--content`を背景色に対して十分暗く／明るくしています。実値のコントラスト比はライトで`--primary`対`--theme`が約10.4:1、ダークで約13.4:1です。通常サイズの文字に対するWCAG 2.2 AAの基準は4.5:1ですが、コードのシンタックス色、リンク、境界線などは個別に確認してください。

## 拡張CSSを追加して確認する

サイトのルートに`assets/css/extended/theme-colors.css`を保存します。PaperMod公式FAQに従い、`assets/css/extended/`内のCSSはテーマのCSSにまとめて読み込まれます。Hugoを起動し、ライト／ダーク切替、カード、本文、インラインコード、コードブロック、リンクを確認します。

## 確認範囲

このパレットは配色例で、すべての文字・画像・操作部品のアクセシビリティ適合を保証しません。特にシンタックスハイライトの色は`--code-block-bg`とは別のCSSで定義されるため、コード背景だけを変えた後に読みやすさを再確認してください。

## 参考資料

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
