---
title: "Hugo PaperMod에서 Twitter Card(X 카드) 설정하기"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "PaperMod 공식 설정에 맞춰 X 카드 이미지를 지정하고 생성된 HTML과 X 게시물 작성 화면에서 미리보기를 확인합니다."
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod는 Open Graph와 Twitter Card 메타데이터를 생성할 수 있습니다. 테마 버전과 사용자 지정 레이아웃에 따라 결과가 달라질 수 있으므로 예시만 믿지 말고 배포된 HTML을 확인하세요.

## 사이트 전체 설정

PaperMod의 SEO 메타데이터는 프로덕션 빌드에서 활성화됩니다. 사이트 환경을 production으로 설정하세요.

```toml
[params]
  env = "production"
```

사이트 전체의 기본 이미지는 `static` 아래에 두고 여기에 지정합니다. 글에서 별도 이미지를 제공하지 않을 때 사용할 수 있습니다. 배포된 사이트에서 실제 URL도 확인하세요.

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## 글별 이미지

글별 이미지는 Page Bundle의 파일을 `cover.image`에 지정합니다. `relative: true`는 Bundle 기준 상대 경로를 뜻합니다. PaperMod 문서에서는 cover 이미지가 우선이며, 없으면 페이지의 `images` 목록, 이어서 조건에 맞는 Bundle 이미지가 사용될 수 있습니다.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## 본문에서 커버 숨기기

PaperMod 변수 문서에 따르면 `cover.hidden: true`는 글 화면에서 커버를 숨기면서 구조화 메타데이터에는 남깁니다. 소셜 카드에만 이미지를 사용하려는 경우 유용합니다. 테마 fork나 사용자 지정 템플릿에서는 생성 HTML을 확인하세요.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## 카드 유형과 이미지 크기

PaperMod가 `summary_large_image`만 지원한다거나 800×418이 고정 크기라는 과거 설명은 일반화할 수 없습니다. 카드 종류는 테마 버전이나 사이트 템플릿에 따라 달라집니다. 가로형 공유 이미지에는 1200×630(약 1.90:1)을 실용적인 디자인 기준으로 삼을 수 있지만 X의 표시를 보장하는 값은 아닙니다.

## HTML과 미리보기 확인

프로덕션 설정으로 빌드한 뒤 글 HTML에서 `twitter:card`, `twitter:image`, `og:image`, 제목과 설명을 확인하세요. 이미지 URL은 HTTPS로 로그인 없이 공개 접근 가능해야 합니다. X는 2022년 Card Validator의 미리보기를 제거하고 게시물 작성 화면을 안내했습니다. URL을 작성 화면에 붙여 게시하지 않고 미리보기를 확인하세요. 캐시 갱신에는 시간이 걸릴 수 있습니다.

2026-11-24에 링크한 PaperMod 문서와 X 개발자 포럼을 확인했습니다. fork, 템플릿 재정의, X의 변경으로 출력이 달라질 수 있습니다.

## 참고 자료

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)
