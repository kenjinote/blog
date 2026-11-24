---
title: 'طريقة تثبيت وإدارة التطبيقات بسهولة باستخدام أمر WinGet في Windows 11'
slug: "WinGet を使ってأمرでتطبيقをتثبيتする"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'نشرح كيفية تثبيت التطبيقات من سطر الأوامر باستخدام مدير الحزم "WinGet" في Windows 11. نقدم خطوات التثبيت والإدارة السريعة للبرامج الرئيسية مثل Chrome و VSCode و Slack عبر سطر الأوامر.'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# تثبيت التطبيقات باستخدام WinGet

يتيح WinGet (Windows Package Manager) البحث عن التطبيقات وتثبيتها وتحديثها وإزالتها من سطر أوامر Windows. تدعم الأداة Windows 11 وWindows 10 الإصدار 1809 أو الأحدث وWindows Server 2025 وفقًا لـ Microsoft، وتكون عادةً مضمنة في App Installer على أجهزة سطح المكتب.

## التحقق والاستخدام

شغّل `winget --version`. إذا لم يُعثر على الأمر، فحدّث Windows وثبّت App Installer أو حدّثه من Microsoft Store. بعد أول تسجيل دخول بحساب جديد، انتظر اكتمال تسجيل Store.

ابحث بالاسم وتحقق من المعرّف والناشر قبل التثبيت:

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

يفرض `-e` التطابق الدقيق، ويحدد `--source winget` مستودع مجتمع WinGet. اقرأ شروط المصدر وترخيص التطبيق قبل الموافقة. وتعرض Microsoft أمثلة `Microsoft.PowerToys` و`Microsoft.PowerShell` و`Git.Git` و`Docker.DockerDesktop`. قد تتغير المعرّفات والإصدارات؛ تحقق باستخدام `winget show` وحدد `--source` عند تعدد المصادر.

## أصبح Paint.NET متاحًا عبر WinGet

تتضمن قائمة المجتمع الحالية المعرّف `dotPDN.PaintDotNet`:

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

قد يتغير التوفر؛ راجع البيان الحالي.

## مراجع

- [Microsoft Learn: نظرة عامة على WinGet](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- [أمر install](https://learn.microsoft.com/en-us/windows/package-manager/winget/install) · [أمر search](https://learn.microsoft.com/en-us/windows/package-manager/winget/search)
- [بيان Paint.NET](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)
