---




title: "Eliminar carpetas grandes rápidamente"
slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
tags: ["Símbolo del sistema"]
draft: false
image: "img.png"
categories: ["TI y Tecnología"]
---




## Eliminar carpetas grandes rápidamente
Al eliminar carpetas grandes en el Explorador, la velocidad es lenta porque primero se realiza una búsqueda completa del contenido de la carpeta antes de ejecutar la eliminación.
Al eliminar usando comandos como se muestra a continuación, la búsqueda y la eliminación se ejecutan simultáneamente, lo que permite eliminar carpetas grandes rápidamente.

1. Navegue al directorio de la carpeta de destino en el Símbolo del sistema.
2. Ejecute `DEL /F /Q /S nombre_de_la_carpeta > NUL`.
3. Ejecute `RMDIR /Q /S nombre_de_la_carpeta`.
