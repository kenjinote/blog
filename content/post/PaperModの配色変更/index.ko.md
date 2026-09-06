---

title: "'PaperMod 색상 변경'"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.png"
categories: ["블로그 운영"]
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
