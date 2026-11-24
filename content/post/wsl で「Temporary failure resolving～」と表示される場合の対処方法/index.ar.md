---
title: "حل خطأ “Temporary failure resolving” في WSL"
slug: "wsl で「Temporary failure resolving～」と表示される場合のطريقة التعامل"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "ميّز بين مشكلات تحليل الأسماء في WSL ومشكلات شبكة Windows، ثم افحص تحديثات WSL ونفق DNS وVPN وجدار الحماية."
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# حل خطأ “Temporary failure resolving” في WSL

يعني هذا الخطأ أن WSL لم يتمكن من تحويل اسم المضيف إلى عنوان IP. إعداد خادم DNS سبب محتمل واحد فقط. حدّد أولاً ما إذا كان الفشل في Windows أو WSL أو كليهما.

## ابدأ بهذه الفحوصات

1. في Windows PowerShell، نفّذ `Resolve-DnsName archive.ubuntu.com`. إذا فشل ذلك في Windows أيضاً، فتحقّق أولاً من شبكة Windows وDNS وVPN.

2. في WSL، نفّذ `getent hosts archive.ubuntu.com`. إذا نجح Windows في تحليل الاسم ولم ينجح WSL، فتابع الخطوات التالية.

في PowerShell، نفّذ `wsl --update` ثم `wsl --shutdown`. أعد تشغيل WSL ثم جرّب `getent hosts archive.ubuntu.com` و`sudo apt update` مجدداً.

في Windows 11 الإصدار 22H2 وما بعده، يكون نفق DNS مفعّلاً افتراضياً في إصدارات WSL الحديثة. إذا فشل تحليل الأسماء أثناء استخدام VPN، فحدّث WSL وتحقق من عدم تعطيل `dnsTunneling=true` ضمن `[wsl2]` في `.wslconfig`. بعد التغيير، نفّذ `wsl --shutdown` في PowerShell.

لا تبدأ بتثبيت خادم DNS عام عشوائي مثل `8.8.8.8` في `/etc/resolv.conf`. فقد يتجاوز سياسات DNS الخاصة بـVPN أو المؤسسة ويتعارض مع إعدادات WSL المُنشأة تلقائياً. إذا كانت بيئتك تتطلب تجاوزاً يدوياً، فاتبع إرشادات Microsoft الخاصة بـVPN واستشر مسؤول الشبكة.

## إذا استمرت المشكلة

إذا استمرت المشكلة، فتحقّق من VPN وجدار حماية Windows وبرامج الأمان وسياسات شبكة المؤسسة. إذا نجح تحليل الاسم لكن `apt update` فشل، فتحقّق أيضاً من الوكيل والمرآة ومستودعات الحزم.

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## المراجع

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
