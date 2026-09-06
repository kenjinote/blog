---
title: "C++ से C++/CLI DLL के माध्यम से PowerShell को निष्पादित करने के चरण"
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["प्रोग्रामिंग"]
---

# 🎯 C++ से C++/CLI DLL के माध्यम से PowerShell को निष्पादित करने के चरण (Visual Studio 2022 / C++)

## ✅ समग्र वास्तुकला

### 🔹 ① CLI रैपर DLL (C++/CLI)
PowerShell स्क्रिप्ट को निष्पादित करने की कार्यक्षमता प्रदान करता है।

### 🔹 ② नेटिव C++ कॉलर
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
2. `System.Management.Automation` खोजें और स्थापित करें  
   (संस्करण 5.x या 7.x)

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

## 🔧 चरण 2: नेटिव C++ से कॉल करना

### 1. C++ कंसोल ऐप प्रोजेक्ट बनाना
- नाम: `NativeApp`

### 2. संदर्भ सेटिंग

- प्रोजेक्ट पर राइट-क्लिक करें → [जोड़ें] → [संदर्भ] → प्रोजेक्ट → `PowerShellWrapper` जोड़ें
- [गुण] → [C/C++] → [कॉमन लैंग्वेज रनटाइम सपोर्ट] → **/clr** में बदलें

---

### 3. निष्पादन कोड (main.cpp)

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

## 💡 अतिरिक्त जानकारी (IDL / TLB / COM पंजीकरण)

- यह कॉन्फ़िगरेशन COM के बजाय सीधे .NET DLL को संदर्भित करता है, इसलिए **IDL, TLB, या COM पंजीकरण की आवश्यकता नहीं है** ।

---

## ✅ अंतिम वास्तुकला

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → DLL कॉल
```
---
