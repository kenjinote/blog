---
title: "使用 Stable Diffusion 生成 AI 插畫：Google Colab 步驟與注意事項"
lastmod: "2026-11-23"
slug: "AI(StableDiffusion)を使って插畫圖片生成する方法"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "插圖", "圖像生成", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["programming", "image-generation"]
description: "介紹使用 Stable Diffusion 和 Google Colab 生成插畫的步驟，並說明 GPU 可用性與模型授權等注意事項。"
---

# 什麼是 Stable diffusion
Stable Diffusion 是一系列根據文字等條件生成圖像的潛在擴散模型。相關研究包含 CompVis 團隊的成果，作者也包括慕尼黑大學的研究人員。

# 需要準備的東西

- Google 帳號

僅此而已

# 生成步驟

本文將 2023 年的範例更新為目前的 Diffusers API。Colab 免費 GPU 不保證隨時可用；使用限制、GPU 類型與執行時間都可能變動。若未取得 GPU，請稍後再試或改用其他可用的執行環境。

載入模型權重前，請閱讀 Hugging Face 上的模型卡與 CreativeML OpenRAIL-M 授權，並遵守禁止用途、散布條款及所在地法律。該授權不保證生成內容合法或不涉及第三方權利。

本範例的`EasyNegative`是另外提供的 Textual Inversion 嵌入檔。以下程式碼會先載入，再於提示詞中使用這個標記。

1. 打開 https://colab.research.google.com
2. 從左上角的 `檔案` 中選擇 `新增筆記本`
3. 從 `編輯` 中選擇 `筆記本設定`
4. 將 `硬體加速器` 更改為 `GPU`
![img_2.png](img_2.webp)
5. 貼上並執行以下程式碼
```
!pip install -U diffusers transformers accelerate
```
6. 貼上並執行以下程式碼
```
import torch
from diffusers import DiffusionPipeline
from huggingface_hub import hf_hub_download
```
7. 貼上並執行以下程式碼
```
pipe = DiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5", dtype=torch.float16)
easynegative_path = hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors")
pipe.load_textual_inversion(easynegative_path, token="EasyNegative")
pipe.to("cuda")
```
8. 貼上並執行以下程式碼
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

這裡使用的 `Prompt` 參考了 [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5) 的 `Prompt`。

## 生成結果（部分）
![img_1.png](img_1.webp)

![img_3.png](img_3.webp)

![img_4.png](img_4.webp)

## 參考

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [花了15分鐘使用人工智慧（AI）製作了圖像生成程式【實況編程】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
- [Google Colab FAQ: resource limits](https://research.google.com/colaboratory/faq.html)
- [Diffusers: loading pipelines](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Stable Diffusion model card and license](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [CompVis: Stable Diffusion research and code](https://github.com/CompVis/stable-diffusion)
- [EasyNegative textual-inversion embedding](https://huggingface.co/datasets/gsdf/EasyNegative)
