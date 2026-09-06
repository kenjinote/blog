---







title: "Obtener solo lo más reciente de un repositorio git"
slug: "gitリポジトリの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
tags: ["git", "repositorio", "comando"]
draft: false
image: "img.png"
categories: ["Herramientas y entorno de desarrollo"]
---








# Obtener solo lo más reciente del repositorio

Con el siguiente comando puedes obtener solo lo más reciente del repositorio.
Es útil cuando quieres obtener el repositorio rápidamente para ahorrar espacio en el disco.

```
git clone --depth 1 <URL del repositorio>
```
