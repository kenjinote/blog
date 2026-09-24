---
title: '在Hugo中启用HTML标签的方法（config.toml的设置）'
slug: "HUGOでHTMLタグを使う"
date: "2026-09-24T16:08:36+09:00"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '本文讲解如何设置静态网站生成器Hugo，以便在Markdown文章中直接编写并使用HTML标签。只需在config.toml中添加markup.goldmark.renderer的unsafe设置即可完成。'
---

HUGO默认情况下是不允许在文章中使用HTML标签的，但是在config.toml中添加以下描述就可以使用了。

```toml
[markup.goldmark.renderer]
    unsafe = true
```

参考: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
