---
title: "طريقة تنزيل مقاطع فيديو YouTube باستخدام yt-dlp.exe"
slug: "yt-dlp.exe による YouTube 動画のダウンロード方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "تنزيل"]
draft: false
image: "img_1.png"
categories: ["تكنولوجيا المعلومات والتكنولوجيا"]
---
# ما هو yt-dlp

`yt-dlp` هو أداة سطر أوامر لتنزيل مقاطع فيديو YouTube.
بالإضافة إلى تنزيل مقاطع الفيديو، يمكنك أيضًا تنزيلها كملفات صوتية بتنسيق mp3.

## التنزيل والتثبيت

1. قم بتنزيل أحدث إصدار من yt-dlp.exe من [صفحة إصدارات yt-dlp](https://github.com/yt-dlp/yt-dlp/releases).
2. ضع yt-dlp.exe في أي مجلد تختاره.
3. أضف مسار مجلد yt-dlp.exe إلى متغير البيئة Path.

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
