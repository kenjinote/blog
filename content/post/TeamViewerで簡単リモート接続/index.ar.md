---
title: '【للمبتدئين】كيفية الاتصال بسهولة بسطح المكتب البعيد باستخدام TeamViewer'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単اتصال عن بعد"
tags: ["TeamViewer", "أوامر", "اتصال عن بعد"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'نشرح كيفية إجراء اتصال بسطح المكتب البعيد بسهولة باستخدام TeamViewer. نقدم أيضاً حيلة مفيدة لأتمتة وتخطي خطوات الاتصال عن طريق تحديد المعرف (ID) وكلمة المرور من سطر الأوامر (Command Line) باستخدام اختصار.'
---
## الاتصال عبر سطر الأوامر في Windows

وفقًا لوثائق TeamViewer الرسمية لسطر الأوامر في Windows، يمكن تشغيل الإصدار الكامل من خلال موجه الأوامر أو برنامج نصي أو اختصار.

يشغّل هذا المثال `TeamViewer.exe` من مجلد التثبيت. أدخل معرّف الشريك في `<ID>` وكلمة المرور في `<Password>`. إذا كان TeamViewer مثبتًا في مكان آخر، فاستبدل مسار الملف التنفيذي.

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

عند حذف `-p`، يستخدم TeamViewer ميزة Easy Access إذا كانت متاحة؛ وإلا فسيطلب كلمة المرور.

يحفظ الاختصار الذي يتضمن كلمة مرور هذه الكلمة بصيغة يمكن قراءتها. لا تشاركه ولا تضعه في مكان يستطيع الآخرون قراءته. للوصول المتكرر دون مراقبة، فكّر في ربط الجهاز بحسابك واستخدام Easy Access وقائمة السماح والمصادقة متعددة العوامل بدلًا من حفظ كلمة مرور.

## مراجع رسمية

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)
