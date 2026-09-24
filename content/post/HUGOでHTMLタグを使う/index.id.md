---
title: 'Cara Mengaktifkan Tag HTML di Hugo (Pengaturan config.toml)'
date: "2026-09-24T19:44:38+09:00"
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Menjelaskan cara agar tag HTML dapat ditulis langsung dan digunakan di dalam artikel Markdown pada pembuat situs statis Hugo. Prosesnya selesai hanya dengan menambahkan pengaturan unsafe dari markup.goldmark.renderer di config.toml.'
---

Secara default, HUGO tidak mengizinkan penggunaan tag HTML di dalam artikel, tetapi Anda dapat mengaktifkannya dengan menambahkan kode berikut pada file config.toml.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Referensi: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
