---



title: "Google 애널리틱스에서 인기 페이지 랭킹을 가져와 배치하는 방법"
date: 2023-04-10T20:26:57+09:00
tags: ["Google 애널리틱스", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["블로그 운영"]
---




## 시작하며

`Ranklet`이라는 서비스를 사용하면 Google 애널리틱스에서 인기 페이지 랭킹을 가져와 쉽게 배치할 수 있습니다.

이 글에서는 HUGO 블로그에 배치하는 방법을 소개합니다.

## 동작 이미지

![img_1.png](img_1.png)

## 준비
- 사이트에 Google 애널리틱스가 설정되어 있을 것

## 절차

1. `Ranklet`에 접속합니다.
2. `Sign in with Google`을 클릭하여 Google 계정으로 로그인합니다 (Google 애널리틱스 계정과 연결되어 있어야 합니다).
![img_2.png](img_2.png)

`허용`을 클릭

3. 기본 정보를 설정합니다.

![img_3.png](img_3.png)
위와 같이 설정했습니다.

- `Google Analytics 뷰`에서는 랭킹을 가져오고 싶은 뷰를 선택합니다.

4. 텍스트 치환을 설정합니다.

![img_4.png](img_4.png)
위와 같이 설정했습니다.
페이지 제목의 ` | kenji.blog`를 삭제하기 위해 설정했습니다.

5. 템플릿을 설정합니다.

- HTML (랭킹 숫자를 숨겼습니다)

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

- CSS (폰트 크기를 변경하고, 설명문이 3줄로 표시되도록 했습니다)

```css
#ranklet-{{context.id}} {
    .ranklet-reset { // 리셋
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
                -webkit-line-clamp: 3; /* 줄 수 */
            }
        }
    }
}
```

- JavaScript는 변경 없음

6. 사이트 게재에서 HTML을 복사합니다.

![img_5.png](img_5.png)

표시된 HTML을 복사합니다.

7. HUGO 템플릿에 붙여넣습니다.

- `layouts/partials/ranklet.html`을 생성하고, 복사한 HTML을 붙여넣습니다.
```html
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- `layouts/_default/single.html`의 `</footer>` 앞 줄에 아래 코드를 붙여넣습니다.
```html
{{- partial "ranklet.html" . }}
```

이상입니다. 이제 이 페이지 아래와 같이 랭킹이 표시됩니다.
