---
title: 'طريقة العثور على موقع (مسار) الملفات التنفيذية في مسار النظام على Windows [أمر where]'
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "مسار", "ملف تنفيذي", "موجه الأوامر"]
draft: false
image: "img.webp"
categories: ["الكمبيوتر والأجهزة الذكية"]
description: 'نشرح كيفية العثور بسهولة على موقع حفظ الملفات التنفيذية (المسار الكامل) باستخدام موجه الأوامر أو PowerShell في Windows. نقدم حيلة مفيدة لتحديد الموقع الدقيق للتطبيقات الموجودة في المسار بسرعة باستخدام أمر "where".'
---

# كيفية العثور على موقع ملف تنفيذي في مسار Windows

عند تشغيل أمر بتحديد ملف تنفيذي، قد ترغب في معرفة مكان هذا الملف التنفيذي. في مثل هذه الحالات، يمكنك استخدام الأمر أدناه للتحقق من موقع الملف التنفيذي.

```powershell
where <اسم الملف التنفيذي>
```

على سبيل المثال، إذا كنت تريد معرفة موقع برنامج الرسام (mspaint.exe)، افعل ما يلي:

```powershell
where mspaint.exe
```

# المراجع

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)
