---







title: 'Cómo clonar un repositorio Git con historial superficial'
slug: "gitRepositorioの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "repositorio", "comando"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Conoce qué transfiere git clone --depth 1, cómo elegir una rama y cómo obtener más historial después.'
---

# Clonar un repositorio con historial superficial

`git clone --depth 1` crea un clon superficial con profundidad de historial uno desde la punta de la rama seleccionada. De forma predeterminada, se selecciona la rama predeterminada del remoto. Esto reduce el historial de commits transferido, pero Git sigue descargando los archivos actuales y los objetos necesarios; por eso, un repositorio con archivos grandes aún puede ocupar mucho.

```sh
git clone --depth 1 <repository-url>
```

Para elegir una rama, indica su nombre:

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

Puedes obtener más historial después, por ejemplo:

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

Sustituye `<directory>` y `<branch>` por los nombres reales. Con `--depth`, Git también implica `--single-branch` salvo que se indique lo contrario. Consulta los manuales oficiales de [`git clone`](https://git-scm.com/docs/git-clone) y [`git fetch`](https://git-scm.com/docs/git-fetch), incluida la opción `--unshallow`.
