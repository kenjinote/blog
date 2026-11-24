---
title: "Customize Hugo PaperMod Colors with CSS Variables"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Override PaperMod color variables for light and dark themes with extended CSS, then check text contrast."
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod colors can be customized with CSS custom properties (variables). Put overrides in your site's `assets/css/extended/` directory rather than editing theme files, so they are easier to keep across theme updates. The example below defines a warm light palette and a dark palette; adjust the values for your site.

## Dark mode and current variables

Current PaperMod switches dark mode by setting `data-theme="dark"` on the `html` element. Older examples that target only `.dark` may not match this theme selector. `--hljs-bg` is also not the current variable for the code-block background; the current name is `--code-block-bg`.

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

## Text contrast

In this example, the normal text colors `--primary` and `--content` contrast strongly with their backgrounds. The sample contrast for `--primary` against `--theme` is about 10.4:1 in light mode and 13.4:1 in dark mode. WCAG 2.2 AA requires 4.5:1 for normal text, but check syntax colors, links, borders, and other states separately.

## Add and check extended CSS

Save the stylesheet as `assets/css/extended/theme-colors.css` at your site root. PaperMod's FAQ says CSS files in `assets/css/extended/` are bundled with the theme styles. Run Hugo and check the light/dark switch, cards, body text, inline code, code blocks, and links.

## Scope

This is an illustrative palette; it does not guarantee accessibility conformance for every text string, image, or interactive component. Syntax-highlight colors are defined separately from `--code-block-bg`, so recheck code readability after changing the block background.

## References

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
