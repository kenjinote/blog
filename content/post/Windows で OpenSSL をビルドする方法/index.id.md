---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: 'Prosedur dan Cara Membangun Lingkungan untuk Build dan Instal OpenSSL di Lingkungan Windows'
slug: "Windows で OpenSSL をBangunする方法"
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Cara membangun OpenSSL dari sumber di Windows, menggunakan OpenSSL 3.5.9 sebagai contoh serta menjelaskan alat dan langkah build x64."
---

# Apa itu OpenSSL

Untuk menggunakan OpenSSL dalam aplikasi, Anda memerlukan header dan pustaka pengembangan. Anda dapat memperoleh distribusi biner atau membangun sumber sesuai kebutuhan; halaman ini membahas opsi build dari sumber.

Below, we will introduce the build procedure.
# Persiapan lingkungan pembangunan

- **Perl**

  Unduh `strawberry-perl-5.42.3.1-64bit.msi` dari [https://strawberryperl.com/](https://strawberryperl.com/). Versi terbaru seharusnya tidak masalah.

- **NASM**

  Unduh `3.02/nasm-3.02-win64.zip` dari `Download` di [https://www.nasm.us/](https://www.nasm.us/). Versi terbaru selain rc seharusnya tidak masalah.
  Setelah instalasi, Anda harus mendaftarkan folder tempat NASM diinstal ke variabel lingkungan PATH.

- **Visual Studio 2022** atau **Build Tools for Visual Studio 2022**

  Instal `Visual Studio 2022 Community` atau `Build Tools for Visual Studio 2022` dari [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# Prosedur pembangunan OpenSSL di Windows

1. Unduh dan ekstrak `openssl-3.5.9.tar.gz` dari [https://openssl-library.org/source/](https://openssl-library.org/source/). Jika Anda tidak dapat mengekstraknya, jalankan perintah `tar -xzf openssl-3.5.9.tar.gz` di command prompt.

Per 2026-11-25, OpenSSL 3.5.9 termasuk seri LTS 3.5 yang didukung hingga 2030-04-08. Saat membangun, periksa patch terbaru yang didukung di halaman unduhan resmi.

2. Gunakan Command Prompt Developer x64 Visual Studio. Jalankan sebagai administrator hanya jika Anda akan memasang di Program Files.
3. Buka folder yang diekstrak
4. Jalankan perintah berikut. *Ubah bagian `Community` sesuai dengan versi Visual Studio yang Anda instal.*
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
5. Jalankan perintah berikut
```
perl Configure VC-WIN64A
```
6. Jalankan perintah berikut (butuh waktu cukup lama)
```
nmake
```
7. Jalankan perintah berikut (butuh waktu cukup lama)
```
nmake test
```
8. Jalankan perintah berikut
```
nmake install
```

Jika berhasil, OpenSSL akan diinstal di `C:\Program Files\OpenSSL`.
Instalasi ke lokasi default ini memerlukan hak administrator. Untuk menghindari elevasi, tentukan prefix yang dapat ditulis saat konfigurasi.

Selesai.

# Referensi

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)