---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: 'خطوات بناء وتثبيت OpenSSL في بيئة Windows وطريقة إعداد البيئة'
slug: "Windows で OpenSSL をبناءする方法"
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "كيفية بناء OpenSSL من المصدر على Windows، باستخدام OpenSSL 3.5.9 مثالًا وشرح الأدوات المطلوبة وخطوات بناء x64."
---

# ما هو OpenSSL

لاستخدام OpenSSL في تطبيق، تحتاج إلى ترويسات ومكتبات التطوير. يمكنك الحصول على توزيع ثنائي أو بناء المصدر حسب احتياجك؛ وتشرح هذه الصفحة خيار البناء من المصدر.

Below, we will introduce the build procedure.
# إعداد بيئة البناء

- **Perl**

  قم بتنزيل `strawberry-perl-5.42.3.1-64bit.msi` من [https://strawberryperl.com/](https://strawberryperl.com/). أعتقد أن أحدث إصدار جيد.

- **NASM**

  قم بتنزيل `3.02/nasm-3.02-win64.zip` من `Download` في [https://www.nasm.us/](https://www.nasm.us/). أعتقد أن أحدث إصدار بخلاف rc جيد.
  بعد التثبيت، يجب عليك تسجيل المجلد الذي تم تثبيت NASM فيه في متغير البيئة PATH.

- **Visual Studio 2022** أو **Build Tools for Visual Studio 2022**

  قم بتثبيت `Visual Studio 2022 Community` أو `Build Tools for Visual Studio 2022` من [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# إجراء بناء OpenSSL على Windows

1. قم بتنزيل وفك ضغط `openssl-3.5.9.tar.gz` من [https://openssl-library.org/source/](https://openssl-library.org/source/). إذا لم تتمكن من فك ضغطه، فقم بتشغيل `tar -xzf openssl-3.5.9.tar.gz` في موجه الأوامر.

اعتبارًا من 2026-11-25، ينتمي OpenSSL 3.5.9 إلى سلسلة LTS المدعومة 3.5 حتى 2030-04-08. تحقق من أحدث تصحيح مدعوم في صفحة التنزيل الرسمية عند البناء.

2. استخدم موجه أوامر المطور x64 الخاص بـ Visual Studio. افتحه بصلاحيات المسؤول فقط إذا كنت ستثبّت ضمن Program Files.
3. افتح المجلد الذي تم فك ضغطه
4. قم بتشغيل الأمر التالي ※قم بتغيير جزء `Community` وفقًا لإصدار Visual Studio الذي قمت بتثبيته
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
5. قم بتشغيل الأمر التالي
```
perl Configure VC-WIN64A
```
6. قم بتشغيل الأمر التالي (يستغرق وقتًا طويلاً)
```
nmake
```
7. قم بتشغيل الأمر التالي (يستغرق وقتًا طويلاً)
```
nmake test
```
8. قم بتشغيل الأمر التالي
```
nmake install
```

في حالة النجاح، سيتم تثبيت OpenSSL في `C:\Program Files\OpenSSL`.
يتطلب التثبيت في الموقع الافتراضي صلاحيات المسؤول. لتجنب رفع الصلاحيات، حدّد prefix قابلًا للكتابة أثناء الإعداد.

هذا كل شيء

# المراجع

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)