---
title: 'Steps to Execute PowerShell from C++ via C++/CLI DLL'
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["Programming"]
---

# 🎯 Steps to Execute PowerShell from C++ via C++/CLI DLL (Visual Studio 2022 / C++)

## ✅ Overall Structure

### 🔹 ① CLI Wrapper DLL (C++/CLI)
Provides functionality to execute PowerShell scripts.

### 🔹 ② Native C++ Caller
Calls the CLI DLL to execute PowerShell scripts.

---

## 🔧 Step 1: Create CLI Wrapper DLL Project

### 1. Create Project
- [Create a new project] → [C++] → **CLR Class Library (.NET Framework)**
- Name: `PowerShellWrapper`

> 💡 If this template is not displayed, install the ".NET desktop development" workload.

---

### 2. Add NuGet Package

1. Right-click the project → [Manage NuGet Packages]
2. Search and install `System.Management.Automation`  
   (Version 5.x or 7.x)

---

### 3. Implement CLI Side Code

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

## 🔧 Step 2: Call from Native C++

### 1. Create C++ Console App Project
- Name: `NativeApp`

### 2. Add Reference

- Right-click the project → [Add] → [Reference] → [Projects] → Add `PowerShellWrapper`
- [Configuration Properties] → [C/C++] → [Common Language Runtime Support] → Change to **/clr**

---

### 3. Execution Code (main.cpp)

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

## 💡 Note (IDL / TLB / COM Registration)

- Since this configuration references the .NET DLL directly instead of using COM, **IDL, TLB, and COM registration are not required**.

---

## ✅ Final Structure

```text
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → Call DLL
```
---
