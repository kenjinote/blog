---
title: "使用 CSS 变量自定义 Hugo PaperMod 配色"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "通过扩展 CSS 覆盖 PaperMod 的浅色与深色主题变量，并检查文本对比度。"
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod 的颜色可以通过 CSS 自定义属性（变量）调整。请将覆盖样式放在站点的 `assets/css/extended/` 中，而不要直接编辑主题文件，这样主题更新后更容易保留修改。下面示例提供暖色浅色主题和深色主题，可按站点需要调整。

## 深色模式与当前变量

当前 PaperMod 通过在 `html` 元素上设置 `data-theme="dark"` 来切换深色模式。旧示例若只选择 `.dark`，可能无法匹配当前主题选择器。`--hljs-bg` 也不再是当前代码块背景变量；现在使用的名称是 `--code-block-bg`。

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

## 文本对比度

示例中的常规文字颜色 `--primary` 和 `--content` 与背景有较强对比。`--primary` 对 `--theme` 的示例对比度在浅色模式约为 10.4:1，在深色模式约为 13.4:1。WCAG 2.2 AA 对常规文本的要求是 4.5:1；语法高亮颜色、链接、边框及其他状态仍需单独检查。

## 添加并检查扩展 CSS

在站点根目录将样式表保存为 `assets/css/extended/theme-colors.css`。PaperMod FAQ 说明，`assets/css/extended/` 中的 CSS 会与主题样式一起打包。运行 Hugo 后检查浅色/深色切换、卡片、正文、行内代码、代码块和链接。方

## 范围

此配色仅为示例，并不保证所有文字、图片和交互组件都符合无障碍要求。语法高亮颜色与 `--code-block-bg` 分开定义，因此修改代码块背景后要重新检查代码的可读性。

## 参考资料

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
