---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25
title: 'تشغيل محرر Hidemaru بأمر "hide" واحد! طريقة إعداد مفيدة في Windows'
slug: "أمر「hide」でمحرر هيديماروを立ち上げる方法"
tags: ["الأوامر", "محرر Hidemaru", "سجل الويندوز"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "سجّل اسمًا في App Paths وشغّل Hidemaru Editor من نافذة Run أو بالأمر start hide في Windows 10/11."
---

## أقدم لكم كيفية تشغيل محرر Hidemaru باستخدام الأمر «hide».

ملاحظة: تم تأكيد عمل هذه الطريقة على `Windows 10/11`.

1. افتح محرر سجل الويندوز (Registry Editor).
2. انتقل إلى `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. أنشئ مفتاحًا باسم `hide.exe` في `App Paths`. ※ الاسم الذي يسبق `.exe` في اسم المفتاح سيكون اسم الأمر.
4. قم بتعيين [مسار](/ar/p/windows-%E3%81%A7%D9%85%D8%B3%D8%A7%D8%B1%E3%81%AE%E9%80%9A%E3%81%A3%E3%81%9F%D9%85%D9%84%D9%81-%D8%AA%D9%86%D9%81%D9%8A%D8%B0%D9%8A%E3%81%AE%E5%A0%B4%E6%89%80%E3%82%92%E8%A6%8B%E3%81%A4%E3%81%91%E3%82%8B%E6%96%B9%E6%B3%95/) الملف التنفيذي لمحرر Hidemaru في `(الافتراضي)` لمفتاح `hide.exe`. في بيئتي، كان المسار `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. قيمة Path اختيارية. لا تضفها إلا عند الحاجة إلى مجلدات DLL إضافية؛ يضيفها ShellExecuteEx إلى PATH للعملية.
6. أدخل hide في نافذة Run (Win + R). استخدم start hide في موجه الأوامر؛ كتابة hide وحدها ليست الطريقة الموضحة.

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
إذا قمت بحفظ المحتوى أعلاه في ملف `.reg` وتشغيله، فستتم إضافة الإعدادات إلى سجل الويندوز.

يسجل مثال .reg التطبيق للمستخدم الحالي فقط. استبدل المسار بمسار الملف التنفيذي الفعلي. لجميع المستخدمين، استبدل HKEY_CURRENT_USER بـ HKEY_LOCAL_MACHINE واستورد بصلاحيات المسؤول.


## المراجع

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)
