---


title: "Cómo generar imágenes de ilustraciones usando IA (Stable Diffusion)"
date: 2023-04-06T00:43:19+09:00
tags: ["IA", "Stable Diffusion", "ilustración", "generación de imágenes", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Programación"]
---



# ¿Qué es Stable Diffusion?
Stable Diffusion es una IA que genera imágenes a partir de información de texto (texto a imagen), desarrollada por un equipo de investigación de la Universidad de Múnich, Alemania.
Al entrenar con diversas imágenes, puede generar una amplia variedad de imágenes, desde fotografías realistas hasta ilustraciones.

En esta ocasión, presentaré cómo generar imágenes de ilustraciones utilizando datos preentrenados de Stable Diffusion.

# Lo que necesitas

- Una cuenta de Google

Solo eso.

# Procedimiento de generación

1. Abre https://colab.research.google.com
2. En la esquina superior izquierda, selecciona `Archivo` y luego `Nuevo cuaderno`
3. Selecciona `Editar` y luego `Configuración del cuaderno`
4. Cambia el `Acelerador de hardware` a `GPU`
![img_2.png](img_2.png)
5. Pega y ejecuta el siguiente código
```
!pip install diffusers==0.8.0 transformers
```
6. Pega y ejecuta el siguiente código
```
from diffusers import StableDiffusionPipeline
```
7. Pega y ejecuta el siguiente código
```
pipe = StableDiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5")
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
![img_1.png](img_1.png)

![img_3.png](img_3.png)

![img_4.png](img_4.png)

## Referencias

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Hice un programa de generación de imágenes con Inteligencia Artificial (IA) en 15 minutos 【Programación en vivo】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
