---
title: "التحكم في قراءة ملفات .DS_Store على مشاركات SMB في macOS"
slug: "macOSで.DS_Storeを自動生成しないようにするأمر"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "اتبع تعليمات Apple لتعطيل قراءة ملفات .DS_Store على مشاركات SMB في macOS أو إعادة تفعيلها. لا يمنع ذلك إنشاء الملفات؛ سجّل الخروج ثم ادخل مجددًا بعد التغيير."
---
تشرح Apple هذا الإعداد بوصفه طريقة لتسريع تصفح SMB، إذ يطلب من macOS **عدم قراءة ملفات `.DS_Store` على مشاركات SMB**. لكنه لا يمنع إنشاء ملفات جديدة ولا يحذف الملفات الموجودة. وقد يتغير عرض المجلدات أو ترتيبها في Finder.

### تعطيل القراءة على مشاركات SMB

نفّذ هذا الأمر في Terminal:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

سجّل الخروج من حساب macOS ثم ادخل مجددًا لتطبيق التغيير. سيستخدم Finder المعلومات الأساسية بدل بيانات `.DS_Store` عند عرض المجلدات.

### إعادة تفعيل القراءة

اضبط القيمة على `FALSE` لاستعادة السلوك الافتراضي:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

بعد ذلك سجّل الخروج ثم ادخل مجددًا. تعرض Apple هذا كخيار لضبط تصفح SMB، وتذكر أن المقال موجّه أساسًا إلى مسؤولي المؤسسات والتعليم. راجع [دعم Apple](https://support.apple.com/en-us/102064).
