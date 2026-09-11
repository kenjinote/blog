---







title: 'Cómo descargar solo el último commit de un repositorio con Git clone'
slug: "gitリポジトリの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
tags: ["git", "repositorio", "comando"]
draft: false
image: "img.webp"
categories: ["Herramientas y entorno de desarrollo"]
description: 'Explicamos cómo obtener únicamente el commit más reciente (shallow clone) sin descargar todo el historial de un repositorio Git. Una técnica muy útil para ahorrar espacio en disco usando la opción "--depth 1" y clonar rápidamente el repositorio.'
---








# Obtener solo lo más reciente del repositorio

Con el siguiente comando puedes obtener solo lo más reciente del repositorio.
Es útil cuando quieres obtener el repositorio rápidamente para ahorrar espacio en el disco.

```
git clone --depth 1 <URL del repositorio>
```
