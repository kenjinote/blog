---
title: 'Cara membuat pintasan untuk mematikan Windows'
slug: "Windows をMatikanするPintasanを作成する方法"
date: 2023-04-11T17:03:32+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["Windows", "Mematikan", "Pintasan"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Buat pintasan desktop yang memulai proses mematikan Windows 10 atau Windows 11 dengan dua klik.'
---
Langkah ini berlaku untuk Windows 10 dan Windows 11. Nama menu dapat sedikit berbeda menurut versi dan bahasa tampilan.

## Membuat pintasan

#### 1. Klik kanan area kosong di desktop, lalu pilih `New` > `Shortcut`.

#### 2. Masukkan perintah berikut sebagai lokasi item, lalu klik `Next`.

```text
shutdown.exe /s /t 0
```

#### 3. Beri nama pintasan, misalnya `Shut down`, lalu klik `Finish`.

## Mengubah ikon (opsional)

Klik kanan pintasan, lalu pilih `Properties` > `Change Icon`. Pilih ikon dari `%SystemRoot%\System32\SHELL32.dll`, lalu klik `OK`.

Simpan pekerjaan sebelum menggunakan pintasan ini. Pintasan akan langsung memulai proses shutdown Windows tanpa langkah konfirmasi tambahan. `/s` meminta shutdown dan `/t 0` berarti tanpa jeda. Perintah ini tidak memakai `/f`, sehingga aplikasi dapat menutup secara normal dan memberi peringatan jika ada pekerjaan yang belum disimpan.

[**Microsoft Learn: perintah shutdown (bahasa Inggris)**](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown/)
