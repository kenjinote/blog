---
title: "如何使用 AI (Stable Diffusion) 生成插圖"
slug: "AI(StableDiffusion)を使ってイラスト画像生成する方法"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "插圖", "圖像生成", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["程式設計"]
---

# 什麼是 Stable diffusion
Stable diffusion 是由德國慕尼黑大學研究團隊開發的，一種根據輸入文字資訊生成圖像的 AI。
透過讓它學習各種圖像，它可以生成從寫實照片到插圖等各式各樣的圖片。

這次，我將介紹如何使用 Stable diffusion 的預訓練資料來生成插圖。

# 需要準備的東西

- Google 帳號

僅此而已

# 生成步驟

1. 打開 https://colab.research.google.com
2. 從左上角的 `檔案` 中選擇 `新增筆記本`
3. 從 `編輯` 中選擇 `筆記本設定`
4. 將 `硬體加速器` 更改為 `GPU`
![img_2.png](img_2.png)
5. 貼上並執行以下程式碼
```
!pip install diffusers==0.8.0 transformers
```
6. 貼上並執行以下程式碼
```
from diffusers import StableDiffusionPipeline
```
7. 貼上並執行以下程式碼
```
pipe = StableDiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5")
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
![img_1.png](img_1.png)

![img_3.png](img_3.png)

![img_4.png](img_4.png)

## 參考

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [花了15分鐘使用人工智慧（AI）製作了圖像生成程式【實況編程】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
