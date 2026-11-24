---
title: 'Cómo agregar el grep de Hidemaru Editor al menú contextual de Windows'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "ExploradorのMenú contextualにHidemaru Editorgrepを追加する"
tags: ["Editor Hidemaru", "Explorador", "Menú contextual", "grep", "Registro"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Presentamos un procedimiento de configuración útil para agregar la función grep de Hidemaru Editor al menú contextual (clic derecho) del Explorador en Windows 10/11. Explicamos un método sencillo utilizando un archivo de registro.'
---
Aquí se explica cómo añadir el grep del editor Hidemaru al menú contextual del Explorador en Windows 10/11.

**※ El siguiente procedimiento modifica el registro, por lo que debe hacerse bajo su propia responsabilidad.**

Este archivo añade comandos de carpeta solo para el usuario actual; no agrega «Abrir con Hidemaru» a todos los archivos ni cambia todo el equipo. Antes de importarlo, ábrelo en el Bloc de notas y comprueba o corrige la ruta del ejecutable. Si las claves ya existen, expórtalas desde el Editor del Registro (Archivo > Exportar). En Windows 11, los comandos heredados pueden estar en «Mostrar más opciones». El soporte de Windows 10 terminó el 14 de octubre de 2025. El archivo de eliminación incluido solo borra estas entradas del usuario actual; no revierte el registro anterior de todo el equipo. Si importaste el archivo antiguo, revisa y elimina sus claves por separado en el Editor del Registro.
## Procedimiento

1. Abra el siguiente enlace y guárdelo en cualquier carpeta.

[秀丸レジストリ登録.reg](秀丸レジストリ登録.reg)

[Quitar las entradas de Hidemaru del registro](秀丸レジストリ解除.reg)

2. Haga doble clic en el archivo `秀丸レジストリ登録.reg` para añadirlo al registro.

## Referencias

- [Ejecutar grep de Hidemaru desde el menú contextual de una carpeta](https://aimek-developer.blogspot.com/2019/02/grep.html)

## Referencias oficiales

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
