---
title: 'How to Set Up Twitter Cards (X Cards) in Hugo PaperMod'
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["Blog Management"]
description: 'Explains how to set up Twitter Cards in Hugo''s PaperMod theme. Introduces how to write in config.toml to apply it to the entire site, and how to specify images individually in the Markdown header of each article. These are setup steps useful for displaying eye-catching images when sharing on SNS.'
---
# Introduction
The PaperMod theme supports Twitter Cards.
However, Twitter Card settings need to be described in `config.toml` or the header information of each article's `*.md`.
If set in both each article and `config.toml`, the header information of each article takes precedence.

# How to Configure
## config.toml
In `config.toml`, add an item named `images` under `[params]`.
In `images`, describe the path to the image to be displayed on the Twitter Card.
If placing the image in the `static` folder, specifying just the file name is sufficient.

```
[params]
  images = ["twitter_card.webp"]
```

Folder structure
```
root
│  config.toml (Describe here)
├─content
│  └─posts
│      └─article folder
│         │  index.md (Describe here)
│         └─images
│             cover.webp (Place here)
└─static
    twitter_card.webp (Place here)
```

## Header Information of Each Article
In the header information of each article, add an item named `image` under `cover`.
If you set `relative` to `true`, you can specify it as a relative path from the article's `*.md`.

```
cover:
  image: "images/cover.webp"
  relative: true
```

### If You Do Not Want to Display It at the Top of the Article
If you do not want to display a cover image at the top of the article, add an item named `hidden` under `cover` and set it to `true`.
```
cover:
  image: "images/cover.webp"
  relative: true
  hidden: true
```

# About Image Size

Based on the current specifications of PaperMod, it seems that Twitter Card sizes are only supported for `summary_large_image`.
The appropriate size (resolution) for `summary_large_image` varies according to different sources, but around `800 x 418` (aspect ratio 1.91:1) seems good.

[Reference Site 1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[Reference Site 2](https://developers.facebook.com/docs/sharing/best-practices)


If possible, it is recommended to resize the image before posting.

# How to Check Settings
To check Twitter Card settings, use the [Twitter Card Validator](https://cards-dev.twitter.com/validator).
However, in my environment, the preview did not display properly, so if the preview does not appear, it is recommended to check once using a private account or similar before posting.
