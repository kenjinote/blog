---
title: "Abrir el menú contextual clásico en Windows 11"
slug: "Windows 11のMenú contextualを従来版に戻す方法"
tags: ["Windows11", "Explorador de archivos"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Cómo abrir el menú contextual clásico con Mostrar más opciones en Windows 11 y una alternativa del Registro que puede no funcionar en todas las versiones."
date: "2024-03-30T13:13:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Abrir el menú contextual clásico en Windows 11

En Windows 11, haz clic con el botón derecho en un elemento y selecciona Mostrar más opciones para abrir el menú contextual clásico. También puedes seleccionar un elemento y pulsar `Mayús`+`F10`, o mantener pulsada `Mayús` mientras haces clic con el botón derecho para abrir Mostrar más opciones. Prueba primero estas opciones integradas.

> El cambio del Registro que se describe a continuación es una solución no oficial para mostrar el menú clásico de forma predeterminada. Microsoft no lo admite como procedimiento oficial y puede no funcionar en algunas versiones de Windows. Haz una copia de seguridad del Registro antes de editarlo.

## Pasos de la alternativa mediante el Registro

1. Abre el Editor del Registro.

Presiona la tecla `Win` + `R`, escribe `regedit` y presiona la tecla `Enter`.
![img_1.png](img_1.webp)　

2. Navega a `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Si esta clave no existe, créala.


3. Navega a `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Si esta clave no existe, créala.
4. Asegúrate de que el valor `(Predeterminado)` de `InprocServer32` esté vacío.

![img_2.png](img_2.webp)

5. Reinicia tu computadora.
6. Comprueba que el menú contextual ha vuelto a la versión clásica.

Para deshacer el cambio, elimina la clave `{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}` que creaste y reinicia el Explorador de archivos. Haz una copia de seguridad de cualquier configuración existente antes de modificarla.

## Referencias

- [Soporte técnico de Microsoft: Explorador de archivos en Windows](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Soporte técnico de Microsoft: Métodos abreviados de teclado de Windows](https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows)
