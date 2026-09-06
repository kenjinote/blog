---
title: "【للمبتدئين】خطوات تثبيت libcurl (مع دعم OpenSSL) في Visual Studio باستخدام vcpkg"
slug: "vcpkg を使って Visual Studio に curl をインストール"
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---

## إذا كنت تريد استخدام libcurl (مع دعم OpenSSL) في Visual Studio، فإن استخدام vcpkg سهل وموصى به

غالبًا ما يتم استخدام `libcurl` عندما تريد التعامل مع اتصالات HTTP في C++. لكن ضبط إعدادات البناء والتبعيات يمكن أن يكون مزعجًا بشكل غير متوقع.

في مثل هذه الأوقات، تكون أداة إدارة مكتبات C++ من Microsoft ** "vcpkg" ** مفيدة.
هذه المرة، سأقدم خطوات استخدام `vcpkg` لتثبيت `libcurl` (مع دعم OpenSSL) واستخدامه بسلاسة في Visual Studio.

---

### تثبيت vcpkg (فقط لمن لم يقم بتثبيته بعد)

أولاً، دعنا نثبت `vcpkg`. يرجى تنفيذ الخطوات التالية في PowerShell.

```powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
```

※ إذا لم يكن لديك Git مثبتًا بعد، يرجى تثبيته من [الموقع الرسمي لـ Git](https://git-scm.com/).

---

### تثبيت libcurl (مع دعم OpenSSL)

بعد ذلك، سنستخدم vcpkg لتثبيت `libcurl`. لتحديد إصدار 64 بت المتوافق مع OpenSSL، قم بتشغيل الأمر التالي.

```powershell
vcpkg install curl[ssl] --triplet x64-windows
```

عند تشغيل هذا الأمر، سيتم أيضًا إعداد التبعيات الضرورية (مثل OpenSSL) تلقائيًا.

---

### إعداد التكامل مع Visual Studio

لتسهيل استخدام المكتبات المثبتة بواسطة vcpkg من مشاريع Visual Studio الخاصة بك، قم بإعداد التكامل باستخدام الأمر التالي.

```powershell
vcpkg integrate install
```

بمجرد إعداد ذلك، ستتمكن تلقائيًا من استخدام `#include <curl/curl.h>` في مشاريع Visual Studio الخاصة بك، ولن تحتاج إلى إعداد مسارات المكتبة أو إعدادات الرابط يدويًا.

---

## خاتمة

الآن أصبحت جاهزًا لاستخدام `libcurl` (مع دعم OpenSSL) في Visual Studio.

* باستخدام vcpkg، يمكنك إدارة التبعيات المزعجة كلها مرة واحدة
* تثبيت libcurl بسهولة باستخدام `vcpkg install curl[ssl] --triplet x64-windows`
* تكامل تلقائي مع Visual Studio باستخدام `vcpkg integrate install`

بعد ذلك، قم بتضمين ملفات الرأس في مشروعك وابدأ التطوير باستخدام واجهة برمجة تطبيقات libcurl.
استفد من vcpkg المريح لزيادة كفاءة تطويرك بشكل كبير.
