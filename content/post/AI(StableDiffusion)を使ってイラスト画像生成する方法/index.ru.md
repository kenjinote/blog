---
title: "Как создать иллюстрации с помощью ИИ (StableDiffusion)"
slug: "как-создать-иллюстрации-с-помощью-ии-stablediffusion"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "иллюстрация", "генерация изображений", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Программирование"]
---

# Что такое Stable diffusion
Stable diffusion — это ИИ, генерирующий изображения на основе введенной текстовой информации, разработанный исследовательской группой Мюнхенского университета в Германии.
Обучаясь на различных изображениях, он может создавать самые разные картинки, от фотореалистичных до иллюстраций.

В этот раз я расскажу, как генерировать иллюстрации с использованием предварительно обученных данных Stable diffusion.

# Что понадобится

- Аккаунт Google

И всё.

# Процесс генерации

1. Откройте https://colab.research.google.com
2. В левом верхнем углу выберите `Файл` и нажмите `Создать блокнот`
3. В меню `Редактировать` выберите `Настройки блокнота`
4. Измените `Аппаратный ускоритель` на `GPU`
![img_2.png](img_2.png)
5. Вставьте следующий код и выполните его
```
!pip install diffusers==0.8.0 transformers
```
6. Вставьте следующий код и выполните его
```
from diffusers import StableDiffusionPipeline
```
7. Вставьте следующий код и выполните его
```
pipe = StableDiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5")
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
![img_1.png](img_1.png)

![img_3.png](img_3.png)

![img_4.png](img_4.png)

## Ссылки

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Я попытался создать программу для генерации изображений с использованием искусственного интеллекта (ИИ) за 15 минут 【Живое программирование】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
