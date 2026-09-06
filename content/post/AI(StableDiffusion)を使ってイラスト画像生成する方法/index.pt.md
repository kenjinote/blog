---
title: "Como gerar imagens de ilustração usando IA (Stable Diffusion)"
slug: "AI(StableDiffusion)を使ってイラスト画像生成する方法"
date: 2023-04-06T00:43:19+09:00
tags: ["IA", "Stable Diffusion", "Ilustração", "Geração de Imagens", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Programação"]
---

# O que é o Stable diffusion
O Stable diffusion é uma IA desenvolvida por uma equipe de pesquisa da Universidade de Munique, na Alemanha, que gera imagens a partir de informações de texto fornecidas.
Ao treinar com várias imagens, ele pode gerar uma variedade de imagens, desde fotografias até ilustrações.

Desta vez, apresentarei como gerar imagens de ilustração usando os dados pré-treinados do Stable diffusion.

# O que você vai precisar

- Conta do Google

Apenas isso

# Procedimento de geração

1. Abra https://colab.research.google.com
2. Selecione `Arquivo` no canto superior esquerdo e depois `Novo notebook`
3. Selecione `Editar` e depois `Configurações do notebook`
4. Altere o `Acelerador de hardware` para `GPU`
![img_2.png](img_2.png)
5. Cole o código abaixo e execute
```
!pip install diffusers==0.8.0 transformers
```
6. Cole o código abaixo e execute
```
from diffusers import StableDiffusionPipeline
```
7. Cole o código abaixo e execute
```
pipe = StableDiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5")
pipe.to("cuda")
```
8. Cole o código abaixo e execute
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

O `Prompt` usado aqui é baseado no `Prompt` de [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5).

## Resultados gerados (alguns)
![img_1.png](img_1.png)

![img_3.png](img_3.png)

![img_4.png](img_4.png)

## Referências

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Criei um programa de geração de imagens usando Inteligência Artificial (IA) em 15 minutos 【Programação ao vivo】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
