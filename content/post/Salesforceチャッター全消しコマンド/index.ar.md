---
title: 'Salesforce: أمر لحذف جميع منشورات Chatter والمرفقات'
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["تكنولوجيا المعلومات"]
description: 'نقدم أمراً لحذف جميع منشورات Chatter، والملفات المرفقة، وبيانات سلة المهملات دفعة واحدة، وهو مفيد عندما تقترب سعة التخزين للمؤسسة في Salesforce من النفاذ. هذه طريقة لتنظيف البيانات بسرعة باستخدام نافذة التنفيذ المجهول (Anonymous Window) من Developer Console.'
---
# أمر حذف جميع بيانات Chatter في Salesforce
هذا الأمر يقوم بحذف جميع المنشورات والمرفقات في Salesforce Chatter.
افتح وحدة تحكم المطور، ثم اختر "Open Execute anonymous Window" من قائمة Debug، والصق الكود التالي وقم بتنفيذه.
أستخدمه شخصياً عندما تكون سعة تخزين المؤسسة على وشك الامتلاء.

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// إفراغ سلة المهملات
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
