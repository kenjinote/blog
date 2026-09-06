---
title: 'HUGOでHTMLタグを使う'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---

HUGOのデフォルトでは記事中のHTMLタグの使用ができなくなっていますが、config.tomlに下記の記述をするとできるようになります。

```toml
[markup.goldmark.renderer]
    unsafe = true
```

参考: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
