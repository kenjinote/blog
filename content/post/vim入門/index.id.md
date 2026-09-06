---
title: "Pengenalan Vim"
slug: "vim-introduction"
date: 2024-04-19T22:06:34+09:00
tags: ["vim", "text editor"]
draft: false
image: "img.png"
categories: ["tools and development environment"]
---

![img_1.png](img_1.png)

# Pengenalan Vim

## Unduh dan Instal

[https://www.vim.org/download.php](https://www.vim.org/download.php)

Dari situs di atas, unduh dan instal modul sesuai dengan OS yang ingin Anda instal.

Untuk Windows, sebaiknya pilih `gvim_X.X.X_x64_signed.exe`.

## Cara Menjalankan

Untuk Windows, folder yang berisi `vim.exe` perlu didaftarkan di Path pada variabel lingkungan.

Cara menjalankan

```
vim
```

Untuk menjalankan dengan menentukan nama file

```
vim filename.txt
```

## Cara Keluar

Untuk keluar, ketik `:` (titik dua), lalu ketik `q`, dan tekan Enter
```
:q
```

Jika Anda telah memperbarui file, pesan `No write since last change (add ! to override)` akan ditampilkan.
Anda dapat membuang konten dan keluar secara paksa.
```
:q!
```

Untuk menyimpan file dan keluar
```
:wq
```

Hal berikut ini juga memiliki arti yang sama.
```
:x
```

Selain itu, Anda juga dapat keluar dengan menekan `z` dua kali sambil menahan `Shift`. (sama dengan :wq)

## Mode

Vim memiliki `command mode` (mode perintah) dan `insert mode` (mode penyisipan). Saat Vim dijalankan, itu akan berada di `command mode`, dan menekan tombol `i` akan beralih ke `insert mode`.

Dalam `insert mode`, Anda dapat mengetik seperti biasa. Untuk beralih dari `insert mode` ke `command mode`, tekan tombol `ESC`.

Fitur transisi mode ini adalah karakteristik dari Vim.

## Gerakan Kursor dan Gulir

Berikut adalah ringkasan pergerakan kursor dan gulir pada saat `command mode`.

| Tombol                               | Deskripsi                 |
|------------------------------------|-------------------------|
| `h` (atau `Ctrl`+`H`, `BackSpace`, `←`) | Pindah ke kiri             |
| `j` (atau `Ctrl`+`J`, `N`, `↓`)         | Pindah ke bawah            |
| `k` (atau `Ctrl`+`P`, `↑`)             | Pindah ke atas             |
| `l` (atau `Space`, `→`)               | Pindah ke kanan            |
| `+` (atau `Enter`)                   | Pindah ke awal baris berikutnya |
| `-`                                | Pindah ke awal baris sebelumnya |
| `Ctrl`+`B` (atau `PageUp`)            | Gulir ke atas             |
| `Ctrl`+`F` (atau `PageDown`)          | Gulir ke bawah            |
| `Ctrl`+`U`                         | Setengah gulir ke atas      |
| `Ctrl`+`D`                         | Setengah gulir ke bawah     |
| `Ctrl`+`Y`                         | Gulir ke atas 1 baris     |
| `Ctrl`+`E`                         | Gulir ke bawah 1 baris    |
| `z` `Enter`                        | Gulir baris kursor ke bagian atas layar |
| `z` `.`                            | Gulir baris kursor ke tengah layar |
| `z` `-`                            | Gulir baris kursor ke bagian bawah layar |
| `0` (atau `\|`)                       | Pindah kursor ke awal baris      |
| `$`                                | Pindah kursor ke akhir baris      |
| `^` (atau `_`)                        | Pindah kursor ke awal baris (tidak termasuk spasi, Tab) |
| `G` (atau `:$`)                       | Pindah kursor ke baris terakhir       |
| `:nomor baris` `Enter`                     | Pindah ke baris yang ditentukan |

Jika Anda memasukkan tombol gerakan di atas setelah `angka`, Anda dapat memindahkannya beberapa kali sesuai dengan angka tersebut.
(Misalnya, mengetik `3j` akan memindahkan Anda ke bawah 3 baris dari posisi kursor saat ini.)

## Perintah Lainnya

| Tombol       | Deskripsi                  |
|------------|----------------------|
| `Ctrl`+`L` | Gambar ulang layar            |
| `Ctrl`+`G` | Tampilkan jumlah baris dari seluruh file, posisi kursor, dll. |
