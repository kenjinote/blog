---







title: "'Probando mermaid.js'"
slug: "mermaid.jsを試してみる"
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["IA y Tecnología"]
---








## ¿Qué es mermaid.js?

mermaid.js es una biblioteca de JavaScript que permite describir diagramas mediante una sintaxis basada en texto (sintaxis de Mermaid) para representar gráficamente diagramas complejos como diagramas de flujo, diagramas de Gantt, etc.
También se utiliza en varios servicios como GitHub, Qiita y Notion. En esta ocasión, configuraremos hugo para poder usar mermaid.js.

## Habilitar mermaid.js en hugo

Los pasos son los siguientes:

1. Añadir lo siguiente a layouts/partials/extend_footer.html:

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
* Solo se carga `mermaid.min.js` si se establece `mermaid: true` en la condición if. Esta biblioteca pesa aproximadamente 3MB, lo cual es sorprendentemente grande.

3. Crear assets/js/load-mermaid.js. Este proceso se utiliza para inicializar y volver a dibujar cuando el tema cambia dinámicamente.

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
El código original en el que me basé fue tomado de la siguiente referencia:
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. Modificar el procesamiento al cambiar de tema en header.html

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

4. Crear layouts/shortcodes/mermaid.html

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

Con esto, la preparación para usar mermaid.js está completa.

## Probando mermaid.js

1. Añadir lo siguiente a la definición del artículo:

```dtd
marmaid: true
```

2. Añadir lo siguiente al cuerpo del artículo:

**Diagrama de flujo**

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[Inicio] -->|Condición 1| B(Condición 2)
    B --> C{Condición 3}
    C -->|Condición 4| D[Fin]
{{</*/mermaid*/>}}
```

**Resultado de salida**

{{<mermaid align="center">}}
graph TD
    A[Inicio] -->|Condición 1| B(Condición 2)
    B --> C{Condición 3}
    C -->|Condición 4| D[Fin]
{{</mermaid>}}

**Diagrama de Gantt**

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    Definición de requisitos :done,      a, 2024-05-25, 5d
    Diseño básico :done,      b, after a,    5d
    Diseño detallado :done,      c, after b,    5d
    Implementación    :active,    d, after c,    10d
    Pruebas unitarias :crit,      e, after d,    5d
    Pruebas de integración :           f, after e,    5d
    Pruebas del sistema :           g, after f,    5d
    Lanzamiento :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

**Resultado de salida**

{{<mermaid align="center">}}
gantt
    section Project
    Definición de requisitos :done,      a, 2024-05-25, 5d
    Diseño básico :done,      b, after a,    5d
    Diseño detallado :done,      c, after b,    5d
    Implementación    :active,    d, after c,    10d
    Pruebas unitarias :crit,      e, after d,    5d
    Pruebas de integración :           f, after e,    5d
    Pruebas del sistema :           g, after f,    5d
    Lanzamiento :milestone, h, after g,    1d
{{</mermaid>}}


**Diagrama de secuencia**

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: Ingreso de ID/PW
    view->>controller: Petición de autenticación
    controller->>model: Petición de autenticación
    model->>database: Petición de autenticación
    database-->>model: Devolución de resultado de autenticación
    model-->>controller: Devolución de resultado de autenticación
    controller-->>view: Devolución de resultado de autenticación
    view-->>user: Mostrar resultado de autenticación
{{</*/mermaid*/>}}
``` 

**Resultado de salida**

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: Ingreso de ID/PW
    view->>controller: Consulta ajax
    controller->>model: Petición de autenticación
    model->>database: Emisión de SQL
    database-->>model: Devolución de resultado SQL
    model-->>controller: Devolución de resultado de petición de autenticación
    controller-->>view: Devolución de resultado de consulta ajax
    view-->>user: Mostrar resultado de autenticación
{{</mermaid>}}

Eso es todo.

### Referencias
- [Sitio oficial de mermaid.js](https://mermaid.js.org/#/)
- [Sitio de demostración para previsualizar la sintaxis de mermaid](https://mermaid.live/)
