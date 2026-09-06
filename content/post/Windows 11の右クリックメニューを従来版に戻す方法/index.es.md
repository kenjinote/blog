---




title: "Cómo restaurar el menú contextual clásico en Windows 11"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "Explorador de archivos"]
draft: false
image: "img.png"
categories: ["PC y Gadgets"]
---





# Cómo restaurar el menú contextual clásico en Windows 11

Aquí se explica cómo restaurar el menú contextual clásico en Windows 11.

1. Abre el Editor del Registro.

Presiona la tecla `Win` + `R`, escribe `regedit` y presiona la tecla `Enter`.
![img_1.png](img_1.png)　

2. Navega a `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Si esta clave no existe, créala.


4. Navega a `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Si esta clave no existe, créala.
5. Asegúrate de que el valor `(Predeterminado)` de `InprocServer32` esté vacío.

![img_2.png](img_2.png)

6. Reinicia tu computadora.
7. Comprueba que el menú contextual ha vuelto a la versión clásica.
