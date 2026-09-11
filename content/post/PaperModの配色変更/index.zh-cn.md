---
title: '如何通过CSS更改Hugo PaperMod主题的配色及颜色主题'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["博客运营"]
description: '讲解如何自定义Hugo PaperMod主题的整体配色。介绍通过编辑包含背景色、文本色及代码块等样式定义的CSS（blank.css），来应用您所偏好的配色方案的具体变量设置示例。'
---
我更改了 PaperMod 主题的配色。更改方法参考了以下链接：

https://github.com/adityatelange/hugo-PaperMod/discussions/645

CSS 的路径如下：

`themes/PaperMod/assets/css/extended/blank.css`

```
:root {
    --entry: #fbf7ef;
    --primary: rgba(113, 103, 91, 1.00);
    --secondary: rgba(113, 103, 91, 0.95);
    --tertiary: rgba(113, 103, 91, 0.50);
    --content: rgba(113, 103, 91, 0.85);
    --hljs-bg: #34231B;
    --code-bg: #ebe4d7;
    --border: #fdfaf5;
    --theme: #fbf7ef;
}
.dark {
}
```

目前暂时不更改暗黑模式。
