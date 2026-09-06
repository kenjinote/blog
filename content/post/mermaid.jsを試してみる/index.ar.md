---
title: "تجربة mermaid.js"
slug: "mermaid.jsを試してみる"
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["الذكاء الاصطناعي والتكنولوجيا"]
---

## ما هو mermaid.js

mermaid.js هي مكتبة JavaScript تتيح لك كتابة بنية مخصصة تعتمد على النص (صيغة Mermaid) لعرض المخططات المعقدة رسومياً مثل المخططات الانسيابية والرسوم البيانية ومخططات جانت.
يتم استخدامها أيضاً في خدمات مختلفة مثل GitHub و Qiita و Notion. في هذه المرة، سنحاول تمكين استخدام mermaid.js في hugo.

## تمكين استخدام mermaid.js في hugo

الخطوات كالتالي:

1. أضف التالي إلى layouts/partials/extend_footer.html.

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
※ يتم تحميل `mermaid.min.js` فقط إذا كان `mermaid: true` في عبارة if. هذه المكتبة كبيرة نوعاً ما، حوالي 3 ميغابايت.

3. قم بإنشاء assets/js/load-mermaid.js. يتم استخدام هذه العملية للتهيئة وإعادة الرسم عند تبديل السمة ديناميكياً.

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
تمت الإشارة إلى الكود الأصلي هنا:
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. قم بتعديل عملية تبديل السمة في header.html

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

4. قم بإنشاء layouts/shortcodes/mermaid.html

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

الآن أصبح mermaid.js جاهزاً للاستخدام.

## استخدام mermaid.js

1. أضف التالي إلى تعريف المقالة

```dtd
marmaid: true
```

2. أضف التالي إلى نص المقالة

 **المخطط الانسيابي** 

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[البداية] -->|الشرط 1| B(الشرط 2)
    B --> C{الشرط 3}
    C -->|الشرط 4| D[النهاية]
{{</*/mermaid*/>}}
```

 **النتيجة** 

{{<mermaid align="center">}}
graph TD
    A[البداية] -->|الشرط 1| B(الشرط 2)
    B --> C{الشرط 3}
    C -->|الشرط 4| D[النهاية]
{{</mermaid>}}

 **مخطط جانت** 

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    تحديد المتطلبات :done,      a, 2024-05-25, 5d
    التصميم الأساسي :done,      b, after a,    5d
    التصميم التفصيلي :done,      c, after b,    5d
    التصنيع    :active,    d, after c,    10d
    اختبار الوحدة :crit,      e, after d,    5d
    اختبار التكامل :           f, after e,    5d
    الاختبار الشامل :           g, after f,    5d
    الإصدار :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

 **النتيجة** 

{{<mermaid align="center">}}
gantt
    section Project
    تحديد المتطلبات :done,      a, 2024-05-25, 5d
    التصميم الأساسي :done,      b, after a,    5d
    التصميم التفصيلي :done,      c, after b,    5d
    التصنيع    :active,    d, after c,    10d
    اختبار الوحدة :crit,      e, after d,    5d
    اختبار التكامل :           f, after e,    5d
    الاختبار الشامل :           g, after f,    5d
    الإصدار :milestone, h, after g,    1d
{{</mermaid>}}


 **مخطط التسلسل** 

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: إدخال المعرف/كلمة المرور
    view->>controller: طلب المصادقة
    controller->>model: طلب المصادقة
    model->>database: طلب المصادقة
    database-->>model: إرجاع نتيجة المصادقة
    model-->>controller: إرجاع نتيجة المصادقة
    controller-->>view: إرجاع نتيجة المصادقة
    view-->>user: عرض نتيجة المصادقة
{{</*/mermaid*/>}}
``` 

 **النتيجة** 

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: إدخال المعرف/كلمة المرور
    view->>controller: استعلام ajax
    controller->>model: طلب المصادقة
    model->>database: إصدار SQL
    database-->>model: إرجاع نتيجة SQL
    model-->>controller: إرجاع نتيجة طلب المصادقة
    controller-->>view: إرجاع نتيجة استعلام ajax
    view-->>user: عرض نتيجة المصادقة
{{</mermaid>}}

هذا كل شيء.

### المراجع
- [موقع mermaid.js الرسمي](https://mermaid.js.org/#/)
- [موقع تجريبي لمعاينة صيغة mermaid](https://mermaid.live/)
