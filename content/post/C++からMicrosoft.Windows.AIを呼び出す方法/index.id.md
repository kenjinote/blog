---
title: '[API Lama] Memuat Model ONNX dari C++ dengan Windows ML'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Pelajari cara memuat model ONNX dari C++/WinRT dengan API Windows ML lama untuk Windows 10 versi 1809 dan yang lebih baru. Artikel ini membedakannya dari API terkini dan menjelaskan bahwa inferensi memerlukan binding input khusus model.'
---

# 🎯 Memuat model ONNX dari C++ dengan API Windows ML lama

> **Cakupan: API lama.** Artikel ini menggunakan API `Windows.AI.MachineLearning` yang diperkenalkan bersama Windows 10 versi 1809. API tersebut telah [digantikan oleh API Windows ML terkini](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference). Untuk aplikasi baru, ikuti [panduan memulai Windows ML terkini dari Microsoft](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started). Kode berikut hanya memuat model; kode ini tidak menjalankan inferensi. Untuk contoh inferensi lengkap, lihat [tutorial C++ desktop Microsoft](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop).

## ✅ Persiapan

### ◾ Kebutuhan Sistem

* Windows 10 (1809+) atau Windows 11
* Visual Studio 2019 atau yang lebih baru (versi Community bisa digunakan)
* Integrasi C++/WinRT untuk Windows SDK lama
* Windows SDK 10.0.17763.0 atau yang lebih tinggi

---

## ✅ Struktur Proyek

Untuk API lama ini, gunakan Windows 10 versi 1809 (build 17763) atau yang lebih baru, Windows SDK yang kompatibel, Visual Studio dengan workload desktop C++, dan C++/WinRT. Jangan samakan paket Windows ML terkini dengan dependensi API lama ini. Lihat [panduan deployment](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app) untuk paket dan persyaratan terkini.

---

## ✅ Contoh Kode

> Ini hanya memeriksa pemuatan model. Nama, tipe, dan bentuk input berbeda untuk setiap model ONNX; memanggil `EvaluateAsync` tanpa mengikat input yang diwajibkan umumnya tidak menjalankan inferensi.

### `main.cpp`

Tetapkan path absolut sebenarnya untuk `model.onnx`. Path relatif dapat diselesaikan dari direktori kerja saat ini, yang belum tentu direktori executable.

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp")

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE, HINSTANCE, LPSTR, int)
{
    winrt::init_apartment();

    try {
        // Replace this with the absolute path to your ONNX model.
        constexpr wchar_t modelPath[] = L"C:\\path\\to\\model.onnx";
        auto modelFile = StorageFile::GetFileFromPathAsync(modelPath).get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        MessageBoxW(nullptr, L"Model loaded", L"Legacy Windows ML", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBoxW(nullptr, ex.message().c_str(), L"Error", MB_OK | MB_ICONERROR);
        return static_cast<int>(ex.code().value);
    }

    return 0;
}
```

## ✅ Tambahan: Contoh binding input model

Cuplikan berikut menunjukkan pola binding input. Sesuaikan `data_0`, tipe, bentuk, dan nilainya dengan model. Cuplikan ini saja bukan program lengkap untuk memuat model dan mengembalikan hasil inferensi.

```cpp
#include <cstdint>
#include <vector>
#include <winrt/Windows.AI.MachineLearning.h>

using namespace Windows::AI::MachineLearning;

void RunWithInput(LearningModel const& model)
{
    LearningModelSession session{model};
    LearningModelBinding binding{session};

    // Example only: replace the feature name, type, shape, and values for your model.
    std::vector<float> inputData{0.5f, 0.3f, 0.2f};
    std::vector<int64_t> shape{1, 3};
    TensorFloat tensor = TensorFloat::CreateFromArray(shape, inputData);
    binding.Bind(L"data_0", tensor);

    auto result = session.Evaluate(binding, L"example");
    // Read result.Outputs() using the output feature name and type defined by the model.
}
```

Nama dan tipe output juga khusus untuk model. Periksa input dan output ONNX dengan alat seperti Netron, lalu ikat nilai yang sesuai.

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ Kesimpulan

Contoh ini hanya menunjukkan pemuatan model dengan API lama `Windows.AI.MachineLearning`. Contoh ini tidak menjamin eksekusi GPU atau inferensi yang berhasil untuk model tertentu. Untuk pengembangan baru, pilih API Windows ML terkini dan periksa persyaratan paket serta OS di panduan resmi.

## ✅ Alternatif: Bagi yang Tidak Ingin Menggunakan WinRT

* Dengan menggunakan `ONNX Runtime` buatan Microsoft, Anda dapat **sepenuhnya menangani model ONNX dari C++ tanpa WinRT sama sekali**.
* Mendukung cross-platform, memungkinkan kode bersama untuk Windows/Linux.

---

## 📌 Penutup

Contoh ini hanya menunjukkan pemuatan model dengan API lama `Windows.AI.MachineLearning`. Contoh ini tidak menjamin eksekusi GPU atau inferensi yang berhasil untuk model tertentu. Untuk pengembangan baru, pilih API Windows ML terkini dan periksa persyaratan paket serta OS di panduan resmi.
