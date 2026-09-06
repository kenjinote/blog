---
title: "Cara Memanggil Microsoft.Windows.AI dari C++"
slug: "cara-memanggil-microsoft-windows-ai-dari-c++"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["Alat & Lingkungan Pengembangan"]
---

# 🎯 Cara Memanggil `Microsoft.Windows.AI` dari C++ [Dengan Contoh Kode]

Mulai dari Windows 10, Windows dilengkapi dengan standar **runtime yang dapat mengeksekusi model AI berformat ONNX**. Itu adalah **Windows ML (Windows.AI.MachineLearning)**.

Artikel ini menjelaskan secara rinci cara memanggil `Microsoft.Windows.AI.MachineLearning` dari **C++ (berbasis aplikasi Win32)**, lengkap dengan **contoh kode**.

---

## ✅ Persiapan

### ◾ Kebutuhan Sistem

* Windows 10 (1809+) atau Windows 11
* Visual Studio 2019 atau yang lebih baru (versi Community bisa digunakan)
* Dukungan C++/WinRT (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 atau yang lebih tinggi

---

## ✅ Struktur Proyek

Buat proyek dengan struktur berikut di Visual Studio.

* Jenis: Aplikasi Desktop Windows C++ (Proyek Kosong)
* Subsistem: Windows (`WinMain`)
* Tambahkan paket berikut melalui NuGet

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ Contoh Kode

Berikut ini adalah contoh minimal yang menggabungkan API Win32 dan `Windows.AI.MachineLearning` menggunakan `WinMain`.

> ※ Model ONNX yang digunakan adalah `model.onnx`, pastikan Anda menempatkannya di folder yang sama dengan file eksekusi.

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // Untuk tautan WinRT

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // Inisialisasi WinRT (MTA atau STA diperbolehkan)
    winrt::init_apartment();

    try {
        // Memuat file model
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // Membuat sesi
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // Input/Output model (input kosong untuk sementara di sini)
        // Sebenarnya, pengikatan diperlukan menggunakan TensorFloat, dll.

        // Menjalankan inferensi
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"Inferensi selesai", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"Error", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ Tambahan: Cara Menentukan Tensor Input dan Output

Tergantung pada modelnya, Anda mungkin perlu melakukan **pembuatan dan pengikatan Tensor** sebelum inferensi.

Contoh:

```cpp
// Mengubah array float 1D menjadi Tensor
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // Bentuk: [1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// Pengikatan input (sesuaikan dengan nama input model)
binding.Bind(L"input_0", tensor);
```

Demikian pula, output dapat diambil dengan `result.Outputs().Lookup(L"output_0")`.

---

## ✅ Catatan Debugging

* Jika file model tidak ada di folder eksekusi, `FileNotFoundException` akan muncul.
* Jika nama input/output tidak cocok, akan terjadi error `invalid_argument`.
* Spesifikasi I/O persis model dapat diperiksa dengan alat seperti [Netron](https://netron.app).

---

## ✅ Kesimpulan

| Item | Konten |
| ----- | ---------------------------------- |
| API yang Digunakan | Windows.AI.MachineLearning (WinRT) |
| Bahasa | C++ (Berbasis Win32) |
| Metode yang Disarankan | Melalui header C++/WinRT |
| Kelebihan | Model ONNX berjalan secara native, didukung GPU juga |
| Perhatian | Perhatikan nama input model dan bentuk Tensor |

---

## ✅ Alternatif: Bagi yang Tidak Ingin Menggunakan WinRT

* Dengan menggunakan `ONNX Runtime` buatan Microsoft, Anda dapat **sepenuhnya menangani model ONNX dari C++ tanpa WinRT sama sekali**.
* Mendukung cross-platform, memungkinkan kode bersama untuk Windows/Linux.

---

## 📌 Penutup

Windows ML (Microsoft.Windows.AI) adalah mesin inferensi AI tangguh yang dapat digunakan dengan baik bahkan dari C++. Jika Anda membutuhkan inferensi native di Windows, silakan dicoba.

Contoh spesifik pembuatan model ONNX dan pengikatan Tensor akan dijelaskan pada artikel berikutnya!
