---
title: "Menyesuaikan Warna Hugo PaperMod dengan Variabel CSS"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Ganti variabel warna PaperMod untuk tema terang dan gelap melalui CSS extended, lalu periksa kontras teks."
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Warna PaperMod dapat disesuaikan dengan properti khusus CSS (variabel). Simpan override di `assets/css/extended/` milik situs, bukan dengan mengedit berkas tema, agar lebih mudah dipertahankan saat tema diperbarui. Contoh ini memberikan palet terang bernuansa hangat dan palet gelap; sesuaikan warnanya untuk situs Anda.

## Mode gelap dan variabel terkini

PaperMod saat ini mengaktifkan mode gelap dengan menetapkan `data-theme="dark"` pada elemen `html`. Contoh lama yang hanya menargetkan `.dark` mungkin tidak cocok dengan pemilih ini. `--hljs-bg` juga bukan lagi variabel terkini untuk latar blok kode; nama yang digunakan sekarang adalah `--code-block-bg`.

```css
/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme="dark"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
```

## Kontras teks

Pada contoh ini, warna teks normal `--primary` dan `--content` memiliki kontras kuat terhadap latarnya. Rasio contoh `--primary` terhadap `--theme` sekitar 10,4:1 dalam mode terang dan 13,4:1 dalam mode gelap. WCAG 2.2 AA mensyaratkan 4,5:1 untuk teks normal; periksa warna sintaks, tautan, batas, dan keadaan lainnya secara terpisah.

## Tambahkan dan periksa CSS extended

Simpan stylesheet sebagai `assets/css/extended/theme-colors.css` di direktori utama situs. FAQ PaperMod menyatakan bahwa CSS di `assets/css/extended/` digabungkan dengan stylesheet tema. Jalankan Hugo dan periksa peralihan terang/gelap, kartu, teks isi, kode sebaris, blok kode, dan tautan.

## Cakupan

Palet ini hanya contoh dan tidak menjamin aksesibilitas setiap teks, gambar, atau komponen interaktif. Warna syntax highlighting ditentukan secara terpisah dari `--code-block-bg`; periksa kembali keterbacaan kode setelah mengubah latar blok.

## Referensi

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
