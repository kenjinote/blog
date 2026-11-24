---
title: "Cómo usar yt-dlp.exe: descargar contenido autorizado y convertirlo a MP3"
slug: "yt-dlp.exe による YouTube VideoのDescargar方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Cómo obtener y actualizar yt-dlp.exe, guardar un vídeo y convertir audio a MP3. Úsalo de acuerdo con los derechos del contenido y las condiciones de YouTube."
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Cómo usar yt-dlp.exe: descargar contenido autorizado y convertirlo a MP3

yt-dlp es una herramienta de línea de comandos de código abierto para descargar vídeo y audio. Estos ejemplos muestran el uso básico en Windows.

## Úsalo solo cuando esté permitido

Usa yt-dlp únicamente con contenido propio o cuyo titular te haya autorizado a descargar, y solo cuando lo permitan las condiciones de YouTube y la legislación aplicable. Puedes descargar tus propias subidas desde YouTube Studio.

## Instalación y actualización

Descarga el `yt-dlp.exe` para Windows desde la página oficial de versiones y guárdalo en una carpeta. Añade esa carpeta a `PATH` para ejecutarlo desde cualquier directorio. Obtén el ejecutable solo de las versiones oficiales.

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## Uso básico

En el Símbolo del sistema o PowerShell, indica la URL del vídeo. El archivo se guarda en el directorio actual.

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

Para convertir el audio a MP3, usa `-x` y `--audio-format mp3`.

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

Comprueba la versión con `yt-dlp.exe --version`. Puedes actualizar una versión binaria con `yt-dlp.exe -U`. La conversión a MP3 requiere `ffmpeg` y `ffprobe`. Si YouTube cambia y deja de funcionar la extracción, actualiza yt-dlp y consulta las dependencias actuales en el README oficial.

Para incrustar miniaturas o metadatos, puedes añadir `--embed-thumbnail` o `--embed-metadata`; según el formato, quizá se necesiten herramientas adicionales.

## Si no funciona

Actualiza a la versión más reciente y consulta la documentación oficial sobre dependencias y compatibilidad actuales. No eludas restricciones ni descargues contenido sin autorización.

## Referencias

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)
