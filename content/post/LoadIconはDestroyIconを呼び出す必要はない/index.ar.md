---
title: 'السبب وراء عدم الحاجة إلى استدعاء DestroyIcon للأيقونات المستردة بواسطة دالة LoadIcon'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["أيقونة", "LoadIcon", "DestroyIcon", "برمجة ويندوز"]
draft: false
categories: ["programming"]
description: 'يعتمد استدعاء DestroyIcon على ما إذا كان مقبض الأيقونة يشير إلى مورد مشترك أم مورد يملكه المستدعي. يشرح هذا الدليل ملكية الموارد في LoadIcon وLoadImage وCopyIcon، وينبه إلى تعارض في وثائق Microsoft لبعض واجهات إنشاء الموارد.'
image: eyecatch.jpg
---

# ملكية مقبض الأيقونة

يعتمد استدعاء `DestroyIcon` على ما إذا كانت الأيقونة مورداً مشتركاً أم مورداً يملكه المستدعي ويتعين عليه تحريره. قد يؤثر تدمير أيقونة مشتركة في أجزاء أخرى من البرنامج تستخدم المورد نفسه.

## متى لا تستدعي DestroyIcon

- الأيقونة التي يعيدها `LoadIcon` مشتركة. لا تدمرها باستخدام `DestroyIcon`. يحمّل `LoadIcon` الأيقونة بحجم مقاييس النظام القياسي؛ استخدم `LoadImage` إذا أردت تحديد الحجم.
- عند تمرير `LR_SHARED` إلى `LoadImage` يكون المقبض مشتركاً. لا تستدعِ `DestroyIcon`. لا تستخدم `LR_SHARED` للصور المحمّلة من الملفات أو ذات الأحجام غير القياسية.
- قد يعيد `CopyImage` المقبض الأصلي عند تمرير `LR_COPYRETURNORG` إذا كانت قيمة `hImage` المدخلة أيقونة مشتركة. لا تدمر ذلك المقبض.

## متى تستدعي DestroyIcon

حرّر الأيقونات التي يملكها المستدعي باستخدام `DestroyIcon` بعد الانتهاء من استخدامها. تذكر Microsoft الأمثلة التالية:

- `CreateIconFromResourceEx` من دون `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon` الذي يعيد مقبض نسخة من الأيقونة
- أيقونة حمّلها `LoadImage` من دون `LR_SHARED`

## تنبيه بشأن CreateIconFromResource

تدرج صفحة Microsoft العامة لـ `DestroyIcon` الدالة `CreateIconFromResource` ضمن مصادر الأيقونات المشتركة، لكن صفحات الدوال الفردية توصي باستدعاء `DestroyIcon`. كما تتضمن صفحات `CreateIconFromResource` و`CreateIconFromResourceEx` تعارضاً داخلياً حول `LR_SHARED` وتحرير المقبض الناتج. لا تستنتج الملكية لهذه الواجهات من القاعدة العامة وحدها؛ راجع أحدث وثائق الدالة المحددة. يختلف هذا التعارض عن سلوك المقابض المشتركة لـ `LoadIcon`.

يجب ألا تكون الأيقونة التي تمررها إلى `DestroyIcon` قيد الاستخدام. تحقق مما إذا كان المقبض مشتركاً وما إذا كانت الوحدة المصدر لا تزال محمّلة.

## المراجع

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
