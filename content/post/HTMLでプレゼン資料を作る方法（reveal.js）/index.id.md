---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23
title: 'Cara Menggunakan reveal.js: Membuat Materi Presentasi dengan HTML dan Markdown'
slug: "HTMLでPresentasi資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "Presentasi"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Menjelaskan instalasi dan penggunaan dasar ''reveal.js'', sebuah alat yang memungkinkan Anda membuat presentasi secara intuitif menggunakan HTML dan Markdown. Memperkenalkan metode pemanfaatan yang mendukung animasi dan output PDF, serta sangat kompatibel dengan manajemen versi seperti Git.'
---

# Cara Membuat Presentasi dengan HTML

reveal.js adalah alat pembuatan presentasi yang menggunakan HTML dan Markdown, serta memiliki fitur-fitur berikut:

- Berbagai fitur presentasi seperti rumus matematika, animasi, dan operasi usap (swipe)
- Tema dan tata letak dapat disesuaikan
- Fitur navigasi yang mendukung berbagai perangkat seperti mouse, keyboard, dan panel sentuh
- Menyediakan fitur-fitur canggih seperti putar otomatis salindia dan penyematan video
- Dapat diekspor dalam format PDF

Dengan fitur-fitur ini, pengguna dapat dengan mudah membuat presentasi yang interaktif dan menarik.

# Instalasi dan Cara Menggunakan reveal.js

Cara paling sederhana untuk menggunakannya adalah mengunduh seluruh ZIP dari halaman berikut dan mengekstraknya.

1. Buka [https://revealjs.com/installation](https://revealjs.com/installation) dan unduh `master.zip` dari tautan tersebut
2. Buka index.html di folder yang telah diekstrak menggunakan browser
3. Edit index.html untuk membuat materi presentasi Anda sendiri

※ Kode HTML demo ditulis di demo.html sehingga Anda dapat menggunakannya sebagai referensi.

# Cara Memanfaatkan

Materi presentasi yang dibuat dapat dipublikasikan sebagai halaman web apa adanya, atau diekspor sebagai PDF.
Selain itu, karena sumber presentasi adalah teks, maka mudah dikelola dengan sistem kontrol versi.

Tampaknya Anda juga dapat membuat materi presentasi dalam format Markdown.

# Membuat slide dasar

Cara termudah adalah mengunduh ZIP Basic Setup terbaru, mengekstraknya, lalu mengedit `index.html`. Seperti pada contoh HTML di bawah, tempatkan setiap slide di dalam `<section>`. Berkas contoh Basic Setup sudah menyertakan gaya dan kode inisialisasi yang diperlukan.

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# Menulis slide dengan Markdown

Plugin Markdown yang disertakan memungkinkan Anda menulis Markdown di dalam berkas HTML. Pisahkan slide horizontal dengan `---` dan tambahkan contoh berikut ke `index.html`. Memuat berkas Markdown eksternal memerlukan server web lokal.

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# Penyiapan pengembangan

Jika memerlukan server lokal atau alat pengembangan sumber, gunakan Full Setup resmi. Jalankan perintah berikut, lalu buka `http://localhost:8000` di browser.

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# Ekspor ke PDF

Tambahkan `?print-pdf` di akhir URL. Di dialog cetak Chrome atau Chromium, pilih Simpan sebagai PDF, orientasi lanskap, tanpa margin, dan aktifkan grafik latar. Panduan resmi mengonfirmasi Chrome dan Chromium.

# Catatan pembicara

Tekan `S` untuk membuka tampilan pembicara di jendela terpisah. Tambahkan catatan di dalam `<aside class="notes">` pada slide. Tampilan pembicara lokal memerlukan server web.

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# Dokumentasi resmi

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

Periksa hak penggunaan gambar dan video pada slide, lalu pastikan materi publik tidak memuat informasi rahasia atau catatan pembicara pribadi.
