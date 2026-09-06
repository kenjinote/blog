---
title: "Langkah-langkah Menjalankan PowerShell dari C++ melalui C++/CLI DLL"
slug: "Langkah-langkah Menjalankan PowerShell dari C++ melalui C++ CLI DLL"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["Pemrograman"]
---

# 🎯 Langkah-langkah Menjalankan PowerShell dari C++ melalui C++/CLI DLL (Visual Studio 2022 / C++)

## ✅ Struktur Keseluruhan

### 🔹 ① Pembungkus CLI DLL (C++/CLI)
Menyediakan fungsionalitas untuk menjalankan skrip PowerShell.

### 🔹 ② Pemanggil Native C++
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
2. Cari dan instal `System.Management.Automation`  
   (versi 5.x atau 7.x)

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
#include "PowerShellWrapper.h"
using namespace System;
using namespace System::Management::Automation;
using namespace System::Collections::ObjectModel;

String^ PowerShellWrapper::PowerShellExecutor::Execute(String^ script)
{
    PowerShell^ ps = PowerShell::Create();
    ps->AddScript(script);
    Collection<PSObject^>^ results = ps->Invoke();

    System::Text::StringBuilder^ sb = gcnew System::Text::StringBuilder();
    for each (PSObject^ result in results)
    {
        sb->AppendLine(result->ToString());
    }

    return sb->ToString();
}
```

---

## 🔧 Langkah 2: Memanggil dari Sisi Native C++

### 1. Membuat Proyek Aplikasi Konsol C++
- Nama: `NativeApp`

### 2. Pengaturan Referensi

- Klik kanan pada proyek → [Tambahkan Referensi] → [Proyek] → tambahkan `PowerShellWrapper`
- [Properti Konfigurasi] → [C/C++] → [Dukungan Runtime Bahasa Umum] → ubah ke **/clr**

---

### 3. Kode Eksekusi (main.cpp)

```cpp
#using <System.dll>
#using "..\\PowerShellWrapper\\Debug\\PowerShellWrapper.dll"

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
├── NativeApp (C++ EXE)
    └── main.cpp → Pemanggilan DLL
```
---
