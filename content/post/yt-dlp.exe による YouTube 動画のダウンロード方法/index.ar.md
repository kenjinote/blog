---
title: 'كيفية استخدام yt-dlp: طريقة تنزيل وحفظ مقاطع فيديو وصوتيات YouTube'
date: "2026-09-24T19:44:38+09:00"
slug: "yt-dlp.exe による YouTube فيديوのتنزيل方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "تنزيل"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: 'نشرح بوضوح كيفية استخدام أداة سطر الأوامر "yt-dlp" لتنزيل وحفظ مقاطع فيديو YouTube بجودة عالية، وخطوات استخراجها وحفظها كملفات صوتية mp3. تغطية شاملة من التثبيت إلى كيفية الاستخدام.'
---
# ما هو yt-dlp

`yt-dlp` هو أداة سطر أوامر لتنزيل مقاطع فيديو YouTube.
بالإضافة إلى تنزيل مقاطع الفيديو، يمكنك أيضًا تنزيلها كملفات صوتية بتنسيق mp3.

## التنزيل والتثبيت

1. قم بتنزيل أحدث إصدار من yt-dlp.exe من [صفحة إصدارات yt-dlp](https://github.com/yt-dlp/yt-dlp/releases).
2. ضع yt-dlp.exe في أي مجلد تختاره.
3. أضف [مسار](/ar/p/windows-%E3%81%A7%D9%85%D8%B3%D8%A7%D8%B1%E3%81%AE%E9%80%9A%E3%81%A3%E3%81%9F%D9%85%D9%84%D9%81-%D8%AA%D9%86%D9%81%D9%8A%D8%B0%D9%8A%E3%81%AE%E5%A0%B4%E6%89%80%E3%82%92%E8%A6%8B%E3%81%A4%E3%81%91%E3%82%8B%E6%96%B9%E6%B3%95/) مجلد yt-dlp.exe إلى متغير البيئة Path.

## طريقة الاستخدام

قم بتشغيل yt-dlp.exe في موجه الأوامر وحدد عنوان URL لمقطع فيديو YouTube.

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※ لا بأس في استخدام جزء VIDEO_ID كمعلمة فقط.

لتنزيله كملف صوتي mp3، قم بتشغيل الأمر التالي.

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

الآن، سيتم تنزيل الفيديو في الدليل الحالي الذي تم تنفيذ الأمر فيه.

انتهى.
