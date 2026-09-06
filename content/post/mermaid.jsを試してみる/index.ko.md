---







title: "'mermaid.js를 사용해 보기'"
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["AI・테크놀로지"]
---








## mermaid.js란

mermaid.js는 JavaScript 라이브러리로, 텍스트 기반의 독자적인 구문(Mermaid 표기법)을 작성하여 플로우차트나 다이어그램, 간트 차트 등 복잡한 도표를 그래픽으로 표시할 수 있습니다.
GitHub나 Qiita, Notion 등 다양한 서비스에서도 채택되어 있습니다. 이번에는 hugo에서 mermaid.js를 사용할 수 있도록 해보겠습니다.

## hugo에서 mermaid.js를 사용할 수 있게 하기

순서는 다음과 같습니다.

1. layouts/partials/extend_footer.html에 다음을 추가합니다.

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
※if문으로 `mermaid: true`로 설정한 경우에만 `mermaid.min.js`를 불러오도록 하고 있습니다. 이 라이브러리는 3MB 정도로 의외로 큽니다.

3. assets/js/load-mermaid.js를 생성합니다. 이 처리는 초기화 및 동적으로 테마가 전환되었을 때 다시 그리기 위해 사용됩니다.

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
여기 바탕이 되는 코드는 다음을 참고했습니다.
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. header.html의 테마 전환 시의 처리를 수정합니다.

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

4. layouts/shortcodes/mermaid.html을 생성합니다.

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

이상으로 mermaid.js를 사용할 준비가 완료되었습니다.

## mermaid.js 사용해 보기

1. 게시글 정의에 다음을 추가합니다.

```dtd
marmaid: true
```

2. 게시글 본문에 다음을 추가합니다.

**플로우차트**

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[시작] -->|조건1| B(조건2)
    B --> C{조건3}
    C -->|조건4| D[종료]
{{</*/mermaid*/>}}
```

**출력 결과**

{{<mermaid align="center">}}
graph TD
    A[시작] -->|조건1| B(조건2)
    B --> C{조건3}
    C -->|조건4| D[종료]
{{</mermaid>}}

**간트 차트**

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    요구사항 정의 :done,      a, 2024-05-25, 5d
    기본 설계 :done,      b, after a,    5d
    상세 설계 :done,      c, after b,    5d
    구현    :active,    d, after c,    10d
    단위 테스트 :crit,      e, after d,    5d
    통합 테스트 :           f, after e,    5d
    종합 테스트 :           g, after f,    5d
    릴리스 :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

**출력 결과**

{{<mermaid align="center">}}
gantt
    section Project
    요구사항 정의 :done,      a, 2024-05-25, 5d
    기본 설계 :done,      b, after a,    5d
    상세 설계 :done,      c, after b,    5d
    구현    :active,    d, after c,    10d
    단위 테스트 :crit,      e, after d,    5d
    통합 테스트 :           f, after e,    5d
    종합 테스트 :           g, after f,    5d
    릴리스 :milestone, h, after g,    1d
{{</mermaid>}}


**시퀀스 다이어그램**

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: ID/PW 입력
    view->>controller: 인증 요청
    controller->>model: 인증 요청
    model->>database: 인증 요청
    database-->>model: 인증 결과 반환
    model-->>controller: 인증 결과 반환
    controller-->>view: 인증 결과 반환
    view-->>user: 인증 결과 표시
{{</*/mermaid*/>}}
``` 

**출력 결과**

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: ID/PW 입력
    view->>controller: ajax 문의
    controller->>model: 인증 요청
    model->>database: SQL 실행
    database-->>model: SQL 결과 반환
    model-->>controller: 인증 요청 결과 반환
    controller-->>view: ajax 문의 결과 반환
    view-->>user: 인증 결과 표시
{{</mermaid>}}

이상입니다.

### 참고
- [mermaid.js 공식 사이트](https://mermaid.js.org/#/)
- [mermaid 구문을 미리 볼 수 있는 데모 사이트](https://mermaid.live/)
