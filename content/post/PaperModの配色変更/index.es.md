---
title: "Personalizar los colores de Hugo PaperMod con variables CSS"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Sobrescribe las variables de color de PaperMod para los temas claro y oscuro mediante CSS extendido y comprueba el contraste."
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Los colores de PaperMod se pueden personalizar con propiedades personalizadas de CSS (variables). Guarda las modificaciones en `assets/css/extended/` de tu sitio en vez de editar los archivos del tema, para conservarlas mejor al actualizarlo. El ejemplo define una paleta cálida clara y otra oscura; adapta los valores a tu sitio.

## Modo oscuro y variables actuales

La versión actual de PaperMod cambia al modo oscuro estableciendo `data-theme="dark"` en el elemento `html`. Algunos ejemplos antiguos que solo seleccionan `.dark` pueden no coincidir con este selector. Además, `--hljs-bg` ya no es la variable actual para el fondo de los bloques de código; ahora se llama `--code-block-bg`.

```css
/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme="dark"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
```

## Contraste del texto

En este ejemplo, los colores de texto normal `--primary` y `--content` contrastan claramente con sus fondos. El contraste de muestra de `--primary` frente a `--theme` es aproximadamente 10,4:1 en el modo claro y 13,4:1 en el oscuro. WCAG 2.2 AA requiere 4,5:1 para texto normal; comprueba por separado colores de sintaxis, enlaces, bordes y otros estados.

## Añadir y comprobar CSS extendido

Guarda la hoja de estilos como `assets/css/extended/theme-colors.css` en la raíz del sitio. Las FAQ de PaperMod indican que los CSS de `assets/css/extended/` se agrupan con los estilos del tema. Ejecuta Hugo y revisa el cambio claro/oscuro, las tarjetas, el texto, el código en línea, los bloques de código y los enlaces.

## Alcance

Esta paleta es un ejemplo; no garantiza la conformidad de accesibilidad para todos los textos, imágenes y controles. Los colores del resaltado de sintaxis se definen aparte de `--code-block-bg`; vuelve a comprobar la legibilidad del código después de cambiar el fondo del bloque.

## Referencias

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
