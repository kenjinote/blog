---
title: "Использование HTML-тегов в HUGO"
slug: "ispolzovanie-html-tegov-v-hugo"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["Управление блогом"]
---

По умолчанию в HUGO запрещено использование HTML-тегов в статьях, но если добавить следующий код в config.toml, это станет возможным.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Ссылка: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
