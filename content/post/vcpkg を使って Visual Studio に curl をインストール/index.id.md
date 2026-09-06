---
title: "[Untuk Pemula] Langkah-langkah menginstal libcurl (dengan dukungan OpenSSL) di Visual Studio menggunakan vcpkg"
slug: "vcpkg を使って Visual Studio に curl をインストール"
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---

## Jika Anda ingin menggunakan libcurl (dengan dukungan OpenSSL) di Visual Studio, menggunakan vcpkg adalah cara yang mudah dan sangat direkomendasikan

`libcurl` sering digunakan ketika Anda ingin menangani komunikasi HTTP dalam C++. Tetapi menyesuaikan pengaturan build dan dependensi seringkali merepotkan.

Di saat-saat seperti itulah, alat manajemen pustaka C++ dari Microsoft yaitu ** "vcpkg" ** sangat berguna.
Kali ini, saya akan memperkenalkan langkah-langkah untuk menggunakan `vcpkg` guna menginstal `libcurl` (dengan dukungan OpenSSL) sehingga dapat digunakan dengan lancar di Visual Studio.

---

### Instalasi vcpkg (Hanya bagi yang belum menginstalnya)

Pertama-tama, mari kita instal `vcpkg`. Silakan jalankan langkah-langkah berikut di PowerShell.

```powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
```

※ Jika Git belum terinstal, silakan instal dari [Situs resmi Git](https://git-scm.com/).

---

### Instalasi libcurl (Dukungan OpenSSL)

Selanjutnya, kita akan menggunakan vcpkg untuk menginstal `libcurl`. Untuk menentukan versi 64-bit yang mendukung OpenSSL, jalankan perintah berikut.

```powershell
vcpkg install curl[ssl] --triplet x64-windows
```

Ketika Anda menjalankan perintah ini, dependensi yang diperlukan (seperti OpenSSL) juga akan diatur secara otomatis.

---

### Pengaturan Integrasi Visual Studio

Agar pustaka yang diinstal dengan vcpkg dapat dengan mudah digunakan dari proyek Visual Studio Anda, lakukan pengaturan integrasi dengan perintah berikut.

```powershell
vcpkg integrate install
```

Setelah Anda mengatur ini, Anda akan secara otomatis dapat menggunakan `#include <curl/curl.h>` dalam proyek Visual Studio Anda, dan Anda tidak perlu lagi mengatur jalur pustaka atau pengaturan linker secara manual.

---

## Penutup

Sekarang Anda siap untuk menggunakan `libcurl` (dengan dukungan OpenSSL) di Visual Studio.

* Dengan menggunakan vcpkg, Anda dapat mengelola dependensi yang merepotkan sekaligus
* Instal libcurl dengan mudah menggunakan `vcpkg install curl[ssl] --triplet x64-windows`
* Integrasi otomatis dengan Visual Studio menggunakan `vcpkg integrate install`

Setelah itu, masukkan header dalam proyek Anda dan mulailah pengembangan menggunakan API libcurl.
Manfaatkan vcpkg yang nyaman ini untuk secara drastis meningkatkan efisiensi pengembangan Anda.
