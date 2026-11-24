---
title: "النشر باستخدام X API وGoogle Colab [Python]"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "اقرأ بيانات الاعتماد من Google Colab Secrets وانشر منشورًا واحدًا باستخدام Tweepy وX API v2. تحقّق من شروط الوصول والرسوم الحالية قبل التشغيل."
---

# مقدمة

هذا مثال بسيط يستخدم Tweepy في Google Colab لنشر منشور واحد على حسابك باستخدام X API v2. قد تتغير إمكانية الوصول والرسوم ومتطلبات المصادقة؛ لذا تحقّق من الوثائق الرسمية وDeveloper Console قبل التشغيل.

## مهم: بيانات الاعتماد في الإصدار السابق

احتوى إصدار سابق من هذا المقال على مفاتيح API ورموز وصول ضمن النص. اعتبر أي بيانات اعتماد نُشرت مكشوفة. إذا كانت القيم حقيقية وفعالة، فألغِ المفاتيح والرموز المعنية من X Developer Console وأنشئ بدائل جديدة. قد تبقى نسخ في سجل المستودع، لذلك لا يكفي حذفها من الصفحة الحالية وحدها.

# قبل البدء

1. أنشئ Project وApp في [X Developer Console](https://developer.x.com/en/portal/dashboard)، ثم أنشئ بيانات اعتماد مستخدم تسمح بالنشر. عند استخدام OAuth 1.0a User Context، اضبط صلاحيات القراءة والكتابة للتطبيق قبل إنشاء رموز الوصول. وعند استخدام OAuth 2.0 PKCE، اطلب النطاقات اللازمة، ومنها `tweet.write`.
2. تحقّق من الخطة الحالية وسعر نقطة الكتابة وحدود الاستخدام في Developer Console. قد تتغير الأسعار وإمكانية الوصول؛ فلا تعتمد على شروحات قديمة أو أسعار سابقة.
3. أنشئ دفترًا في [Google Colab](https://colab.research.google.com/). من لوحة Secrets (رمز المفتاح) أضف الأسرار الأربعة بالأسماء التالية واسمح لهذا الدفتر بالوصول إليها. أدخل قيم تطبيقك ولا تلصقها في الشيفرة أو المخرجات.
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# نشر منشور واحد

يؤدي تشغيل الخلية التالية إلى نشر النص الموجود في `text` علنًا من حسابك على X. تحقّق من الحساب والنص قبل التشغيل. قد تُفرض رسوم لاستخدام X API.

```python
%pip install -q tweepy

from google.colab import userdata
import tweepy

client = tweepy.Client(
    consumer_key=userdata.get("X_API_KEY"),
    consumer_secret=userdata.get("X_API_KEY_SECRET"),
    access_token=userdata.get("X_ACCESS_TOKEN"),
    access_token_secret=userdata.get("X_ACCESS_TOKEN_SECRET"),
)

text = "Hello from the X API"
response = client.create_tweet(text=text)
print(response.data["id"])
```

## حول الأتمتة

ينشر هذا المثال منشورًا واحدًا فقط عند تشغيل الخلية يدويًا. قبل توسيعه للنشر المجدول أو الردود التلقائية، اقرأ [قواعد الأتمتة في X](https://help.x.com/en/rules-and-policies/x-automation). للردود التلقائية شروط إضافية، منها إظهار المستلم رغبة واضحة في تلقي الرد. لا يضمن Colab تشغيلًا مستمرًا، وقد تتغير الجلسات وحدود الاستخدام.

## المراجع

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)
