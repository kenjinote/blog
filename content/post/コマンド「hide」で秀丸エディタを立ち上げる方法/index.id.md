---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25
title: 'Buka Hidemaru Editor Seketika dengan Perintah ''hide''! Cara Pengaturan Praktis di Windows'
slug: "Perintah「hide」でEditor Hidemaruを立ち上げる方法"
tags: ["perintah", "editor Hidemaru", "registry"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "Daftarkan nama di App Paths dan jalankan Hidemaru Editor dari Run atau dengan start hide di Windows 10/11."
---

## Berikut adalah cara menjalankan Editor Hidemaru dengan perintah «hide».

Catatan: Metode ini telah dikonfirmasi berfungsi pada `Windows 10/11`.

1. Buka Registry Editor.
2. Buka `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Buat kunci bernama `hide.exe` di `App Paths`. ※ Bagian sebelum `.exe` pada nama kunci ini akan menjadi nama perintah.
4. Atur jalur file yang dapat dieksekusi dari Editor Hidemaru di `(Default)` pada kunci `hide.exe`. Di lingkungan saya, jalurnya adalah `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. Nilai Path opsional. Tambahkan hanya jika aplikasi memerlukan direktori DLL tambahan; ShellExecuteEx menambahkannya ke PATH proses.
6. Ketik hide di Run (Win + R). Di Command Prompt gunakan start hide; mengetik hide saja bukan cara yang dijelaskan.

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
Jika Anda menyimpan konten di atas dalam file `.reg` dan menjalankannya, pengaturan akan ditambahkan ke registry.

Contoh .reg ini hanya mendaftarkan aplikasi bagi pengguna saat ini. Ganti jalur dengan lokasi file executable yang sebenarnya. Untuk semua pengguna, ubah HKEY_CURRENT_USER menjadi HKEY_LOCAL_MACHINE dan impor dengan hak administrator.


## Referensi

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)
