---


title: "Cómo generar ilustraciones con IA usando Stable Diffusion: guía de Google Colab y advertencias"
lastmod: "2026-11-23"
slug: "AI(StableDiffusion)を使ってIlustraciónGeneración de imágenesする方法"
date: 2023-04-06T00:43:19+09:00
tags: ["IA", "Stable Diffusion", "ilustración", "generación de imágenes", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["programming", "image-generation"]
description: "Guía paso a paso para generar ilustraciones con Stable Diffusion y Google Colab, con advertencias sobre la disponibilidad de GPU y la licencia del modelo."
---



# ¿Qué es Stable Diffusion?
Stable Diffusion es una familia de modelos de difusión latente que genera imágenes a partir de condiciones como el texto. La investigación relacionada incluye el trabajo del equipo CompVis, entre cuyos autores hay investigadores de la Universidad Ludwig Maximilian de Múnich.

# Lo que necesitas

- Una cuenta de Google

Solo eso.

# Procedimiento de generación

Este tutorial actualiza un ejemplo de 2023 para la API actual de Diffusers. No se garantiza que Colab asigne una GPU gratuita; los límites, los tipos de GPU y la disponibilidad cambian. Si no se asigna una GPU, inténtalo más tarde o usa otro entorno disponible.

Antes de cargar los pesos, lee la ficha del modelo y su licencia CreativeML OpenRAIL-M en Hugging Face. Respeta los usos prohibidos, las condiciones de distribución y las leyes locales. La licencia no garantiza que el resultado sea legal ni que esté libre de derechos de terceros.

`EasyNegative` en este ejemplo es una incrustación de textual inversion distribuida por separado. El código siguiente la carga antes de usar el token en el prompt.

1. Abre https://colab.research.google.com
2. En la esquina superior izquierda, selecciona `Archivo` y luego `Nuevo cuaderno`
3. Selecciona `Editar` y luego `Configuración del cuaderno`
4. Cambia el `Acelerador de hardware` a `GPU`
![img_2.png](img_2.webp)
5. Pega y ejecuta el siguiente código
```
!pip install -U diffusers transformers accelerate
```
6. Pega y ejecuta el siguiente código
```
import torch
from diffusers import DiffusionPipeline
from huggingface_hub import hf_hub_download
```
7. Pega y ejecuta el siguiente código
```
pipe = DiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5", dtype=torch.float16)
easynegative_path = hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors")
pipe.load_textual_inversion(easynegative_path, token="EasyNegative")
pipe.to("cuda")
```
8. Pega y ejecuta el siguiente código
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

El `Prompt` utilizado aquí está basado en el `Prompt` de [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5).

## Resultados generados (algunos)
![img_1.png](img_1.webp)

![img_3.png](img_3.webp)

![img_4.png](img_4.webp)

## Referencias

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Hice un programa de generación de imágenes con Inteligencia Artificial (IA) en 15 minutos 【Programación en vivo】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
- [Google Colab FAQ: resource limits](https://research.google.com/colaboratory/faq.html)
- [Diffusers: loading pipelines](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Stable Diffusion model card and license](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [CompVis: Stable Diffusion research and code](https://github.com/CompVis/stable-diffusion)
- [EasyNegative textual-inversion embedding](https://huggingface.co/datasets/gsdf/EasyNegative)
