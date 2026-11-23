---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23
title: 'reveal.jsの使い方：HTMLとMarkdownでプレゼン資料を作成'
slug: "HTMLでプレゼン資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "プレゼン"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'HTMLとMarkdownで直感的にプレゼンテーションが作成できるツール「reveal.js」のインストールと基本的な使い方を解説します。アニメーションやPDF出力に対応し、Git等のバージョン管理とも相性抜群の活用法を紹介します。'
---

# HTMLでプレゼン資料を作る方法

reveal.jsは、HTMLとMarkdownを使用したプレゼンテーション作成ツールで、以下の機能があります。

- 数式やアニメーション、スワイプ操作などの多彩なプレゼンテーション機能
- テーマやレイアウトのカスタマイズが可能
- マウスやキーボード、タッチパッドなど、複数のデバイスに対応したナビゲーション機能
- スライドの自動再生や、ビデオの組み込みなど、高度な機能を提供
- PDF形式でのエクスポートが可能

これらの機能により、ユーザーは簡単にインタラクティブで魅力的なプレゼンテーションを作成することができます。

# reveal.jsのインストールと使い方

一番簡単な使い方は、以下のページからZIPを丸ごとダウンロードして解凍する方法です。

1. [https://revealjs.com/installation](https://revealjs.com/installation) を開き、リンクより`master.zip`をダウンロードする
2. 解凍したフォルダ内のindex.htmlをブラウザで開く
3. index.htmlを書き換えて、自分のプレゼン資料を作成する

※demo.htmlにデモ用のHTMLコードが書かれているので参考にできると思います。

# 活用方法

作ったプレゼン資料は、そのままWebページとして公開したり、PDFとしてエクスポートすることができます。
また、プレゼンのソースがテキストなので、バージョン管理システムで管理することが容易です。

マークダウン形式でプレゼン資料を作成することもできるようです。

# 基本的なスライドの作成

Basic Setupは最新版ZIPを解凍して`index.html`を編集する簡単な方法です。下のHTML例のように、各スライドを`<section>`で囲みます。Basic Setupの`index.html`には必要なスタイルと初期化コードが含まれています。

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# Markdownでスライドを作る

同梱のMarkdownプラグインで、HTML内にMarkdownを書けます。`---`で横方向のスライドを分けます。次の例は`index.html`に追加します。外部Markdownファイルの読み込みにはローカルWebサーバーが必要です。

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# 開発用セットアップ

ローカルWebサーバーやソース編集機能が必要な場合は、公式Full Setupを使います。次のコマンドを実行し、ブラウザーで`http://localhost:8000`を開きます。

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# PDFへの書き出し

`?print-pdf`をURL末尾に付け、ChromeまたはChromiumの印刷画面でPDF保存、横向き、余白なし、背景グラフィック有効を選びます。公式に確認されているのはChromeとChromiumです。

# 発表者ノート

発表者ビューは`S`キーで別ウィンドウに開きます。スライド内の`<aside class="notes">`にノートを書けます。ローカルで使う場合はWebサーバーが必要です。

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# 公式ドキュメント

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

スライドに使う画像・動画の利用条件を確認し、公開資料に機密情報や非公開の発表者ノートが含まれていないか確認してください。
