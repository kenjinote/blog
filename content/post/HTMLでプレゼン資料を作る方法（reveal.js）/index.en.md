---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23
title: 'How to Use reveal.js: Creating Presentation Materials with HTML and Markdown'
slug: "HTMLでPresentation資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "Presentation"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'We explain the installation and basic usage of ''reveal.js'', a tool that allows you to intuitively create presentations using HTML and Markdown. We introduce ways to utilize it that support animations and PDF output, and have excellent compatibility with version control like Git.'
---

# How to make a presentation with HTML

reveal.js is a presentation creation tool using HTML and Markdown, with the following features:

- A variety of presentation features such as mathematical formulas, animations, and swipe operations
- Customizable themes and layouts
- Navigation features compatible with multiple devices such as mice, keyboards, and touchpads
- Advanced features such as automatic slide playback and video embedding
- Can be exported in PDF format

With these features, users can easily create interactive and engaging presentations.

# How to install and use reveal.js

The easiest way to use it is to download the entire ZIP from the following page and extract it.

1. Open [https://revealjs.com/installation](https://revealjs.com/installation) and download `master.zip` from the link
2. Open index.html in the extracted folder in a browser
3. Rewrite index.html to create your own presentation

* You can use demo.html as a reference since it contains HTML code for a demo.

# Use Cases

The presentations you create can be published as web pages as is, or exported as PDFs.
Also, since the source of the presentation is text, it is easy to manage it with a version control system.

It seems you can also create presentations in Markdown format.

# Create basic slides

Basic Setup is the easiest option: unzip the latest archive and edit its `index.html`. Wrap each slide in a `<section>` as in the HTML example below. The supplied Basic Setup file already includes the styles and initialization code.

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# Write slides in Markdown

The bundled Markdown plugin lets you write Markdown inside the HTML file. Separate horizontal slides with `---`. Add the example below to `index.html`. Loading Markdown from an external file requires a local web server.

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# Development setup

For a local server or source-development tools, use the official Full Setup. Run these commands, then open `http://localhost:8000` in a browser.

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# Export to PDF

Append `?print-pdf` to the URL. In Chrome or Chromium, choose Save as PDF, landscape, no margins, and enable background graphics. The official guide confirms Chrome and Chromium.

# Speaker notes

Press `S` to open speaker view in a separate window. Add notes inside `<aside class="notes">` on a slide. A local web server is required for local speaker view.

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# Official documentation

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

Check the usage rights for images and videos in your slides, and make sure public materials do not contain confidential information or private speaker notes.
