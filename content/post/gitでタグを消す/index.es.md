---


title: "'Eliminar etiquetas en git'"
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.png"
categories: ["Herramientas y Entornos de Desarrollo"]
---


# Eliminar etiquetas locales

1. Usa `git tag` para verificar las etiquetas locales existentes.
2. Usa `git tag -d v0.1.0` para eliminar una etiqueta. (Especifica la etiqueta que deseas eliminar en lugar de `v0.1.0`)

# Eliminar etiquetas remotas

1. Usa `git ls-remote --tags` para verificar las etiquetas remotas existentes.
2. Usa `git push origin --delete v0.1.0` para eliminar una etiqueta remota. (Especifica la etiqueta que deseas eliminar en lugar de `v0.1.0`)

## Referencia
[¡Cómo eliminar un tag en git de forma remota y local!](https://qumeru.com/magazine/528)
