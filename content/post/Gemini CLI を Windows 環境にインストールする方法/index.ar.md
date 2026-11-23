---
title: 'كيفية تثبيت Gemini CLI على Windows | شرح مفصل من إعداد Node.js'
slug: "Gemini CLI を Windows 環境にتثبيتする方法"
tags: ["Gemini", "CLI", "Windows", "تثبيت", "開発"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "دليل تثبيت Gemini CLI على Windows باستخدام Node.js وnpm، مع التشغيل العام أو المؤقت والمصادقة وفحص PATH والموافقات الآمنة."
---

# تثبيت Gemini CLI واستخدامه على Windows

Gemini CLI أداة مفتوحة المصدر لسطر الأوامر تتيح استخدام Gemini من الطرفية. تتبع الخطوات الإرشادات الرسمية الحالية؛ راجع [دليل التثبيت الرسمي](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx) لأي تحديثات.

## 1. إعداد Node.js وnpm

يتطلب Gemini CLI إصدار Node.js 20.0.0 أو أحدث. توصي الوثائق الرسمية بـ Windows 11 24H2 أو أحدث، وتدعم PowerShell وتتطلب اتصالًا بالإنترنت. نزّل مثبت LTS لنظام Windows من [موقع Node.js](https://nodejs.org/en/download/).

```powershell
node --version
npm --version
```

## 2. تثبيت Gemini CLI عبر npm

للاستخدام المتكرر، ثبّت الحزمة تثبيتًا عامًا:

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

إذا لم يُعثر على `gemini`، نفّذ `npm config get prefix`، وأضف المجلد إلى `PATH` في Windows، ثم افتح نافذة PowerShell جديدة وتحقق باستخدام `Get-Command gemini`. راجع [وثائق npm](https://docs.npmjs.com/cli/v11/configuring-npm/folders/).

## 3. التشغيل الأول والمصادقة

شغّل `gemini` في PowerShell واتبع خطوات المصادقة عند أول تشغيل. تشمل الخيارات الموثقة حساب Google ومفتاح Gemini API وVertex AI. يختلف التوفر والسعر والحصص والشروط بحسب الحساب والخدمة؛ راجع [دليل المصادقة](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx). تعامل مع مفاتيح API كأسرار ولا تضعها في المطالبات أو المستودعات العامة.

```powershell
gemini
```

استخدم `gemini --help` لعرض الأوامر، وأدخل `/quit` لإنهاء الجلسة التفاعلية.

## 4. التشغيل مرة واحدة دون تثبيت عام

للتشغيل مرة واحدة، استخدم `npx`؛ فهذا لا يثبت الأمر بصورة دائمة، لذا شغّل الأمر مجددًا في الجلسات التالية. يمكن لـ Gemini CLI قراءة الملفات وتعديلها وتنفيذ أوامر shell. استخدمه في مشروع موثوق وراجع طلبات التأكيد قبل الموافقة. راجع [دليل الأدوات والأمان](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md).

```powershell
npx @google/gemini-cli
```

## 5. الخلاصة

1. جهّز Node.js 20 أو أحدث.
2. للاستخدام المتكرر، ثبّت الحزمة عالميًا عبر npm.
3. شغّل `gemini` وأكمل المصادقة.
4. للتشغيل المؤقت، استخدم `npx`. راجع الوثائق الرسمية للاطلاع على المتطلبات والشروط الحالية.
