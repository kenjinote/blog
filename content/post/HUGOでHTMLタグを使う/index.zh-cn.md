---
title: '在HUGO中使用HTML标签'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["博客运营"]
---

HUGO默认情况下是不允许在文章中使用HTML标签的，但是在config.toml中添加以下描述就可以使用了。

```toml
[markup.goldmark.renderer]
    unsafe = true
```

参考: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
