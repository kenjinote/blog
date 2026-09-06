---
title: "Como obter e colocar o ranking de páginas populares do Google Analytics"
slug: "Googleアナリティクスから人気ページランキングを取得して配置する方法"
date: 2023-04-10T20:26:57+09:00
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["Operação do Blog"]
---

## Introdução

Usando um serviço chamado `Ranklet`, você pode facilmente obter o ranking de páginas populares do Google Analytics e colocá-lo em seu site.

Neste artigo, apresentamos como adicioná-lo a um blog HUGO.

## Exemplo de funcionamento

![img_1.png](img_1.png)

## Preparação
- Ter o Google Analytics configurado em seu site

## Passos

1. Acesse o `Ranklet`
2. Clique em `Sign in with Google` e faça login com sua conta do Google (ela deve estar vinculada à sua conta do Google Analytics)
![img_2.png](img_2.png)

Clique em `Permitir` (`許可`)

3. Configure as informações básicas

![img_3.png](img_3.png)
Configurei como mostrado acima.

- Em `Google Analytics ビュー` (Visualização do Google Analytics), selecione a visualização da qual deseja obter o ranking.

4. Configure a substituição de texto

![img_4.png](img_4.png)
Configurei como mostrado acima.
Esta configuração serve para remover ` | kenji.blog` do título da página.

5. Configure o template

- HTML (os números do ranking foram ocultados)

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

- CSS (o tamanho da fonte foi alterado e o texto da descrição foi configurado para ser exibido em até 3 linhas)

```css
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

- JavaScript sem alterações

6. Copie o HTML da seção de publicação no site

![img_5.png](img_5.png)

Copie o HTML exibido

7. Cole no template do HUGO

- Crie `layouts/partials/ranklet.html` e cole o HTML copiado
```html
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- Cole o código abaixo na linha antes de `</footer>` em `layouts/_default/single.html`
```html
{{- partial "ranklet.html" . }}
```

É isso. Agora o ranking será exibido na parte inferior da página, como mostrado abaixo.
