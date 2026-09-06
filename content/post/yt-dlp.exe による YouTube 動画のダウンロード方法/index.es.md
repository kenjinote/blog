---








title: "Cómo descargar videos de YouTube con yt-dlp.exe"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "Descarga"]
draft: false
image: "img_1.png"
categories: ["IT y Tecnología"]
---








# ¿Qué es yt-dlp?

`yt-dlp` es una herramienta de línea de comandos para descargar videos de YouTube.
No solo te permite descargar videos, sino que también puedes descargarlos como archivos de música en formato mp3.

## Descarga e instalación

1. Descarga la versión más reciente de yt-dlp.exe desde la [página de lanzamientos de yt-dlp](https://github.com/yt-dlp/yt-dlp/releases).
2. Coloca yt-dlp.exe en la carpeta que desees.
3. Agrega la ruta de la carpeta de yt-dlp.exe a la variable de entorno Path.

## Modo de uso

Ejecuta yt-dlp.exe en el símbolo del sistema y especifica la URL del video de YouTube.

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※ Como argumento, puedes usar solo la parte de VIDEO_ID en lugar de la URL completa.

Si deseas descargar un archivo de música en formato mp3, ejecuta el siguiente comando:

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

Con esto, el video se descargará en el directorio actual desde donde ejecutaste el comando.

Eso es todo.
