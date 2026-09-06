---




title: "【HUGO】Vista previa en entorno local"
slug: "【HUGO】ローカルで環境で表示プレビュー"
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["Gestión de blogs"]
---




# Instalación de HUGO

## Descargar
[Descarga de HUGO](https://github.com/gohugoio/hugo/releases)

Descarga el módulo de Windows que se adapte a tu entorno desde el sitio anterior y extráelo.
En mi caso, descargué "hugo_0.102.3_Windows-64bit.zip".

## Extraer
Extrae el archivo zip descargado y copia el archivo hugo.exe que contiene en una carpeta, por ejemplo, C:\bin.

## Registrar en variables de entorno
Regístralo en las variables de entorno para poder ejecutar hugo.exe desde cualquier lugar.
La operación es para Windows 11, pero creo que puedes registrarlo siguiendo estos pasos.

1. Presiona las teclas Win+Pause para abrir la información de la versión
2. Haz clic en Configuración avanzada del sistema
3. Haz clic en Variables de entorno
4. Selecciona Path y haz clic en Editar
5. Haz clic en Nuevo, ingresa "C:\bin" en una nueva línea y cierra el cuadro de diálogo con Aceptar
 
# Previsualizar el blog
Ve a la carpeta del blog de HUGO en el símbolo del sistema y ejecuta el siguiente comando.

`hugo server -D`

El resultado de la ejecución es el siguiente. (La opción -D muestra los artículos en borrador).

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
Pages            | 39
Paginator pages  |  0
Non-page files   |  7
Static files     |  0
Processed images |  0
Aliases          | 13
Sitemaps         |  1
Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

La dirección se muestra al ejecutar el comando (en el ejemplo anterior `http://localhost:1313/`), cópiala en el navegador.
La vista previa se actualiza automáticamente cada vez que se guarda el archivo.
Para finalizar la vista previa, presiona Ctrl+C en el símbolo del sistema.
