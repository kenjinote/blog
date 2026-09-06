---
title: "Wie man Illustrationsbilder mit KI (Stable Diffusion) generiert"
slug: "AI(StableDiffusion)を使ってイラスト画像生成する方法"
date: 2023-04-06T00:43:19+09:00
tags: ["KI", "Stable Diffusion", "Illustration", "Bildgenerierung", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---

# Was ist Stable diffusion
Stable diffusion ist eine KI, die von einem Forschungsteam der Universität München, Deutschland, entwickelt wurde und Bilder aus eingegebenen Textinformationen generiert.
Indem sie mit verschiedenen Bildern trainiert wurde, kann sie eine Vielzahl von Bildern generieren, von Fotos bis hin zu Illustrationen.

Dieses Mal werde ich vorstellen, wie man Illustrationsbilder mit den vortrainierten Daten von Stable diffusion generiert.

# Was Sie benötigen

- Google-Konto

Nur das

# Generierungsverfahren

1. Öffnen Sie https://colab.research.google.com
2. Wählen Sie `Datei` oben links und dann `Neues Notebook`
3. Wählen Sie `Bearbeiten` und dann `Notebook-Einstellungen`
4. Ändern Sie den `Hardwarebeschleuniger` auf `GPU`
![img_2.png](img_2.png)
5. Fügen Sie den folgenden Code ein und führen Sie ihn aus
```
!pip install diffusers==0.8.0 transformers
```
6. Fügen Sie den folgenden Code ein und führen Sie ihn aus
```
from diffusers import StableDiffusionPipeline
```
7. Fügen Sie den folgenden Code ein und führen Sie ihn aus
```
pipe = StableDiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5")
pipe.to("cuda")
```
8. Fügen Sie den folgenden Code ein und führen Sie ihn aus
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

Der hier verwendete `Prompt` basiert auf dem `Prompt` von [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5).

## Generierte Ergebnisse (einige)
![img_1.png](img_1.png)

![img_3.png](img_3.png)

![img_4.png](img_4.png)

## Referenzen

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Ich habe in 15 Minuten ein Bildgenerierungsprogramm mit Künstlicher Intelligenz (KI) erstellt 【Live-Programmierung】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
