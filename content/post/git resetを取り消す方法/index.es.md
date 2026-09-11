---







title: 'Cómo deshacer un git reset ejecutado por error｜Pasos para restaurar commits'
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "restaurar", "deshacer"]
draft: false
image: "img.webp"
categories: ["Herramientas y Entornos de Desarrollo"]
description: 'Explicamos cómo cancelar y restaurar el estado original de un commit cuando has ejecutado "git reset" por error en Git. Mostramos de forma clara cómo usar "git reflog" para verificar el ID del commit y restaurar correctamente el estado.'
---







# Cómo deshacer git reset
Si después de realizar un git commit ejecutas git reset por error, te mostraré cómo deshacer el git reset (cómo restaurar el estado en el momento del git commit).

1. Verifica el ID del commit antes del reset con `git reflog`
2. Vuelve al estado antes del reset con `git reset --hard HEAD@{número}`

Eso es todo sobre cómo deshacer un git reset.
