---
title: 'Trying out mermaid.js'
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["AI & Technology"]
---

## What is mermaid.js?

mermaid.js is a JavaScript library that allows you to graphically display complex charts and diagrams, such as flowcharts, diagrams, and Gantt charts, using its own text-based syntax (Mermaid syntax).
It is also adopted by various services like GitHub, Qiita, and Notion. This time, we will make mermaid.js usable in hugo.

## Making mermaid.js usable in hugo

The procedure is as follows:

1. Add the following to layouts/partials/extend_footer.html.

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
* `mermaid.min.js` is loaded only when `mermaid: true` is set via the if statement. This library is about 3MB and unexpectedly large.

2. Create assets/js/load-mermaid.js. This process is used for initialization and to redraw when the theme is dynamically switched.

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
The base code was referenced from below:
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. Modify the theme switching process in header.html

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

4. Create layouts/shortcodes/mermaid.html

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

The preparation to use mermaid.js is now complete.

## Trying out mermaid.js

1. Add the following to the article's front matter

```dtd
mermaid: true
```

2. Add the following to the article body

**Flowchart**

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[Start] -->|Condition 1| B(Condition 2)
    B --> C{Condition 3}
    C -->|Condition 4| D[End]
{{</*/mermaid*/>}}
```

**Output Result**

{{<mermaid align="center">}}
graph TD
    A[Start] -->|Condition 1| B(Condition 2)
    B --> C{Condition 3}
    C -->|Condition 4| D[End]
{{</mermaid>}}

**Gantt Chart**

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    Requirement Definition :done,      a, 2024-05-25, 5d
    Basic Design :done,      b, after a,    5d
    Detailed Design :done,      c, after b,    5d
    Manufacturing    :active,    d, after c,    10d
    Unit Testing :crit,      e, after d,    5d
    Integration Testing :           f, after e,    5d
    System Testing :           g, after f,    5d
    Release :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

**Output Result**

{{<mermaid align="center">}}
gantt
    section Project
    Requirement Definition :done,      a, 2024-05-25, 5d
    Basic Design :done,      b, after a,    5d
    Detailed Design :done,      c, after b,    5d
    Manufacturing    :active,    d, after c,    10d
    Unit Testing :crit,      e, after d,    5d
    Integration Testing :           f, after e,    5d
    System Testing :           g, after f,    5d
    Release :milestone, h, after g,    1d
{{</mermaid>}}


**Sequence Diagram**

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: ID/PW Input
    view->>controller: Authentication Request
    controller->>model: Authentication Request
    model->>database: Authentication Request
    database-->>model: Return Authentication Result
    model-->>controller: Return Authentication Result
    controller-->>view: Return Authentication Result
    view-->>user: Display Authentication Result
{{</*/mermaid*/>}}
``` 

**Output Result**

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: ID/PW Input
    view->>controller: ajax query
    controller->>model: Authentication Request
    model->>database: Issue SQL
    database-->>model: Return SQL Result
    model-->>controller: Return Authentication Request Result
    controller-->>view: Return ajax query result
    view-->>user: Display Authentication Result
{{</mermaid>}}

That is all.

### References
- [mermaid.js Official Site](https://mermaid.js.org/#/)
- [Demo site to preview mermaid syntax](https://mermaid.live/)
