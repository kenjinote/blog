---
title: "Stable Diffusion से AI चित्र बनाएं: Google Colab की प्रक्रिया और सावधानियां"
lastmod: "2026-11-23"
slug: "AI(StableDiffusion)を使ってचित्रणछवि निर्माणする方法"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "इलस्ट्रेशन", "इमेज जनरेशन", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["programming", "image-generation"]
description: "Stable Diffusion और Google Colab से चित्र बनाने की चरण-दर-चरण जानकारी, जिसमें GPU उपलब्धता और मॉडल लाइसेंस से जुड़ी सावधानियां शामिल हैं।"
---

# Stable diffusion क्या है
Stable Diffusion latent diffusion मॉडलों का एक परिवार है, जो टेक्स्ट जैसी शर्तों के आधार पर चित्र बनाता है। इससे जुड़े शोध में CompVis टीम का काम शामिल है; इसके लेखकों में म्यूनिख के लुडविग मैक्सिमिलियन विश्वविद्यालय के शोधकर्ता भी हैं।

# आपको क्या चाहिए

- Google अकाउंट

केवल यही

# जनरेशन प्रक्रिया

यह ट्यूटोरियल 2023 के उदाहरण को मौजूदा Diffusers API के अनुसार अपडेट करता है। Colab मुफ्त GPU की गारंटी नहीं देता; उपयोग सीमाएँ, GPU के प्रकार और उपलब्धता बदलती रहती हैं। GPU न मिले तो बाद में फिर कोशिश करें या कोई अन्य उपलब्ध रनटाइम इस्तेमाल करें।

मॉडल वज़न लोड करने से पहले Hugging Face पर मॉडल कार्ड और CreativeML OpenRAIL-M लाइसेंस पढ़ें। प्रतिबंधित उपयोग, वितरण की शर्तों और स्थानीय कानून का पालन करें। यह लाइसेंस आउटपुट की वैधता या तीसरे पक्ष के अधिकारों से मुक्त होने की गारंटी नहीं देता।

इस उदाहरण में `EasyNegative` अलग से वितरित किया गया textual inversion embedding है। नीचे का कोड prompt में इसका token इस्तेमाल करने से पहले इसे लोड करता है।

1. https://colab.research.google.com खोलें
2. ऊपर बाईं ओर `फ़ाइल` से `नई नोटबुक` चुनें
3. `संपादित करें` से `नोटबुक सेटिंग` चुनें
4. `हार्डवेयर एक्सेलेरेटर` को `GPU` में बदलें
![img_2.png](img_2.webp)
5. नीचे दिए गए कोड को पेस्ट करें और चलाएं
```
!pip install -U diffusers transformers accelerate
```
6. नीचे दिए गए कोड को पेस्ट करें और चलाएं
```
import torch
from diffusers import DiffusionPipeline
from huggingface_hub import hf_hub_download
```
7. नीचे दिए गए कोड को पेस्ट करें और चलाएं
```
pipe = DiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5", dtype=torch.float16)
easynegative_path = hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors")
pipe.load_textual_inversion(easynegative_path, token="EasyNegative")
pipe.to("cuda")
```
8. नीचे दिए गए कोड को पेस्ट करें और चलाएं
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

यहाँ उपयोग किया गया `Prompt`, [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5) के `Prompt` पर आधारित है।

## जनरेट किए गए परिणाम (कुछ)
![img_1.png](img_1.webp)

![img_3.png](img_3.webp)

![img_4.png](img_4.webp)

## संदर्भ

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [मैंने 15 मिनट में आर्टिफिशियल इंटेलिजेंस (AI) का उपयोग करके एक इमेज जनरेशन प्रोग्राम बनाया 【लाइव प्रोग्रामिंग】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
- [Google Colab FAQ: resource limits](https://research.google.com/colaboratory/faq.html)
- [Diffusers: loading pipelines](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Stable Diffusion model card and license](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [CompVis: Stable Diffusion research and code](https://github.com/CompVis/stable-diffusion)
- [EasyNegative textual-inversion embedding](https://huggingface.co/datasets/gsdf/EasyNegative)
