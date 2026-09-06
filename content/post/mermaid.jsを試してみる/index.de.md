---
title: "mermaid.js ausprobieren"
slug: "mermaid.jsを試してみる"
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["KI und Technologie"]
---

## Was ist mermaid.js

mermaid.js ist eine JavaScript-Bibliothek, mit der Sie komplexe Diagramme wie Flussdiagramme, Diagramme und Gantt-Diagramme grafisch darstellen können, indem Sie eine textbasierte Original-Syntax (Mermaid-Syntax) schreiben.
Es wird auch in verschiedenen Diensten wie GitHub, Qiita und Notion übernommen. Dieses Mal werden wir versuchen, mermaid.js in hugo zu verwenden.

## mermaid.js in hugo aktivieren

Die Schritte sind wie folgt:

1. Fügen Sie Folgendes in layouts/partials/extend_footer.html hinzu.

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
※ `mermaid.min.js` wird nur geladen, wenn `mermaid: true` in der if-Anweisung festgelegt ist. Diese Bibliothek ist etwa 3 MB groß und überraschend groß.

3. Erstellen Sie assets/js/load-mermaid.js. Dieser Prozess wird zum Initialisieren und dynamischen Neuzeichnen verwendet, wenn das Thema geändert wird.

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
Der Basiscode dafür wurde aus Folgendem referenziert:
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. Ändern Sie den Prozess beim Ändern von Themen in header.html

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

4. Erstellen Sie layouts/shortcodes/mermaid.html

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

Mit den obigen Schritten ist die Vorbereitung zur Verwendung von mermaid.js abgeschlossen.

## mermaid.js ausprobieren

1. Fügen Sie Folgendes zur Artikeldefinition hinzu

```dtd
marmaid: true
```

2. Fügen Sie Folgendes zum Artikeltext hinzu

**Flussdiagramm** 

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[Start] -->|Bedingung 1| B(Bedingung 2)
    B --> C{Bedingung 3}
    C -->|Bedingung 4| D[Ende]
{{</*/mermaid*/>}}
```

**Ausgabeergebnis** 

{{<mermaid align="center">}}
graph TD
    A[Start] -->|Bedingung 1| B(Bedingung 2)
    B --> C{Bedingung 3}
    C -->|Bedingung 4| D[Ende]
{{</mermaid>}}

**Gantt-Diagramm** 

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    Anforderungsdefinition :done,      a, 2024-05-25, 5d
    Basisdesign            :done,      b, after a,    5d
    Detailliertes Design   :done,      c, after b,    5d
    Herstellung            :active,    d, after c,    10d
    Komponententest        :crit,      e, after d,    5d
    Integrationstest       :           f, after e,    5d
    Systemtest             :           g, after f,    5d
    Veröffentlichung       :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

**Ausgabeergebnis** 

{{<mermaid align="center">}}
gantt
    section Project
    Anforderungsdefinition :done,      a, 2024-05-25, 5d
    Basisdesign            :done,      b, after a,    5d
    Detailliertes Design   :done,      c, after b,    5d
    Herstellung            :active,    d, after c,    10d
    Komponententest        :crit,      e, after d,    5d
    Integrationstest       :           f, after e,    5d
    Systemtest             :           g, after f,    5d
    Veröffentlichung       :milestone, h, after g,    1d
{{</mermaid>}}


**Sequenzdiagramm** 

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: ID/PW eingeben
    view->>controller: Authentifizierungsanforderung
    controller->>model: Authentifizierungsanforderung
    model->>database: Authentifizierungsanforderung
    database-->>model: Authentifizierungsergebnis zurückgeben
    model-->>controller: Authentifizierungsergebnis zurückgeben
    controller-->>view: Authentifizierungsergebnis zurückgeben
    view-->>user: Authentifizierungsergebnis anzeigen
{{</*/mermaid*/>}}
``` 

**Ausgabeergebnis** 

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: ID/PW eingeben
    view->>controller: Ajax-Abfrage
    controller->>model: Authentifizierungsanforderung
    model->>database: SQL-Ausgabe
    database-->>model: SQL-Ergebnis zurückgeben
    model-->>controller: Anforderungsergebnis zurückgeben
    controller-->>view: Ajax-Abfrageergebnis zurückgeben
    view-->>user: Authentifizierungsergebnis anzeigen
{{</mermaid>}}

Das ist alles.

### Referenzen
- [Offizielle mermaid.js-Website](https://mermaid.js.org/#/)
- [Demo-Website, auf der Sie die Mermaid-Syntax in der Vorschau anzeigen können](https://mermaid.live/)
