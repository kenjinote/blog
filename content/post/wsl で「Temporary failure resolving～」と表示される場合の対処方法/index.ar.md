---
title: "كيفية إصلاح خطأ 'Temporary failure resolving...' في WSL"
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "استكشاف الأخطاء وإصلاحها"]
draft: false
image: "img.png"
categories: ["أدوات وبيئة التطوير"]
---

# كيفية إصلاح خطأ 'Temporary failure resolving...' في WSL

`
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
`

عند ظهور الخطأ أعلاه في WSL، قد يكون إعداد خادم DNS غير صحيح.
في بيئتي، تم حل المشكلة باتباع الخطوات التالية:

1. قم بتشغيل WSL.
2. قم بتنفيذ `sudo nano /etc/resolv.conf`.
3. قم بتغيير سطر `nameserver` إلى ما يلي:
`
nameserver 8.8.8.8
`
4. احفظ باستخدام `Ctrl` + `S` واخرج باستخدام `Ctrl` + `X`.
5. قم بتنفيذ `sudo apt update`.
6. إذا لم يظهر الخطأ، فقد تم الحل.

## إذا لم تحل الخطوات أعلاه المشكلة

يبدو أن الخطوات أعلاه قد لا تحل المشكلة في بعض الحالات. يرجى الرجوع إلى المقال التالي.

- [كيفية حل 'Temporary failure resolving...' عند تحديث apt في WSL](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)