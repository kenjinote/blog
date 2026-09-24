---
title: 'كيفية تثبيت وإلغاء تثبيت PowerToys باستخدام أمر winget'
slug: "PowerToysのتثبيت"
date: "2026-09-24T16:08:36+09:00"
tags: ["cmd", "موجه الأوامر", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'نعرض في بيئة Windows خطوات سهلة لتثبيت وإلغاء تثبيت Microsoft PowerToys باستخدام أداة إدارة الحزم winget. يمكن تنفيذ ذلك فوراً عبر موجه الأوامر (Command Prompt).'
---

# تثبيت PowerToys من موجه الأوامر

إليك كيفية تثبيت PowerToys من موجه الأوامر.

```
winget install Microsoft.PowerToys --source winget
```

# إلغاء تثبيت PowerToys من موجه الأوامر

```
winget uninstall --name PowerToys 
```
