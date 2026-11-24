---
title: "Resize and Reposition PaperMod Cover Images in Post Lists"
slug: "PaperModのImageの配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Use PaperMod's extended CSS feature and CSS Grid to shrink cover images in post-list cards and place them beside the summary."
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

This example makes cover images in PaperMod post-list cards smaller and places each image below its title, beside the summary. It uses site-level extended CSS instead of editing theme CSS or bundled templates. The selectors target PaperMod classes, so check the result in a browser after a theme update.

## Add extended CSS

Create `assets/css/extended/custom.css` at the site root. PaperMod includes CSS from this directory alongside its theme styles. CSS Grid changes the visual placement while leaving the existing HTML structure intact.

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

## Adjust for narrow screens

Reduce the column width and gap on narrow screens so the summary remains readable. Adjust the 150px width and breakpoint to suit your design. `height: auto` preserves the image ratio. Add `aspect-ratio` and `object-fit: cover` only if you want to crop images to a uniform shape.

## Avoid editing theme files

PaperMod documents `blank.css` as a placeholder used when the extended CSS directory has no files. You do not need to edit the bundled `post-entry.css` or remove the commented `/* width: 100%; */` line; deleting a CSS comment does not change the style. If you need to change the HTML structure itself, you can copy a layout into your site's `layouts/` directory and override it, but you must maintain that copy when the theme changes.

## Check the layout

Run Hugo and inspect the home, tag, and category lists on wide and narrow screens. Make sure the image, title, summary, and metadata do not overlap, and that the theme's full-card link remains usable. If a theme update changes the classes or markup, adjust the CSS. This example affects post-list covers, not images inside article content.

## References

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
