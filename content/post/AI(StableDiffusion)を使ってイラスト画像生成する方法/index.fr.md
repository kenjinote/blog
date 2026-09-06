---
title: "Comment générer des images d'illustration à l'aide de l'IA (Stable Diffusion)"
slug: "AI(StableDiffusion)を使ってイラスト画像生成する方法"
date: 2023-04-06T00:43:19+09:00
tags: ["IA", "Stable Diffusion", "Illustration", "Génération d'images", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

# Qu'est-ce que Stable diffusion
Stable diffusion est une IA développée par une équipe de recherche de l'Université de Munich, en Allemagne, qui génère des images à partir d'informations textuelles fournies.
En lui apprenant diverses images, il peut générer une grande variété d'images allant des photographies aux illustrations.

Cette fois, je vais vous présenter comment générer des images d'illustration à l'aide des données pré-entraînées de Stable diffusion.

# Ce dont vous aurez besoin

- Compte Google

Seulement ça

# Procédure de génération

1. Ouvrez https://colab.research.google.com
2. Sélectionnez `Fichier` en haut à gauche, puis `Nouveau notebook`
3. Sélectionnez `Modifier`, puis `Paramètres du notebook`
4. Changez l'`Accélérateur matériel` en `GPU`
![img_2.png](img_2.png)
5. Collez et exécutez le code ci-dessous
```
!pip install diffusers==0.8.0 transformers
```
6. Collez et exécutez le code ci-dessous
```
from diffusers import StableDiffusionPipeline
```
7. Collez et exécutez le code ci-dessous
```
pipe = StableDiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5")
pipe.to("cuda")
```
8. Collez et exécutez le code ci-dessous
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

Le `Prompt` utilisé ici est basé sur le `Prompt` de [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5).

## Résultats générés (quelques-uns)
![img_1.png](img_1.png)

![img_3.png](img_3.png)

![img_4.png](img_4.png)

## Références

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [J'ai créé un programme de génération d'images à l'aide de l'Intelligence Artificielle (IA) en 15 minutes 【Programmation en direct】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
