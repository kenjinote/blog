---
title: "Пробуем mermaid.js"
slug: "mermaid.jsを試してみる"
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["ИИ и Технологии"]
---

## Что такое mermaid.js

mermaid.js — это библиотека JavaScript, которая позволяет писать текстовый синтаксис (синтаксис Mermaid) для графического отображения сложных диаграмм, таких как блок-схемы, графы и диаграммы Ганта.
Она также используется в различных сервисах, таких как GitHub, Qiita и Notion. На этот раз мы попробуем включить использование mermaid.js в hugo.

## Включение mermaid.js в hugo

Шаги следующие:

1. Добавьте следующее в layouts/partials/extend_footer.html.

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
※ `mermaid.min.js` загружается только если `mermaid: true` в условии if. Эта библиотека довольно большая, около 3 МБ.

3. Создайте assets/js/load-mermaid.js. Этот процесс используется для инициализации и перерисовки при динамическом переключении темы.

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
Исходный код основан на следующем:
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. Измените обработку переключения темы в header.html

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

4. Создайте layouts/shortcodes/mermaid.html

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

Теперь mermaid.js готов к использованию.

## Использование mermaid.js

1. Добавьте следующее в определение статьи

```dtd
marmaid: true
```

2. Добавьте следующее в тело статьи

 **Блок-схема** 

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[Начало] -->|Условие 1| B(Условие 2)
    B --> C{Условие 3}
    C -->|Условие 4| D[Конец]
{{</*/mermaid*/>}}
```

 **Результат** 

{{<mermaid align="center">}}
graph TD
    A[Начало] -->|Условие 1| B(Условие 2)
    B --> C{Условие 3}
    C -->|Условие 4| D[Конец]
{{</mermaid>}}

 **Диаграмма Ганта** 

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    Определение требований :done,      a, 2024-05-25, 5d
    Базовое проектирование :done,      b, after a,    5d
    Детальное проектирование :done,      c, after b,    5d
    Производство    :active,    d, after c,    10d
    Модульное тестирование :crit,      e, after d,    5d
    Интеграционное тестирование :           f, after e,    5d
    Системное тестирование :           g, after f,    5d
    Релиз :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

 **Результат** 

{{<mermaid align="center">}}
gantt
    section Project
    Определение требований :done,      a, 2024-05-25, 5d
    Базовое проектирование :done,      b, after a,    5d
    Детальное проектирование :done,      c, after b,    5d
    Производство    :active,    d, after c,    10d
    Модульное тестирование :crit,      e, after d,    5d
    Интеграционное тестирование :           f, after e,    5d
    Системное тестирование :           g, after f,    5d
    Релиз :milestone, h, after g,    1d
{{</mermaid>}}


 **Диаграмма последовательности** 

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: Ввод ID/PW
    view->>controller: Запрос аутентификации
    controller->>model: Запрос аутентификации
    model->>database: Запрос аутентификации
    database-->>model: Возврат результата
    model-->>controller: Возврат результата
    controller-->>view: Возврат результата
    view-->>user: Показ результата
{{</*/mermaid*/>}}
``` 

 **Результат** 

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: Ввод ID/PW
    view->>controller: ajax запрос
    controller->>model: Запрос аутентификации
    model->>database: Выполнение SQL
    database-->>model: Возврат результата SQL
    model-->>controller: Возврат результата аутентификации
    controller-->>view: Возврат результата ajax запроса
    view-->>user: Показ результата аутентификации
{{</mermaid>}}

На этом всё.

### Ссылки
- [Официальный сайт mermaid.js](https://mermaid.js.org/#/)
- [Демо-сайт для предпросмотра синтаксиса mermaid](https://mermaid.live/)
