---
title: "كيفية تشغيل محرر Hidemaru باستخدام الأمر «hide»"
slug: "コマンド「hide」で秀丸エディタを立ち上げる方法"
date: 2024-03-29T23:45:37+09:00
tags: ["الأوامر", "محرر Hidemaru", "سجل الويندوز"]
draft: false
image: "img_2.png"
categories: ["الأدوات وبيئة التطوير"]
---

## أقدم لكم كيفية تشغيل محرر Hidemaru باستخدام الأمر «hide».

ملاحظة: تم تأكيد عمل هذه الطريقة على `Windows 10/11`.

1. افتح محرر سجل الويندوز (Registry Editor).
2. انتقل إلى `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. أنشئ مفتاحًا باسم `hide.exe` في `App Paths`. ※ الاسم الذي يسبق `.exe` في اسم المفتاح سيكون اسم الأمر.
4. قم بتعيين مسار الملف التنفيذي لمحرر Hidemaru في `(الافتراضي)` لمفتاح `hide.exe`. في بيئتي، كان المسار `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. أنشئ قيمة سلسلة نصية (String Value) باسم `Path` في مفتاح `hide.exe`.
6. قم بتعيين مسار المجلد الذي يحتوي على الملف التنفيذي لمحرر Hidemaru في بيانات `Path`. في بيئتي، كان المسار `"C:\Program Files (x86)\Hidemaru"`.
7. الآن يمكنك تشغيل محرر Hidemaru باستخدام الأمر `hide` من خلال نافذة **Run** التي تظهر بالضغط على مفتاحي `Win` + `R`. بالإضافة إلى ذلك، في موجه الأوامر (Command Prompt)، يمكنك تشغيل محرر Hidemaru باستخدام الأمر `start hide`.

```text
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="\"C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe\""
"Path"="\"C:\\Program Files (x86)\\Hidemaru\\\""
```
إذا قمت بحفظ المحتوى أعلاه في ملف `.reg` وتشغيله، فستتم إضافة الإعدادات إلى سجل الويندوز.

![img_1.png](img_1.png)
