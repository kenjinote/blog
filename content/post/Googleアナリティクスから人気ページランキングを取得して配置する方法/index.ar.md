---
title: "كيفية الحصول على ترتيب الصفحات الشائعة من Google Analytics ووضعه"
slug: "Googleアナリティクスから人気ページランキングを取得して配置する方法"
date: 2023-04-10T20:26:57+09:00
tags: ["Googleアナリティクス", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---

## مقدمة

باستخدام خدمة تسمى **Ranklet** ، يمكنك بسهولة الحصول على ترتيب الصفحات الشائعة من Google Analytics ووضعه.

في هذه المقالة، سأوضح لك كيفية وضعه في مدونة HUGO.

## صورة للعمل

![img_1.png](img_1.png)

## التحضير
- يجب إعداد Google Analytics في الموقع

## الخطوات

1. قم بالوصول إلى **Ranklet**
2. انقر فوق **Sign in with Google** لتسجيل الدخول بحساب Google (يجب أن يكون مرتبطًا بحساب Google Analytics)
![img_2.png](img_2.png)

انقر فوق **السماح**

3. قم بتعيين المعلومات الأساسية

![img_3.png](img_3.png)
لقد قمت بإعداده كما هو موضح أعلاه.

- في **Google Analytics View** حدد العرض الذي تريد الحصول على الترتيب له.

4. قم بتعيين استبدال النص

![img_4.png](img_4.png)
لقد قمت بإعداده كما هو موضح أعلاه.
تم تعيين هذا لإزالة ` | kenji.blog` من عنوان الصفحة.

5. قم بتعيين القالب

- HTML (تم إخفاء أرقام الترتيب)

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

- CSS (تم تغيير حجم الخط، وسيتم عرض الوصف في 3 أسطر)

```
#ranklet-{{context.id}} {
    .ranklet-reset { // リセット
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

- لم يتم تغيير JavaScript

6. انسخ HTML من النشر على الموقع

![img_5.png](img_5.png)

انسخ HTML المعروض

7. الصقه في قالب HUGO

- قم بإنشاء `layouts/partials/ranklet.html` والصق HTML المنسوخ
```
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- الصق الرمز أدناه في السطر الذي يسبق `</footer>` في `layouts/_default/single.html`
```
{{- partial "ranklet.html" . }}
```

هذا كل شيء. سيتم عرض الترتيب في أسفل هذه الصفحة كما هو موضح أدناه.
