---
title: "從 C++ 透過 C++/CLI DLL 執行 PowerShell 的步驟"
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["程式設計"]
---

# 🎯 從 C++ 透過 C++/CLI DLL 執行 PowerShell 的步驟（Visual Studio 2022 / C++）

## ✅ 整體架構

### 🔹 ① CLI 封裝 DLL（C++/CLI）
提供執行 PowerShell 腳本的功能。

### 🔹 ② 原生 C++ 呼叫端
呼叫 CLI DLL 以執行 PowerShell 腳本。

---

## 🔧 步驟 1：建立 CLI 封裝 DLL 專案

### 1. 建立專案
- [建立新專案] → [C++] → **CLR 類別庫 (.NET Framework)** 
- 名稱：`PowerShellWrapper`

> 💡 如果未顯示此範本，請安裝「.NET 桌面開發」工作負載。

---

### 2. 新增 NuGet 套件

1. 在專案上按一下右鍵 → [管理 NuGet 套件]
2. 搜尋並安裝 `System.Management.Automation`  
   （版本 5.x 或 7.x）

---

### 3. CLI 端程式碼實作

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

## 🔧 步驟 2：從原生 C++ 端呼叫

### 1. 建立 C++ 主控台應用程式專案
- 名稱：`NativeApp`

### 2. 參考設定

- 在專案上按一下右鍵 → [加入] → [參考] → [專案] → 新增 `PowerShellWrapper`
- [組態屬性] → [C/C++] → [Common Language Runtime 支援] → 變更為 **/clr** 

---

### 3. 執行程式碼（main.cpp）

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

## 💡 補充說明（IDL / TLB / COM 註冊）

- 此架構是直接參考 .NET DLL 而不是 COM，因此 **不需要 IDL、TLB 或是 COM 註冊** 。

---

## ✅ 最終架構

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → 呼叫 DLL
```
---
