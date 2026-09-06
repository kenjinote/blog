---
title: "كيفية التغريد باستخدام Twitter API و Google Colaboratory"
slug: "كيفية-التغريد-باستخدام-twitter-api-و-google-colaboratory"
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["برمجة"]
---

# المتطلبات

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- حساب Google

يرجى الرجوع إلى المواقع المرجعية لمعرفة كيفية الحصول على Twitter API.

# خطوات التغريد باستخدام API

1. قم بزيارة [https://colab.research.google.com/](https://colab.research.google.com/)
2. حدد "ملف" -> "دفتر ملاحظات جديد"
3. الصق الكود التالي وقم بتشغيله (استخدم القيم الفعلية التي حصلت عليها بنفسك)
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. الصق الكود التالي وقم بتشغيله
```
import tweepy
```
4. الصق الكود التالي وقم بتشغيله (API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→ سيتم نشر تغريدة `hello`

5. الصق الكود التالي وقم بتشغيله (API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→ سيتم نشر تغريدة `hello v2`

هذا كل شيء

# المراجع
- [[اعتبارًا من أبريل 2021] شرح شامل لطلب استخدام Twitter API مع أمثلة للاستخدام ولقطات شاشة](https://bloomtectec.com/twitter-api-application-procedure/)
- [[لا حاجة لإعدادات مزعجة!] نوصي بـ Google Colaboratory كبيئة تجريبية لـ Twitter API [سنشارك الكود المصدري أيضًا]](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [[Tweepy] Twitter API v2: تغريدة، رد، تغريدة مع استطلاع، تغريدة مع وسائط (v1.1) [Python]](https://3pysci.com/tweepy-28/)
