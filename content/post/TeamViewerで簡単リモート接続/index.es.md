---
title: '【Para principiantes】Cómo realizar una conexión de escritorio remoto fácilmente con TeamViewer'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単Conexión remota"
tags: ["TeamViewer", "comando", "conexión remota"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Explicamos cómo realizar fácilmente una conexión de escritorio remoto usando TeamViewer. También presentamos pequeños trucos útiles como especificar el ID y la contraseña desde la línea de comandos, y automatizar/omitir la conexión mediante accesos directos.'
---
## Conexión por línea de comandos en Windows

La documentación oficial de TeamViewer para Windows indica que la versión completa puede iniciarse desde el Símbolo del sistema, un script o un acceso directo.

Este ejemplo inicia `TeamViewer.exe` desde su carpeta de instalación. Escribe el ID del equipo asociado en `<ID>` y la contraseña en `<Password>`. Si TeamViewer está instalado en otra ubicación, sustituye la ruta del ejecutable.

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

Si omites `-p`, TeamViewer usa Easy Access cuando está disponible; de lo contrario, solicita la contraseña.

Un acceso directo que incluye una contraseña la guarda en un formato legible. No lo compartas ni lo guardes donde otras personas puedan leerlo. Para el acceso desatendido recurrente, considera asignar el dispositivo a tu cuenta y usar Easy Access, una lista de permitidos y autenticación multifactor en lugar de guardar una contraseña.

## Referencias oficiales

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)
