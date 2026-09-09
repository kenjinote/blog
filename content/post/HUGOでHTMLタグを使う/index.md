---
title: 'HugoでHTMLタグを有効にする方法（config.tomlの設定）'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["ブログ運営"]
description: '静的サイトジェネレータHugoのMarkdown記事内でHTMLタグを直接記述して使用できるようにする方法を解説します。config.tomlにmarkup.goldmark.rendererのunsafe設定を追加するだけで完了します。'
---

HUGOのデフォルトでは記事中のHTMLタグの使用ができなくなっていますが、config.tomlに下記の記述をするとできるようになります。

```toml
[markup.goldmark.renderer]
    unsafe = true
```

参考: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
