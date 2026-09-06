---
title: '如何从Google Analytics获取并配置热门页面排行榜'
slug: "Googleアナリティクスから人気ページランキングを取得して配置する方法"
date: 2023-04-10T20:26:57+09:00
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["博客运营"]
---

## 简介

使用名为 `Ranklet` 的服务，您可以从 Google Analytics 中获取热门页面排行榜并轻松进行配置。

本文将介绍如何在 HUGO 博客中进行配置。

## 运行效果

![img_1.png](img_1.png)

## 准备工作
- 网站已设置 Google Analytics

## 步骤

1. 访问 `Ranklet`
2. 点击 `Sign in with Google`，使用 Google 账号登录（需与 Google Analytics 账号绑定）
![img_2.png](img_2.png)

点击 `允许`

3. 设置基本信息

![img_3.png](img_3.png)
如上图所示进行了设置。

- 在 `Google Analytics ビュー`（Google Analytics 视图）中，选择要获取排行榜的视图。

4. 设置文本替换

![img_4.png](img_4.png)
如上图所示进行了设置。
设置目的是删除页面标题中的 ` | kenji.blog`。

5. 设置模板

- HTML（隐藏了排行榜的数字）

```
<div class="ranklet ranklet-reset">
    <table class="ranklet-table">
        <tbody class="ranklet-pages">
            {{#context.pages}}
            <tr class="ranklet-page">
                <td class="ranklet-image">
                    {{#image}}
                    <a href="{{url}}" class="ranklet-link">
                        <img class="ranklet-img" src="{{image}}" />
                    </a>
                    {{/image}}
                </td>
                <td class="ranklet-meta">
                    <div class="ranklet-title">
                        <a href="{{url}}" class="ranklet-link">
                            {{title}}
                        </a>
                    </div>
                    {{#description}}
                    <div class="ranklet-description">
                        <a href="{{url}}" class="ranklet-link">
                            {{description}}
                        </a>
                    </div>
                    {{/description}}
                </td>
            </tr>
            {{/context.pages}}
        </tbody>
    </table>
</div>
```

- CSS（更改了字体大小，使说明文字显示为3行）

```
#ranklet-{{context.id}} {
    .ranklet-reset { // 重置
        table, tr, td, div, span {
            margin: 0;
            padding: 0;
            border: 0;
            font-size: 100%;
            font: inherit;
            vertical-align: baseline;
            line-height: 1;
            box-sizing: border-box;
        }
    }

    .ranklet-table {
        border-collapse: separate;
        border-spacing: 8px 24px;
        width: 100%;
        word-break: break-all;

        td {
            vertical-align: middle;
        }

        .ranklet-rank {
            text-align: center;
            font-size: 120%;
        }

        .ranklet-image {
            text-align: center;
            img {
                max-width: 128px;
                max-height: 128px;
            }
        }

        .ranklet-meta {
            .ranklet-title {
                font-size: 20px;
                line-height: 125%;
            }

            .ranklet-description {
                font-size: 16px;
                margin-top: 8px;
                line-height: 125%;
                display: -webkit-box;
                overflow: hidden;
                -webkit-box-orient: vertical;
                -webkit-line-clamp: 3; /* 行数 */
            }
        }
    }
}
```

- JavaScript 保持不变

6. 从网站发布中复制 HTML

![img_5.png](img_5.png)

复制显示的 HTML

7. 粘贴到 HUGO 模板中

- 创建 `layouts/partials/ranklet.html`，并粘贴复制的 HTML
```
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- 在 `layouts/_default/single.html` 中的 `</footer>` 前一行粘贴以下代码
```
{{- partial "ranklet.html" . }}
```

以上。这样，页面底部就会像下面这样显示排行榜了。
