---
title: "كيفية التراجع عن git reset"
slug: "كيفية التراجع عن git reset"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "استعادة", "تراجع"]
draft: false
image: "img.png"
categories: ["أدوات وبيئة التطوير"]
---
# كيفية التراجع عن git reset
إذا قمت بتشغيل git reset عن طريق الخطأ بعد إجراء git commit، فإليك كيفية التراجع عن git reset (كيفية استعادة الحالة وقت إجراء git commit).

1. تحقق من معرف الالتزام (commit ID) قبل إعادة الضبط باستخدام `git reflog`
2. ارجع إلى الحالة قبل إعادة الضبط باستخدام `git reset --hard HEAD@{number}`

هذه كانت طريقة التراجع عن git reset.
