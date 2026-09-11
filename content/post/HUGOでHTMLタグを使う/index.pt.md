---
title: 'Como Habilitar Tags HTML no Hugo (Configuração do config.toml)'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["Gestão de Blog"]
description: 'Aprenda como habilitar o uso de tags HTML diretas em artigos em Markdown no gerador de sites estáticos Hugo. É tão simples quanto adicionar a configuração ''unsafe'' em ''markup.goldmark.renderer'' no arquivo config.toml.'
---

Por padrão, o HUGO não permite o uso de tags HTML em artigos, mas você pode ativá-lo adicionando a seguinte descrição ao config.toml.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Referência: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
