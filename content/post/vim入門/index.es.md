---



title: "Introducción a vim"
date: 2024-04-19T22:06:34+09:00
tags: ["vim", "editor de texto"]
draft: false
image: "img.png"
categories: ["Herramientas・Entorno de desarrollo"]
---




![img_1.png](img_1.png)

# Introducción a vim

## Descarga e instalación

[https://www.vim.org/download.php](https://www.vim.org/download.php)

Desde el sitio anterior, descarga e instala el módulo según el SO que desees instalar.

Para Windows, es recomendable elegir `gvim_X.X.X_x64_signed.exe`.

##  Cómo iniciar

Para Windows, es necesario registrar la carpeta que contiene `vim.exe` en la variable de entorno Path.

Cómo iniciar

```
vim
```

Para iniciar especificando un nombre de archivo

```
vim filename.txt
```

## Cómo salir

Para salir, ingresa `:` (dos puntos), luego ingresa `q` y presiona Enter.
```
:q
```

Si has modificado el archivo, aparecerá el mensaje `No se ha guardado el último cambio (añade ! para descartar los cambios)`.
Puedes descartar el contenido y forzar la salida.
```
:q!
```

Para guardar el archivo y salir
```
:wq
```

Lo siguiente también tiene el mismo significado.
```
:x
```

Además, puedes salir presionando `z` dos veces mientras mantienes presionado `Shift`. (Igual que :wq)

## Modos

vim tiene el `modo comando` y el `modo inserción`. Cuando inicias vim, entra en el `modo comando`, y si presionas la tecla `i`, pasará al `modo inserción`.

En el `modo inserción`, como su nombre indica, es posible introducir texto. Para pasar del `modo inserción` al `modo comando`, presiona la tecla `ESC`.

Tener este cambio de modo de inserción es una de las características de vim.

## Movimiento del cursor y desplazamiento

Aquí se resume el movimiento del cursor y el desplazamiento en el `modo comando`.

| Tecla                                | Descripción                      |
|------------------------------------|-------------------------|
| `h` (o `Ctrl`+`H`, `Retroceso`, `←`) | Mover a la izquierda                    |
| `j` (o `Ctrl`+`J`・`N`, `↓`)         | Mover hacia abajo                    |
| `k` (o `Ctrl`+`P`, `↑`)             | Mover hacia arriba                    |
| `l` (o `Espacio`, `→`)               | Mover a la derecha                    |
| `+` (o `Enter`)                   | Mover al principio de la siguiente línea               |
| `-`                                | Mover al principio de la línea anterior               |
| `Ctrl`+`B` (o `RePág`)            | Desplazar hacia arriba               |
| `Ctrl`+`F` (o `AvPág`)          | Desplazar hacia abajo               |
| `Ctrl`+`U`                         | Medio desplazamiento hacia arriba              |
| `Ctrl`+`D`                         | Medio desplazamiento hacia abajo              |
| `Ctrl`+`Y`                         | Desplazar 1 línea hacia arriba             |
| `Ctrl`+`E`                         | Desplazar 1 línea hacia abajo             |
| `z` `Enter`                        | Desplazar la línea del cursor a la parte superior de la pantalla        |
| `z` `.`                            | Desplazar la línea del cursor al centro de la pantalla        |
| `z` `-`                            | Desplazar la línea del cursor a la parte inferior de la pantalla        |
| `0` (o `\|`)                       | Mover el cursor al principio de la línea              |
| `$`                                | Mover el cursor al final de la línea              |
| `^` (o `_`)                        | Mover el cursor al principio de la línea (excluyendo espacios y tabulaciones) |
| `G` (o `:$`)                       | Mover el cursor a la última línea             |
| `:número de línea` `Enter`                     | Mover a la línea especificada                  |

Si introduces un `número` seguido de las teclas de movimiento anteriores, puedes moverte varias veces esa cantidad.
(Por ejemplo, si introduces `3j`, te moverás 3 líneas hacia abajo desde la posición actual del cursor.)

## Otros comandos

| Tecla         | Descripción                   |
|------------|----------------------|
| `Ctrl`+`L` | Redibujar la pantalla               |
| `Ctrl`+`G` | Mostrar el número total de líneas del archivo, posición del cursor, etc. |
