---



title: "Cómo configurar Twitter Card en PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["Administración del blog"]
---



# Introducción
El tema PaperMod soporta Twitter Cards.
Sin embargo, la configuración de Twitter Card debe escribirse en `config.toml` o en la información de cabecera de los archivos `*.md` de cada artículo.
Si se configura tanto en cada artículo como en `config.toml`, la información de cabecera de cada artículo tendrá prioridad.

# Método de configuración
## config.toml
En `config.toml`, agrega un elemento llamado `images` bajo `[params]`.
En `images`, escribe la ruta de la imagen que se mostrará en la Twitter Card.
Si colocas la imagen en la carpeta `static`, solo necesitas especificar el nombre del archivo.

```
[params]
  images = ["twitter_card.jpg"]
```

Estructura de carpetas
```
root
│  config.toml (Escribir aquí)
├─content
│  └─posts
│      └─carpeta del artículo
│         │  index.md (Escribir aquí)
│         └─images
│             cover.png (Colocar aquí)
└─static
    twitter_card.jpg (Colocar aquí)
```

## Información de cabecera de cada artículo
En la información de cabecera de cada artículo, agrega un elemento llamado `image` bajo `cover`.
Si configuras `relative` como `true`, puedes especificarlo con una ruta relativa desde el archivo `*.md` del artículo.

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### Si no deseas que se muestre en la parte superior del artículo
Si no deseas mostrar la imagen de portada en la parte superior del artículo, agrega un elemento llamado `hidden` bajo `cover` y configúralo como `true`.
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# Sobre el tamaño de la imagen

En la especificación actual de PaperMod, parece que el tamaño de Twitter Card solo soporta `summary_large_image`.
El tamaño adecuado (resolución) para `summary_large_image` tiene varias opiniones, pero parece que alrededor de `800 x 418` (proporción de imagen 1.91:1) es una buena opción.

[Sitio de referencia 1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[Sitio de referencia 2](https://developers.facebook.com/docs/sharing/best-practices)


Si es posible, se recomienda redimensionar la imagen antes de publicarla.

# Método de confirmación de la configuración
Para confirmar la configuración de Twitter Card, utiliza el [Twitter Card Validator](https://cards-dev.twitter.com/validator).
Sin embargo, en mi entorno la vista previa no se mostraba correctamente, por lo que si no se muestra la vista previa, se recomienda verificarlo una vez antes de publicar usando una cuenta privada, etc.
