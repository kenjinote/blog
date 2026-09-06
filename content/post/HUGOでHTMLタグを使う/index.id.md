---
title: "Menggunakan Tag HTML di HUGO"
slug: "menggunakan-tag-html-di-hugo"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["Manajemen Blog"]
---

Secara default, HUGO tidak mengizinkan penggunaan tag HTML di dalam artikel, tetapi Anda dapat mengaktifkannya dengan menambahkan kode berikut pada file config.toml.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Referensi: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
