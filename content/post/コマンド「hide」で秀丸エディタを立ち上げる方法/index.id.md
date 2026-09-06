---
title: "Cara Menjalankan Editor Hidemaru dengan Perintah «hide»"
slug: "コマンド「hide」で秀丸エディタを立ち上げる方法"
date: 2024-03-29T23:45:37+09:00
tags: ["perintah", "editor Hidemaru", "registry"]
draft: false
image: "img_2.png"
categories: ["Alat & Lingkungan Pengembangan"]
---

## Berikut adalah cara menjalankan Editor Hidemaru dengan perintah «hide».

Catatan: Metode ini telah dikonfirmasi berfungsi pada `Windows 10/11`.

1. Buka Registry Editor.
2. Buka `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Buat kunci bernama `hide.exe` di `App Paths`. ※ Bagian sebelum `.exe` pada nama kunci ini akan menjadi nama perintah.
4. Atur jalur file yang dapat dieksekusi dari Editor Hidemaru di `(Default)` pada kunci `hide.exe`. Di lingkungan saya, jalurnya adalah `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. Buat nilai string bernama `Path` di kunci `hide.exe`.
6. Atur jalur folder yang berisi file yang dapat dieksekusi Editor Hidemaru ke data `Path`. Di lingkungan saya, jalurnya adalah `"C:\Program Files (x86)\Hidemaru"`.
7. Sekarang, Anda dapat menjalankan Editor Hidemaru dengan perintah `hide` di jendela **Run** yang ditampilkan dengan menekan tombol `Win` + `R`. Selain itu, di Command Prompt, Anda dapat menjalankan Editor Hidemaru dengan perintah `start hide`.

```text
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="\"C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe\""
"Path"="\"C:\\Program Files (x86)\\Hidemaru\\\""
```
Jika Anda menyimpan konten di atas dalam file `.reg` dan menjalankannya, pengaturan akan ditambahkan ke registry.

![img_1.png](img_1.png)
