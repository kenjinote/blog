---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23


title: 'Cómo usar reveal.js: Creación de presentaciones en HTML y Markdown'
slug: "HTMLでPresentación資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "Presentación"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Explicamos la instalación y el uso básico de "reveal.js", una herramienta que te permite crear presentaciones de forma intuitiva usando HTML y Markdown. Compatible con animaciones y exportación a PDF, te mostraremos cómo aprovecharla en sintonía con sistemas de control de versiones como Git.'
---



# Cómo crear presentaciones con HTML

reveal.js es una herramienta para crear presentaciones utilizando HTML y Markdown, que incluye las siguientes características:

- Variadas funciones de presentación, como fórmulas matemáticas, animaciones y operaciones de deslizamiento (swipe).
- Permite personalizar temas y diseños.
- Funciones de navegación compatibles con múltiples dispositivos, como ratones, teclados y paneles táctiles (touchpads).
- Ofrece funciones avanzadas, como reproducción automática de diapositivas e incrustación de vídeos.
- Permite exportar en formato PDF.

Gracias a estas funciones, los usuarios pueden crear fácilmente presentaciones interactivas y atractivas.

# Instalación y uso de reveal.js

La forma más sencilla de utilizarlo es descargar el archivo ZIP completo desde la siguiente página y descomprimirlo.

1. Abre [https://revealjs.com/installation](https://revealjs.com/installation) y descarga el `master.zip` desde el enlace.
2. Abre el archivo index.html de la carpeta descomprimida en un navegador.
3. Edita el archivo index.html para crear tu propia presentación.

* Como referencia, en demo.html encontrarás código HTML de demostración.

# Casos de uso

Las presentaciones creadas pueden publicarse directamente como páginas web o exportarse como PDF.
Además, dado que el código fuente de la presentación es texto, resulta fácil gestionarlo mediante sistemas de control de versiones.

Al parecer, también es posible crear presentaciones en formato Markdown.

# Crear diapositivas básicas

Basic Setup es la opción más sencilla: descomprime el ZIP más reciente y edita su `index.html`. Como en el ejemplo HTML siguiente, cada diapositiva se coloca dentro de un `<section>`. El archivo de ejemplo ya incluye los estilos y el código de inicialización.

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# Escribir diapositivas en Markdown

El complemento Markdown incluido permite escribir Markdown dentro del archivo HTML. Separa las diapositivas horizontales con `---`. Añade el ejemplo siguiente a `index.html`. Cargar Markdown desde un archivo externo requiere un servidor web local.

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# Configuración de desarrollo

Para tener un servidor local o herramientas para desarrollar el código fuente, usa el Full Setup oficial. Ejecuta estos comandos y abre `http://localhost:8000` en el navegador.

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# Exportar a PDF

Añade `?print-pdf` al final de la URL. En Chrome o Chromium, elige Guardar como PDF, orientación horizontal, sin márgenes y activa los gráficos de fondo. La guía oficial confirma Chrome y Chromium.

# Notas del presentador

Pulsa `S` para abrir la vista del presentador en otra ventana. Añade notas dentro de `<aside class="notes">` en una diapositiva. La vista local necesita un servidor web.

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# Documentación oficial

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

スライドに使う画像・動画の利用条件を確認し、公開資料に機密情報や非公開の発表者ノートが含まれていないか確認してください。
