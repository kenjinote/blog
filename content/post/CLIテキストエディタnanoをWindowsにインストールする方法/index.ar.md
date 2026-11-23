---
title: 'استخدام محرر النصوص nano في Windows عبر WSL أو MSYS2'
slug: "CLIمحرر نصوصnanoをWindowsにتثبيتする方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "محرر نصوص"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'طرق حديثة لاستخدام GNU nano في Windows: تثبيته داخل WSL للحصول على بيئة Linux، أو داخل MSYS2 لاستخدام أدوات تطوير Windows، مع شرح الاختصارات الأساسية.'
---


توجد عدة طرق لاستخدام GNU nano في Windows. قد يصعب التحقق من مصدر ملفات `nano.exe` المنفردة في مواقع التنزيل القديمة ومن استمرار صيانتها، لذلك يعرض هذا الدليل طريقتين لهما قنوات توزيع مدعومة.

## الطريقة الأولى: استخدام nano داخل WSL

اختر WSL إذا كنت تحتاج أيضًا إلى أدوات سطر أوامر Linux. في Windows 11 أو Windows 10 الإصدار 2004 (البنية 19041) أو أحدث، افتح PowerShell بصفة مسؤول وشغّل:

```powershell
wsl --install
```

بعد إعادة التشغيل، افتح Ubuntu وثبّت nano من طرفية Linux:

```bash
sudo apt update
sudo apt install nano
nano --version
```

افتح ملفًا بالأمر `nano filename`. يتوفر قرص Windows C: داخل WSL ضمن `/mnt/c/`، مثل `nano /mnt/c/Users/اسمك/notes.txt`. راجع [دليل Microsoft لتثبيت WSL](https://learn.microsoft.com/en-us/windows/wsl/install) لمعرفة الإعداد والوصول إلى الملفات.

## الطريقة الثانية: استخدام nano من MSYS2

إذا لم تكن بحاجة إلى توزيعة Linux كاملة وتريد أدوات تطوير بأوامر شبيهة بـ Unix، فاختر [MSYS2](https://www.msys2.org/). اتبع [دليل التثبيت الرسمي](https://www.msys2.org/docs/installer/) ثم افتح طرفية “MSYS2 MSYS”. يتطلب المثبّت الرسومي Windows 10 بنظام 64 بت، الإصدار 1809 أو أحدث، أو Windows Server 2019؛ وقد تختلف متطلبات الحزم الفردية (راجع [إصدارات Windows المدعومة](https://www.msys2.org/docs/windows_support/)). حدّث قاعدة بيانات الحزم والحزم المثبتة أولًا. إذا طلب التحديث إعادة تشغيل الطرفية، فأعد فتحها وأكمل التحديث قبل تثبيت nano.

```bash
pacman -Suy
pacman -S nano
nano --version
```

راجع [دليل تحديث MSYS2 الرسمي](https://www.msys2.org/docs/updating/) لمعرفة خطوات التحديث وإعادة التشغيل.

يمكنك مراجعة اسم الحزمة وأمر التثبيت في [صفحة حزمة nano لدى MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64). شغّل nano داخل طرفية MSYS2. ويتطلب تشغيله من موجه الأوامر أو PowerShell العادي إعداد PATH وبيئة التشغيل إضافيًا؛ ولا يُنصح بإضافة `/usr/bin` الخاص بـ MSYS2 إلى PATH في Windows دون تقييم.

## الاختصارات الأساسية

ابدأ بأمر مثل `nano notes.txt`. تظهر الاختصارات أسفل الشاشة: `^` تعني Ctrl و`M-` تعني Meta (وغالبًا Alt). اضغط `Ctrl+O` لكتابة الملف، ثم أكّد اسم الملف الظاهر باستخدام Enter، واضغط `Ctrl+X` للخروج. كما تحفظ الإصدارات الحالية المخزن المؤقت باستخدام `Ctrl+S`. راجع [قائمة اختصارات GNU nano الرسمية](https://www.nano-editor.org/dist/latest/cheatsheet.html).

يدعم nano التدويل وUTF-8، لكن إدخال اليابانية وعرضها يعتمدان أيضًا على الطرفية والخطوط والإعدادات المحلية وطريقة الإدخال. إذا ظهرت رموز غير مقروءة أو تعذّر إدخال اليابانية في WSL أو MSYS2، فتحقق من إعداد UTF-8 وطريقة الإدخال في الطرفية.

## المراجع

- [GNU nano](https://www.nano-editor.org/)
- [قائمة اختصارات GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn: تثبيت WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- [دليل تثبيت MSYS2](https://www.msys2.org/docs/installer/)
- [إصدارات Windows المدعومة](https://www.msys2.org/docs/windows_support/)
- [حزمة nano في MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64)
