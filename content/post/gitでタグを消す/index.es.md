---
title: 'Cómo eliminar etiquetas (tags) locales y remotas en Git'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["git"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Una explicación simple sobre cómo eliminar etiquetas (tags) que ya no son necesarias en Git. Cubrimos desde la eliminación de etiquetas en el entorno local con "git tag -d" hasta la eliminación de etiquetas en el repositorio remoto usando "git push origin --delete".'
---
# Eliminar etiquetas locales

1. Usa `git tag` para verificar las etiquetas locales existentes.
2. Usa `git tag -d v0.1.0` para eliminar una etiqueta. (Especifica la etiqueta que deseas eliminar en lugar de `v0.1.0`)

# Eliminar etiquetas remotas

1. Usa `git ls-remote --tags --refs origin` para verificar las etiquetas remotas existentes.
2. Usa `git push origin --delete v0.1.0` para eliminar una etiqueta remota. (Especifica la etiqueta que deseas eliminar en lugar de `v0.1.0`)

Eliminar la etiqueta remota no borra automáticamente las copias locales de los colaboradores. Confirma el destino, ya que afecta a quienes usan ese remoto.

## Referencias
[git-tag](https://git-scm.com/docs/git-tag), [git-ls-remote](https://git-scm.com/docs/git-ls-remote), [git-push](https://git-scm.com/docs/git-push)
