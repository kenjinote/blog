---
title: "Exclusão Rápida em Lote de Pastas Grandes"
slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
tags: ["Prompt de Comando"]
draft: false
image: "img.png"
categories: ["TI・Tecnologia"]
---
## Exclusão Rápida em Lote de Pastas Grandes
Ao excluir pastas grandes com o Explorer, a velocidade é lenta porque o conteúdo da pasta é verificado primeiro antes da execução da exclusão.
Ao excluir com comandos como abaixo, a verificação e a exclusão são executadas ao mesmo tempo, permitindo a exclusão rápida de pastas grandes.

1. No Prompt de Comando, navegue até a hierarquia da pasta de destino.
2. Execute `DEL /F /Q /S NomeDaPasta > NUL`.
3. Execute `RMDIR /Q /S NomeDaPasta`.
