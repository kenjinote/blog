---



title: 'Cómo crear un acceso directo para apagar Windows'
slug: "Windows をApagarするAtajoを作成する方法"
date: 2023-04-11T17:03:32+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["Windows", "apagar", "acceso directo"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Crea un acceso directo en el escritorio para iniciar el apagado de Windows 10 o Windows 11 con un doble clic.'
---
Estos pasos son para Windows 10 y Windows 11. Los nombres de los menús pueden variar ligeramente según la versión y el idioma.

## Crear el acceso directo

#### 1. Haz clic derecho en un espacio vacío del escritorio y selecciona `Nuevo` > `Acceso directo`.

#### 2. Escribe este comando como ubicación del elemento y haz clic en `Siguiente`.

```text
shutdown.exe /s /t 0
```

#### 3. Pon un nombre al acceso directo, por ejemplo, `Apagar`, y haz clic en `Finalizar`.

## Cambiar el icono (opcional)

Haz clic derecho en el acceso directo y selecciona `Propiedades` > `Cambiar icono`. Elige un icono de `%SystemRoot%\System32\SHELL32.dll` y pulsa `Aceptar`.

Guarda tu trabajo antes de usar el acceso directo. Este inicia el apagado de Windows sin un paso adicional de confirmación. `/s` solicita el apagado y `/t 0` indica que no haya espera. Se omite `/f`, por lo que las aplicaciones pueden cerrarse normalmente y avisar si hay trabajo sin guardar.

[**Microsoft Learn: comando shutdown (en inglés)**](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown/)
