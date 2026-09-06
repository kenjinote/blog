---





title: "Cómo instalar el editor de texto micro en Windows"
date: 2024-03-31T21:50:39+09:00
tags: ["micro", "editor de texto"]
draft: false
image: "img.png"
categories: ["Herramientas y Entorno de Desarrollo"]
---






## Descargar micro
https://github.com/zyedidia/micro/releases

Abra el enlace anterior, haga clic en `Show all XX assets` (donde la parte X es un número) y descargue `micro-X.X.XX-win64.zip` (donde la parte X es un número).
Extraiga el archivo zip y coloque los archivos en cualquier carpeta que desee.

## Configurar variables de entorno
Para usar `micro.exe` desde el símbolo del sistema, es necesario configurar las variables de entorno.

1. Presione la `Tecla Win` + `Tecla R`, escriba `sysdm.cpl` y presione la `Tecla Enter`.
2. Haga clic en `Configuración avanzada del sistema` en `Propiedades del sistema`.
3. Haga clic en `Variables de entorno`.
4. Seleccione `Path` en `Variables del sistema` y haga clic en `Editar`.
5. Haga clic en `Nuevo` y agregue la ruta de la carpeta que contiene `micro.exe`.
6. Haga clic en `Aceptar` para cerrar todos los cuadros de diálogo.
7. Reinicie el símbolo del sistema y verifique si puede ejecutarlo escribiendo `nano`.

## Cómo usar micro

Al escribir `micro` en el símbolo del sistema y ejecutarlo, se mostrará la siguiente pantalla.
![img_3.png](img_3.png)

A continuación se muestran las operaciones principales y los atajos de teclado.

| Atajo de teclado | Operación | 
|--------|-----| 
| Ctrl+Q | Cerrar archivo | 
| Ctrl+S | Guardar archivo | 
| Ctrl+O | Abrir archivo | 
| Ctrl+A | Seleccionar todo | 
| Ctrl+X | Cortar selección | 
| Ctrl+C | Copiar selección | 
| Ctrl+V | Pegar | 
| Ctrl+Z | Deshacer | 
| Ctrl+Y | Rehacer | 
| Ctrl+E | Ejecutar comando del editor | 

## Referencias
- [micro](https://micro-editor.github.io/)
