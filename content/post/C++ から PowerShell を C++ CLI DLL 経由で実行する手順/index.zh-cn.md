---
title: '通过 C++/CLI DLL 从 C++ 执行 PowerShell 的步骤'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["编程"]
---

# 🎯 通过 C++/CLI DLL 从 C++ 执行 PowerShell 的步骤（Visual Studio 2022 / C++）

## ✅ 整体架构

### 🔹 ① CLI 包装 DLL (C++/CLI)
提供执行 PowerShell 脚本的功能。

### 🔹 ② 原生 C++ 调用方
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
2. 搜索并安装 `System.Management.Automation`  
   （版本 5.x 或 7.x）

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

## 🔧 步骤 2：从原生 C++ 端调用

### 1. 创建 C++ 控制台应用项目
- 名称：`NativeApp`

### 2. 添加引用

- 右键单击项目 → [添加] → [引用] → [项目] → 添加 `PowerShellWrapper`
- [配置属性] → [C/C++] → [常规] → [公共语言运行时支持] → 更改为 **/clr**

---

### 3. 执行代码 (main.cpp)

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

## 💡 补充说明（IDL / TLB / COM 注册）

- 由于此架构直接引用 .NET DLL 而不是 COM，因此 **无需 IDL、TLB 或 COM 注册**。

---

## ✅ 最终结构

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → DLL 调用
```
---
