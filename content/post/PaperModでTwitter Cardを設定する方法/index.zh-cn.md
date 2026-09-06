---
title: '如何在PaperMod中设置Twitter Card'
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["博客运营"]
---
# 简介
PaperMod主题支持Twitter Card。
但是，Twitter Card的设置必须写在`config.toml`或每篇文章的`*.md`头部信息中。
如果同时在文章和`config.toml`中进行了设置，则优先使用文章的头部信息。

# 设置方法
## config.toml
在`config.toml`中，在`[params]`下添加一个名为`images`的项目。
在`images`中，填写要在Twitter Card中显示的图像路径。
如果将图像放置在`static`文件夹中，只需指定文件名即可。

```
[params]
  images = ["twitter_card.jpg"]
```

文件夹结构
```
root
│  config.toml (在此编写)
├─content
│  └─posts
│      └─文章文件夹
│         │  index.md (在此编写)
│         └─images
│             cover.png (放置在此)
└─static
    twitter_card.jpg (放置在此)
```

## 各文章的头部信息
在每篇文章的头部信息中，在`cover`下添加一个名为`image`的项目。
如果将`relative`设置为`true`，则可以使用相对于文章`*.md`的相对路径来指定。

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### 如果不想在文章顶部显示
如果不想在文章顶部显示封面图像，可以在`cover`下添加一个名为`hidden`的项目，并将其设置为`true`。
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# 关于图像尺寸

根据目前PaperMod的规范，Twitter Card的尺寸似乎只支持`summary_large_image`。
关于`summary_large_image`的合适尺寸（分辨率）有很多说法，但大约`800 x 418`（图像比例 1.91:1）似乎是不错的选择。

[参考网站1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[参考网站2](https://developers.facebook.com/docs/sharing/best-practices)


建议您在发布前调整图像大小。

# 确认设置的方法
要确认Twitter Card的设置，请使用[Twitter Card Validator](https://cards-dev.twitter.com/validator)。
但是，在我的环境中，预览没有成功显示。因此，如果没有显示预览，建议您在发布之前使用私人帐户等进行确认。
