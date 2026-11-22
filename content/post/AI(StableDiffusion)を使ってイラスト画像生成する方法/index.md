---
title: "Stable DiffusionでAIイラスト画像を生成する方法：Google Colabの手順と注意点"
lastmod: "2026-11-23"
slug: "AI(StableDiffusion)を使ってイラスト画像生成する方法"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "イラスト", "画像生成", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["programming", "image-generation"]
description: "Stable DiffusionとGoogle Colabを使ったイラスト画像生成の手順を解説。GPUの利用可否やモデルライセンスなど、実行前に確認したい注意点も紹介します。"
---

# Stable diffusionとは
Stable Diffusionは、テキストなどの条件から画像を生成する潜在拡散モデルの系統です。関連する研究には、ミュンヘン大学の研究者らを含むCompVisチームの成果があります。

# 用意するもの

- Googleアカウント

のみとなります

# 生成手順

この手順は2023年に作成した例を、現在のDiffusers APIに合わせて更新したものです。Colabの無料GPUは常に利用できるとは限らず、利用枠・GPUの種類・実行時間は変動します。GPUが割り当てられない場合は、時間をおいて再試行するか、利用可能な別の実行環境を使ってください。

モデルの重みを読み込む際はHugging Face上のモデルカードとCreativeML OpenRAIL-Mライセンスを確認し、禁止用途、配布条件、利用地域の法令を守ってください。生成物の権利や適法性が保証されるわけではありません。

この例の`EasyNegative`は別配布のTextual Inversion埋め込みです。以下のコードで読み込んでからプロンプトに使います。

1. https://colab.research.google.com を開く
2. 左上の`ファイル`から`ノートブックを新規作成`を選択
3. `編集`から`ノートブックの設定`を選択
4. `ハードウェアアクセラレータ`を`GPU`に変更
![img_2.png](img_2.webp)
5. 下記のコードを貼り付けて実行
```
!pip install -U diffusers transformers accelerate
```
6. 下記のコードを貼り付けて実行
```
import torch
from diffusers import DiffusionPipeline
from huggingface_hub import hf_hub_download
```
7. 下記のコードを貼り付けて実行
```
pipe = DiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5", dtype=torch.float16)
easynegative_path = hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors")
pipe.load_textual_inversion(easynegative_path, token="EasyNegative")
pipe.to("cuda")
```
8. 下記のコードを貼り付けて実行
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

ここで使用した`Prompt`は、[https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)の`Prompt`を参考にしています。

## 生成結果(いくつか)
![img_1.png](img_1.webp)

![img_3.png](img_3.webp)

![img_4.png](img_4.webp)

## 参考

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [人工知能（AI）を使った画像生成プログラムを15分で作ってみた【実況プログラミング】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
- [Google Colab FAQ: resource limits](https://research.google.com/colaboratory/faq.html)
- [Diffusers: loading pipelines](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Stable Diffusion model card and license](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [CompVis: Stable Diffusion research and code](https://github.com/CompVis/stable-diffusion)
- [EasyNegative textual-inversion embedding](https://huggingface.co/datasets/gsdf/EasyNegative)
