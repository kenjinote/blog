---
title: "Saya Mencoba Menginstal Qt Extension Pack di Visual Studio Code"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
date: 2024-09-13T00:53:53+09:00
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.png"
categories: ["Alat & Lingkungan Pengembangan"]
---

# Memulai Pengembangan Qt di VSCode: Cara Menginstal Qt Extension Pack

Halo, saya Kenji.
Kali ini saya akan memperkenalkan "Cara mengatur lingkungan pengembangan Qt di Visual Studio Code (selanjutnya disebut VSCode)".

Akhir-akhir ini, selain Qt Creator resmi, semakin banyak orang yang ingin mengembangkan aplikasi Qt menggunakan VSCode yang ringan dan sangat dapat diperluas.
Bagi Anda yang merasa demikian, saya merekomendasikan ** "Qt Extension Pack" **.
Hanya dengan menginstal paket ekstensi ini, Anda akan mendapatkan semua ekstensi utama terkait Qt sekaligus.

---

## Target Pembaca

* Mereka yang ingin mulai mengembangkan aplikasi GUI menggunakan Qt
* Mereka yang ingin mengembangkan menggunakan VSCode daripada Qt Creator
* Mereka yang merasa repot mencari ekstensi satu per satu

---

## Prasyarat

* VSCode sudah terinstal
  ([Anda dapat mengunduhnya secara gratis dari situs web resmi](https://code.visualstudio.com/))
* Pustaka inti Qt sudah terinstal ([Situs web resmi Qt](https://www.qt.io/))

---

## Apa itu Qt Extension Pack?

Qt Extension Pack adalah paket ekstensi untuk VSCode.
Dengan menginstalnya, fitur-fitur berikut akan ditambahkan secara otomatis:

* Dukungan file `.ui` (Qt Designer)
* Sorotan sintaks untuk file `.pro` dan file `.qrc`
* Penyelesaian kode C++ untuk Qt, pembuatan, dan dukungan debugging
* Qt Resource Browser (referensi sumber daya)

---

## Langkah-langkah Instalasi

### 1. Buka VSCode

Pertama, jalankan VSCode.

### 2. Buka Tampilan Ekstensi

Klik bilah aktivitas di sebelah kiri (ikon blok persegi) untuk menampilkan "Ekstensi".

Atau Anda dapat menekan pintasan
`Ctrl + Shift + X`.

### 3. Cari "Qt Extension Pack"

Masukkan kata kunci berikut di bilah pencarian:

```
Qt Extension Pack
```

![img.png](img.png)

### 4. Klik Tombol Instal

Setelah paket yang dituju muncul, klik tombol "Instal".
Ini akan menginstal beberapa ekstensi berikut sekaligus:

* Qt Language Support
* QML Support
* Qt Designer Integration
* CMake Tools (wajib untuk pengembangan Qt berbasis CMake)

---

## Tambahan Pengaturan Proyek (Contoh CMake + Qt)

Jika Anda menggunakan Qt berbasis CMake, kami merekomendasikan kombinasi dengan ekstensi berikut:

* [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
* [CMake Language Support](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)

Selain itu, jika Anda menambahkan deskripsi berikut ke CMakeLists.txt, integrasi dengan Qt akan menjadi lancar:

```cmake
find_package(Qt6 REQUIRED COMPONENTS Widgets)
target_link_libraries(MyApp PRIVATE Qt6::Widgets)
```

---

## Bonus: Bagaimana cara membuka file .ui?

File `.ui` dapat diedit di Qt Designer.
Di VSCode, Anda dapat mengklik kanan file `.ui` → pilih `Open with Qt Designer` (Qt Designer harus disertakan dalam variabel lingkungan `PATH`).

---

## Kesimpulan

| Langkah | Deskripsi |
| -- | --------------------------- |
| 1 | Jalankan VSCode |
| 2 | Buka panel Ekstensi |
| 3 | Cari "Qt Extension Pack" |
| 4 | Klik tombol Instal |

Membangun lingkungan Qt di VSCode kini jauh lebih mudah dari sebelumnya.
Ia memiliki fitur yang cukup untuk menjadi alternatif bagi Qt Creator, dan disarankan bagi mereka yang ingin bekerja dengan ringan.

---

## Kumpulan Tautan yang Disarankan

* [Situs resmi Qt](https://www.qt.io/)
* [Qt Extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt)
* [Situs resmi VSCode](https://code.visualstudio.com/)
* [Ekstensi CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

---

## Akhir Kata

Ke depannya, saya berencana untuk terus mengembangkan menggunakan alat UI Qt dan QML di lingkungan ini.
Lain kali, saya berencana untuk menjelaskan ** cara membangun & menjalankan aplikasi Hello World di Qt dari VSCode **.

Sampai jumpa!
