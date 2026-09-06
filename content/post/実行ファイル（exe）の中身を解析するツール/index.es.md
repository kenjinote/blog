---
title: "Herramientas para analizar el contenido de archivos ejecutables (exe)"
slug: "herramientas-para-analizar-el-contenido-de-archivos-ejecutables-exe"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "archivo ejecutable", "análisis"]
draft: false
image: "img_1.png"
categories: ["PC y Gadgets"]
---

# Qué es un archivo ejecutable (exe)

Un archivo ejecutable en Windows. Básicamente, está escrito en un formato llamado formato PE.
Contiene código en lenguaje de máquina para su ejecución, así como recursos como iconos e imágenes.

Dado que existen varias herramientas para analizar archivos ejecutables, las presentaremos en esta ocasión.

## 7-Zip

![img.png](img.png)

Los archivos EXE, como tienden a ser grandes si se dejan como están, a veces se crean mediante compresión de archivos. En este caso, utilizando el software de compresión y descompresión de archivos 7-Zip, puede descomprimir el archivo ejecutable e investigar su contenido. También existe una herramienta llamada WinRAR que puede descomprimir de la misma manera.

## Resource Hacker
![img_2.png](img_2.png)

Puede extraer los recursos (iconos, mapas de bits, cuadros de diálogo, cadenas de texto, etc.) dentro del archivo EXE. Además, como también funciona como un editor hexadecimal, puede editar y reescribir el contenido del archivo EXE.

## PE Explorer
![img_3.png](img_3.png)

Puede analizar archivos PE para Windows (EXE, DLL, OCX, SYS, controladores). PE Explorer proporciona varias funciones de análisis, como mostrar la estructura del archivo, mostrar el encabezado del archivo, mostrar entradas de directorio, y mostrar funciones y símbolos exportados.

## Dependency Walker
![img_4.png](img_4.png)

Puede verificar de qué archivos DLL depende un archivo EXE y si se han cargado correctamente. También puede rastrear llamadas a funciones en archivos DLL.

## Ghidra

Es una poderosa herramienta de ingeniería inversa desarrollada por la NSA (Agencia de Seguridad Nacional de EE. UU.) y publicada gratuitamente como código abierto. No solo desensambla (convierte a lenguaje ensamblador) archivos EXE, sino que también tiene una función de descompilación a un formato cercano al lenguaje C, lo que la hace muy popular.

## IDA Free / IDA Pro

Es un desensamblador y descompilador avanzado que se ha convertido en un estándar mundial de la industria en análisis de malware e ingeniería inversa. La versión Pro es muy cara, pero si es para fines personales o no comerciales, puede usar la versión con funciones limitadas "IDA Free" de forma gratuita.

## x64dbg (x32dbg)

Es un depurador de código abierto para Windows. Se especializa en "análisis dinámico", que analiza el contenido y el estado de la memoria paso a paso mientras se ejecuta el archivo ejecutable, y se usa a menudo para descifrar crackmes (programas de desafío de análisis) e investigar el comportamiento del malware.

## ILSpy / dotPeek

Si el archivo EXE de destino fue creado en un lenguaje del sistema .NET como C#, puede usar estas herramientas para descompilarlo a un estado casi idéntico al código fuente original y exponer completamente su contenido.

Estas herramientas son útiles para investigar el contenido de archivos EXE, pero requieren precaución. Editar archivos o usarlos con fines maliciosos puede causar problemas de seguridad o relacionados con la ley de derechos de autor, así que úselos solo después de comprender esto completamente.
