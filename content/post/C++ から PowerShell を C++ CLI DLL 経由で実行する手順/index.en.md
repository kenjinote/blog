---
title: '[VS2022] Execute PowerShell from C++! Integration Steps via C++/CLI DLL'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Host Windows PowerShell 5.1 from a C++/CLI DLL in Visual Studio 2022. Covers the matching .NET Framework target, reference assemblies, runtime limits, and script safety.'
---

# 🎯 Steps to Execute PowerShell from C++ via C++/CLI DLL (Visual Studio 2022 / C++)

## ✅ Overall Structure

### 🔹 ① CLI Wrapper DLL (C++/CLI)
Provides functionality to execute PowerShell scripts.

### 🔹 ② C++ caller with /clr enabled
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
2. Add the `Microsoft.PowerShell.5.ReferenceAssemblies` NuGet package, version 1.1.0. It provides reference assemblies for Windows PowerShell 5.1.


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

## 🔧 Step 2: Create the caller with /clr enabled

### 1. Create C++ Console App Project
- Name: `NativeApp`

### 2. Add Reference

- Right-click the project → [Add] → [Reference] → [Projects] → Add `PowerShellWrapper`
- [Configuration Properties] → [C/C++] → [Common Language Runtime Support] → Change to **/clr**

---

### 3. Execution Code (main.cpp)

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

## 💡 Note (IDL / TLB / COM Registration)

- Since this configuration references the .NET DLL directly instead of using COM, **IDL, TLB, and COM registration are not required**.

---

## ✅ Final Structure

```text
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → Call DLL
```

## ⚠️ Runtime and security notes

The target Windows machine must provide Windows PowerShell 5.1 and a compatible .NET Framework.

This example targets Windows PowerShell 5.1 and .NET Framework 4.7.2 or later. Install “C++/CLI support for v143 build tools” in Visual Studio Installer and select the matching target framework.

This example does not run PowerShell 7. For PowerShell 7, design a separate host targeting the same .NET runtime, or launch `pwsh` as a child process. C++/CLI projects targeting modern .NET build as DLLs.

`AddScript` executes its string as code. Never concatenate untrusted input. For user-supplied values, prefer fixed commands with parameters and consider a constrained runspace. Scripts run with the application's user permissions. This sample uses the default runspace.


Build both projects for the same .NET Framework target, configuration (Debug/Release), and platform architecture (x86/x64). Enabling `/clr` makes the caller a mixed-mode executable, not a native-only executable.
## Official documentation
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
