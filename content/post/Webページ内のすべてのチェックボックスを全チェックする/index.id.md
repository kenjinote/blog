---
title: "Mencentang Semua Kotak Centang di Halaman Web"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "otomatisasi"]
draft: false
image: "img.png"
categories: ["manajemen blog"]
---

Untuk mencentang semua kotak centang di halaman web, buka DevTools dengan F12, tempelkan kode berikut ke dalam konsol, dan jalankan.
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

Atau,

Buat bookmark baru, dan tempelkan kode berikut ke alamat saat mendaftar (biasanya di bagian Anda memasukkan https://...).
Buka halaman web di mana Anda ingin mencentang kotak, klik bookmark yang telah dibuat, dan semua kotak centang akan dicentang.
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

Jika Anda ingin menghapus semua centang, ubah bagian `boxes[i].checked = true;` pada skrip di atas menjadi `boxes[i].checked = false;`.
