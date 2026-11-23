---
date: 2022-09-11T22:59:52+09:00
lastmod: 2026-11-23
title: 'Hugo Built-in Shortcodes: Embeds, Versions, and Privacy'
slug: "HUGOで使えるShortコード"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Learn which shortcodes Hugo includes, how they vary by version, and how to configure media embeds with privacy in mind.'
---

# Hugo Built-in Shortcodes: Embeds, Versions, and Privacy

Shortcodes call template features from Markdown content. Hugo provides embedded shortcodes; themes and modules may add others, and projects can define their own. Names and arguments vary by Hugo version, so check the official documentation for the version you run.

## Hugo’s embedded shortcodes

Flickr is not an embedded shortcode in Hugo core. If a `flickr` call works in a project, it is supplied by its theme, module, or a custom template such as `layouts/_shortcodes/flickr.html`. Do not assume a same-named shortcode is built in.

The current official list includes `details`, `figure`, `highlight`, `instagram`, `param`, `qr`, `ref`, `relref`, `vimeo`, `x`, and `youtube`, among others. See the official page for the full list and arguments.

## Media examples

### YouTube

Use the ID in the video URL’s `v` parameter.

`{{</* youtube 0RKpf3rK57I */>}}`

### X (Hugo 0.141.0 and later)

Provide the username and post ID from the post URL.

`{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Legacy Twitter (Hugo 0.139.0)

Hugo 0.139.0 uses the following named arguments.

`{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Instagram

The final part of an Instagram post URL is its post ID.

`{{</* instagram CxOWiQNP2MO */>}}`

### Vimeo

Use the numeric ID at the end of a Vimeo video URL.

`{{</* vimeo 19899678 */>}}`

## Mind the version

This blog’s build is pinned to Hugo 0.139.0. In that version, the built-in name for X (formerly Twitter) is `twitter`, and it requires named `user` and `id` arguments. The `x` shortcode was added in Hugo 0.141.0; `twitter` was deprecated in a later release. Check your project’s Hugo version before copying an example from newer documentation.

## Privacy settings

Embeds for YouTube, X, Instagram, and Vimeo can connect visitors’ browsers to those services. Hugo’s `privacy` configuration can disable embeds or enable simpler modes where available. YouTube’s `privacyEnhanced` setting limits information storage until a visitor plays the video.

YouTube privacy-enhanced mode:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

X simple mode:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

Legacy Twitter (Hugo 0.139.0):

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

Check the official documentation for the Hugo version you use to confirm each setting name.

Instagram’s simple mode still loads the image directly from Instagram’s servers. Vimeo’s simple mode fetches a thumbnail and opens Vimeo in a new tab when clicked. These modes do not eliminate all third-party requests.

Before publishing an embed, check requests to the provider, cookie behavior, and the privacy requirements that apply to your audience.

## Display syntax as text

To display shortcode syntax literally in an article, escape the delimiters by adding `/*` and `*/`, as shown below.

`{{</*/* youtube 0RKpf3rK57I */*/>}}`

## Official documentation

- [Shortcodes overview](https://gohugo.io/content-management/shortcodes/)
- [Embedded shortcodes](https://gohugo.io/shortcodes/)
- [YouTube](https://gohugo.io/shortcodes/youtube/)
- [X](https://gohugo.io/shortcodes/x/)
- [Instagram](https://gohugo.io/shortcodes/instagram/)
- [Vimeo](https://gohugo.io/shortcodes/vimeo/)
- [Privacy configuration](https://gohugo.io/configuration/privacy/)
