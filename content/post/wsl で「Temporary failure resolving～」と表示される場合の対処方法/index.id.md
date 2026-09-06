---
title: "Cara mengatasi 'Temporary failure resolving...' di WSL"
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "pemecahan masalah"]
draft: false
image: "img.png"
categories: ["Alat & Lingkungan Pengembangan"]
---

# Cara mengatasi 'Temporary failure resolving...' di WSL

`
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
`

Ketika kesalahan di atas muncul di WSL, pengaturan server DNS mungkin tidak benar.
Di lingkungan saya, masalah teratasi dengan langkah-langkah berikut:

1. Mulai WSL.
2. Jalankan `sudo nano /etc/resolv.conf`.
3. Ubah baris `nameserver` menjadi seperti berikut:
`
nameserver 8.8.8.8
`
4. Simpan dengan `Ctrl` + `S` dan keluar dengan `Ctrl` + `X`.
5. Jalankan `sudo apt update`.
6. Jika kesalahan tidak muncul, masalah selesai.

## Jika langkah di atas tidak menyelesaikan masalah

Sepertinya ada kasus di mana langkah di atas tidak menyelesaikan masalah. Silakan merujuk ke artikel berikut.

- [Cara mengatasi 'Temporary failure resolving...' saat apt update di WSL](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)