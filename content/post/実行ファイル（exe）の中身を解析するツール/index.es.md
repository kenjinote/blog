---

title: "Herramientas para analizar el contenido de un archivo ejecutable (exe)"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "archivo ejecutable", "análisis"]
draft: false
image: "img_1.png"
categories: ["PC y Gadgets"]
---


# ¿Qué es un archivo ejecutable (exe)?

Un archivo ejecutable en Windows. Básicamente está escrito en un formato llamado formato PE.
Contiene código en lenguaje de máquina para su ejecución, así como recursos como iconos e imágenes.

Dado que existen varias herramientas para analizar archivos ejecutables, las presentaremos en esta ocasión.

## 7-Zip

![img.png](img.png)

Los archivos EXE a veces se crean comprimiendo archivos porque su tamaño tiende a ser grande tal como están. En este caso, puede usar el software de compresión y descompresión de archivos 7-Zip para descomprimir el archivo ejecutable e inspeccionar su contenido. WinRAR es otra herramienta que puede descomprimir de manera similar.

## Resource Hacker
![img_2.png](img_2.png)

Permite extraer recursos (iconos, mapas de bits, cuadros de diálogo, cadenas de texto, etc.) que se encuentran dentro de un archivo EXE. Además, dado que también funciona como un editor hexadecimal, puede editar y reescribir el contenido del archivo EXE.

## PE Explorer
![img_3.png](img_3.png)

Permite analizar archivos PE para Windows (EXE, DLL, OCX, SYS, controladores). PE Explorer ofrece diversas funciones de análisis, como la visualización de la estructura del archivo, la visualización del encabezado del archivo, la visualización de las entradas del directorio y la visualización de funciones y símbolos exportados.

## Dependency Walker
![img_4.png](img_4.png)

Permite investigar los archivos DLL de los que depende un archivo EXE y verificar si se cargan correctamente. También puede rastrear las llamadas a funciones en los archivos DLL.

Estas herramientas son útiles para investigar el contenido de un archivo EXE, pero requieren precaución. Editar archivos o usarlos para fines ilícitos puede causar problemas de derechos de autor o de seguridad, por lo que debe utilizarlas con una comprensión suficiente de los riesgos.
