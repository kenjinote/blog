---


title: "Cómo obtener y colocar una clasificación de páginas populares desde Google Analytics"
date: 2023-04-10T20:26:57+09:00
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["Gestión de blog"]
---



## Introducción

Usando un servicio llamado `Ranklet`, puedes obtener fácilmente una clasificación de páginas populares desde Google Analytics y colocarla en tu sitio.

En este artículo, te mostraremos cómo colocarlo en un blog HUGO.

## Imagen de funcionamiento

![img_1.png](img_1.png)

## Preparación
- Asegúrate de haber configurado Google Analytics en tu sitio.

## Pasos

1. Accede a `Ranklet`
2. Haz clic en `Sign in with Google` e inicia sesión con tu cuenta de Google (asegúrate de que esté vinculada a tu cuenta de Google Analytics)
![img_2.png](img_2.png)

Haz clic en `Permitir` (`許可`)

3. Configura la información básica

![img_3.png](img_3.png)
Lo he configurado como se muestra arriba.

- En `Vista de Google Analytics` (`Google Analytics ビュー`), selecciona la vista de la que deseas obtener la clasificación.

4. Configura el reemplazo de texto

![img_4.png](img_4.png)
Lo he configurado como se muestra arriba.
Se configura para eliminar ` | kenji.blog` del título de la página.

5. Configura la plantilla

- HTML (Se ocultaron los números de clasificación)

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

- CSS (Se cambió el tamaño de la fuente y se configuró la descripción para que se muestre en 3 líneas)

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

- JavaScript sin cambios

6. Copia el HTML de "Publicación en el sitio" (`サイトへの掲載`)

![img_5.png](img_5.png)

Copia el HTML que se muestra.

7. Pégalo en la plantilla de HUGO

- Crea `layouts/partials/ranklet.html` y pega el HTML copiado.
```
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- Pega el siguiente código en la línea anterior a `</footer>` en `layouts/_default/single.html`.
```
{{- partial "ranklet.html" . }}
```

Eso es todo. Ahora la clasificación se mostrará en la parte inferior de esta página como se muestra a continuación.
