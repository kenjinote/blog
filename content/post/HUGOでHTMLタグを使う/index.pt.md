---
title: "Usando tags HTML no HUGO"
slug: "usando-tags-html-no-hugo"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["Gestão de Blog"]
---

Por padrão, o HUGO não permite o uso de tags HTML em artigos, mas você pode ativá-lo adicionando a seguinte descrição ao config.toml.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Referência: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
