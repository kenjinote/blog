---
title: "如何在 Hugo PaperMod 中设置 Twitter Card（X 卡片）"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "按 PaperMod 文档设置 X 卡片图片，并检查生成的 HTML 及 X 发帖编辑器中的预览。"
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod 可以生成 Open Graph 和 Twitter Card 元数据。输出会因主题版本和自定义模板而异，因此应检查已发布的 HTML，而不要认为某个配置示例必然产生特定卡片。

## 全站设置

PaperMod 的 SEO 元数据在 production 构建中启用。请将站点环境设为 production。

```toml
[params]
  env = "production"
```

如需全站默认图片，可将图片放在 `static` 目录并在此配置。当文章没有单独指定图片时，它可能作为候选图片。还应检查部署后实际生成的图片 URL。

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## 为文章单独指定图片

如需为文章单独指定图片，请将 Page Bundle 中的图片设为 `cover.image`。`relative: true` 表示使用相对于 Bundle 的路径。PaperMod 文档优先使用封面图；若没有封面图，则可能使用页面的 `images` 列表，再尝试符合条件的 Bundle 图片。

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## 隐藏文章中的封面

根据 PaperMod 变量文档，`cover.hidden: true` 会在文章页面隐藏封面，但保留结构化元数据中的图片。如果图片只用于社交卡片，这一设置会很有用。使用主题 fork 或自定义模板时，请检查生成的 HTML。

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## 卡片类型与图片尺寸

旧文中“PaperMod 只支持 `summary_large_image`”和“尺寸固定为 800×418”的说法不应一概而论。卡片类型可能取决于主题版本或站点模板。宽图可将 1200×630（约 1.90:1）作为实用设计参考，但这不是 X 保证的显示要求。

## 检查输出和预览

使用 production 设置构建后，在文章 HTML 中检查 `twitter:card`、`twitter:image`、`og:image`、标题和描述。图片 URL 应通过 HTTPS 公开访问，无需登录且直接返回图片。X 于 2022 年移除了 Card Validator 的预览功能，并建议使用发帖编辑器。将链接粘贴到编辑器，在不发布的情况下查看预览。缓存更新可能需要时间。

已于 2026-11-24 对照链接的 PaperMod 文档和 X 开发者论坛核查。主题 fork、自定义模板及 X 的变更都可能影响实际输出。

## 参考资料

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)
