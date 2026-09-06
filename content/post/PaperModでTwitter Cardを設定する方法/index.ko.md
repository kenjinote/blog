---

title: "'PaperMod에서 Twitter Card를 설정하는 방법'"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["블로그 운영"]
---

# 시작하며
PaperMod 테마는 Twitter Card를 지원합니다.
단, Twitter Card 설정은 `config.toml` 또는 각 게시물의 `*.md` 헤더 정보에 작성해야 합니다.
각 게시물과 `config.toml` 양쪽에 설정한 경우에는, 각 게시물의 헤더 정보가 우선됩니다.

# 설정 방법
## config.toml
`config.toml`에는 `[params]` 아래에 `images`라는 항목을 추가합니다.
`images`에는 Twitter Card에 표시할 이미지의 경로를 작성합니다.
이미지를 `static` 폴더에 배치할 경우에는 파일 이름만 지정하면 됩니다.

```
[params]
  images = ["twitter_card.jpg"]
```

폴더 구성
```
root
│  config.toml (여기에 작성)
├─content
│  └─posts
│      └─게시물 폴더
│         │  index.md (여기에 작성)
│         └─images
│             cover.png (여기에 배치)
└─static
    twitter_card.jpg (여기에 배치)
```

## 각 게시물의 헤더 정보
각 게시물의 헤더 정보에는 `cover` 아래에 `image`라는 항목을 추가합니다.
`relative`를 `true`로 하면, 게시물의 `*.md`로부터의 상대 경로로 지정할 수 있습니다.

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### 게시물 상단에는 표시하고 싶지 않은 경우
게시물 상단에 커버 이미지를 표시하고 싶지 않은 경우에는 `cover` 아래에 `hidden`이라는 항목을 추가하고 `true`로 설정합니다.
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# 이미지 크기에 대하여

현재 PaperMod의 사양상 Twitter Card의 크기는 `summary_large_image`만 지원하는 것 같습니다.
`summary_large_image`의 적절한 크기(해상도)는 여러 의견이 있지만 `800 x 418`(이미지 비율 1.91:1) 정도가 좋을 것 같습니다.

[참고 사이트1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[참고 사이트2](https://developers.facebook.com/docs/sharing/best-practices)


가능하다면, 이미지 크기를 리사이징하여 게시하는 것을 추천합니다.

# 설정 확인 방법
Twitter Card의 설정을 확인하려면 [Twitter Card Validator](https://cards-dev.twittercom/validator)를 이용합니다.
단, 제 환경에서는 미리보기가 잘 표시되지 않았기 때문에, 만약 미리보기가 표시되지 않는다면 비공개 계정 등을 이용해 게시 전에 한번 확인해 보는 것을 추천합니다.
