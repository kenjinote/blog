---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25







title: '¡Inicia el Hidemaru Editor con solo el comando ''hide''! Práctica configuración en Windows'
slug: "Comando「hide」でHidemaru Editorを立ち上げる方法"
tags: ["Comandos", "Editor Hidemaru", "Registro"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "Registra un nombre en App Paths e inicia Hidemaru Editor desde Ejecutar o con start hide en Windows 10/11."
---








## Te mostraré cómo iniciar el editor Hidemaru con el comando `hide`.

Nota: Se ha comprobado que este método funciona en `Windows 10/11`.

1. Abre el Editor del Registro.
2. Ve a `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Crea una clave llamada `hide.exe` en `App Paths`. *El nombre antes de `.exe` en el nombre de esta clave será el nombre del comando.
4. Establece la ruta al archivo ejecutable del editor Hidemaru en el valor `(Predeterminado)` de la clave `hide.exe`. En mi entorno era `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. El valor Path es opcional. Omítelo salvo que la aplicación necesite directorios DLL adicionales; ShellExecuteEx los agrega al PATH del proceso.
6. Escribe hide en Ejecutar (Win + R). En el Símbolo del sistema usa start hide; no basta con escribir hide allí.

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
Si guardas el contenido anterior en un archivo `.reg` y lo ejecutas, la configuración se agregará al registro.

Este .reg registra la aplicación para el usuario actual. Sustituye la ruta por la del ejecutable real. Para todos los usuarios, cambia HKEY_CURRENT_USER por HKEY_LOCAL_MACHINE e importa como administrador.


## Referencias

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)
