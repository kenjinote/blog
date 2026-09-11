---




title: 'Hugo PaperMod 테마의 배색·색상 테마를 CSS로 변경하는 방법'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["블로그 운영"]
description: 'Hugo의 PaperMod 테마에서 전체 배색을 커스터마이징하는 방법을 설명합니다. 배경색, 텍스트 색상, 코드 블록 등의 스타일 정의가 포함된 CSS(blank.css)를 편집하여 원하는 색상 스킴을 적용하기 위한 구체적인 변수 설정 예를 소개합니다.'
---




PaperMod 테마의 색상을 변경했습니다. 변경 방법은 아래를 참고했습니다.

https://github.com/adityatelange/hugo-PaperMod/discussions/645

CSS 경로는 아래와 같습니다.

`themes/PaperMod/assets/css/extended/blank.css`

```css
:root {
    --entry: #fbf7ef;
    --primary: rgba(113, 103, 91, 1.00);
    --secondary: rgba(113, 103, 91, 0.95);
    --tertiary: rgba(113, 103, 91, 0.50);
    --content: rgba(113, 103, 91, 0.85);
    --hljs-bg: #34231B;
    --code-bg: #ebe4d7;
    --border: #fdfaf5;
    --theme: #fbf7ef;
}
.dark {
}
```

다크 모드는 일단 변경하지 않았습니다.
