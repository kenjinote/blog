---
title: "كيفية بناء OpenSSL على Windows"
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.png"
categories: ["Programming"]
---

# ما هو OpenSSL

إنه مكتبة مفتوحة المصدر توفر المعالجة اللازمة لإجراء اتصالات مشفرة.

لاستخدامه من برنامج، يتم نشر كود مصدر لغة C، لذلك تحتاج إلى بناء وإنشاء مكتبة.

أدناه، سوف نقدم إجراء البناء.

# إعداد بيئة البناء

- **Perl**

  قم بتنزيل `strawberry-perl-5.32.1.1-64bit.msi` من [https://strawberryperl.com/](https://strawberryperl.com/). أعتقد أن أحدث إصدار جيد.

- **NASM**

  قم بتنزيل `2.16.01/nasm-2.16.01-win64.zip` من `Download` في [https://www.nasm.us/](https://www.nasm.us/). أعتقد أن أحدث إصدار بخلاف rc جيد.
  بعد التثبيت، يجب عليك تسجيل المجلد الذي تم تثبيت NASM فيه في متغير البيئة PATH.

- **Visual Studio 2022** أو **Build Tools for Visual Studio 2022**

  قم بتثبيت `Visual Studio 2022 Community` أو `Build Tools for Visual Studio 2022` من [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# إجراء بناء OpenSSL على Windows

1. قم بتنزيل وفك ضغط `openssl-3.1.0.tar.gz` من [https://www.openssl.org/source/](https://www.openssl.org/source/). إذا لم تتمكن من فك ضغطه، فقم بتشغيل `tar -xzf openssl-3.1.0.tar.gz` في موجه الأوامر.
2. ابدأ موجه الأوامر **بصلاحيات المسؤول** 
3. افتح المجلد الذي تم فك ضغطه
4. قم بتشغيل الأمر التالي ※قم بتغيير جزء `Community` وفقًا لإصدار Visual Studio الذي قمت بتثبيته
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
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

هذا كل شيء

# المراجع
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
