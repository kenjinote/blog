---
title: "Mengubah Skema Warna PaperMod"
slug: "mengubah-skema-warna-papermod"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.png"
categories: ["Manajemen Blog"]
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
