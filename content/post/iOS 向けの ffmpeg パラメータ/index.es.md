---




title: "Parámetros de ffmpeg para iOS"
date: 2025-03-02T04:16:07+09:00
tags: ["iOS", "ffmpeg"]
draft: false
image: "img.png"
categories: ["PC y Gadgets"]
---





# Parámetros de conversión de ffmpeg optimizados para iOS

A continuación, se presenta el comando `ffmpeg` para convertir videos y que se reproduzcan sin problemas en dispositivos iOS (iPhone o iPad).

```bash
ffmpeg -i input.mp4 \
-c:v libx264 -profile:v high -level 4.1 \
-vf "scale=1920:-2" -r 30 \
-crf 20 -preset slow \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart output.mp4
```

### Significado de cada opción (breve explicación)

| Opción                            | Descripción                                                                            |
| --------------------------------- | -------------------------------------------------------------------------------------- |
| `-i input.mp4`                    | Archivo de entrada (video a convertir)                                                 |
| `-c:v libx264`                    | Codifica el video en H.264 (compatible con iOS)                                        |
| `-profile:v high -level 4.1`      | Perfil y nivel de amplia compatibilidad en iOS                                         |
| `-vf "scale=1920:-2"`             | Redimensiona a 1920px de ancho, ajuste automático de altura para mantener la relación de aspecto |
| `-r 30`                           | Convierte la tasa de cuadros a 30fps                                                   |
| `-crf 20`                         | Calidad de video (menor valor = mayor calidad, recomendado 18-23)                      |
| `-preset slow`                    | Balance entre velocidad de codificación y compresión (slow = alta compresión y calidad)  |
| `-c:a aac`                        | Codifica el audio en formato AAC                                                       |
| `-b:a 128k`                       | Establece la tasa de bits de audio en 128kbps                                          |
| `-ar 48000`                       | Establece la frecuencia de muestreo de audio en 48kHz (recomendado para iOS)           |
| `-movflags +faststart`            | Coloca el índice al inicio del video, **acelerando la reproducción por streaming en Web e iOS** |

---

Se espera que los videos convertidos con esta configuración tengan alta compatibilidad y una reproducción fluida en dispositivos de Apple como iPhone e iPad.

---

Si es necesario, puedes ajustar el tamaño del archivo y la calidad de la imagen modificando la resolución y la tasa de bits. Si necesitas alta calidad, intenta establecer `-crf` alrededor de 18; si deseas reducir el tamaño del archivo, configúralo entre 22 y 25.
