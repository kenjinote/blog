---
title: 'How to Get and Place Popular Page Rankings from Google Analytics'
date: 2023-04-10T20:26:57+09:00
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["Blog Management"]
---

## Introduction

By using a service called `Ranklet`, you can easily get and place popular page rankings from Google Analytics.

In this article, I will show you how to place it on a HUGO blog.

## Demo

![img_1.png](img_1.png)

## Preparation
- Google Analytics must be set up on your site.

## Steps

1. Access `Ranklet`.
2. Click `Sign in with Google` and log in with your Google account (it must be linked to your Google Analytics account).
![img_2.png](img_2.png)

Click `Allow`.

3. Set up basic information.

![img_3.png](img_3.png)
I configured it as above.

- In `Google Analytics View`, select the view from which you want to get the ranking.

4. Set up text replacement.

![img_4.png](img_4.png)
I configured it as above.
This is set to remove ` | kenji.blog` from the page title.

5. Set up the template.

- HTML (Hid the ranking numbers)

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

- CSS (Changed font size and set the description to be displayed in 3 lines)

```css
#ranklet-{{context.id}} {
    .ranklet-reset { // Reset
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
                -webkit-line-clamp: 3; /* Number of lines */
            }
        }
    }
}
```

- JavaScript remains unchanged.

6. Copy the HTML from "Publish on site".

![img_5.png](img_5.png)

Copy the displayed HTML.

7. Paste it into the HUGO template.

- Create `layouts/partials/ranklet.html` and paste the copied HTML.
```html
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- Paste the following code on the line before `</footer>` in `layouts/_default/single.html`.
```html
{{- partial "ranklet.html" . }}
```

That's it. Now the ranking will be displayed as shown at the bottom of this page.
