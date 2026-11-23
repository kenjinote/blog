---
title: '使用 Ranklet4 在 Hugo 中显示 GA4 热门页面排名'
date: 2023-04-10T20:26:57+09:00
lastmod: 2026-11-23




slug: "Google分析から人気ページランキングを取得して配置する方法"
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '使用面向 GA4、接替已停用 Ranklet 小组件的 Ranklet4，在 Hugo 中添加热门页面排名。本文介绍迁移、权限、模板以及使用第三方服务时的注意事项。'
---

# 使用 Ranklet4 在 Hugo 中显示 GA4 热门页面排名

旧教程使用 Google Analytics 视图和旧版 Ranklet 小组件。旧 Ranklet 服务已于 2023 年结束。请将旧标签替换为 GA4 专用独立服务 Ranklet4 生成的新标签。请参阅[官方迁移说明](https://docs.ranklet4.com/changes.html)。

Ranklet4 汇总 GA4 报告数据，并通过 JavaScript 小组件提供排名，也支持 Hugo 等静态网站。菜单和方案可能变化，请以[官方教程](https://docs.ranklet4.com/tutorial.html)为准。

## 开始前

* 网站需要有记录访问数据的 GA4 媒体资源。
* 用于登录的 Google 账号在该媒体资源中至少需要**查看者**权限，无需使用管理员账号。
* Ranklet4 将获得 Google Analytics 数据访问权限。其条款授予广泛许可，可使用、复制、分发、创作衍生作品、展示和执行分析数据；条款还允许使用和发布无法识别个人身份的统计信息。连接前请阅读[服务条款](https://docs.ranklet4.com/agreement.html)和[隐私政策](https://ranklet4.com/docs/privacy)，并确认你有权共享这些数据。

## 创建并发布排名

1. 使用可查看目标 GA4 媒体资源的账号登录 [Ranklet4](https://ranklet4.com/)。授权前请检查所请求的权限。
2. 创建排名并选择 GA4 媒体资源、统计周期和显示数量。可按标题或 URL 设置筛选，例如排除首页。
3. 按需设置标题文字替换，并在预览中确认标题和结果。
4. 从设计库选择模板，或自定义 HTML/CSS。新模板使用 Handlebars；字段名和语法请查看[模板指南](https://docs.ranklet4.com/template.html)。
5. 保存并发布，然后复制管理页面生成的排名标签。不要继续使用旧 Ranklet 标签或 ID。

以下是最小 HTML 模板示例。支持的字段和循环语法请参阅官方指南。

```handlebars
<ol class="popular-pages">
  {{#each rankings}}
  <li><a href="{{url}}">{{title}}</a></li>
  {{/each}}
</ol>
```

## 添加到 Hugo

1. 创建 `layouts/partials/ranklet4.html`，粘贴 Ranklet4 生成的完整排名标签。
2. 在要显示排名的布局中加入以下 Hugo 调用，例如 `layouts/_default/single.html` 或侧边栏 partial：

```go-html-template
{{- partial "ranklet4.html" . }}
```

3. 在本地预览页面，发布后确认小组件通过 HTTPS 加载。它依赖第三方 JavaScript；请考虑页面速度、隐私声明和网站安全策略。

## 更新与迁移注意事项

排名根据 GA4 报告和 Ranklet4 的更新计划刷新，因此访问发生后排名不一定立即变化。刷新频率、套餐功能、服务积分和广告政策可能会变，请查看[当前方案](https://docs.ranklet4.com/plan.html)。Ranklet4 爬虫会读取公开页面信息，详见[常见问题](https://docs.ranklet4.com/faq.html)。

## 官方资料

* [Ranklet4 官方教程](https://docs.ranklet4.com/tutorial.html)
* [与旧版 Ranklet 的变化](https://docs.ranklet4.com/changes.html)
* [Ranklet4 模板指南](https://docs.ranklet4.com/template.html)
* [Ranklet4 常见问题](https://docs.ranklet4.com/faq.html)
* [Ranklet4 服务条款](https://docs.ranklet4.com/agreement.html)
* [Ranklet4 隐私政策](https://ranklet4.com/docs/privacy)
