---







title: "Cómo iniciar el editor Hidemaru con el comando ''hide''"
slug: "コマンド「hide」で秀丸エディタを立ち上げる方法"
date: 2024-03-29T23:45:37+09:00
tags: ["Comandos", "Editor Hidemaru", "Registro"]
draft: false
image: "img_2.png"
categories: ["Herramientas y Entornos de Desarrollo"]
---








## Te mostraré cómo iniciar el editor Hidemaru con el comando `hide`.

Nota: Se ha comprobado que este método funciona en `Windows 10/11`.

1. Abre el Editor del Registro.
2. Ve a `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Crea una clave llamada `hide.exe` en `App Paths`. *El nombre antes de `.exe` en el nombre de esta clave será el nombre del comando.
4. Establece la ruta al archivo ejecutable del editor Hidemaru en el valor `(Predeterminado)` de la clave `hide.exe`. En mi entorno era `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. Crea un valor de cadena llamado `Path` en la clave `hide.exe`.
6. Establece la ruta a la carpeta donde se encuentra el archivo ejecutable del editor Hidemaru en la información del valor de `Path`. En mi entorno era `"C:\Program Files (x86)\Hidemaru"`.
7. Ahora podrás iniciar el editor Hidemaru con el comando `hide` en el cuadro de diálogo *Ejecutar* (que se muestra presionando la tecla `Win` + `R`). Además, en el símbolo del sistema puedes iniciar el editor Hidemaru con el comando `start hide`.

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="\"C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe\""
"Path"="\"C:\\Program Files (x86)\\Hidemaru\\\""
```
Si guardas el contenido anterior en un archivo `.reg` y lo ejecutas, la configuración se agregará al registro.

![img_1.png](img_1.png)
