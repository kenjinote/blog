---



title: 'Cómo habilitar las etiquetas HTML en Hugo (Configuración de config.toml)'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["Administración del blog"]
description: 'Explicamos cómo usar y escribir directamente etiquetas HTML dentro de los artículos Markdown en Hugo, un generador de sitios estáticos. Se puede completar simplemente añadiendo la configuración unsafe a markup.goldmark.renderer en el archivo config.toml.'
---




De manera predeterminada, el uso de etiquetas HTML en los artículos está deshabilitado en HUGO, pero puedes habilitarlo agregando la siguiente configuración en config.toml.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Referencia: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
