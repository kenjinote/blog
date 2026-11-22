---
title: "Разрешить необработанный HTML в Markdown Hugo"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Узнайте, как разрешить необработанный HTML в Markdown Hugo: примеры YAML, TOML и JSON, риски безопасности и случаи, когда эту настройку не следует включать."
---

По умолчанию Markdown-рендерер Goldmark в Hugo не выводит необработанный HTML. Если это необходимо, задайте `markup.goldmark.renderer.unsafe: true` в конфигурации сайта. Hugo поддерживает файлы конфигурации YAML, TOML и JSON. Например, в `hugo.yaml`:

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

В `hugo.toml`:

```toml
[markup.goldmark.renderer]
  unsafe = true
```

Или в `hugo.json`:

```json
{
  "markup": {
    "goldmark": {
      "renderer": {
        "unsafe": true
      }
    }
  }
}
```

Значение по умолчанию — `false`. Параметр `unsafe: true` разрешает необработанному HTML из Markdown попадать в результат и ослабляет границу доверия к содержимому в Hugo. Не включайте его, если сайт обрабатывает Markdown от ненадёжных авторов или из внешних источников. Используйте настройку только для содержимого, которое вы контролируете и проверяете, понимая последствия. Для сложной разметки лучше подойдут шорткод или HTML-файл содержимого.

Справка: [Настройка разметки](https://gohugo.io/configuration/markup/) · [Модель безопасности Hugo](https://gohugo.io/about/security/)
