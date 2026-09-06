---
title: "Как получить и разместить рейтинг популярных страниц из Google Analytics"
slug: "Googleアナリティクスから人気ページランキングを取得して配置する方法"
date: 2023-04-10T20:26:57+09:00
tags: ["Googleアナリティクス", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---

## Введение

Используя сервис под названием **Ranklet** , вы можете легко получить и разместить рейтинг популярных страниц из Google Analytics.

В этой статье я расскажу, как разместить его в блоге HUGO.

## Пример работы

![img_1.png](img_1.png)

## Подготовка
- Google Analytics должен быть настроен на сайте

## Шаги

1. Перейдите в **Ranklet**
2. Нажмите **Sign in with Google** , чтобы войти с помощью учетной записи Google (должна быть привязана к учетной записи Google Analytics)
![img_2.png](img_2.png)

Нажмите **Разрешить**

3. Настройте основную информацию

![img_3.png](img_3.png)
Я настроил, как показано выше.

- В **Google Analytics View** выберите представление, для которого вы хотите получить рейтинг.

4. Настройте замену текста

![img_4.png](img_4.png)
Я настроил, как показано выше.
Это настроено для удаления ` | kenji.blog` из заголовка страницы.

5. Настройте шаблон

- HTML (числа рейтинга скрыты)

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

- CSS (изменен размер шрифта, описание будет отображаться в 3 строки)

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

- JavaScript без изменений

6. Скопируйте HTML из публикации на сайте

![img_5.png](img_5.png)

Скопируйте отображаемый HTML

7. Вставьте в шаблон HUGO

- Создайте `layouts/partials/ranklet.html` и вставьте скопированный HTML
```
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- Вставьте приведенный ниже код в строку перед `</footer>` в `layouts/_default/single.html`
```
{{- partial "ranklet.html" . }}
```

На этом все. Рейтинг будет отображаться в нижней части этой страницы, как показано ниже.
