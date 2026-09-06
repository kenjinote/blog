---





title: "'Cómo instalar el editor de texto CLI nano en Windows'"
date: 2024-03-31T18:09:32+09:00
tags: ["nano", "editor de texto"]
draft: false
image: "img_1.png"
categories: ["Herramientas/Entorno de desarrollo"]
---






## Descargar nano.exe
https://sourceforge.net/projects/nano-for-windows/

Abre el enlace de arriba, haz clic en `Download` y descarga `GNU-Nano_Win32(static).zip`.
Descomprime el archivo zip y coloca `nano.exe` en la carpeta que desees.
* La entrada en japonés no es compatible. (A partir del 31/03/2024)

## Configurar variables de entorno
Para usar `nano.exe` desde el símbolo del sistema, necesitas configurar las variables de entorno.

1. Presiona la `tecla Win` + `tecla R`, escribe `sysdm.cpl` y presiona la `tecla Enter`.
2. Haz clic en `Propiedades del sistema` en `Propiedades del sistema`.
3. Haz clic en `Variables de entorno`.
4. Selecciona `Path` en `Variables del sistema` y haz clic en `Editar`.
5. Haz clic en `Nuevo` y agrega la ruta de `nano.exe`.
6. Haz clic en `Aceptar` para cerrar todos los cuadros de diálogo.
7. Reinicia el símbolo del sistema y verifica si puedes ejecutarlo escribiendo `nano`.

## Cómo usar nano

Cuando escribes `nano` y lo ejecutas, se muestra la siguiente pantalla.

![img_2.png](img_2.png)

Una descripción de los accesos directos se muestra en la parte inferior de la pantalla.

El significado de los símbolos es el siguiente:

- `^` representa la tecla `Ctrl`.
- `M-` representa la tecla `Alt`.

Para guardar y cerrar, presiona `Ctrl` + `S` y luego `Ctrl` + `X`.

## Referencias
- [GNU nano](https://www.nano-editor.org/)
