---
date: 2022-09-11T22:59:52+09:00
lastmod: 2026-11-23
title: 'Hugo内置短代码：媒体嵌入、版本差异与隐私设置'
slug: "HUGOで使える短路コード"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '了解Hugo内置短代码、各版本的差异，以及如何配置媒体嵌入和隐私选项。'
---

# Hugo内置短代码：媒体嵌入、版本差异与隐私设置

短代码是在Markdown内容中调用模板功能的语法。Hugo提供内置短代码，主题和模块也可能添加短代码，项目还可以自行定义。名称和参数会随Hugo版本变化，请查阅实际使用版本的官方文档。

## Hugo内置短代码

Flickr不是Hugo核心内置短代码。如果项目中的`flickr`调用可用，它来自主题、模块或项目自定义模板，例如`layouts/_shortcodes/flickr.html`。不要仅凭名称相同就认为它是内置功能。

当前官方列表包括`details`、`figure`、`highlight`、`instagram`、`param`、`qr`、`ref`、`relref`、`vimeo`、`x`和`youtube`等。完整列表和参数请参阅官方页面。

## 媒体示例

### YouTube

使用视频网址`v`参数中的ID。

`{{</* youtube 0RKpf3rK57I */>}}`

### X（Hugo 0.141.0及更高版本）

填写帖子网址中的用户名和帖子ID。

`{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}`

### 旧版Twitter（Hugo 0.139.0）

Hugo 0.139.0使用以下命名参数。

`{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Instagram

Instagram帖子网址的最后一段就是帖子ID。

`{{</* instagram CxOWiQNP2MO */>}}`

### Vimeo

使用Vimeo视频网址末尾的数字ID。

`{{</* vimeo 19899678 */>}}`

## 注意版本差异

本博客的构建版本固定为Hugo 0.139.0。在该版本中，X（原Twitter）的内置名称是`twitter`，需要用命名参数传入用户名和帖子ID。`x`短代码从Hugo 0.141.0开始提供，之后的版本将`twitter`标记为弃用。复制新版文档中的示例前，请先确认项目使用的Hugo版本。

## 隐私设置

YouTube、X、Instagram和Vimeo嵌入可能让访问者的浏览器连接到这些服务。Hugo的`privacy`配置可以禁用嵌入，或在支持时启用简化模式。YouTube的`privacyEnhanced`设置会限制信息保存，直到访问者播放视频。

YouTube隐私增强模式:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

X简化模式:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

旧版Twitter（Hugo 0.139.0）:

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

请查阅与你所用Hugo版本对应的官方文档，确认各项设置名称。

Instagram简化模式仍会直接从Instagram服务器加载图片。Vimeo简化模式会获取缩略图，点击后在新标签页打开Vimeo。这些模式不会完全消除第三方请求。

发布嵌入内容前，请检查对服务提供商的网络请求、Cookie行为，以及面向读者所在地区的隐私要求。

## 将语法作为文本显示

若要在文章中原样显示短代码语法，请像下面这样在分隔符中加入`/*`和`*/`进行转义。

`{{</*/* youtube 0RKpf3rK57I */*/>}}`

## 官方文档

- [短代码概述](https://gohugo.io/content-management/shortcodes/)
- [内置短代码](https://gohugo.io/shortcodes/)
- [YouTube](https://gohugo.io/shortcodes/youtube/)
- [X](https://gohugo.io/shortcodes/x/)
- [Instagram](https://gohugo.io/shortcodes/instagram/)
- [Vimeo](https://gohugo.io/shortcodes/vimeo/)
- [隐私配置](https://gohugo.io/configuration/privacy/)
