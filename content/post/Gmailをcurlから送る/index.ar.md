---
title: 'كيفية إرسال رسائل بريد إلكتروني من Gmail باستخدام أمر curl'
slug: "Gmailをcurlから送る"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["AI・テクノロジー"]
description: 'نشرح كيفية إرسال رسائل بريد إلكتروني عبر حساب Gmail باستخدام أداة سطر الأوامر ''curl''. نقدم تفاصيل حول كيفية الحصول على كلمة مرور تطبيقات جوجل، وتحديد خيارات curl، وأوامر إنشاء وإرسال ملف نص البريد الإلكتروني.'
---

# إرسال بريد Gmail باستخدام curl

## 1. الحصول على كلمة مرور التطبيق
https://myaccount.google.com/apppasswords
انقر على الرابط أعلاه وأدخل اسم التطبيق.
احفظ كلمة المرور التي تم إنشاؤها.

## 2. إرسال بريد إلكتروني باستخدام أمر curl
قم بتنفيذ الأمر التالي.

في المثال أدناه، تم كتابة محتوى البريد الإلكتروني في mail.txt.

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: رسالة اختبار
Content-Type: text/plain; charset="UTF-8"

هذه رسالة اختبار.
```

قم بإنشاء الملف أعلاه، وقم بتنفيذ الأمر التالي.

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ يرجى استبدال xxxxxxxxxxxxxxxx بكلمة مرور التطبيق.
