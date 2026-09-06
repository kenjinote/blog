---
title: "Essayer mermaid.js"
slug: "mermaid.jsを試してみる"
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["IA et Technologie"]
---

## Qu'est-ce que mermaid.js

mermaid.js est une bibliothèque JavaScript qui vous permet d'afficher graphiquement des diagrammes complexes tels que des organigrammes, des diagrammes et des diagrammes de Gantt en écrivant une syntaxe originale basée sur du texte (syntaxe Mermaid).
Il est également adopté dans divers services tels que GitHub, Qiita et Notion. Cette fois, nous allons essayer d'utiliser mermaid.js dans hugo.

## Activer mermaid.js dans hugo

Les étapes sont les suivantes :

1. Ajoutez ce qui suit dans layouts/partials/extend_footer.html.

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
※ `mermaid.min.js` n'est chargé que lorsque `mermaid: true` est défini dans la condition if. Cette bibliothèque pèse environ 3 Mo et est étonnamment volumineuse.

3. Créez assets/js/load-mermaid.js. Ce processus est utilisé pour initialiser et redessiner dynamiquement lorsque le thème est modifié.

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
Le code de base pour cela a été référencé à partir de ce qui suit :
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. Modifiez le processus lors du changement de thèmes dans header.html

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

4. Créez layouts/shortcodes/mermaid.html

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

Avec les étapes ci-dessus, la préparation pour utiliser mermaid.js est terminée.

## Essayer mermaid.js

1. Ajoutez ce qui suit à la définition de l'article

```dtd
marmaid: true
```

2. Ajoutez ce qui suit au corps de l'article

**Organigramme** 

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[Début] -->|Condition 1| B(Condition 2)
    B --> C{Condition 3}
    C -->|Condition 4| D[Fin]
{{</*/mermaid*/>}}
```

**Résultat de la sortie** 

{{<mermaid align="center">}}
graph TD
    A[Début] -->|Condition 1| B(Condition 2)
    B --> C{Condition 3}
    C -->|Condition 4| D[Fin]
{{</mermaid>}}

**Diagramme de Gantt** 

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    Définition des exigences :done,      a, 2024-05-25, 5d
    Conception de base       :done,      b, after a,    5d
    Conception détaillée     :done,      c, after b,    5d
    Fabrication              :active,    d, after c,    10d
    Test unitaire            :crit,      e, after d,    5d
    Test d'intégration       :           f, after e,    5d
    Test système             :           g, after f,    5d
    Version                  :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

**Résultat de la sortie** 

{{<mermaid align="center">}}
gantt
    section Project
    Définition des exigences :done,      a, 2024-05-25, 5d
    Conception de base       :done,      b, after a,    5d
    Conception détaillée     :done,      c, after b,    5d
    Fabrication              :active,    d, after c,    10d
    Test unitaire            :crit,      e, after d,    5d
    Test d'intégration       :           f, after e,    5d
    Test système             :           g, after f,    5d
    Version                  :milestone, h, after g,    1d
{{</mermaid>}}


**Diagramme de séquence** 

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: Entrer ID/PW
    view->>controller: Demande d'authentification
    controller->>model: Demande d'authentification
    model->>database: Demande d'authentification
    database-->>model: Renvoyer le résultat de l'authentification
    model-->>controller: Renvoyer le résultat de l'authentification
    controller-->>view: Renvoyer le résultat de l'authentification
    view-->>user: Afficher le résultat de l'authentification
{{</*/mermaid*/>}}
``` 

**Résultat de la sortie** 

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: Entrer ID/PW
    view->>controller: requête ajax
    controller->>model: Demande d'authentification
    model->>database: Émission de SQL
    database-->>model: Renvoyer le résultat SQL
    model-->>controller: Renvoyer le résultat de la demande
    controller-->>view: Renvoyer le résultat de la requête ajax
    view-->>user: Afficher le résultat de l'authentification
{{</mermaid>}}

C'est tout.

### Références
- [Site officiel de mermaid.js](https://mermaid.js.org/#/)
- [Site de démonstration où vous pouvez prévisualiser la syntaxe Mermaid](https://mermaid.live/)
