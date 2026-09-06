---
title: "mermaid.js का परीक्षण"
slug: "mermaid.jsを試してみる"
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["AI और प्रौद्योगिकी"]
---

## mermaid.js क्या है

mermaid.js एक JavaScript लाइब्रेरी है जो आपको फ्लोचार्ट, डायग्राम और गैंट चार्ट जैसे जटिल डायग्राम को टेक्स्ट-आधारित मूल सिंटैक्स (Mermaid सिंटैक्स) लिखकर ग्राफिक रूप से प्रदर्शित करने की अनुमति देती है।
इसे GitHub, Qiita और Notion जैसी विभिन्न सेवाओं में भी अपनाया गया है। इस बार, हम hugo में mermaid.js का उपयोग करने का प्रयास करेंगे।

## hugo में mermaid.js को सक्षम करना

चरण इस प्रकार हैं:

1. layouts/partials/extend_footer.html में निम्नलिखित जोड़ें।

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
※ `mermaid.min.js` केवल तभी लोड होता है जब if स्टेटमेंट में `mermaid: true` सेट किया जाता है। यह लाइब्रेरी लगभग 3MB की है और आश्चर्यजनक रूप से बड़ी है।

3. assets/js/load-mermaid.js बनाएं। इस प्रक्रिया का उपयोग थीम बदलने पर इनिशियलाइज़ करने और गतिशील रूप से फिर से बनाने के लिए किया जाता है।

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
इसके लिए आधार कोड निम्नलिखित से संदर्भित किया गया था:
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. header.html में थीम बदलते समय प्रक्रिया को संशोधित करें

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

4. layouts/shortcodes/mermaid.html बनाएं

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

उपरोक्त चरणों के साथ, mermaid.js का उपयोग करने की तैयारी पूरी हो गई है।

## mermaid.js का प्रयास करना

1. लेख की परिभाषा में निम्नलिखित जोड़ें

```dtd
marmaid: true
```

2. लेख के मुख्य भाग में निम्नलिखित जोड़ें

**फ्लोचार्ट** 

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[प्रारंभ] -->|शर्त 1| B(शर्त 2)
    B --> C{शर्त 3}
    C -->|शर्त 4| D[अंत]
{{</*/mermaid*/>}}
```

**आउटपुट परिणाम** 

{{<mermaid align="center">}}
graph TD
    A[प्रारंभ] -->|शर्त 1| B(शर्त 2)
    B --> C{शर्त 3}
    C -->|शर्त 4| D[अंत]
{{</mermaid>}}

**गैंट चार्ट** 

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    आवश्यकता परिभाषा :done,      a, 2024-05-25, 5d
    मूल डिज़ाइन      :done,      b, after a,    5d
    विस्तृत डिज़ाइन   :done,      c, after b,    5d
    निर्माण          :active,    d, after c,    10d
    यूनिट टेस्ट       :crit,      e, after d,    5d
    एकीकरण परीक्षण   :           f, after e,    5d
    सिस्टम टेस्ट      :           g, after f,    5d
    रिलीज़           :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

**आउटपुट परिणाम** 

{{<mermaid align="center">}}
gantt
    section Project
    आवश्यकता परिभाषा :done,      a, 2024-05-25, 5d
    मूल डिज़ाइन      :done,      b, after a,    5d
    विस्तृत डिज़ाइन   :done,      c, after b,    5d
    निर्माण          :active,    d, after c,    10d
    यूनिट टेस्ट       :crit,      e, after d,    5d
    एकीकरण परीक्षण   :           f, after e,    5d
    सिस्टम टेस्ट      :           g, after f,    5d
    रिलीज़           :milestone, h, after g,    1d
{{</mermaid>}}


**अनुक्रम आरेख** 

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: ID/PW दर्ज करें
    view->>controller: प्रमाणीकरण अनुरोध
    controller->>model: प्रमाणीकरण अनुरोध
    model->>database: प्रमाणीकरण अनुरोध
    database-->>model: प्रमाणीकरण परिणाम वापस करें
    model-->>controller: प्रमाणीकरण परिणाम वापस करें
    controller-->>view: प्रमाणीकरण परिणाम वापस करें
    view-->>user: प्रमाणीकरण परिणाम प्रदर्शित करें
{{</*/mermaid*/>}}
``` 

**आउटपुट परिणाम** 

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: ID/PW दर्ज करें
    view->>controller: ajax पूछताछ
    controller->>model: प्रमाणीकरण अनुरोध
    model->>database: SQL जारी करना
    database-->>model: SQL परिणाम वापस करें
    model-->>controller: अनुरोध परिणाम वापस करें
    controller-->>view: ajax पूछताछ परिणाम वापस करें
    view-->>user: प्रमाणीकरण परिणाम प्रदर्शित करें
{{</mermaid>}}

बस इतना ही।

### संदर्भ
- [mermaid.js आधिकारिक साइट](https://mermaid.js.org/#/)
- [डेमो साइट जहाँ आप mermaid सिंटैक्स का पूर्वावलोकन कर सकते हैं](https://mermaid.live/)
