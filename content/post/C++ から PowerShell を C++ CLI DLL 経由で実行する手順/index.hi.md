---
title: '【VS2022】C++ से PowerShell चलाएं! C++/CLI DLL के माध्यम से एकीकरण प्रक्रिया'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Visual Studio 2022 में C++/CLI DLL से Windows PowerShell 5.1 चलाने की विधि; उपयुक्त .NET Framework, reference assemblies, runtime सीमाएँ और script सुरक्षा।'
---

# 🎯 C++ से C++/CLI DLL के माध्यम से PowerShell को निष्पादित करने के चरण (Visual Studio 2022 / C++)

## ✅ समग्र वास्तुकला

### 🔹 ① CLI रैपर DLL (C++/CLI)
PowerShell स्क्रिप्ट को निष्पादित करने की कार्यक्षमता प्रदान करता है।

### 🔹 ② /clr सक्षम वाला C++ कॉलर
PowerShell स्क्रिप्ट चलाने के लिए CLI DLL को कॉल करता है।

---

## 🔧 चरण 1: CLI रैपर DLL प्रोजेक्ट बनाना

### 1. प्रोजेक्ट बनाना
- [नया प्रोजेक्ट बनाएँ] → [C++] → **CLR क्लास लाइब्रेरी (.NET Framework)** 
- नाम: `PowerShellWrapper`

> 💡 यदि यह टेम्प्लेट प्रदर्शित नहीं होता है, तो ".NET डेस्कटॉप विकास" वर्कलोड स्थापित करें।

---

### 2. NuGet पैकेज जोड़ें

1. प्रोजेक्ट पर राइट-क्लिक करें → [NuGet पैकेज प्रबंधित करें]
2. `Microsoft.PowerShell.5.ReferenceAssemblies` NuGet पैकेज का संस्करण 1.1.0 जोड़ें। यह Windows PowerShell 5.1 के reference assemblies देता है।


---

### 3. CLI कोड कार्यान्वयन

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

## 🔧 चरण 2: /clr सक्षम करके कॉलर बनाएँ

### 1. C++ कंसोल ऐप प्रोजेक्ट बनाना
- नाम: `NativeApp`

### 2. संदर्भ सेटिंग

- प्रोजेक्ट पर राइट-क्लिक करें → [जोड़ें] → [संदर्भ] → प्रोजेक्ट → `PowerShellWrapper` जोड़ें
- [गुण] → [C/C++] → [कॉमन लैंग्वेज रनटाइम सपोर्ट] → **/clr** में बदलें

---

### 3. निष्पादन कोड (main.cpp)

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

## 💡 अतिरिक्त जानकारी (IDL / TLB / COM पंजीकरण)

- यह कॉन्फ़िगरेशन COM के बजाय सीधे .NET DLL को संदर्भित करता है, इसलिए **IDL, TLB, या COM पंजीकरण की आवश्यकता नहीं है** ।

---

## ✅ अंतिम वास्तुकला

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → DLL कॉल
```

## ⚠️ Runtime और सुरक्षा संबंधी बातें

लक्ष्य Windows मशीन पर Windows PowerShell 5.1 और संगत .NET Framework उपलब्ध होना चाहिए।

यह उदाहरण Windows PowerShell 5.1 और .NET Framework 4.7.2 या बाद के संस्करण के लिए है। Visual Studio Installer में “C++/CLI support for v143 build tools” इंस्टॉल करें और वही target framework चुनें।

यह उदाहरण PowerShell 7 के साथ नहीं चलता। उसके लिए उसी .NET runtime को लक्ष्य करने वाला अलग host बनाएँ या `pwsh` को child process के रूप में चलाएँ। आधुनिक .NET के C++/CLI प्रोजेक्ट DLL बनाते हैं।

`AddScript` दी गई string को code की तरह चलाता है। अविश्वसनीय input को उसमें न जोड़ें। उपयोगकर्ता के मानों के लिए fixed commands और parameters लें तथा सीमित runspace पर विचार करें। Script ऐप चलाने वाले उपयोगकर्ता के अधिकारों से चलता है। यह उदाहरण default Runspace का उपयोग करता है।


दोनों प्रोजेक्ट में एक ही .NET Framework target, configuration (Debug/Release) और platform architecture (x86/x64) रखें। `/clr` सक्षम करने पर caller mixed-mode executable बनता है, केवल native executable नहीं।
## आधिकारिक दस्तावेज़
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
