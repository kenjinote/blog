---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "إرسال بريد Gmail باستخدام curl"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "شرح إرسال البريد عبر Gmail SMTP باستخدام curl، مع كلمات مرور التطبيقات وTLS وملف رسالة RFC 5322 وأوامر Bash وWindows PowerShell."
---

يمكن لـcurl الاتصال بخادم Gmail SMTP وتحميل ملف رسالة أعددته مسبقًا. هذه ليست طريقة استخدام Gmail API. توصي Google عمومًا بـOAuth 2.0؛ والمثال التالي لاختبار يدوي بحساب تتوفر له كلمة مرور تطبيق.

## اختيار طريقة المصادقة

لا تستخدم كلمة مرور حساب Google العادية مع SMTP. فضّل OAuth 2.0 إذا كان التطبيق يدعمه. للاختبار اليدوي، قد تعمل كلمة مرور تطبيق إذا كان التحقق بخطوتين مفعّلًا. أنشئها من [كلمات مرور التطبيقات في حساب Google](https://myaccount.google.com/apppasswords). لا تتوفر هذه الميزة لكل الحسابات؛ وقد تخفيها سياسة المؤسسة أو إعدادات الأمان. لا توصي Google بكلمات مرور التطبيقات لمعظم الاستخدامات. ألغِها عندما لا تعود بحاجة إليها.

## إنشاء ملف الرسالة

في إرسال SMTP، لا ينشئ curl الرسالة ولا يحوّلها. يجب أن يحتوي الملف على الترويسات والمتن بتنسيق RFC 5322. يستخدم المثال عناوين ASCII. اجعل ترويسة `From` مطابقة لحساب Gmail المستخدم للمصادقة. يحتاج الموضوع غير ASCII إلى ترميز MIME.

احفظ هذه الرسالة باسم `mail.txt`.

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## الإرسال باستخدام curl

يستخدم المثال TLS ضمنيًا على المنفذ 465. وبما أن `--user` يحتوي اسم المستخدم فقط، سيطلب curl كلمة المرور؛ أدخل كلمة مرور التطبيق عند الطلب. لاستخدام المنفذ 587، استخدم `smtp://smtp.gmail.com:587` مع `--ssl-reqd` لطلب STARTTLS.

### Bash وzsh وLinux وmacOS

```bash
curl --url "smtps://smtp.gmail.com:465" \
  --mail-from "sender@gmail.com" \
  --mail-rcpt "recipient@example.com" \
  --user "sender@gmail.com" \
  --upload-file mail.txt
```

### Windows PowerShell

```powershell
curl.exe --url "smtps://smtp.gmail.com:465" --mail-from "sender@gmail.com" --mail-rcpt "recipient@example.com" --user "sender@gmail.com" --upload-file "mail.txt"
```

## حماية بيانات الاعتماد

لا تضع كلمة مرور التطبيق في سطر الأوامر أو ملف الرسالة أو سجل shell أو مستودع أو سجل تشغيل. استخدم مطالبة كلمة المرور في curl. واحمِ ملف الرسالة أيضًا إذا احتوى معلومات شخصية أو سرية.

الوثائق الرسمية: [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
