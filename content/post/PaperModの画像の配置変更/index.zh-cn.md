---
title: "调整 PaperMod 文章列表中封面图的大小与位置"
slug: "PaperModの图像の配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "使用 PaperMod 的扩展 CSS 功能和 CSS Grid 缩小文章卡片封面图，并将其放在摘要旁边。"
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

本文示例会缩小 PaperMod 文章列表卡片中的封面图，并将其放在标题下方、摘要旁边。通过站点级扩展 CSS 实现，无需直接修改主题自带的样式表或模板。选择器依赖 PaperMod 的类名，升级主题后请在浏览器中检查效果。

## 添加扩展 CSS

在站点根目录创建 `assets/css/extended/custom.css`。PaperMod 会将此目录中的 CSS 与主题样式一同加载。CSS Grid 可以调整视觉布局，同时保留现有 HTML 结构。

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## 适配窄屏

在窄屏上缩小列宽和间距，让摘要保持易读。可根据设计调整 150px 和断点。`height: auto` 会保留图片比例。只有需要统一裁切形状时才添加 `aspect-ratio` 和 `object-fit: cover`。

## 避免直接修改主题文件

PaperMod 文档说明，`blank.css` 是扩展 CSS 目录为空时使用的占位文件。无需修改主题自带的 `post-entry.css`，也无需删除其中注释掉的 `/* width: 100%; */`；删除 CSS 注释不会改变样式。如果确实要更改 HTML 结构，可以将模板复制到站点的 `layouts/` 目录进行覆盖，但主题更新后需要维护这份副本。

## 检查布局

运行 Hugo，在宽屏和窄屏上检查首页、标签页和分类页列表。图片、标题、摘要和元数据不应互相遮挡，覆盖整张卡片的链接也应继续可用。若主题更新更改了类名或 HTML，请相应调整 CSS。此示例只影响列表卡片的封面，不影响文章正文中的图片。

## 参考资料

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
