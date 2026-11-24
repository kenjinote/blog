---
title: "Cambiar el tamaño y la posición de las portadas en las listas de PaperMod"
slug: "PaperModのImagenの配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Usa el CSS extendido de PaperMod y CSS Grid para reducir las portadas de las tarjetas y colocarlas junto al resumen."
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Este ejemplo reduce las portadas de las tarjetas de las listas de PaperMod y las coloca debajo del título, junto al resumen. Usa CSS extendido del sitio en lugar de editar los estilos o las plantillas incluidas con el tema. Los selectores se basan en clases de PaperMod; comprueba el resultado en el navegador después de actualizar el tema.

## Añadir CSS extendido

Crea `assets/css/extended/custom.css` en la raíz del sitio. PaperMod incorpora los CSS de esta carpeta junto con sus estilos. CSS Grid cambia la disposición visual sin modificar la estructura HTML existente.

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## Ajustar para pantallas estrechas

Reduce el ancho de la columna y el espacio en pantallas estrechas para que el resumen siga siendo legible. Ajusta los 150 px y el punto de interrupción según tu diseño. `height: auto` conserva la proporción de la imagen. Añade `aspect-ratio` y `object-fit: cover` solo si quieres recortarlas con una forma uniforme.

## Evitar editar archivos del tema

PaperMod describe `blank.css` como un archivo de reserva que evita errores cuando la carpeta de CSS extendido está vacía. No hace falta editar el `post-entry.css` del tema ni quitar la línea comentada `/* width: 100%; */`; borrar un comentario CSS no cambia el estilo. Si necesitas cambiar la estructura HTML, puedes copiar una plantilla a `layouts/` en tu sitio y sobrescribirla, pero tendrás que mantener esa copia cuando cambie el tema.

## Comprobar el diseño

Ejecuta Hugo y revisa las listas de inicio, etiquetas y categorías en pantallas anchas y estrechas. Asegúrate de que la imagen, el título, el resumen y los metadatos no se superpongan y de que siga funcionando el enlace que cubre toda la tarjeta. Si una actualización del tema cambia las clases o el HTML, ajusta el CSS. Este ejemplo afecta a las portadas de las listas, no a las imágenes del cuerpo del artículo.

## Referencias

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
