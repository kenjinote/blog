---
title: 'كيفية استدعاء OpenAI API باستخدام curl من موجه أوامر Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "أمر"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'أرسل طلبًا نصيًا إلى Responses API من OpenAI عبر cmd.exe في Windows. اضبط مفتاح API كمتغير بيئة وأرسل JSON من دون وضع المفتاح في ملف الطلب.'
---


يشرح هذا الدليل استدعاء OpenAI API من `cmd.exe` في Windows. يُوصى باستخدام Responses API للتطبيقات الجديدة. إن ChatGPT وAPI Platform خدمتان منفصلتان، وتُحاسب على استخدام API بشكل منفصل عن اشتراك ChatGPT. راجع [إعداد فوترة API](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) قبل إرسال الطلبات.

## تعيين مفتاح API كمتغير بيئة

أنشئ مفتاحًا من صفحة [API keys في API Platform](https://platform.openai.com/api-keys). لا تضعه في الشيفرة المصدرية أو ملف الطلب. في Windows اضغط `Win+R` وشغّل `sysdm.cpl`، ثم اختر **خيارات متقدمة > متغيرات البيئة > متغيرات المستخدم > جديد**. اجعل اسم المتغير `OPENAI_API_KEY` وقيمته المفتاح، ثم افتح موجه أوامر جديدًا. تحقق من وجود المتغير من دون عرض السر:

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

يُبقي متغير البيئة المفتاح خارج مصدر التطبيق، لكنه لا يجعل نشره أو مشاركته آمنًا. ألغِ المفتاح المكشوف واستبدله من صفحة API keys. راجع أيضًا [أفضل ممارسات أمان مفاتيح API](https://developers.openai.com/api/docs/guides/production-best-practices).

## إنشاء الطلب

احفظ JSON التالي باسم `request.json` في مجلد العمل. استخدم ترميز UTF-8 إذا أضفت نصًا غير ASCII.

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

قد تتغير معرّفات النماذج، كما يختلف الوصول إليها حسب مشروع API. راجع [قائمة النماذج الحالية](https://developers.openai.com/api/docs/models) قبل استخدام نموذج المثال.

## إرسال الطلب عبر curl.exe

في موجه الأوامر، انتقل إلى المجلد الذي يحتوي على `request.json` ثم نفّذ:

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

يعرض `--include` حالة HTTP ورؤوس الاستجابة. تُرجع Responses API بيانات JSON. يوجد النص المُنشأ في عنصر محتوى `output_text` داخل رسالة الإخراج. قد تتضمن استدعاءات الأدوات وأنواع الاستجابة الأخرى عناصر مختلفة؛ استخدم محلل JSON وافحص `type` لكل عنصر بدل افتراض رقم ثابت في المصفوفة. راجع [مرجع Responses API](https://developers.openai.com/api/reference/resources/responses/methods/create).

## الأخطاء والاستخدام

- قد يعني `401` أن المفتاح غير موجود أو غير صالح أو غير مخوّل للمشروع. افحص الإعداد من دون طباعة القيمة أو مشاركتها.
- قد يعني `429` تجاوز حد المعدل أو نفاد الرصيد أو حد الاستخدام. افحص نص الاستجابة وصفحتي Usage وBilling في API Platform.
- تعتمد التكلفة على النموذج ورموز الإدخال والإخراج. تحقق من الأسعار الحالية واستخدام المشروع في API Platform، واضبط حدودًا أو تنبيهات عند الحاجة.

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
