---
title: "استعادة commit بعد git reset باستخدام reflog"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "استعادة", "تراجع"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "اعثر على HEAD السابق عبر reflog واحفظه بفرع وافهم مخاطر --hard."
---

# استعادة commit بعد git reset باستخدام reflog

قد تكون الاستعادة ممكنة إذا ظل reflog المحلي يحتفظ بمرجع إلى commit السابق لـ reset. افحص `git reflog --date=local` واختر إدخال `HEAD@{n}` الصحيح؛ `HEAD@{1}` أدناه مثال فقط.

يتخلّص `git reset --hard` من التغييرات غير المثبتة في الملفات التي يتتبعها Git. احفظ العمل المطلوب أولًا واختر اسم فرع إنقاذ غير مستخدم. لا يستعيد reflog التعديلات التي فُقدت بالفعل بسبب hard reset. إذا كان السجل مشتركًا، فنسّق مع المتعاونين وفكّر عادةً في `git revert`.

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

استبدل `HEAD@{1}` بإدخال reflog الذي اخترته، و`rescue-before-reset` باسم فرع جديد. افحص commit وتأكد من إنشاء الفرع قبل تنفيذ الأمر الأخير.

## مراجع

[الدليل الرسمي لـ git reset](https://git-scm.com/docs/git-reset)

[الدليل الرسمي لـ git reflog](https://git-scm.com/docs/git-reflog)
