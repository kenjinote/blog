---
title: "تنظيف منشورات Salesforce Chatter: التخزين وخطوات آمنة"

slug: "Salesforceثرثرة全消しأمر"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "لا تُحتسب منشورات Chatter ضمن مساحة تخزين بيانات Salesforce. تعرّف على نوع التخزين، وراجع المنشورات المحددة وانسخها احتياطيًا قبل حذفها بأمان عبر Data Loader."
---
**مهم:** لا تُحتسب منشورات Chatter وتعليقاته والتغييرات المتعقبة ضمن تخزين بيانات Salesforce، بينما تُحتسب الملفات المرفقة ضمن تخزين الملفات. تحقق أولًا من **Storage Usage** في Setup لمعرفة نوع التخزين القريب من الحد. لن يؤدي حذف جميع المنشورات إلى توفير مساحة بيانات.

## مراجعة المنشورات ذات المرفقات بأمان

مثال SOQL التالي للقراءة فقط. يعرض المنشورات ذات مرفقات الملفات (`Type = 'ContentPost'`) للمراجعة ولا يحذف أي بيانات.

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. صدّر المعرّفات المرشحة باستخدام Data Loader أو Workbench، ثم حدّد المجموعة حسب التاريخ أو المؤلف أو السجل الأب أو معايير أخرى معتمدة.
2. تحقق من خطة النسخ الاحتياطي والاستعادة للمؤسسة واختبر الإجراء في Sandbox. اطلب من المسؤول ومالك البيانات مراجعة المعرّفات وعدد العناصر قبل الحذف.
3. بعد الموافقة، احذف المعرّفات المحددة فقط باستخدام Data Loader. كما تصدّر العملية الجماعية الموثقة من Salesforce معرّفات FeedItem ذات `Type = ContentPost` قبل حذفها.

قد يكون حذف FeedItem نهائيًا ولا يمر بسلة المحذوفات، لذا قد يتعذر استرداده. يؤدي حذف المنشور إلى إزالة المرفق من الموجز؛ أما بقاء الملف في موقعه الأصلي أو مشاركات أخرى فيعتمد على حالته. لا تحذف جميع `ContentDocument` بلا ترشيح ولا تفرغ سلة المحذوفات بأكملها. لتنظيف تخزين الملفات، راجع Storage Usage وتحقق من مالك كل ملف ومشاركاته وتأثير حذفه قبل الإقدام عليه.

## مراجع

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
