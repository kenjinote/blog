---
title: '[VS2022] Menjalankan PowerShell dari C++! Langkah Integrasi Melalui C++/CLI DLL'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Cara meng-host Windows PowerShell 5.1 dari DLL C++/CLI di Visual Studio 2022: target .NET Framework yang sesuai, reference assembly, batas runtime, dan keamanan skrip.'
---

# 🎯 Langkah-langkah Menjalankan PowerShell dari C++ melalui C++/CLI DLL (Visual Studio 2022 / C++)

## ✅ Struktur Keseluruhan

### 🔹 ① Pembungkus CLI DLL (C++/CLI)
Menyediakan fungsionalitas untuk menjalankan skrip PowerShell.

### 🔹 ② Pemanggil C++ dengan /clr aktif
Memanggil CLI DLL untuk menjalankan skrip PowerShell.

---

## 🔧 Langkah 1: Membuat Proyek Pembungkus CLI DLL

### 1. Membuat Proyek
- [Buat baru] → [C++] → **Pustaka Kelas CLR (.NET Framework)**
- Nama: `PowerShellWrapper`

> 💡 Jika templat ini tidak ditampilkan, instal beban kerja "Pengembangan desktop .NET".

---

### 2. Menambahkan Paket NuGet

1. Klik kanan pada proyek → [Kelola Paket NuGet]
2. Tambahkan paket NuGet `Microsoft.PowerShell.5.ReferenceAssemblies` versi 1.1.0. Paket ini menyediakan reference assembly untuk Windows PowerShell 5.1.


---

### 3. Implementasi Kode Sisi CLI

#### PowerShellWrapper.h

```cpp
#pragma once

using namespace System;

namespace PowerShellWrapper {
    public ref class PowerShellExecutor {
    public:
        String^ Execute(String^ script);
    };
}
```

#### PowerShellWrapper.cpp

```cpp
String^ PowerShellWrapper::PowerShellExecutor::Execute(String^ script)
{
    PowerShell^ ps = PowerShell::Create();
    try
    {
        ps->AddScript(script);
        Collection<PSObject^>^ results = ps->Invoke();
        if (ps->HadErrors)
        {
            String^ message = "PowerShell reported an error.";
            if (ps->Streams->Error->Count > 0)
                message = ps->Streams->Error[0]->ToString();
            throw gcnew InvalidOperationException(message);
        }

        System::Text::StringBuilder^ sb = gcnew System::Text::StringBuilder();
        for each (PSObject^ result in results)
            sb->AppendLine(result->ToString());

        return sb->ToString();
    }
    finally
    {
        delete ps;
    }
}
```

---

## 🔧 Langkah 2: Buat pemanggil dengan /clr aktif

### 1. Membuat Proyek Aplikasi Konsol C++
- Nama: `NativeApp`

### 2. Pengaturan Referensi

- Klik kanan pada proyek → [Tambahkan Referensi] → [Proyek] → tambahkan `PowerShellWrapper`
- [Properti Konfigurasi] → [C/C++] → [Dukungan Runtime Bahasa Umum] → ubah ke **/clr**

---

### 3. Kode Eksekusi (main.cpp)

```cpp
#using <System.dll>

using namespace System;
using namespace PowerShellWrapper;

int main()
{
    PowerShellExecutor^ executor = gcnew PowerShellExecutor();
    String^ result = executor->Execute("Get-Process | Select-Object -First 1");
    Console::WriteLine(result);
    return 0;
}
```

---

## 💡 Catatan Tambahan (Pendaftaran IDL / TLB / COM)

- Karena konfigurasi ini merujuk langsung ke .NET DLL daripada COM, **IDL, TLB, atau pendaftaran COM tidak diperlukan** .

---

## ✅ Struktur Akhir

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → Pemanggilan DLL
```

## ⚠️ Catatan runtime dan keamanan

Komputer Windows tujuan harus menyediakan Windows PowerShell 5.1 dan .NET Framework yang kompatibel.

Contoh ini menargetkan Windows PowerShell 5.1 dan .NET Framework 4.7.2 atau lebih baru. Instal “C++/CLI support for v143 build tools” di Visual Studio Installer dan pilih target framework yang sesuai.

Contoh ini tidak berjalan dengan PowerShell 7. Untuk itu, rancang host terpisah dengan target .NET runtime yang sama atau jalankan `pwsh` sebagai proses anak. Proyek C++/CLI untuk .NET modern dibuat sebagai DLL.

`AddScript` menjalankan string sebagai kode. Jangan pernah menggabungkan input yang tidak tepercaya. Untuk nilai dari pengguna, gunakan perintah tetap dengan parameter dan pertimbangkan runspace terbatas. Skrip berjalan dengan hak pengguna aplikasi. Contoh ini menggunakan runspace default.


Gunakan target .NET Framework, konfigurasi (Debug/Release), dan arsitektur platform (x86/x64) yang sama untuk kedua proyek. `/clr` membuat pemanggil menjadi executable mixed-mode, bukan native saja.
## Dokumentasi resmi
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
