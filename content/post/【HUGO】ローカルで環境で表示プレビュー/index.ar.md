---
title: "【HUGO】معاينة العرض في البيئة المحلية"
slug: "【HUGO】ローカルで環境で表示プレビュー"
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---
# تثبيت HUGO

## التحميل
[تحميل HUGO](https://github.com/gohugoio/hugo/releases)

من الموقع أعلاه، قم بتنزيل واستخراج وحدة Windows التي تناسب بيئتك.
في حالتي، قمت بتنزيل "hugo_0.102.3_Windows-64bit.zip".

## الاستخراج
قم باستخراج ملف zip الذي تم تنزيله وانسخ hugo.exe الموجود بداخله إلى مجلد تقوم بإنشائه، مثل C:\bin.

## التسجيل في متغيرات البيئة
قم بالتسجيل في متغيرات البيئة لتشغيل hugo.exe من أي مكان.
هذه العملية في Windows 11، لكن أعتقد أنه يمكنك تسجيلها باتباع الخطوات التالية.

1. اضغط على زر Win+Pause لفتح حول.
2. انقر فوق إعدادات النظام المتقدمة.
3. انقر فوق متغيرات البيئة.
4. حدد Path وانقر فوق تحرير.
5. انقر فوق جديد، واكتب "C:\bin" في سطر جديد، ثم انقر فوق موافق لإغلاق مربع الحوار.
 
# معاينة المدونة
انتقل إلى مجلد مدونة HUGO في موجه الأوامر وقم بتشغيل الأمر التالي.

`hugo server -D`

نتيجة التنفيذ أدناه. (-D هو خيار لعرض مسودات المقالات.)

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
  Pages            | 39
  Paginator pages  |  0
  Non-page files   |  7
  Static files     |  0
  Processed images |  0
  Aliases          | 13
  Sitemaps         |  1
  Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

يتم إخراج العنوان في وقت التنفيذ (في المثال أعلاه، `http://localhost:1313/`)، لذلك انسخ العنوان إلى متصفحك.
يتم تحديث المعاينة تلقائيًا في كل مرة يتم فيها حفظ الملف.
لإنهاء المعاينة، أدخل Ctrl+C في موجه الأوامر.
