---
title: "Cómo configurar Twitter Cards (X Cards) en Hugo PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Configura imágenes de tarjetas X con los ajustes documentados de PaperMod y revisa el HTML generado y la vista previa en el editor de publicaciones de X."
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod puede generar metadatos Open Graph y Twitter Card. El resultado depende de la versión del tema y de las plantillas personalizadas; comprueba el HTML publicado en vez de asumir que un ejemplo garantiza una tarjeta concreta.

## Configuración global

Los metadatos SEO de PaperMod se activan en las compilaciones de producción. Configura el entorno del sitio como production.

```toml
[params]
  env = "production"
```

Para una imagen alternativa de todo el sitio, coloca un archivo en `static` y configúralo aquí. Se utiliza como opción cuando una entrada no proporciona una imagen propia. Comprueba la URL resultante en el sitio publicado.

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## Imagen por entrada

Para asignar una imagen a una entrada, define `cover.image` con una imagen del Page Bundle. `relative: true` indica que se resuelva una ruta relativa al bundle. PaperMod documenta la portada como imagen preferida; si no existe, puede usar la lista `images` de la página y después imágenes del bundle que cumplan los criterios.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## Ocultar la portada en el artículo

Según la referencia de variables de PaperMod, `cover.hidden: true` oculta la portada en la vista del artículo pero la conserva en los metadatos estructurados. Puede servir si la imagen se reserva para redes sociales. Verifica el HTML cuando uses una bifurcación del tema o plantillas propias.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## Tipo de tarjeta y dimensiones

No conviene generalizar las antiguas afirmaciones de que PaperMod solo admite `summary_large_image` y de que 800×418 sea un tamaño fijo. El tipo depende de la versión del tema o de las plantillas del sitio. Para una imagen horizontal, 1200×630 (aprox. 1,90:1) es una referencia práctica de diseño, no una garantía de requisitos de X.

## Comprobar el resultado y la vista previa

Genera el sitio en modo producción e inspecciona el HTML del artículo: `twitter:card`, `twitter:image`, `og:image`, título y descripción. Confirma que la imagen se sirve directamente por HTTPS y es pública, sin inicio de sesión. En 2022, X eliminó la vista previa del Card Validator y recomendó el editor de publicaciones. Pega allí el enlace y revisa la vista previa sin publicar. La caché puede tardar en actualizarse.

Revisado el 24-11-2026 con las referencias enlazadas de PaperMod y el foro de desarrolladores de X. Las bifurcaciones, plantillas personalizadas y cambios de X pueden modificar el resultado.

## Referencias

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)
