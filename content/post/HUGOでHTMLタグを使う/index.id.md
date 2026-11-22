---
title: "Mengizinkan HTML Mentah di Markdown Hugo"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Pelajari cara mengaktifkan HTML mentah di Markdown Hugo dengan contoh YAML, TOML, dan JSON, beserta risiko keamanan dan kondisi saat opsi ini sebaiknya tidak diaktifkan."
---

Perender Markdown Goldmark Hugo tidak merender HTML mentah secara default. Jika diperlukan, atur `markup.goldmark.renderer.unsafe` menjadi `true` di konfigurasi situs. Hugo mendukung berkas konfigurasi YAML, TOML, dan JSON. Contohnya, di `hugo.yaml`:

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

Di `hugo.toml`:

```toml
[markup.goldmark.renderer]
  unsafe = true
```

Atau di `hugo.json`:

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

Nilai default-nya adalah `false`. `unsafe: true` mengizinkan HTML mentah di Markdown diteruskan ke keluaran dan melemahkan batas kepercayaan konten Hugo. Jangan aktifkan jika situs memproses Markdown dari kontributor yang tidak tepercaya atau masukan eksternal. Gunakan hanya untuk konten yang Anda kendalikan dan periksa, serta pahami konsekuensinya. Untuk tata letak kompleks, shortcode atau berkas konten HTML mungkin lebih sesuai.

Referensi: [Mengonfigurasi markup](https://gohugo.io/configuration/markup/) · [Model keamanan Hugo](https://gohugo.io/about/security/)
