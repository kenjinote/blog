---
title: "How to Generate AI Illustrations with Stable Diffusion: Google Colab Guide and Caveats"
lastmod: "2026-11-23"
slug: "AI(StableDiffusion)を使ってIllustrationImage Generationする方法"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "Illustration", "Image Generation", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["programming", "image-generation"]
description: "A step-by-step guide to generating illustrations with Stable Diffusion and Google Colab, including caveats about GPU availability and model licensing."
---

# What is Stable Diffusion?
Stable Diffusion is a family of latent diffusion models that generate images from conditions such as text. Related research includes work by the CompVis team, whose authors include researchers from Ludwig Maximilian University of Munich.

# What you need

- Google Account

That's all.

# Generation steps

This tutorial updates a 2023 example for the current Diffusers API. A free Colab GPU is not guaranteed; usage limits, GPU types, and runtime availability change. If no GPU is assigned, try again later or use another available runtime.

Before loading the model weights, read the model card and its CreativeML OpenRAIL-M license on Hugging Face. Follow its prohibited-use and distribution terms and the laws where you use it. The license does not guarantee that an output is lawful or free of third-party rights.

`EasyNegative` in this example is a separately distributed textual-inversion embedding. The code below loads it before using the token in the prompt.

1. Open https://colab.research.google.com
2. Select `File` on the top left and choose `New notebook`
3. Select `Edit` and choose `Notebook settings`
4. Change the `Hardware accelerator` to `GPU`
![img_2.png](img_2.webp)
5. Paste and execute the following code
```
!pip install -U diffusers transformers accelerate
```
6. Paste and execute the following code
```
import torch
from diffusers import DiffusionPipeline
from huggingface_hub import hf_hub_download
```
7. Paste and execute the following code
```
pipe = DiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5", dtype=torch.float16)
easynegative_path = hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors")
pipe.load_textual_inversion(easynegative_path, token="EasyNegative")
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
![img_1.png](img_1.webp)

![img_3.png](img_3.webp)

![img_4.png](img_4.webp)

## References

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Tried making an image generation program using Artificial Intelligence (AI) in 15 minutes [Live Programming]](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
- [Google Colab FAQ: resource limits](https://research.google.com/colaboratory/faq.html)
- [Diffusers: loading pipelines](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Stable Diffusion model card and license](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [CompVis: Stable Diffusion research and code](https://github.com/CompVis/stable-diffusion)
- [EasyNegative textual-inversion embedding](https://huggingface.co/datasets/gsdf/EasyNegative)
