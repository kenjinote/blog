---
title: 'Как включить HTML-теги в Hugo (настройки config.toml)'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["Управление блогом"]
description: 'Объясняется, как разрешить прямое написание и использование HTML-тегов в статьях Markdown в генераторе статических сайтов Hugo. Достаточно добавить настройку unsafe для markup.goldmark.renderer в файл config.toml.'
---

По умолчанию в HUGO запрещено использование HTML-тегов в статьях, но если добавить следующий код в config.toml, это станет возможным.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Ссылка: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
