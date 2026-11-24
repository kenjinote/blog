---
title: "PaperMod 글 목록에서 커버 이미지 크기와 위치 바꾸기"
slug: "PaperModの이미지の配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "PaperMod의 확장 CSS와 CSS Grid를 사용해 글 카드의 커버 이미지를 줄이고 요약 옆에 배치합니다."
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

이 예시는 PaperMod 글 목록 카드의 커버 이미지를 줄여 제목 아래, 요약 옆에 배치합니다. 테마에 포함된 CSS나 템플릿을 직접 고치지 않고 사이트의 확장 CSS를 사용합니다. PaperMod 클래스 선택자를 사용하므로 테마 업데이트 후 브라우저에서 결과를 확인하세요.

## 확장 CSS 추가

사이트 루트에 `assets/css/extended/custom.css`를 만드세요. PaperMod는 이 폴더의 CSS를 테마 스타일과 함께 포함합니다. CSS Grid는 기존 HTML 구조를 바꾸지 않고 화면 배치만 조정합니다.

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## 좁은 화면 조정

좁은 화면에서는 요약을 읽기 쉽도록 열 너비와 간격을 줄이세요. 150px와 중단점을 디자인에 맞게 조절할 수 있습니다. `height: auto`는 이미지 비율을 유지합니다. 이미지를 같은 모양으로 자를 경우에만 `aspect-ratio`와 `object-fit: cover`를 추가하세요.

## 테마 파일 직접 수정 피하기

PaperMod 문서에서 `blank.css`는 확장 CSS 폴더에 파일이 없을 때 사용하는 빈 자리표시자입니다. 테마의 `post-entry.css`를 수정하거나 주석 처리된 `/* width: 100%; */`를 지울 필요가 없습니다. CSS 주석을 삭제해도 스타일은 변하지 않습니다. HTML 구조를 바꿔야 한다면 사이트의 `layouts/`에 템플릿을 복사해 재정의할 수 있지만, 테마 업데이트 때 복사본을 직접 관리해야 합니다.

## 레이아웃 확인

Hugo를 실행하고 홈, 태그, 카테고리 목록을 넓은 화면과 좁은 화면에서 확인하세요. 이미지, 제목, 요약, 메타 정보가 겹치지 않고 카드 전체 링크도 동작해야 합니다. 테마 업데이트로 클래스나 HTML이 바뀌면 CSS를 맞추세요. 이 예시는 글 목록의 커버에만 적용되며 본문 이미지는 바꾸지 않습니다.

## 참고 자료

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
