---
date: 2022-09-11T22:59:52+09:00
lastmod: 2026-11-23
title: 'Hugo 내장 쇼트코드: 미디어 삽입, 버전 차이와 개인정보 보호'
slug: "HUGOで使える쇼트コード"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Hugo에 포함된 쇼트코드와 버전별 차이, 미디어 삽입의 개인정보 보호 설정을 알아봅니다.'
---

# Hugo 내장 쇼트코드: 미디어 삽입, 버전 차이와 개인정보 보호

쇼트코드는 Markdown 본문에서 템플릿 기능을 호출하는 문법입니다. Hugo 내장 기능 외에도 테마와 모듈이 제공하는 쇼트코드가 있고, 프로젝트에서 직접 만들 수도 있습니다. 이름과 인수는 Hugo 버전에 따라 다르므로 사용하는 버전의 공식 문서를 확인하세요.

## Hugo 내장 쇼트코드

Flickr는 Hugo 코어의 내장 쇼트코드가 아닙니다. 프로젝트에서 `flickr` 호출이 작동한다면 테마, 모듈 또는 `layouts/_shortcodes/flickr.html` 같은 사용자 정의 템플릿이 제공하는 것입니다. 이름만 보고 기본 제공 기능이라고 가정하지 마세요.

현재 공식 목록에는 `details`, `figure`, `highlight`, `instagram`, `param`, `qr`, `ref`, `relref`, `vimeo`, `x`, `youtube` 등이 있습니다. 전체 목록과 인수는 공식 페이지를 확인하세요.

## 미디어 예시

### YouTube

동영상 URL의 `v` 매개변수에 있는 ID를 지정합니다.

`{{</* youtube 0RKpf3rK57I */>}}`

### X (Hugo 0.141.0 이상)

게시물 URL에 있는 사용자 이름과 게시물 ID를 지정합니다.

`{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}`

### 이전 Twitter (Hugo 0.139.0)

Hugo 0.139.0에서는 다음과 같이 이름이 지정된 인수를 사용합니다.

`{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Instagram

Instagram 게시물 URL의 마지막 부분이 게시물 ID입니다.

`{{</* instagram CxOWiQNP2MO */>}}`

### Vimeo

Vimeo 동영상 URL 끝에 있는 숫자 ID를 사용합니다.

`{{</* vimeo 19899678 */>}}`

## 버전 차이 주의

이 블로그의 빌드는 Hugo 0.139.0으로 고정되어 있습니다. 이 버전에서 X(구 Twitter)의 내장 이름은 `twitter`이며 `user`와 `id`라는 이름 지정 인수가 필요합니다. `x` 쇼트코드는 Hugo 0.141.0에서 추가되었고, 이후 버전에서 `twitter`는 폐기 예정으로 표시되었습니다. 최신 문서의 예제를 복사하기 전에 프로젝트의 Hugo 버전을 확인하세요.

## 개인정보 보호 설정

YouTube, X, Instagram, Vimeo 삽입은 방문자의 브라우저를 해당 서비스에 연결할 수 있습니다. Hugo의 `privacy` 설정으로 삽입을 끄거나 가능한 경우 간소 모드를 사용할 수 있습니다. YouTube의 `privacyEnhanced` 설정은 방문자가 영상을 재생할 때까지 정보 저장을 제한합니다.

YouTube 개인정보 보호 강화:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

X 간소 모드:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

이전 Twitter (Hugo 0.139.0):

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

사용 중인 Hugo 버전의 공식 문서에서 각 설정의 이름을 확인하세요.

Instagram 간소 모드에서도 이미지는 Instagram 서버에서 직접 불러옵니다. Vimeo 간소 모드는 미리보기 이미지를 가져오며 클릭하면 새 탭에서 Vimeo를 엽니다. 이런 모드도 제3자 요청을 완전히 없애지는 않습니다.

삽입 내용을 공개하기 전에 제공업체에 대한 요청, 쿠키 동작, 독자가 있는 지역의 개인정보 보호 요건을 확인하세요.

## 문법을 텍스트로 표시하기

문서에서 쇼트코드 문법을 그대로 표시하려면 아래 예시처럼 구분자에 `/*`와 `*/`를 추가해 이스케이프합니다.

`{{</*/* youtube 0RKpf3rK57I */*/>}}`

## 공식 문서

- [쇼트코드 개요](https://gohugo.io/content-management/shortcodes/)
- [내장 쇼트코드](https://gohugo.io/shortcodes/)
- [YouTube](https://gohugo.io/shortcodes/youtube/)
- [X](https://gohugo.io/shortcodes/x/)
- [Instagram](https://gohugo.io/shortcodes/instagram/)
- [Vimeo](https://gohugo.io/shortcodes/vimeo/)
- [개인정보 보호 설정](https://gohugo.io/configuration/privacy/)
