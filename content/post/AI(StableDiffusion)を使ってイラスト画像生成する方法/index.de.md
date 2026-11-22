---
title: "KI-Illustrationen mit Stable Diffusion erstellen: Google-Colab-Anleitung und Hinweise"
lastmod: "2026-11-23"
slug: "AI(StableDiffusion)を使ってIllustrationBilderzeugungする方法"
date: 2023-04-06T00:43:19+09:00
tags: ["KI", "Stable Diffusion", "Illustration", "Bildgenerierung", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["programming", "image-generation"]
description: "Schritt-für-Schritt-Anleitung zum Erstellen von Illustrationen mit Stable Diffusion und Google Colab, einschließlich Hinweisen zur GPU-Verfügbarkeit und Modelllizenz."
---

# Was ist Stable diffusion
Stable Diffusion ist eine Familie latenter Diffusionsmodelle, die Bilder anhand von Bedingungen wie Text erzeugt. Zu den einschlägigen Forschungsarbeiten gehört die Arbeit des CompVis-Teams, zu dessen Autoren Forschende der Ludwig-Maximilians-Universität München zählen.

# Was Sie benötigen

- Google-Konto

Nur das

# Generierungsverfahren

Diese Anleitung aktualisiert ein Beispiel aus dem Jahr 2023 für die aktuelle Diffusers-API. Colab garantiert keine kostenlose GPU; Nutzungslimits, GPU-Typen und Verfügbarkeit ändern sich. Wird keine GPU zugewiesen, versuchen Sie es später erneut oder verwenden Sie eine andere verfügbare Laufzeitumgebung.

Lesen Sie vor dem Laden der Modellgewichte die Modellkarte und die CreativeML OpenRAIL-M-Lizenz auf Hugging Face. Beachten Sie verbotene Nutzungen, Weitergabebedingungen und das örtliche Recht. Die Lizenz garantiert weder die Rechtmäßigkeit der Ergebnisse noch die Freiheit von Rechten Dritter.

`EasyNegative` ist in diesem Beispiel ein separat bereitgestelltes Textual-Inversion-Embedding. Der folgende Code lädt es, bevor das Token im Prompt verwendet wird.

1. Öffnen Sie https://colab.research.google.com
2. Wählen Sie `Datei` oben links und dann `Neues Notebook`
3. Wählen Sie `Bearbeiten` und dann `Notebook-Einstellungen`
4. Ändern Sie den `Hardwarebeschleuniger` auf `GPU`
![img_2.png](img_2.webp)
5. Fügen Sie den folgenden Code ein und führen Sie ihn aus
```
!pip install -U diffusers transformers accelerate
```
6. Fügen Sie den folgenden Code ein und führen Sie ihn aus
```
import torch
from diffusers import DiffusionPipeline
from huggingface_hub import hf_hub_download
```
7. Fügen Sie den folgenden Code ein und führen Sie ihn aus
```
pipe = DiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5", dtype=torch.float16)
easynegative_path = hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors")
pipe.load_textual_inversion(easynegative_path, token="EasyNegative")
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
![img_1.png](img_1.webp)

![img_3.png](img_3.webp)

![img_4.png](img_4.webp)

## Referenzen

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Ich habe in 15 Minuten ein Bildgenerierungsprogramm mit Künstlicher Intelligenz (KI) erstellt 【Live-Programmierung】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
- [Google Colab FAQ: resource limits](https://research.google.com/colaboratory/faq.html)
- [Diffusers: loading pipelines](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Stable Diffusion model card and license](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [CompVis: Stable Diffusion research and code](https://github.com/CompVis/stable-diffusion)
- [EasyNegative textual-inversion embedding](https://huggingface.co/datasets/gsdf/EasyNegative)
