---
title: "嘗試使用 mermaid.js"
slug: "mermaid.jsを試してみる"
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["AI・科技"]
---

## 什麼是 mermaid.js

mermaid.js 是一個 JavaScript 函式庫，它允許你透過編寫基於文字的獨特語法 (Mermaid 語法) 來圖形化顯示複雜的圖表，例如流程圖、圖表和甘特圖。
它也被應用在 GitHub、Qiita 和 Notion 等各種服務中。這次我們將嘗試在 hugo 中使用 mermaid.js。

## 讓 mermaid.js 可以在 hugo 中使用

步驟如下：

1. 在 layouts/partials/extend_footer.html 中加入以下內容。

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
※ 只有當 if 判斷式中設定為 `mermaid: true` 時，才會載入 `mermaid.min.js`。這個函式庫大約有 3MB，出乎意料地大。

3. 建立 assets/js/load-mermaid.js。這個程序用於初始化，以及在動態切換主題時重新繪製。

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
此處的基本程式碼參考了以下內容：
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. 修改 header.html 中切換主題時的處理程序

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

4. 建立 layouts/shortcodes/mermaid.html

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

以上就完成了使用 mermaid.js 的準備工作。

## 嘗試使用 mermaid.js

1. 在文章定義中加入以下內容

```dtd
marmaid: true
```

2. 在文章內文中加入以下內容

**流程圖** 

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[開始] -->|條件1| B(條件2)
    B --> C{條件3}
    C -->|條件4| D[結束]
{{</*/mermaid*/>}}
```

**輸出結果** 

{{<mermaid align="center">}}
graph TD
    A[開始] -->|條件1| B(條件2)
    B --> C{條件3}
    C -->|條件4| D[結束]
{{</mermaid>}}

**甘特圖** 

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    需求定義 :done,      a, 2024-05-25, 5d
    基本設計 :done,      b, after a,    5d
    詳細設計 :done,      c, after b,    5d
    製造    :active,    d, after c,    10d
    單元測試 :crit,      e, after d,    5d
    整合測試 :           f, after e,    5d
    系統測試 :           g, after f,    5d
    發布     :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

**輸出結果** 

{{<mermaid align="center">}}
gantt
    section Project
    需求定義 :done,      a, 2024-05-25, 5d
    基本設計 :done,      b, after a,    5d
    詳細設計 :done,      c, after b,    5d
    製造    :active,    d, after c,    10d
    單元測試 :crit,      e, after d,    5d
    整合測試 :           f, after e,    5d
    系統測試 :           g, after f,    5d
    發布     :milestone, h, after g,    1d
{{</mermaid>}}


**循序圖** 

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: 輸入 ID/PW
    view->>controller: 認證請求
    controller->>model: 認證請求
    model->>database: 認證請求
    database-->>model: 傳回認證結果
    model-->>controller: 傳回認證結果
    controller-->>view: 傳回認證結果
    view-->>user: 顯示認證結果
{{</*/mermaid*/>}}
``` 

**輸出結果** 

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: 輸入 ID/PW
    view->>controller: ajax 查詢
    controller->>model: 認證請求
    model->>database: 發出 SQL
    database-->>model: 傳回 SQL 結果
    model-->>controller: 傳回請求結果
    controller-->>view: 傳回 ajax 查詢結果
    view-->>user: 顯示認證結果
{{</mermaid>}}

就是這樣。

### 參考
- [mermaid.js 官網](https://mermaid.js.org/#/)
- [可以預覽 mermaid 語法的展示網站](https://mermaid.live/)
