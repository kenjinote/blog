---
title: "How to Set Up Twitter Cards (X Cards) in Hugo PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Configure X card images with PaperMod's documented settings, then check the generated HTML and preview in X's post composer."
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod can generate Open Graph and Twitter Card metadata. Output can vary by theme version and custom layouts, so inspect the published HTML instead of assuming a configuration example guarantees a particular card.

## Site-wide configuration

PaperMod's SEO metadata is enabled for production builds. Set the site environment to production.

```toml
[params]
  env = "production"
```

For a site-wide fallback image, place an image under `static` and set it here. This is a candidate when a post does not provide its own image. Check how the URL is emitted on your deployed site.

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## Post-specific image

For a post-specific image, set `cover.image` to an image in the page bundle. `relative: true` tells PaperMod to resolve a page-bundle-relative path. PaperMod documents the cover image as the preferred card image; without one, it can use the page's `images` list and then qualifying bundle images.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## Hide the cover in the article

`cover.hidden: true` hides the cover in the article display while retaining it for structured metadata, according to PaperMod's variables reference. This can be useful when the image is only for social cards. Verify the generated HTML if you use a theme fork or template overrides.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## Card type and image dimensions

The old claims that PaperMod supports only `summary_large_image` and that 800×418 is a fixed size should not be generalized. Card type can depend on the theme version or site templates. For a wide share image, 1200×630 (about 1.90:1) is a practical design target, not a promise of X display requirements.

## Inspect output and preview

Build with the production setting and inspect the article's HTML source for `twitter:card`, `twitter:image`, `og:image`, title, and description. Confirm the image URL is HTTPS, publicly reachable without login, and serves the image directly. X removed preview functionality from the Card Validator in 2022 and directed developers to the post composer. Paste the URL into X's composer and inspect the preview without publishing. Cached card data may take time to update.

This guide was checked against the linked PaperMod references and X developer forum on 2026-11-24. Forks, template overrides, and changes to X can affect the rendered card.

## References

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)
