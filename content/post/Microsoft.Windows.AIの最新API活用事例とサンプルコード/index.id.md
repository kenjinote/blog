---
title: "Windows AI API saat ini: memilih Phi Silica, Windows ML, dan DirectML"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "Panduan November 2026 tentang Windows AI API, ketersediaan Phi Silica, Windows ML, DirectML, dan metrik kinerja NPU berdasarkan dokumentasi resmi Microsoft."
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows AI API saat ini: memilih Phi Silica, Windows ML, dan DirectML

> **Diperbarui 24 November 2026.** Windows AI API berubah cepat; panduan ini mengikuti dokumentasi Microsoft yang diperiksa pada tanggal tersebut. Contoh konteks percakapan dan streaming lama, versi NuGet yang dipatok, serta klaim bahwa DirectML memilih NPU tidak menggambarkan API saat ini dengan benar, sehingga dihapus.

## Windows AI API dan Phi Silica

Persyaratan perangkat keras, OS, dan Windows App SDK berbeda untuk setiap API. Phi Silica adalah model bahasa lokal untuk Windows, tetapi tidak tersedia di semua PC. Persyaratannya berbeda untuk Copilot+ PC dan GPU lain yang didukung. Phi Silica juga merupakan Limited Access Feature dan memiliki batasan wilayah. Periksa [dukungan API dan perangkat keras](https://learn.microsoft.com/en-us/windows/ai/apis) serta [panduan penyiapan](https://learn.microsoft.com/en-us/windows/ai/apis/get-started) sebelum memilihnya.

Jika model belum siap, jelaskan ukuran unduhan dan penggunaan jaringan, lalu minta persetujuan pengguna sebelum memulai penyiapan. Tangani perangkat yang tidak didukung dan fitur yang dinonaktifkan pengguna secara terpisah, serta sediakan alternatif. Microsoft mengumumkan rencana peralihan dari Phi Silica ke Aion Instruct; nama model dan tanggal ketersediaan dapat berubah.

## Contoh C# minimal

```csharp
using System;
using Microsoft.Windows.AI;
using Microsoft.Windows.AI.Text;

var state = LanguageModel.GetReadyState();
if (state == AIFeatureReadyState.NotReady)
{
    // Explain the download and obtain user consent before this call.
    var result = await LanguageModel.EnsureReadyAsync();
    if (result.Status != AIFeatureReadyResultState.Success)
        throw result.ExtendedError;
    state = LanguageModel.GetReadyState();
}
if (state != AIFeatureReadyState.Ready)
    throw new InvalidOperationException($"LanguageModel unavailable: {state}");

using LanguageModel model = await LanguageModel.CreateAsync();
var response = await model.GenerateResponseAsync("Explain what an NPU does.");
Console.WriteLine(response.Text);
```

## Model ONNX kustom dan perangkat keras

Untuk model ONNX kustom, Microsoft merekomendasikan Windows ML di Windows. Ini membantu memilih Execution Provider yang sesuai serta mengelola distribusinya. DirectML tetap didukung, tetapi pengembangan fitur baru telah beralih ke Windows ML. DirectML adalah jalur GPU berbasis Direct3D 12; `device_id = 0` tidak berarti NPU dipilih. Untuk NPU, ikuti panduan Windows ML dan Execution Provider vendor yang didukung.

## Memahami metrik kinerja

“40+ TOPS” adalah persyaratan NPU terkait kategori Copilot+ PC. TOPS saja tidak membandingkan kecepatan aplikasi; presisi, operasi yang didukung, dan kondisi daya juga berpengaruh. Jika laju memori sudah dalam MT/s, jangan kalikan dua lagi untuk kedua sisi DDR. Bus total 128-bit pada 8.533 MT/s memiliki laju teoretis `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`. Nilai nyata lebih rendah. Inferensi lokal hanya menghindari lalu lintas jaringan untuk operasi yang benar-benar dijalankan di perangkat; ini tidak menjamin seluruh aplikasi offline atau tidak mengirim data.

## Referensi resmi

- [Windows AI APIs: fitur dan perangkat keras](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Penyiapan aplikasi Windows AI](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Panduan Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Panduan pengembangan NPU](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [Status DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

Kode mengikuti dokumentasi Microsoft, tetapi belum dibangun di sini dengan Windows SDK. Periksa kembali SDK, OS, dan status Limited Access Feature.
