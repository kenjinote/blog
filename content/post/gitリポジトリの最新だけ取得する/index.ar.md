---
title: 'كيفية استنساخ مستودع Git بسجل تاريخي ضحل'
slug: "gitمستودعの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "مستودع", "أمر"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'تعرّف على ما ينقله git clone --depth 1 وكيفية اختيار فرع وجلب مزيد من السجل لاحقًا.'
---

# استنساخ مستودع بسجل تاريخي ضحل

ينشئ الأمر `git clone --depth 1` نسخة ضحلة بعمق تاريخ يساوي واحدًا انطلاقًا من رأس الفرع المحدد. افتراضيًا، يكون الفرع المحدد هو الفرع الافتراضي للمستودع البعيد. يقلل ذلك سجل الالتزامات المنقول، لكن Git يظل ينزّل الملفات الحالية والكائنات اللازمة؛ لذلك قد يظل المستودع الذي يحتوي على ملفات كبيرة كبيرًا.

```sh
git clone --depth 1 <repository-url>
```

لاختيار فرع بعينه، اذكر اسمه:

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

يمكنك جلب مزيد من السجل لاحقًا، مثلًا:

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

استبدل `<directory>` و`<branch>` بالاسمين الفعليين. يعني استخدام `--depth` أيضًا استخدام `--single-branch` ما لم تغيّر ذلك صراحةً. راجع الدليلين الرسميين [`git clone`](https://git-scm.com/docs/git-clone) و[`git fetch`](https://git-scm.com/docs/git-fetch)، بما في ذلك خيار `--unshallow`.
