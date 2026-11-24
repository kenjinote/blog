---
title: "CSS 변수로 Hugo PaperMod 색상 사용자 지정하기"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "확장 CSS로 PaperMod의 라이트·다크 색상 변수를 재정의하고 텍스트 대비를 확인합니다."
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod 색상은 CSS 사용자 지정 속성(변수)으로 조정할 수 있습니다. 테마 파일을 직접 수정하는 대신 사이트의 `assets/css/extended/`에 재정의 파일을 두면 테마 업데이트 후에도 변경 사항을 유지하기 쉽습니다. 아래 예시는 따뜻한 라이트 팔레트와 다크 팔레트를 정의하며, 색상은 사이트에 맞게 조정하세요.

## 다크 모드와 현재 변수

현재 PaperMod는 `html` 요소에 `data-theme="dark"`를 설정해 다크 모드를 전환합니다. `.dark`만 대상으로 하는 예전 코드는 이 테마 선택자에 적용되지 않을 수 있습니다. `--hljs-bg`도 현재 코드 블록 배경 변수가 아니며, 현재 이름은 `--code-block-bg`입니다.

```css
/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme="dark"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
```

## 텍스트 대비

이 예시의 일반 텍스트 색상 `--primary`와 `--content`는 배경과 충분히 대비됩니다. `--primary`와 `--theme`의 대비는 라이트 모드에서 약 10.4:1, 다크 모드에서 약 13.4:1입니다. 일반 텍스트의 WCAG 2.2 AA 기준은 4.5:1이며, 구문 강조 색상, 링크, 테두리와 다른 상태는 별도로 확인해야 합니다.

## 확장 CSS 추가 및 확인

사이트 루트에 `assets/css/extended/theme-colors.css`로 저장하세요. PaperMod FAQ는 `assets/css/extended/`의 CSS가 테마 스타일과 함께 묶인다고 설명합니다. Hugo를 실행하고 라이트/다크 전환, 카드, 본문, 인라인 코드, 코드 블록, 링크를 확인하세요.

## 범위

이 팔레트는 예시이며 모든 텍스트, 이미지, 인터랙티브 요소의 접근성을 보장하지 않습니다. 구문 강조 색상은 `--code-block-bg`와 별도로 정의되므로 코드 블록 배경을 바꾼 뒤 코드 가독성을 다시 점검하세요.

## 참고 자료

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
