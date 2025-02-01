---
title: 'mermaid.jsを試してみる'
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
---

## mermaid.jsとは

mermaid.jsは、JavaScriptのライブラリで、テキストベースの独自の構文(Mermaid記法)を記述し、フローチャートやダイヤグラム、ガントチャートなど、複雑な図表をグラフィカルに表示できます。
GitHubやQiita、Notionなど、いろいろなサービスでも採用されています。今回は、hugoでmermaid.jsを使えるようにしてみます。

## hugoでmermaid.jsを使えるようにする

手順は以下の通りです。

1. layouts/partials/extend_footer.htmlに以下を追加。

```html
{{ if or .Params.mermaid .Site.Params.mermaid }}
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.3.0/dist/mermaid.min.js"></script>
{{- $loadmermaid := resources.Get "js/load-mermaid.js" }}
<script src="{{ $loadmermaid.RelPermalink }}"></script>
<script>
    window.initMermaid();
    if (isDarkTheme()) {
        setPrefTheme('dark');
    } else {
        setPrefTheme('light');
    }
</script>
{{ end }}
```
※if文で`mermaid: true`とした場合のみ`mermaid.min.js`を読み込むようにしています。このライブラリは3MBほどあり意外と大きい。

3. assets/js/load-mermaid.jsを作成。この処理は初期化および動的にテーマが切り替えられた際、再描画するために使われます。

```javascript
(function(window){
'use strict'

  const elementCode = '.mermaid'
  const loadMermaid = function(theme) {
    window.mermaid.initialize({theme})
    window.mermaid.init({theme}, document.querySelectorAll(elementCode))
  }
  const saveOriginalData = function(){
    return new Promise((resolve, reject) => {
      try {
        var els = document.querySelectorAll(elementCode),
            count = els.length;
        els.forEach(element => {
          element.setAttribute('data-original-code', element.innerHTML)
          count--
          if(count == 0){
            resolve()
          }
        });
      } catch (error) {
       reject(error) 
      }
    })
  }
  const resetProcessed = function(){
    return new Promise((resolve, reject) => {
      try {
        var els = document.querySelectorAll(elementCode),
            count = els.length;
        els.forEach(element => {
          if(element.getAttribute('data-original-code') != null){
            element.removeAttribute('data-processed')
            element.innerHTML = element.getAttribute('data-original-code')
          }
          count--
          if(count == 0){
            resolve()
          }
        });
      } catch (error) {
       reject(error) 
      }
    })
  } 

  const init = ()=>{
    saveOriginalData()
    .catch( console.error )
    document.body.addEventListener('dark-theme-set', ()=>{
      resetProcessed()
      .then(loadMermaid('dark'))
      .catch(console.error)
    })
    document.body.addEventListener('light-theme-set', ()=>{
      resetProcessed()
      .then(loadMermaid('default'))
      .catch(console.error)
    })
  }
  window.initMermaid = init
})(window);
```
こちら元となるコードは下記を参考にしました。
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. header.htmlのテーマ切り替え時の処理を修正

```javascript
function switchTheme(theme) {
  switch (theme) {
    case 'light':
{{ if or .Params.mermaid .Site.Params.mermaid }}
      document.body.dispatchEvent(new CustomEvent('light-theme-set'));
{{ end }}
      document.body.classList.remove('dark');
      break;
    case 'dark':
{{ if or .Params.mermaid .Site.Params.mermaid }}
      document.body.dispatchEvent(new CustomEvent('dark-theme-set'));
{{ end }}
      document.body.classList.add('dark');
      break;
    // auto
    default:
      if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
{{ if or .Params.mermaid .Site.Params.mermaid }}
        document.body.dispatchEvent(new CustomEvent('dark-theme-set'));
{{ end }}
        document.body.classList.add('dark');
      }
  }
}
```

4. layouts/shortcodes/mermaid.htmlを作成

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

以上でmermaid.jsを使える準備が整いました。

## mermaid.jsを使ってみる

1. 記事の定義に下記を追加

```dtd
marmaid: true
```

2. 記事の本文に下記を追加

**フローチャート**

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[開始] -->|条件1| B(条件2)
    B --> C{条件3}
    C -->|条件4| D[終了]
{{</*/mermaid*/>}}
```

**出力結果**

{{<mermaid align="center">}}
graph TD
    A[開始] -->|条件1| B(条件2)
    B --> C{条件3}
    C -->|条件4| D[終了]
{{</mermaid>}}

**ガントチャート**

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    要件定義 :done,      a, 2024-05-25, 5d
    基本設計 :done,      b, after a,    5d
    詳細設計 :done,      c, after b,    5d
    製造    :active,    d, after c,    10d
    単体試験 :crit,      e, after d,    5d
    結合試験 :           f, after e,    5d
    総合試験 :           g, after f,    5d
    リリース :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

**出力結果**

{{<mermaid align="center">}}
gantt
    section Project
    要件定義 :done,      a, 2024-05-25, 5d
    基本設計 :done,      b, after a,    5d
    詳細設計 :done,      c, after b,    5d
    製造    :active,    d, after c,    10d
    単体試験 :crit,      e, after d,    5d
    結合試験 :           f, after e,    5d
    総合試験 :           g, after f,    5d
    リリース :milestone, h, after g,    1d
{{</mermaid>}}


**シーケンス図**

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: ID/PW入力
    view->>controller: 認証リクエスト
    controller->>model: 認証リクエスト
    model->>database: 認証リクエスト
    database-->>model: 認証結果返却
    model-->>controller: 認証結果返却
    controller-->>view: 認証結果返却
    view-->>user: 認証結果表示
{{</*/mermaid*/>}}
``` 

**出力結果**

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: ID/PW入力
    view->>controller: ajax問い合わせ
    controller->>model: 認証リクエスト
    model->>database: SQL発行
    database-->>model: SQL結果返却
    model-->>controller: 認証リクエスト結果返却
    controller-->>view: ajax問い合わせ結果返却
    view-->>user: 認証結果表示
{{</mermaid>}}

以上です。

### 参考
- [mermaid.js本家](https://mermaid.js.org/#/)
- [mermaid構文をプレビューできるデモサイト](https://mermaid.live/)
