---
title: '【VS2022】從C++執行PowerShell！透過C++/CLI DLL的整合步驟'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '介紹如何在 Visual Studio 2022 中透過 C++/CLI DLL 裝載 Windows PowerShell 5.1，並說明相容的 .NET Framework、參考組件、執行限制與指令碼安全。'
---

# 🎯 從 C++ 透過 C++/CLI DLL 執行 PowerShell 的步驟（Visual Studio 2022 / C++）

## ✅ 整體架構

### 🔹 ① CLI 封裝 DLL（C++/CLI）
提供執行 PowerShell 腳本的功能。

### 🔹 ② 啟用 /clr 的 C++ 呼叫端
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
2. 加入 NuGet 套件 `Microsoft.PowerShell.5.ReferenceAssemblies` 1.1.0 版。它提供 Windows PowerShell 5.1 的參考組件。


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

## 🔧 步驟 2：建立啟用 /clr 的呼叫端

### 1. 建立 C++ 主控台應用程式專案
- 名稱：`NativeApp`

### 2. 參考設定

- 在專案上按一下右鍵 → [加入] → [參考] → [專案] → 新增 `PowerShellWrapper`
- [組態屬性] → [C/C++] → [Common Language Runtime 支援] → 變更為 **/clr** 

---

### 3. 執行程式碼（main.cpp）

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

## 💡 補充說明（IDL / TLB / COM 註冊）

- 此架構是直接參考 .NET DLL 而不是 COM，因此 **不需要 IDL、TLB 或是 COM 註冊** 。

---

## ✅ 最終架構

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → 呼叫 DLL
```

## ⚠️ 執行階段與安全注意事項

目標 Windows 電腦必須可使用 Windows PowerShell 5.1 與相容的 .NET Framework。

本範例適用於 Windows PowerShell 5.1 與 .NET Framework 4.7.2 或更新版本。請在 Visual Studio Installer 安裝「C++/CLI support for v143 build tools」，並選取相符的目標 Framework。

本範例不適用於 PowerShell 7。若要使用，請設計目標 .NET 執行階段相同的獨立主機，或將 `pwsh` 作為子處理程序啟動。以現代 .NET 為目標的 C++/CLI 專案會建置為 DLL。

`AddScript` 會將字串當成程式碼執行。切勿串接不可信的輸入。處理使用者提供的值時，請使用固定命令與參數，並考慮採用受限 Runspace。指令碼會以應用程式執行使用者的權限執行。 本範例使用預設 Runspace。


兩個專案應使用相同的 .NET Framework 目標版本、組態（Debug/Release）與平台架構（x86/x64）。啟用`/clr`後，呼叫端是混合模式可執行檔，而非純原生程式。
## 官方文件
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
