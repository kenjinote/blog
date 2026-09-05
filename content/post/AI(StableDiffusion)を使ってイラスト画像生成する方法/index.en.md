---
title: 'How to generate illustration images using AI (Stable Diffusion)'
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "Illustration", "Image Generation", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Programming"]
---

# What is Stable Diffusion?
Stable diffusion is an AI developed by a research team at the University of Munich in Germany that generates images from inputted text information.
By training on various images, it is possible to generate a wide variety of images, from photorealistic ones to illustrations.

This time, I will introduce how to generate illustration images using the pre-trained data of Stable diffusion.

# What you need

- Google Account

That's all.

# Generation steps

1. Open https://colab.research.google.com
2. Select `File` on the top left and choose `New notebook`
3. Select `Edit` and choose `Notebook settings`
4. Change the `Hardware accelerator` to `GPU`
![img_2.png](img_2.png)
5. Paste and execute the following code
```
!pip install diffusers==0.8.0 transformers
```
6. Paste and execute the following code
```
from diffusers import StableDiffusionPipeline
```
7. Paste and execute the following code
```
pipe = StableDiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5")
pipe.to("cuda")
```
8. Paste and execute the following code
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

The `Prompt` used here is based on the `Prompt` at [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5).

## Generation results (some)
![img_1.png](img_1.png)

![img_3.png](img_3.png)

![img_4.png](img_4.png)

## References

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Tried making an image generation program using Artificial Intelligence (AI) in 15 minutes [Live Programming]](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
