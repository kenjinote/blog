---
title: 'كيفية تثبيت وتفعيل GitHub Copilot في IntelliJ IDEA'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'تعرّف على طريقة تثبيت إضافة GitHub Copilot في IntelliJ IDEA، وتسجيل الدخول بحساب GitHub، واستخدام اقتراحات التعليمات البرمجية داخل المحرر. يشرح الدليل متطلبات الوصول وخطوات المصادقة الحالية مع روابط إلى الوثائق الرسمية.'
---

# مقدمة

تضيف إضافة GitHub Copilot اقتراحات التعليمات البرمجية داخل المحرر وميزة Copilot Chat إلى بيئات JetBrains. يشرح هذا الدليل التثبيت الأساسي وتسجيل الدخول في IntelliJ IDEA. قد تختلف أسماء القوائم والشاشات بحسب إصدار البيئة والإضافة.

## قبل البدء

تحتاج إلى حساب GitHub لديه إمكانية استخدام Copilot وإصدار متوافق من IntelliJ IDEA. يفرض Copilot Free حدوداً على الاستخدام، بينما تتيح الخطط المدفوعة استخداماً أوسع. قد تتغير الخطط والتوافق، لذا راجع الوثائق الرسمية الحالية.

## تثبيت الإضافة

1. افتح إعدادات Plugins. في Windows أو Linux اختر **File > Settings > Plugins**، وفي macOS اختر **IntelliJ IDEA > Settings > Plugins**.
2. ابحث في Marketplace عن **GitHub Copilot**، ثم انقر **Install** بجوار الإضافة المقدمة من GitHub.
3. أعد تشغيل بيئة التطوير بعد التثبيت.

## تسجيل الدخول إلى GitHub

1. افتح **Tools > GitHub Copilot > Login to GitHub**.
2. في نافذة تسجيل الدخول انقر **Copy and Open** لفتح المتصفح.
3. سجّل الدخول إلى GitHub في المتصفح، والصق رمز الجهاز الذي تعرضه بيئة التطوير، ثم انقر **Continue**.
4. راجع الأذونات المطلوبة واختر **Authorize GitHub Copilot Plugin**. عُد إلى بيئة التطوير وانقر **OK** في شاشة التأكيد.

## استخدام اقتراحات التعليمات البرمجية

ابدأ الكتابة في المحرر. يعرض Copilot اقتراحاً بلون رمادي؛ اضغط **Tab** لقبوله. راجع الاقتراح قبل استخدامه لأنه يُنشأ بحسب السياق وقد يحتاج إلى تعديل. افتح أيقونة GitHub Copilot Chat على الجانب الأيمن لبدء محادثة.

قد تتغير القوائم والميزات. راجع الوثائق الرسمية لمعرفة الخطوات والتوافق الحاليين.

## مراجع

- [تثبيت الإضافة وتسجيل الدخول](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [الحصول على اقتراحات التعليمات البرمجية في JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [إضافة GitHub Copilot في JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
