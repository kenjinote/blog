---
title: "Pilih atau hapus pilihan semua kotak centang di halaman web"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Gunakan JavaScript atau bookmarklet untuk memilih atau menghapus pilihan kotak centang aktif pada halaman saat ini. Periksa perilaku halaman sebelum menjalankan kode."
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Pilih atau hapus pilihan semua kotak centang di halaman web

Skrip ini mengeklik kotak centang aktif pada halaman saat ini agar dapat diubah sekaligus.

## Sebelum menjalankan

Jalankan hanya pada halaman tepercaya. Halaman dapat merespons klik dengan mengubah pengaturan atau mengirim permintaan. Periksa hasil pilihan sebelum mengirim atau menyimpan apa pun.

## Jalankan di DevTools

Buka halaman tujuan lalu jalankan kode berikut di Console DevTools. Jika F12 tidak membuka DevTools di browser Anda, gunakan menu browser.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

Untuk menghapus pilihan semua kotak centang aktif, gunakan kode ini.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## Buat bookmarklet

Buat bookmark dan tempel kode satu baris di bawah ke kolom URL melalui editor bookmark. Jangan masukkan ke bilah alamat. Pilih bookmark saat berada di halaman tujuan untuk memilih kotak centang aktif.

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

Untuk menghapus pilihan, gunakan contoh kedua atau bookmarklet hapus semua. Skrip hanya bekerja pada dokumen saat ini dan melewati kotak centang yang dinonaktifkan.

Mengubah properti `.checked` saja mungkin tidak memberi tahu kode halaman melalui peristiwa yang biasanya terjadi saat klik. `.click()` memicu perilaku klik; kode khusus halaman tetap dapat mencegah beberapa perubahan.

## Referensi

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
