---
title: "如何從 Google Analytics 取得並配置熱門頁面排行榜"
slug: "Googleアナリティクスから人気ページランキングを取得して配置する方法"
date: 2023-04-10T20:26:57+09:00
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["部落格營運"]
---

## 前言

使用名為 `Ranklet` 的服務，可以從 Google Analytics 取得熱門頁面排行榜並輕鬆進行配置。

本文將介紹如何將其配置到 HUGO 部落格中。

## 效果預覽

![img_1.png](img_1.png)

## 事前準備
- 網站已設定 Google Analytics

## 步驟

1. 前往 `Ranklet`
2. 點擊 `Sign in with Google` 並使用 Google 帳號登入（需與已綁定 Google Analytics 的帳號一致）
![img_2.png](img_2.png)

點擊 `允許`

3. 設定基本資訊

![img_3.png](img_3.png)
如上圖所示進行設定。

- 在 `Google Analytics ビュー`（Google Analytics 檢視）中，選擇想要取得排行榜的檢視。

4. 設定文字取代

![img_4.png](img_4.png)
如上圖所示進行設定。
此設定是為了刪除頁面標題中的 ` | kenji.blog`。

5. 設定範本

- HTML（隱藏了排名的數字）

```html
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

- CSS（修改了字型大小，並讓說明文字以 3 行顯示）

```css
#ranklet-{{context.id}} {
    .ranklet-reset { // 重設
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
                -webkit-line-clamp: 3; /* 行數 */
            }
        }
    }
}
```

- JavaScript 保持不變

6. 從「サイトへの掲載（發佈至網站）」複製 HTML

![img_5.png](img_5.png)

複製畫面上顯示的 HTML

7. 貼上至 HUGO 範本中

- 建立 `layouts/partials/ranklet.html`，並將複製的 HTML 貼上
```html
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- 在 `layouts/_default/single.html` 中的 `</footer>` 前一行貼上以下程式碼
```html
{{- partial "ranklet.html" . }}
```

以上步驟完成。這樣一來，頁面下方就會像本頁底部一樣顯示出排行榜。
