---
title: '【VS2022】تشغيل PowerShell من C++! خطوات التكامل عبر C++/CLI DLL'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'شرح استضافة Windows PowerShell 5.1 من مكتبة C++/CLI في Visual Studio 2022، مع إطار عمل .NET المناسب والتجميعات المرجعية وحدود التشغيل وأمان السكربتات.'
---

# 🎯 خطوات تشغيل PowerShell من C++ عبر C++/CLI DLL (Visual Studio 2022 / C++)

## ✅ الهيكل العام

### 🔹 ① غلاف CLI DLL (C++/CLI)
يوفر وظيفة لتشغيل نصوص PowerShell.

### 🔹 ② جانب استدعاء C++ مع تمكين /clr
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
2. أضف حزمة NuGet ‏`Microsoft.PowerShell.5.ReferenceAssemblies` بالإصدار 1.1.0؛ فهي توفر التجميعات المرجعية لـ Windows PowerShell 5.1.


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

## 🔧 الخطوة 2: إنشاء المستدعي مع تمكين /clr

### 1. إنشاء مشروع تطبيق وحدة تحكم C++
- الاسم: `NativeApp`

### 2. إعدادات المرجع

- انقر بزر الماوس الأيمن على المشروع → [إضافة مرجع] → [مشاريع] → أضف `PowerShellWrapper`
- [خصائص التكوين] → [C/C++] → [دعم وقت تشغيل اللغة المشتركة] → التغيير إلى **/clr**

---

### 3. كود التنفيذ (main.cpp)

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

## 💡 ملاحظات إضافية (IDL / TLB / تسجيل COM)

- نظراً لأن هذا التكوين يشير مباشرة إلى .NET DLL بدلاً من COM، فإنه **لا حاجة إلى IDL أو TLB أو تسجيل COM** .

---

## ✅ التكوين النهائي

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → استدعاء DLL
```

## ⚠️ ملاحظات حول بيئة التشغيل والأمان

يجب أن يتوفر على جهاز Windows المستهدف Windows PowerShell 5.1 وإطار عمل .NET متوافق.

يستهدف هذا المثال Windows PowerShell 5.1 و.NET Framework 4.7.2 أو أحدث. ثبّت مكوّن C++/CLI لـ v143 من Visual Studio Installer واضبط إطار العمل المستهدف وفقاً لذلك.

لا يعمل هذا المثال مع PowerShell 7. لاستخدامه، صمّم مضيفاً منفصلاً يستهدف إصدار .NET نفسه أو شغّل `pwsh` كعملية فرعية. تُبنى مشاريع C++/CLI الموجهة إلى .NET الحديث كملفات DLL.

تنفذ `AddScript` السلسلة البرمجية كتعليمات. لا تدمج فيها إدخالاً غير موثوق. استخدم أوامر ثابتة ومعلمات للقيم التي يقدمها المستخدم، وفكّر في Runspace مقيّد. تعمل السكربتات بصلاحيات مستخدم التطبيق. يستخدم هذا المثال بيئة Runspace الافتراضية.


استخدم إطار عمل .NET وإعداد البناء والمعمارية نفسيهما (x86/x64) للمشروعين. يؤدي تمكين `/clr` إلى إنشاء ملف تنفيذي مختلط، وليس ملفاً أصلياً فقط.
## الوثائق الرسمية
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
