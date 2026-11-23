---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23



title: 'reveal.js 사용법: HTML과 Markdown으로 프레젠테이션 자료 작성'
slug: "HTMLで프레젠테이션資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "프레젠테이션"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'HTML과 Markdown으로 직관적으로 프레젠테이션을 작성할 수 있는 도구 ''reveal.js''의 설치 및 기본적인 사용법을 해설합니다. 애니메이션이나 PDF 출력에 대응하며, Git 등의 버전 관리와도 궁합이 뛰어난 활용법을 소개합니다.'
---




# HTML로 프레젠테이션 자료를 만드는 방법

reveal.js는 HTML과 Markdown을 사용한 프레젠테이션 작성 도구로, 다음과 같은 기능이 있습니다.

- 수식, 애니메이션, 스와이프 조작 등 다양한 프레젠테이션 기능
- 테마 및 레이아웃 커스터마이즈 가능
- 마우스, 키보드, 터치패드 등 여러 디바이스를 지원하는 내비게이션 기능
- 슬라이드 자동 재생 및 비디오 포함 등 고급 기능 제공
- PDF 형식으로 내보내기 가능

이러한 기능을 통해 사용자는 쉽게 인터랙티브하고 매력적인 프레젠테이션을 만들 수 있습니다.

# reveal.js 설치 및 사용법

가장 간단한 사용법은 다음 페이지에서 ZIP 파일을 통째로 다운로드하여 압축을 푸는 것입니다.

1. [https://revealjs.com/installation](https://revealjs.com/installation)을 열고, 링크에서 `master.zip`을 다운로드한다
2. 압축을 푼 폴더 내의 index.html을 브라우저로 연다
3. index.html을 수정하여 자신의 프레젠테이션 자료를 만든다

※demo.html에 데모용 HTML 코드가 작성되어 있으므로 참고할 수 있습니다.

# 활용 방법

만든 프레젠테이션 자료는 그대로 웹 페이지로 공개하거나, PDF로 내보낼 수 있습니다.
또한, 프레젠테이션 소스가 텍스트이므로 버전 관리 시스템으로 관리하기가 용이합니다.

마크다운 형식으로 프레젠테이션 자료를 작성하는 것도 가능한 것 같습니다.

# 기본 슬라이드 만들기

가장 간단한 방법은 최신 Basic Setup ZIP을 내려받아 압축을 풀고 `index.html`을 편집하는 것입니다. 아래 HTML 예시처럼 각 슬라이드를 `<section>`으로 감쌉니다. 샘플 파일에는 필요한 스타일과 초기화 코드가 들어 있습니다.

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# Markdown으로 슬라이드 작성

포함된 Markdown 플러그인을 사용하면 HTML 파일 안에 Markdown을 작성할 수 있습니다. `---`로 가로 슬라이드를 나눕니다. 아래 예시를 `index.html`에 추가하세요. 외부 Markdown 파일을 불러오려면 로컬 웹 서버가 필요합니다.

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# 개발 환경 설정

로컬 서버나 소스 개발 도구가 필요하면 공식 Full Setup을 사용하세요. 다음 명령을 실행한 뒤 브라우저에서 `http://localhost:8000`을 여세요.

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# PDF로 내보내기

URL 끝에 `?print-pdf`를 추가합니다. Chrome 또는 Chromium의 인쇄 화면에서 PDF로 저장, 가로 방향, 여백 없음, 배경 그래픽 사용을 선택하세요. 공식 안내에서 확인된 브라우저는 Chrome과 Chromium입니다.

# 발표자 노트

`S` 키를 누르면 별도 창에서 발표자 보기가 열립니다. 슬라이드의 `<aside class="notes">` 안에 노트를 작성할 수 있습니다. 로컬 발표자 보기에는 웹 서버가 필요합니다.

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# 공식 문서

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

スライドに使う画像・動画の利用条件を確認し、公開資料に機密情報や非公開の発表者ノートが含まれていないか確認してください。
