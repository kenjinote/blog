---
title: "Experimentando o mermaid.js"
slug: "mermaid.jsを試してみる"
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["IA e Tecnologia"]
---

## O que é o mermaid.js

mermaid.js é uma biblioteca JavaScript que permite exibir graficamente diagramas complexos, como fluxogramas, diagramas e gráficos de Gantt, escrevendo uma sintaxe original baseada em texto (sintaxe Mermaid).
Também é adotado em vários serviços como GitHub, Qiita e Notion. Desta vez, vamos tentar usar o mermaid.js no hugo.

## Habilitando o mermaid.js no hugo

Os passos são os seguintes:

1. Adicione o seguinte em layouts/partials/extend_footer.html.

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
※ O `mermaid.min.js` é carregado apenas quando `mermaid: true` está definido na declaração if. Esta biblioteca tem cerca de 3MB e é surpreendentemente grande.

3. Crie assets/js/load-mermaid.js. Este processo é usado para inicializar e redesenhar dinamicamente quando o tema é alterado.

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
O código base para isso foi referenciado a partir do seguinte:
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. Modifique o processo ao alterar temas no header.html

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

4. Crie layouts/shortcodes/mermaid.html

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

Com os passos acima, a preparação para usar o mermaid.js está completa.

## Tentando o mermaid.js

1. Adicione o seguinte à definição do artigo

```dtd
marmaid: true
```

2. Adicione o seguinte ao corpo do artigo

**Fluxograma** 

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[Início] -->|Condição 1| B(Condição 2)
    B --> C{Condição 3}
    C -->|Condição 4| D[Fim]
{{</*/mermaid*/>}}
```

**Resultado da saída** 

{{<mermaid align="center">}}
graph TD
    A[Início] -->|Condição 1| B(Condição 2)
    B --> C{Condição 3}
    C -->|Condição 4| D[Fim]
{{</mermaid>}}

**Gráfico de Gantt** 

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    Definição de Requisitos :done,      a, 2024-05-25, 5d
    Design Básico          :done,      b, after a,    5d
    Design Detalhado       :done,      c, after b,    5d
    Fabricação            :active,    d, after c,    10d
    Teste Unitário         :crit,      e, after d,    5d
    Teste de Integração    :           f, after e,    5d
    Teste de Sistema       :           g, after f,    5d
    Lançamento            :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

**Resultado da saída** 

{{<mermaid align="center">}}
gantt
    section Project
    Definição de Requisitos :done,      a, 2024-05-25, 5d
    Design Básico          :done,      b, after a,    5d
    Design Detalhado       :done,      c, after b,    5d
    Fabricação            :active,    d, after c,    10d
    Teste Unitário         :crit,      e, after d,    5d
    Teste de Integração    :           f, after e,    5d
    Teste de Sistema       :           g, after f,    5d
    Lançamento            :milestone, h, after g,    1d
{{</mermaid>}}


**Diagrama de Sequência** 

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: Inserir ID/PW
    view->>controller: Solicitação de autenticação
    controller->>model: Solicitação de autenticação
    model->>database: Solicitação de autenticação
    database-->>model: Retornar resultado da autenticação
    model-->>controller: Retornar resultado da autenticação
    controller-->>view: Retornar resultado da autenticação
    view-->>user: Exibir resultado da autenticação
{{</*/mermaid*/>}}
``` 

**Resultado da saída** 

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: Inserir ID/PW
    view->>controller: consulta ajax
    controller->>model: Solicitação de autenticação
    model->>database: Emissão de SQL
    database-->>model: Retornar resultado SQL
    model-->>controller: Retornar resultado da solicitação
    controller-->>view: Retornar resultado da consulta ajax
    view-->>user: Exibir resultado da autenticação
{{</mermaid>}}

Isso é tudo.

### Referências
- [Site oficial do mermaid.js](https://mermaid.js.org/#/)
- [Site de demonstração onde você pode visualizar a sintaxe Mermaid](https://mermaid.live/)
