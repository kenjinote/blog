---
title: "Eliminar una carpeta grande desde el símbolo del sistema de Windows: pasos y riesgos"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Símbolo del sistema"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Método documentado por Microsoft para borrar carpetas con DEL y RMDIR, con advertencias sobre el borrado recursivo silencioso, la ruta y las copias de seguridad."
---
Estos comandos eliminan de forma recursiva los archivos y subcarpetas del objetivo. `/Q` omite la confirmación. Un objetivo equivocado puede provocar una pérdida de datos irreversible: haz una copia de seguridad y comprueba la ruta del directorio padre y el nombre de la carpeta antes de ejecutar el borrado. La velocidad depende del número de archivos y del almacenamiento; no se garantiza que sea mayor.

## Pasos

En este ejemplo, `C:\Parent` es el directorio padre y `Large Folder` es la carpeta que se eliminará. Primero muestra el contenido y verifica el objetivo; después, bórralo.

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S` elimina los archivos del objetivo (`/F` incluye archivos de solo lectura, `/Q` omite avisos y `/S` incluye subdirectorios). Después, `RMDIR /S /Q` elimina todo el árbol de directorios sin pedir confirmación. Sustituye `C:\Parent` y `Large Folder` por los valores reales y revisa la salida de `dir` antes de ejecutar cualquier comando de borrado.

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)
