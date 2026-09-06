---
title: "اتصال عن بعد سهل باستخدام TeamViewer"
slug: "اتصال-عن-بعد-سهل-باستخدام-teamviewer"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "أوامر", "اتصال عن بعد"]
draft: false
image: "img.png"
categories: ["تكنولوجيا المعلومات"]
---

# اتصال عن بعد سهل باستخدام TeamViewer

يجعل TeamViewer من السهل الاتصال بسطح المكتب عن بعد.

قم بتشغيل TeamViewer على كل من الكمبيوتر المحلي والكمبيوتر البعيد،
وأدخل المعرف (ID) وكلمة المرور (Password) الخاصة بالكمبيوتر البعيد على الكمبيوتر المحلي لإجراء الاتصال.

للاتصال عن بعد باستخدام سطر الأوامر، استخدم ما يلي:

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
أدخل معرف الكمبيوتر البعيد في `<ID>`، وكلمة المرور الخاصة به في `<Password>`.

من المفيد إنشاء ملف اختصار باستخدام الأمر أعلاه لتخطي إدخال المعرف وكلمة المرور في كل مرة.

الموقع المرجعي: [Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
