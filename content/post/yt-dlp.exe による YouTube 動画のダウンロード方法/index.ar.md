---
title: "استخدام yt-dlp.exe: تنزيل الفيديوهات المصرح بها وتحويلها إلى MP3"
slug: "yt-dlp.exe による YouTube فيديوのتنزيل方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "كيفية الحصول على yt-dlp.exe وتحديثه وحفظ فيديو وتحويل الصوت إلى MP3. استخدم الأداة مع مراعاة حقوق المحتوى وشروط YouTube."
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# استخدام yt-dlp.exe: تنزيل الفيديوهات المصرح بها وتحويلها إلى MP3

yt-dlp أداة مفتوحة المصدر تعمل بسطر الأوامر لتنزيل الفيديو والصوت. توضح الأمثلة الاستخدام الأساسي في Windows.

## استخدمها عند السماح فقط

استخدم yt-dlp للمحتوى الذي تملكه أو لديك إذن من صاحبه بتنزيله فقط، وبالقدر الذي تسمح به شروط YouTube والقوانين المعمول بها. يمكنك تنزيل فيديوهاتك التي رفعتها بنفسك من YouTube Studio.

## التثبيت والتحديث

نزّل `yt-dlp.exe` الخاص بنظام Windows من صفحة الإصدارات الرسمية وضعه في مجلد. أضف هذا المجلد إلى `PATH` لتشغيله من أي مجلد. احصل على الملف التنفيذي من الإصدارات الرسمية فقط.

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## الاستخدام الأساسي

في موجه الأوامر أو PowerShell، حدّد رابط الفيديو. يُحفظ الملف الناتج في المجلد الحالي.

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

لتحويل الصوت إلى MP3، استخدم `-x` و`--audio-format mp3`.

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

تحقق من الإصدار باستخدام `yt-dlp.exe --version`. حدّث الملف التنفيذي للإصدار باستخدام `yt-dlp.exe -U`. يتطلب تحويل MP3 وجود `ffmpeg` و`ffprobe`. إذا توقف الاستخراج بعد تغيير في YouTube، فحدّث yt-dlp وراجع الاعتماديات الحالية في README الرسمي.

لإضافة صورة مصغرة أو بيانات وصفية، أضف `--embed-thumbnail` أو `--embed-metadata`؛ وقد تلزم أدوات إضافية وفقاً للتنسيق.

## إذا لم يعمل

حدّث إلى أحدث إصدار وراجع الوثائق الرسمية لمعرفة الاعتماديات والدعم الحاليين. لا تتجاوز القيود ولا تنزّل محتوى دون إذن.

## المراجع

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)
