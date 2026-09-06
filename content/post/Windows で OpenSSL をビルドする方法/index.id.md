---
title: "Cara Membangun OpenSSL di Windows"
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.png"
categories: ["Programming"]
---

# Apa itu OpenSSL

Ini adalah pustaka sumber terbuka yang menyediakan pemrosesan yang diperlukan untuk komunikasi terenkripsi.

Untuk menggunakannya dari sebuah program, kode sumber bahasa C dipublikasikan, jadi Anda perlu membangunnya dan membuat pustaka.

Di bawah ini kami akan memperkenalkan prosedur pembangunannya.

# Persiapan lingkungan pembangunan

- **Perl**

  Unduh `strawberry-perl-5.32.1.1-64bit.msi` dari [https://strawberryperl.com/](https://strawberryperl.com/). Versi terbaru seharusnya tidak masalah.

- **NASM**

  Unduh `2.16.01/nasm-2.16.01-win64.zip` dari `Download` di [https://www.nasm.us/](https://www.nasm.us/). Versi terbaru selain rc seharusnya tidak masalah.
  Setelah instalasi, Anda harus mendaftarkan folder tempat NASM diinstal ke variabel lingkungan PATH.

- **Visual Studio 2022** atau **Build Tools for Visual Studio 2022**

  Instal `Visual Studio 2022 Community` atau `Build Tools for Visual Studio 2022` dari [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# Prosedur pembangunan OpenSSL di Windows

1. Unduh dan ekstrak `openssl-3.1.0.tar.gz` dari [https://www.openssl.org/source/](https://www.openssl.org/source/). Jika Anda tidak dapat mengekstraknya, jalankan perintah `tar -xzf openssl-3.1.0.tar.gz` di command prompt.
2. Jalankan command prompt **sebagai administrator** 
3. Buka folder yang diekstrak
4. Jalankan perintah berikut. *Ubah bagian `Community` sesuai dengan versi Visual Studio yang Anda instal.*
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
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

Selesai.

# Referensi
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
