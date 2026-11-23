---
title: '【VS2022】从C++执行PowerShell！通过C++/CLI DLL协作的步骤'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '介绍如何在 Visual Studio 2022 中通过 C++/CLI DLL 宿主运行 Windows PowerShell 5.1，并说明兼容的 .NET Framework、引用程序集、运行限制和脚本安全。'
---

# 🎯 通过 C++/CLI DLL 从 C++ 执行 PowerShell 的步骤（Visual Studio 2022 / C++）

## ✅ 整体架构

### 🔹 ① CLI 包装 DLL (C++/CLI)
提供执行 PowerShell 脚本的功能。

### 🔹 ② 启用 /clr 的 C++ 调用端
调用 CLI DLL 以执行 PowerShell 脚本。

---

## 🔧 步骤 1：创建 CLI 包装 DLL 项目

### 1. 创建项目
- [新建项目] → [C++] → **CLR 类库 (.NET Framework)**
- 名称：`PowerShellWrapper`

> 💡 如果未显示此模板，请安装“.NET 桌面开发”工作负载。

---

### 2. 添加 NuGet 包

1. 右键单击项目 → [管理 NuGet 程序包]
2. 添加 NuGet 包 `Microsoft.PowerShell.5.ReferenceAssemblies` 1.1.0 版。它提供 Windows PowerShell 5.1 的引用程序集。


---

### 3. CLI 端代码实现

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

## 🔧 步骤 2：创建启用 /clr 的调用端

### 1. 创建 C++ 控制台应用项目
- 名称：`NativeApp`

### 2. 添加引用

- 右键单击项目 → [添加] → [引用] → [项目] → 添加 `PowerShellWrapper`
- [配置属性] → [C/C++] → [常规] → [公共语言运行时支持] → 更改为 **/clr**

---

### 3. 执行代码 (main.cpp)

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

## 💡 补充说明（IDL / TLB / COM 注册）

- 由于此架构直接引用 .NET DLL 而不是 COM，因此 **无需 IDL、TLB 或 COM 注册** 。

---

## ✅ 最终结构

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → DLL 调用
```

## ⚠️ 运行时与安全注意事项

目标 Windows 计算机必须可用 Windows PowerShell 5.1 和兼容的 .NET Framework。

本示例面向 Windows PowerShell 5.1 和 .NET Framework 4.7.2 或更高版本。请在 Visual Studio Installer 中安装“C++/CLI support for v143 build tools”，并选择匹配的目标框架。

本示例不适用于 PowerShell 7。若要使用它，请设计目标 .NET 运行时相同的独立宿主，或将 `pwsh` 作为子进程启动。面向现代 .NET 的 C++/CLI 项目会生成 DLL。

`AddScript` 会把字符串作为代码执行。切勿拼接不可信输入。处理用户提供的值时，应使用固定命令和参数，并考虑采用受限 Runspace。脚本以应用运行用户的权限执行。 本示例使用默认 Runspace。


两个项目应使用相同的 .NET Framework 目标版本、配置（Debug/Release）和平台架构（x86/x64）。启用`/clr`后，调用端是混合模式可执行文件，而非纯原生程序。
## 官方文档
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
