---
title: "خطوات تشغيل PowerShell من C++ عبر C++/CLI DLL"
slug: "خطوات تشغيل PowerShell من C++ عبر C++ CLI DLL"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["البرمجة"]
---

# 🎯 خطوات تشغيل PowerShell من C++ عبر C++/CLI DLL (Visual Studio 2022 / C++)

## ✅ الهيكل العام

### 🔹 ① غلاف CLI DLL (C++/CLI)
يوفر وظيفة لتشغيل نصوص PowerShell.

### 🔹 ② الجانب المتصل بـ Native C++
يستدعي CLI DLL لتشغيل نصوص PowerShell.

---

## 🔧 الخطوة 1: إنشاء مشروع غلاف CLI DLL

### 1. إنشاء المشروع
- [إنشاء جديد] → [C++] → **CLR Class Library (.NET Framework)**
- الاسم: `PowerShellWrapper`

> 💡 إذا لم يظهر هذا القالب، قم بتثبيت بيئة عمل ".NET desktop development".

---

### 2. إضافة حزمة NuGet

1. انقر بزر الماوس الأيمن على المشروع → [إدارة حزم NuGet]
2. ابحث عن `System.Management.Automation` وقم بتثبيته
   (الإصدار 5.x أو 7.x)

---

### 3. تنفيذ الكود من جانب CLI

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

## 🔧 الخطوة 2: الاستدعاء من جانب Native C++

### 1. إنشاء مشروع تطبيق وحدة تحكم C++
- الاسم: `NativeApp`

### 2. إعدادات المرجع

- انقر بزر الماوس الأيمن على المشروع → [إضافة مرجع] → [مشاريع] → أضف `PowerShellWrapper`
- [خصائص التكوين] → [C/C++] → [دعم وقت تشغيل اللغة المشتركة] → التغيير إلى **/clr**

---

### 3. كود التنفيذ (main.cpp)

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

## 💡 ملاحظات إضافية (IDL / TLB / تسجيل COM)

- نظراً لأن هذا التكوين يشير مباشرة إلى .NET DLL بدلاً من COM، فإنه **لا حاجة إلى IDL أو TLB أو تسجيل COM** .

---

## ✅ التكوين النهائي

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → استدعاء DLL
```
---
