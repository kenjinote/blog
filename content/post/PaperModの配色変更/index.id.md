---
title: 'Cara Mengubah Skema Warna dan Tema Warna pada Tema Hugo PaperMod dengan CSS'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["Manajemen Blog"]
description: 'Menjelaskan cara mengkustomisasi skema warna secara keseluruhan pada tema PaperMod di Hugo. Memperkenalkan contoh pengaturan variabel spesifik untuk menerapkan skema warna pilihan Anda dengan mengedit CSS (blank.css) yang menyertakan definisi gaya untuk warna latar belakang, warna teks, blok kode, dll.'
---
Saya telah mengubah skema warna tema PaperMod. Saya merujuk ke bawah ini untuk metode perubahannya.

https://github.com/adityatelange/hugo-PaperMod/discussions/645

Path CSS adalah sebagai berikut.

`themes/PaperMod/assets/css/extended/blank.css`

```
:root {
    --entry: #fbf7ef;
    --primary: rgba(113, 103, 91, 1.00);
    --secondary: rgba(113, 103, 91, 0.95);
    --tertiary: rgba(113, 103, 91, 0.50);
    --content: rgba(113, 103, 91, 0.85);
    --hljs-bg: #34231B;
    --code-bg: #ebe4d7;
    --border: #fdfaf5;
    --theme: #fbf7ef;
}
.dark {
}
```

Untuk saat ini, tidak ada perubahan pada mode gelap.
