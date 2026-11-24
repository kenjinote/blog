---







title: '¡Úsalo en Windows! Cómo instalar el editor de texto ligero ''micro'''
slug: "Editor de textomicroをWindowsにInstalaciónする方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "editor de texto"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Explicamos de forma sencilla los pasos para instalar ''micro'', un editor de texto orientado a terminal que funciona fluidamente en el símbolo del sistema, en Windows y cómo configurar las variables de entorno para usarlo.'
---








## Descargar micro
https://github.com/micro-editor/micro/releases/latest
En Assets de la versión más reciente, descarga el archivo para Windows x64 (por ejemplo, `micro-<version>-win64.zip`) y extráelo en una carpeta de tu elección.

Para Windows en ARM, elige en su lugar el archivo ARM64 correspondiente.

## Configurar variables de entorno
Para usar `micro.exe` desde el símbolo del sistema, es necesario configurar las variables de entorno.

1. Pulsa `Win` + `R`, escribe `sysdm.cpl` y pulsa `Enter`.
2. Abre la pestaña Opciones avanzadas y haz clic en Variables de entorno.
3. En Variables de usuario de tu cuenta, selecciona `Path` y haz clic en Editar. Si no aparece, crea `Path`.
4. Haz clic en Nuevo y agrega la ruta de la carpeta que contiene `micro.exe`.
5. Haz clic en Aceptar para cerrar los cuadros de diálogo.
6. Vuelve a abrir el símbolo del sistema y ejecuta `micro` para comprobar que se inicia.

## Cómo usar micro

Al escribir `micro` en el símbolo del sistema y ejecutarlo, se mostrará la siguiente pantalla.
![img_3.png](img_3.webp)

A continuación se muestran las operaciones principales y los atajos de teclado.

| Atajo de teclado | Operación | 
|--------|-----| 
| Ctrl+Q | Cerrar el archivo actual (micro se cierra si es el último archivo) |
| Ctrl+S | Guardar archivo | 
| Ctrl+O | Abrir archivo | 
| Ctrl+A | Seleccionar todo | 
| Ctrl+X | Cortar selección | 
| Ctrl+C | Copiar selección | 
| Ctrl+V | Pegar | 
| Ctrl+Z | Deshacer | 
| Ctrl+Y | Rehacer | 
| Ctrl+E | Ejecutar comando del editor | 

## Referencias
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)
