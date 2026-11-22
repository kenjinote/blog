---
title: "Как создавать иллюстрации с помощью Stable Diffusion: руководство по Google Colab и важные замечания"
lastmod: "2026-11-23"
slug: "AI(StableDiffusion)を使ってИллюстрацияГенерация изображенийする方法"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "иллюстрация", "генерация изображений", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["programming", "image-generation"]
description: "Пошаговое руководство по созданию иллюстраций с Stable Diffusion и Google Colab с замечаниями о доступности GPU и лицензии модели."
---

# Что такое Stable diffusion
Stable Diffusion — семейство моделей латентной диффузии, создающих изображения по условиям, например по тексту. К связанным исследованиям относится работа команды CompVis; среди авторов есть исследователи из Мюнхенского университета Людвига — Максимилиана.

# Что понадобится

- Аккаунт Google

И всё.

# Процесс генерации

В этом руководстве пример 2023 года обновлён для текущего API Diffusers. Colab не гарантирует бесплатный GPU; лимиты, типы GPU и доступность меняются. Если GPU не назначен, попробуйте позже или используйте другую доступную среду выполнения.

Перед загрузкой весов прочитайте карточку модели и лицензию CreativeML OpenRAIL-M на Hugging Face. Соблюдайте ограничения на использование, условия распространения и местное законодательство. Лицензия не гарантирует законность результата или отсутствие прав третьих лиц.

В этом примере `EasyNegative` — отдельно распространяемый embedding Textual Inversion. Следующий код загружает его до использования токена в запросе.

1. Откройте https://colab.research.google.com
2. В левом верхнем углу выберите `Файл` и нажмите `Создать блокнот`
3. В меню `Редактировать` выберите `Настройки блокнота`
4. Измените `Аппаратный ускоритель` на `GPU`
![img_2.png](img_2.webp)
5. Вставьте следующий код и выполните его
```
!pip install -U diffusers transformers accelerate
```
6. Вставьте следующий код и выполните его
```
import torch
from diffusers import DiffusionPipeline
from huggingface_hub import hf_hub_download
```
7. Вставьте следующий код и выполните его
```
pipe = DiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5", dtype=torch.float16)
easynegative_path = hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors")
pipe.load_textual_inversion(easynegative_path, token="EasyNegative")
pipe.to("cuda")
```
8. Вставьте следующий код и выполните его
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

Используемый здесь `Prompt` основан на `Prompt` с [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5).

## Результаты генерации (несколько)
![img_1.png](img_1.webp)

![img_3.png](img_3.webp)

![img_4.png](img_4.webp)

## Ссылки

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Я попытался создать программу для генерации изображений с использованием искусственного интеллекта (ИИ) за 15 минут 【Живое программирование】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
- [Google Colab FAQ: resource limits](https://research.google.com/colaboratory/faq.html)
- [Diffusers: loading pipelines](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Stable Diffusion model card and license](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [CompVis: Stable Diffusion research and code](https://github.com/CompVis/stable-diffusion)
- [EasyNegative textual-inversion embedding](https://huggingface.co/datasets/gsdf/EasyNegative)
