---
title: "تثبيت PowerToys وإلغاء تثبيته باستخدام WinGet"
slug: "PowerToysのتثبيت"
tags: ["cmd", "موجه الأوامر", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "ثبّت PowerToys أو أزل تثبيته باستخدام معرّف حزمة Microsoft في WinGet، وراجع متطلبات النظام الحالية."
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys مجموعة من أدوات Microsoft لتخصيص Windows. توصي Microsoft بالتثبيت من GitHub أو Microsoft Store؛ ويشرح هذا الدليل طريقة WinGet.

## متطلبات النظام

متطلبات PowerToys الحالية هي Windows 11 أو Windows 10 الإصدار 2004 (20H1، البنية 19041) أو أحدث، ومعالج 64 بت من نوع x64 أو ARM64. يثبت الإعداد أحدث إصدار مستقر من Microsoft Edge WebView2 Runtime. قد تتغير المتطلبات وطرق التوزيع، لذا راجع الوثائق الرسمية قبل التثبيت.

## التثبيت باستخدام WinGet

أولاً، شغّل `winget --version` في موجه الأوامر أو PowerShell للتأكد من توفر WinGet. يحدد هذا الأمر معرّف الحزمة Microsoft.PowerToys من مصدر winget. اقرأ أي تنبيهات أو طلبات موافقة قبل المتابعة.

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## إلغاء التثبيت

يحدد أمر إلغاء التثبيت أيضاً المعرّف ومصدر winget. قبل المتابعة، تأكد من أن الحزمة المحددة هي PowerToys واقرأ أي رسالة تأكيد تظهر.

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## مراجع Microsoft الرسمية

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)
