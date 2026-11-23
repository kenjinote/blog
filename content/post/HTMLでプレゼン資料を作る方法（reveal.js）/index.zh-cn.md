---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23
title: 'reveal.js使用教程：用HTML和Markdown制作演示文稿'
slug: "HTMLで演示資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "演示文稿"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '本文讲解能用HTML和Markdown直观创建演示文稿的工具“reveal.js”的安装和基本使用方法。支持动画和PDF输出，并介绍与Git等版本控制系统兼容性极佳的运用方法。'
---

# 使用HTML制作演示文稿的方法

reveal.js 是一个使用 HTML 和 Markdown 的演示文稿制作工具，具有以下功能：

- 公式、动画、滑动操作等丰富多彩的演示功能
- 可以自定义主题和布局
- 支持鼠标、键盘、触摸板等多种设备的导航功能
- 提供幻灯片自动播放、嵌入视频等高级功能
- 可以导出为 PDF 格式

通过这些功能，用户可以轻松创建交互式且富有吸引力的演示文稿。

# reveal.js 的安装与使用方法

最简单的使用方法是从以下页面下载整个 ZIP 文件并解压缩。

1. 打开 [https://revealjs.com/installation](https://revealjs.com/installation) ，从链接下载 `master.zip`
2. 在浏览器中打开解压后文件夹内的 index.html
3. 修改 index.html，创建自己的演示文稿资料

※可以参考 demo.html，里面写有用于演示的 HTML 代码。

# 应用方法

制作好的演示文稿可以直接作为网页公开，也可以导出为 PDF。
另外，由于演示文稿的源码是文本，因此很容易用版本控制系统进行管理。

似乎还可以使用 Markdown 格式来创建演示资料。

# 创建基本幻灯片

Basic Setup 是最简单的方式：解压最新 ZIP 并编辑其中的 `index.html`。如下面的 HTML 示例所示，每张幻灯片放在一个 `<section>` 中。Basic Setup 的示例文件已包含样式和初始化代码。

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# 使用 Markdown 编写幻灯片

内置的 Markdown 插件允许你直接在 HTML 文件中写 Markdown。使用 `---` 分隔横向幻灯片。将下面的示例加入 `index.html`。从外部文件加载 Markdown 需要本地 Web 服务器。

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# 开发环境

如需本地服务器或源码开发工具，请使用官方 Full Setup。运行以下命令，然后在浏览器中打开 `http://localhost:8000`。

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# 导出为 PDF

在网址末尾添加 `?print-pdf`。在 Chrome 或 Chromium 的打印界面选择“另存为 PDF”、横向、无边距并启用背景图形。官方指南确认支持 Chrome 和 Chromium。

# 演讲者备注

按 `S` 可在单独窗口打开演讲者视图。在幻灯片的 `<aside class="notes">` 中添加备注。本地使用演讲者视图需要 Web 服务器。

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# 官方文档

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

スライドに使う画像・動画の利用条件を確認し、公開資料に機密情報や非公開の発表者ノートが含まれていないか確認してください。
