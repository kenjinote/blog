---



title: "Cómo cerrar y reiniciar el Explorador de archivos"
date: 2024-03-30T15:40:24+09:00
tags: ["Explorador de archivos"]
draft: false
image: "img_2.png"
categories: ["TI y Tecnología"]
---




## Cómo cerrar desde el clic derecho en la barra de tareas

Este es el método para Windows 10. Parece que el menú no se muestra en Windows 11.
Mantenga presionado `Shift` y `Ctrl` mientras hace clic derecho en la barra de tareas, y `Cerrar el Explorador` aparecerá en el menú.

![img.png](img.png)

## Cómo cerrar desde el Administrador de tareas

1. Presione `Ctrl` + `Shift` + `Esc` para abrir el Administrador de tareas.
2. Seleccione `Detalles`.

![img_3.png](img_3.png)

3. Seleccione `explorer.exe`, presione la tecla `Suprimir` (Delete) y, cuando se le pregunte `¿Desea finalizar explorer.exe?`, seleccione `Finalizar proceso`.

![img_1.png](img_1.png)

## Cómo cerrar desde el Símbolo del sistema

1. Presione `Win` + `R`, escriba `cmd` y presione `Enter`.
2. Escriba `taskkill /f /im explorer.exe` y presione `Enter`.

## Cómo iniciar el Explorador desde el Administrador de tareas

1. Presione `Ctrl` + `Shift` + `Esc` para abrir el Administrador de tareas.
2. En el menú Archivo, seleccione `Ejecutar nueva tarea`.
3. Escriba `explorer.exe` y presione `Enter`.
