---
title: "إنشاء رسومات بالذكاء الاصطناعي باستخدام Stable Diffusion: دليل Google Colab والتنبيهات"
lastmod: "2026-11-23"
slug: "AI(StableDiffusion)を使ってرسم توضيحيتوليد الصورする方法"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "توضيح", "إنشاء صور", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["programming", "image-generation"]
description: "دليل خطوة بخطوة لإنشاء الرسومات باستخدام Stable Diffusion وGoogle Colab، مع تنبيهات بشأن توفر GPU وترخيص النموذج."
---

# ما هو Stable diffusion
Stable Diffusion عائلة من نماذج الانتشار الكامن التي تولّد الصور اعتمادًا على شروط مثل النص. وتشمل الأبحاث المرتبطة بها أعمال فريق CompVis، ومن بين مؤلفيها باحثون من جامعة لودفيغ ماكسيميليان في ميونخ.

# الأشياء المطلوبة

- حساب Google

فقط

# خطوات الإنشاء

يحدّث هذا الدليل مثالًا من عام 2023 ليتوافق مع واجهة Diffusers الحالية. لا تضمن Colab توفير GPU مجاني؛ فالحدود وأنواع وحدات GPU والتوفر تتغير. إذا لم تُخصّص لك وحدة GPU، فأعد المحاولة لاحقًا أو استخدم بيئة تشغيل أخرى متاحة.

قبل تحميل أوزان النموذج، اقرأ بطاقة النموذج وترخيص CreativeML OpenRAIL-M على Hugging Face. التزم بالاستخدامات المحظورة وشروط التوزيع والقوانين المحلية. لا يضمن الترخيص قانونية النتائج أو خلوها من حقوق أطراف أخرى.

إن `EasyNegative` في هذا المثال تضمين Textual Inversion يُوزّع منفصلًا. يحمّله الكود أدناه قبل استخدام الرمز في الموجّه.

1. افتح https://colab.research.google.com
2. من `ملف` في الزاوية العلوية اليسرى، حدد `إنشاء دفتر ملاحظات جديد`
3. من `تعديل`، حدد `إعدادات دفتر الملاحظات`
4. قم بتغيير `مسرع الأجهزة` إلى `GPU`
![img_2.png](img_2.webp)
5. الصق الكود التالي وقم بتشغيله
```
!pip install -U diffusers transformers accelerate
```
6. الصق الكود التالي وقم بتشغيله
```
import torch
from diffusers import DiffusionPipeline
from huggingface_hub import hf_hub_download
```
7. الصق الكود التالي وقم بتشغيله
```
pipe = DiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5", dtype=torch.float16)
easynegative_path = hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors")
pipe.load_textual_inversion(easynegative_path, token="EasyNegative")
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
![img_1.png](img_1.webp)

![img_3.png](img_3.webp)

![img_4.png](img_4.webp)

## مراجع

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [حاولت إنشاء برنامج توليد صور باستخدام الذكاء الاصطناعي (AI) في 15 دقيقة【برمجة حية】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
- [Google Colab FAQ: resource limits](https://research.google.com/colaboratory/faq.html)
- [Diffusers: loading pipelines](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Stable Diffusion model card and license](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [CompVis: Stable Diffusion research and code](https://github.com/CompVis/stable-diffusion)
- [EasyNegative textual-inversion embedding](https://huggingface.co/datasets/gsdf/EasyNegative)
