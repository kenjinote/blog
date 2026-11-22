---
title: "Como gerar ilustrações com IA usando Stable Diffusion: guia do Google Colab e observações"
lastmod: "2026-11-23"
slug: "AI(StableDiffusion)を使ってIlustraçãoGeração de Imagemする方法"
date: 2023-04-06T00:43:19+09:00
tags: ["IA", "Stable Diffusion", "Ilustração", "Geração de Imagens", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["programming", "image-generation"]
description: "Guia passo a passo para gerar ilustrações com Stable Diffusion e Google Colab, incluindo observações sobre disponibilidade de GPU e licença do modelo."
---

# O que é o Stable diffusion
Stable Diffusion é uma família de modelos de difusão latente que gera imagens a partir de condições como texto. A pesquisa relacionada inclui o trabalho da equipe CompVis, com pesquisadores da Universidade Ludwig Maximilian de Munique entre os autores.

# O que você vai precisar

- Conta do Google

Apenas isso

# Procedimento de geração

Este tutorial atualiza um exemplo de 2023 para a API atual do Diffusers. O Colab não garante uma GPU gratuita; limites, modelos de GPU e disponibilidade de execução variam. Se uma GPU não for atribuída, tente novamente mais tarde ou use outro ambiente disponível.

Antes de carregar os pesos, leia o cartão do modelo e a licença CreativeML OpenRAIL-M no Hugging Face. Respeite os usos proibidos, os termos de distribuição e as leis locais. A licença não garante que o resultado seja legal nem livre de direitos de terceiros.

`EasyNegative` neste exemplo é um embedding de textual inversion distribuído separadamente. O código abaixo o carrega antes de usar o token no prompt.

1. Abra https://colab.research.google.com
2. Selecione `Arquivo` no canto superior esquerdo e depois `Novo notebook`
3. Selecione `Editar` e depois `Configurações do notebook`
4. Altere o `Acelerador de hardware` para `GPU`
![img_2.png](img_2.webp)
5. Cole o código abaixo e execute
```
!pip install -U diffusers transformers accelerate
```
6. Cole o código abaixo e execute
```
import torch
from diffusers import DiffusionPipeline
from huggingface_hub import hf_hub_download
```
7. Cole o código abaixo e execute
```
pipe = DiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5", dtype=torch.float16)
easynegative_path = hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors")
pipe.load_textual_inversion(easynegative_path, token="EasyNegative")
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
![img_1.png](img_1.webp)

![img_3.png](img_3.webp)

![img_4.png](img_4.webp)

## Referências

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Criei um programa de geração de imagens usando Inteligência Artificial (IA) em 15 minutos 【Programação ao vivo】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
- [Google Colab FAQ: resource limits](https://research.google.com/colaboratory/faq.html)
- [Diffusers: loading pipelines](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Stable Diffusion model card and license](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [CompVis: Stable Diffusion research and code](https://github.com/CompVis/stable-diffusion)
- [EasyNegative textual-inversion embedding](https://huggingface.co/datasets/gsdf/EasyNegative)
