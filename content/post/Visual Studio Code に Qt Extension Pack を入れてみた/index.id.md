---
title: "Memulai Qt di VS Code: Memasang dan Mengonfigurasi Ekstensi Qt"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "Pilih paket ekstensi Qt resmi untuk VS Code, lalu konfigurasi Qt SDK, CMake, dan toolchain."
---

# Menggunakan Qt dengan VS Code

Qt Extension for VS Code resmi memungkinkan Anda mengembangkan aplikasi Qt, termasuk proyek Qt Widgets dan Qt Quick, di VS Code. Paket ekstensi menggabungkan beberapa ekstensi Qt. Isi paket dan fitur yang dijelaskan dalam versi lama artikel ini telah berubah; panduan ini mengikuti dokumentasi Qt terbaru.

Qt Creator dan VS Code sama-sama merupakan pilihan. Tidak ada yang selalu menggantikan yang lain; pilih sesuai alat yang digunakan dan kebutuhan proyek.

## Prasyarat

- Visual Studio Code
- Qt 6 SDK untuk OS dan arsitektur target, termasuk modul dan alat yang diperlukan (seperti Qt Widgets Designer)
- Untuk pengembangan C++, CMake serta compiler dan toolchain build C++ yang kompatibel

Ekstensi tidak memasang Qt SDK atau compiler C++. Pasang Qt, CMake, dan compiler secara terpisah dengan versi yang kompatibel.

## Memasang paket ekstensi

1. Buka tampilan Extensions di VS Code (ikon di Activity Bar atau `Ctrl+Shift+X`).
2. Cari `Qt extension packs`.
3. Pilih paket yang sesuai dengan proyek, lalu tekan Install. Qt C++ ditujukan untuk Qt C++/Qt Quick, Qt Python untuk Qt for Python, dan Qt WebAssembly untuk proyek WebAssembly. Anda juga dapat memasang `Qt Extension Pack` yang berisi semua ekstensi Qt.

Pemasangan paket Qt juga memasang `CMake For VisualStudio Code` dan `CMake Tools` secara otomatis. CMake, compiler, dan Qt SDK tetap harus dipasang secara terpisah.

## Mengonfigurasi Qt dan CMake untuk proyek

Jika Qt tidak dipasang di lokasi default, jalankan `Qt: Register Qt installation` dari Command Palette untuk mendaftarkannya. Lalu jalankan `Qt: Scan for kits` dan pilih kit yang cocok dengan versi Qt serta toolchain Anda. Untuk proyek CMake, dokumentasi Qt menyarankan penggunaan CMake Presets jika memungkinkan.

Contoh berikut adalah aplikasi Qt Widgets minimal. Simpan `main.cpp` dan `CMakeLists.txt` dalam folder yang sama.

```cpp
#include <QApplication>
#include <QLabel>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QLabel label("Hello Qt");
    label.show();
    return app.exec();
}
```

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyQtApp VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)
qt_standard_project_setup()

qt_add_executable(MyQtApp main.cpp)
target_link_libraries(MyQtApp PRIVATE Qt6::Widgets)
```



Ekstensi Qt juga mendukung pengeditan file `.ui` dengan Qt Widgets Designer. Nama menu dan langkah dapat berubah antarversi; lihat panduan resmi untuk prosedur terbaru. Ekstensi mengumpulkan data penggunaan anonim; [ringkasan resmi](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection) menjelaskan data yang dikumpulkan dan yang tidak.

## Referensi

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
