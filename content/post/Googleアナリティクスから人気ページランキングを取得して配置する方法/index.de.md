---
title: "Wie man das Ranking beliebter Seiten aus Google Analytics abruft und einbindet"
slug: "Googleアナリティクスから人気ページランキングを取得して配置する方法"
date: 2023-04-10T20:26:57+09:00
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["Blog-Betrieb"]
---

## Einleitung

Mit dem Dienst `Ranklet` können Sie ganz einfach ein Ranking beliebter Seiten aus Google Analytics abrufen und auf Ihrer Website einbinden.

In diesem Artikel zeige ich Ihnen, wie Sie dieses Ranking in einem HUGO-Blog einbinden.

## Vorschau

![img_1.png](img_1.png)

## Vorbereitung
- Auf Ihrer Website muss Google Analytics eingerichtet sein.

## Schritte

1. Rufen Sie `Ranklet` auf.
2. Klicken Sie auf `Sign in with Google` und melden Sie sich mit Ihrem Google-Konto an (dieses muss mit Ihrem Google Analytics-Konto verknüpft sein).
![img_2.png](img_2.png)

Klicken Sie auf `Zulassen` (`許可`).

3. Richten Sie die grundlegenden Informationen ein.

![img_3.png](img_3.png)
Die Einstellungen wurden wie oben abgebildet vorgenommen.

- Wählen Sie unter `Google Analytics-Ansicht` (`Google Analytics ビュー`) die Datenansicht aus, aus der Sie das Ranking abrufen möchten.

4. Richten Sie die Textersetzung ein.

![img_4.png](img_4.png)
Die Einstellungen wurden wie oben abgebildet vorgenommen.
Dies ist so eingestellt, dass ` | kenji.blog` aus dem Seitentitel entfernt wird.

5. Richten Sie die Vorlage ein.

- HTML (Die Platzierungsnummern des Rankings wurden ausgeblendet)

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

- CSS (Schriftgröße geändert und die Beschreibung auf maximal 3 Zeilen begrenzt)

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
                -webkit-line-clamp: 3; /* Zeilenanzahl */
            }
        }
    }
}
```

- JavaScript bleibt unverändert

6. Kopieren Sie den HTML-Code aus „Auf Website einbinden“ (`サイトへの掲載`)

![img_5.png](img_5.png)

Kopieren Sie den angezeigten HTML-Code.

7. In das HUGO-Template einfügen

- Erstellen Sie `layouts/partials/ranklet.html` und fügen Sie den kopierten HTML-Code ein.
```html
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- Fügen Sie den folgenden Code in der Zeile vor `</footer>` in `layouts/_default/single.html` ein.
```html
{{- partial "ranklet.html" . }}
```

Das ist alles. Damit wird das Ranking wie unten auf dieser Seite angezeigt.
