---



title: "Usar etiquetas HTML en HUGO"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["Administración del blog"]
---




De manera predeterminada, el uso de etiquetas HTML en los artículos está deshabilitado en HUGO, pero puedes habilitarlo agregando la siguiente configuración en config.toml.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Referencia: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
