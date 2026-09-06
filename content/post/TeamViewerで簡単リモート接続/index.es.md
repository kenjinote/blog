---



title: "Conexión remota sencilla con TeamViewer"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "comando", "conexión remota"]
draft: false
image: "img.png"
categories: ["IT y Tecnología"]
---




# Conexión remota sencilla con TeamViewer

Con TeamViewer puedes realizar conexiones de escritorio remoto fácilmente.

Inicia TeamViewer tanto en el equipo local como en el remoto,
y en el equipo local ingresa el ID y la contraseña del equipo remoto para establecer la conexión.

Para conectarte remotamente desde la línea de comandos, haz lo siguiente:

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
En `<ID>` ingresa el ID del equipo remoto y en `<Password>` ingresa la contraseña del equipo remoto.

Es útil crear un archivo de acceso directo con el comando anterior, ya que te permite omitir la introducción del ID y la contraseña.

Sitio de referencia: [Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
