---
title: '尝试使用mermaid.js'
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["AI・技术"]
---

## mermaid.js是什么

mermaid.js 是一个 JavaScript 库，可以使用基于文本的独特语法（Mermaid 语法）进行编写，从而以图形方式显示复杂的图表，如流程图、图表、甘特图等。
GitHub、Qiita、Notion 等各种服务也都采用了它。这次，我们将尝试在 hugo 中使用 mermaid.js。

## 在 hugo 中启用 mermaid.js

步骤如下。

1. 在 layouts/partials/extend_footer.html 中添加以下内容。

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
※ 仅在使用 if 语句且 `mermaid: true` 时才加载 `mermaid.min.js`。该库大约有 3MB，出乎意料地大。

3. 创建 assets/js/load-mermaid.js。此过程用于初始化以及在动态切换主题时进行重绘。

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
这里的原始代码参考了以下内容。
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. 修改 header.html 中主题切换时的处理流程

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

4. 创建 layouts/shortcodes/mermaid.html

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

以上，mermaid.js 的使用准备工作就完成了。

## 尝试使用 mermaid.js

1. 在文章的定义中添加以下内容

```dtd
marmaid: true
```

2. 在文章正文中添加以下内容

**流程图**

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[开始] -->|条件1| B(条件2)
    B --> C{条件3}
    C -->|条件4| D[结束]
{{</*/mermaid*/>}}
```

**输出结果**

{{<mermaid align="center">}}
graph TD
    A[开始] -->|条件1| B(条件2)
    B --> C{条件3}
    C -->|条件4| D[结束]
{{</mermaid>}}

**甘特图**

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    需求定义 :done,      a, 2024-05-25, 5d
    基本设计 :done,      b, after a,    5d
    详细设计 :done,      c, after b,    5d
    开发    :active,    d, after c,    10d
    单元测试 :crit,      e, after d,    5d
    集成测试 :           f, after e,    5d
    系统测试 :           g, after f,    5d
    发布 :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

**输出结果**

{{<mermaid align="center">}}
gantt
    section Project
    需求定义 :done,      a, 2024-05-25, 5d
    基本设计 :done,      b, after a,    5d
    详细设计 :done,      c, after b,    5d
    开发    :active,    d, after c,    10d
    单元测试 :crit,      e, after d,    5d
    集成测试 :           f, after e,    5d
    系统测试 :           g, after f,    5d
    发布 :milestone, h, after g,    1d
{{</mermaid>}}


**时序图**

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: 输入账号/密码
    view->>controller: 认证请求
    controller->>model: 认证请求
    model->>database: 认证请求
    database-->>model: 返回认证结果
    model-->>controller: 返回认证结果
    controller-->>view: 返回认证结果
    view-->>user: 显示认证结果
{{</*/mermaid*/>}}
``` 

**输出结果**

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: 输入账号/密码
    view->>controller: ajax请求
    controller->>model: 认证请求
    model->>database: 执行SQL
    database-->>model: 返回SQL结果
    model-->>controller: 返回认证请求结果
    controller-->>view: 返回ajax请求结果
    view-->>user: 显示认证结果
{{</mermaid>}}

以上。

### 参考
- [mermaid.js 官网](https://mermaid.js.org/#/)
- [可预览 mermaid 语法的演示网站](https://mermaid.live/)
