---
date: 2022-09-11T22:59:52+09:00
lastmod: 2026-11-23
title: 'Shortcodes integrados de Hugo: inserciones, versiones y privacidad'
slug: "HUGOで使えるCortoコード"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Conoce los shortcodes integrados de Hugo, sus diferencias entre versiones y las opciones de privacidad para contenido multimedia.'
---

# Shortcodes integrados de Hugo: inserciones, versiones y privacidad

Los shortcodes llaman funciones de plantilla desde el contenido Markdown. Hugo incluye algunos; los temas y módulos pueden añadir otros, y cada proyecto puede definir los suyos. Los nombres y argumentos cambian según la versión de Hugo: consulta la documentación oficial de la versión que utilizas.

## Shortcodes integrados de Hugo

Flickr no es un shortcode integrado en el núcleo de Hugo. Si una llamada `flickr` funciona en un proyecto, la proporciona su tema, módulo o una plantilla propia como `layouts/_shortcodes/flickr.html`. No supongas que está integrado solo porque tenga ese nombre.

La lista oficial actual incluye, entre otros, `details`, `figure`, `highlight`, `instagram`, `param`, `qr`, `ref`, `relref`, `vimeo`, `x` y `youtube`. Consulta la página oficial para ver la lista completa y sus argumentos.

## Ejemplos multimedia

### YouTube

Indica el ID que aparece en el parámetro `v` de la URL del video.

`{{</* youtube 0RKpf3rK57I */>}}`

### X (Hugo 0.141.0 y posteriores)

Indica el nombre de usuario y el ID de la publicación que aparecen en su URL.

`{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Twitter anterior (Hugo 0.139.0)

Hugo 0.139.0 utiliza estos argumentos con nombre.

`{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Instagram

La parte final de la URL de una publicación de Instagram es su ID.

`{{</* instagram CxOWiQNP2MO */>}}`

### Vimeo

Usa el ID numérico al final de la URL del video de Vimeo.

`{{</* vimeo 19899678 */>}}`

## Ten en cuenta la versión

La compilación de este blog está fijada en Hugo 0.139.0. En esa versión, el nombre integrado para X (antes Twitter) es `twitter` y requiere los argumentos con nombre `user` e `id`. El shortcode `x` se incorporó en Hugo 0.141.0; en una versión posterior se marcó `twitter` como obsoleto. Comprueba tu versión antes de copiar ejemplos de documentación reciente.

## Configuración de privacidad

Las inserciones de YouTube, X, Instagram y Vimeo pueden conectar el navegador del visitante con esos servicios. La configuración `privacy` de Hugo permite desactivarlas o usar modos simplificados cuando están disponibles. `privacyEnhanced` de YouTube limita el almacenamiento de información hasta que el visitante reproduce el vídeo.

Modo de privacidad mejorada de YouTube:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

Modo simple de X:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

Twitter anterior (Hugo 0.139.0):

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

Consulta la documentación oficial de la versión de Hugo que utilizas para confirmar los nombres de los ajustes.

El modo simple de Instagram sigue cargando la imagen directamente desde sus servidores. El modo simple de Vimeo obtiene una miniatura y abre Vimeo en una pestaña nueva al hacer clic. Estos modos no eliminan todas las solicitudes a terceros.

Antes de publicar una inserción, comprueba las solicitudes al proveedor, el uso de cookies y los requisitos de privacidad aplicables a tus lectores.

## Mostrar la sintaxis como texto

Para mostrar literalmente la sintaxis de un shortcode en un artículo, escapa los delimitadores añadiendo `/*` y `*/`, como en el ejemplo.

`{{</*/* youtube 0RKpf3rK57I */*/>}}`

## Documentación oficial

- [Introducción a los shortcodes](https://gohugo.io/content-management/shortcodes/)
- [Shortcodes integrados](https://gohugo.io/shortcodes/)
- [YouTube](https://gohugo.io/shortcodes/youtube/)
- [X](https://gohugo.io/shortcodes/x/)
- [Instagram](https://gohugo.io/shortcodes/instagram/)
- [Vimeo](https://gohugo.io/shortcodes/vimeo/)
- [Configuración de privacidad](https://gohugo.io/configuration/privacy/)
