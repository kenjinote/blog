---
title: "使用Stable Diffusion生成AI插画：Google Colab步骤与注意事项"
lastmod: "2026-11-23"
slug: "AI(StableDiffusion)を使って插画图像生成する方法"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "插画", "图片生成", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["programming", "image-generation"]
description: "介绍使用Stable Diffusion和Google Colab生成插画的步骤，并说明GPU可用性与模型许可等注意事项。"
---

# 什么是 Stable Diffusion
Stable Diffusion是一类根据文本等条件生成图像的潜在扩散模型。相关研究包括CompVis团队的工作，作者中也有慕尼黑大学的研究人员。

# 准备工作

- Google账号

只需要这个。

# 生成步骤

本文将2023年的示例更新为当前Diffusers API。Colab免费GPU并非始终可用；使用限制、GPU类型和运行时间会变化。如果没有分配GPU，请稍后重试或使用其他可用的运行环境。

加载模型权重前，请阅读Hugging Face上的模型卡及CreativeML OpenRAIL-M许可证，并遵守其中的禁止用途、分发条款和使用地法律。该许可证不保证生成内容合法或不涉及第三方权利。

本例中的`EasyNegative`是单独发布的Textual Inversion嵌入文件。下面的代码会先加载它，再在提示词中使用该标记。

1. 打开 https://colab.research.google.com
2. 选择左上角`文件`中的`新建笔记本`
3. 选择`编辑`中的`笔记本设置`
4. 将`硬件加速器`更改为`GPU`
![img_2.png](img_2.webp)
5. 粘贴并运行以下代码
```
!pip install -U diffusers transformers accelerate
```
6. 粘贴并运行以下代码
```
import torch
from diffusers import DiffusionPipeline
from huggingface_hub import hf_hub_download
```
7. 粘贴并运行以下代码
```
pipe = DiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5", dtype=torch.float16)
easynegative_path = hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors")
pipe.load_textual_inversion(easynegative_path, token="EasyNegative")
pipe.to("cuda")
```
8. 粘贴并运行以下代码
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

这里使用的`Prompt`参考了[https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)的`Prompt`。

## 生成结果（部分）
![img_1.png](img_1.webp)

![img_3.png](img_3.webp)

![img_4.png](img_4.webp)

## 参考

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [花15分钟制作了使用人工智能（AI）的图片生成程序【实况编程】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
- [Google Colab FAQ: resource limits](https://research.google.com/colaboratory/faq.html)
- [Diffusers: loading pipelines](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Stable Diffusion model card and license](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [CompVis: Stable Diffusion research and code](https://github.com/CompVis/stable-diffusion)
- [EasyNegative textual-inversion embedding](https://huggingface.co/datasets/gsdf/EasyNegative)
