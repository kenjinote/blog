---
title: "كيفية إنشاء صور توضيحية باستخدام الذكاء الاصطناعي (StableDiffusion)"
slug: "كيفية-إنشاء-صور-توضيحية-باستخدام-الذكاء-الاصطناعي-StableDiffusion"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "توضيح", "إنشاء صور", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["برمجة"]
---

# ما هو Stable diffusion
Stable diffusion هو ذكاء اصطناعي لإنشاء الصور من المعلومات النصية المدخلة، طوره فريق بحث في جامعة ميونخ في ألمانيا.
من خلال تدريبه على صور متنوعة، يمكنه إنشاء صور مختلفة من الصور الواقعية إلى الرسوم التوضيحية.

في هذه المرة، سأقدم طريقة لإنشاء صور توضيحية باستخدام البيانات المدربة مسبقًا لـ Stable diffusion.

# الأشياء المطلوبة

- حساب Google

فقط

# خطوات الإنشاء

1. افتح https://colab.research.google.com
2. من `ملف` في الزاوية العلوية اليسرى، حدد `إنشاء دفتر ملاحظات جديد`
3. من `تعديل`، حدد `إعدادات دفتر الملاحظات`
4. قم بتغيير `مسرع الأجهزة` إلى `GPU`
![img_2.png](img_2.png)
5. الصق الكود التالي وقم بتشغيله
```
!pip install diffusers==0.8.0 transformers
```
6. الصق الكود التالي وقم بتشغيله
```
from diffusers import StableDiffusionPipeline
```
7. الصق الكود التالي وقم بتشغيله
```
pipe = StableDiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5")
pipe.to("cuda")
```
8. الصق الكود التالي وقم بتشغيله
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

إن `Prompt` المستخدم هنا مبني على `Prompt` من [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5).

## نتائج الإنشاء (بعض منها)
![img_1.png](img_1.png)

![img_3.png](img_3.png)

![img_4.png](img_4.png)

## مراجع

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [حاولت إنشاء برنامج توليد صور باستخدام الذكاء الاصطناعي (AI) في 15 دقيقة【برمجة حية】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
