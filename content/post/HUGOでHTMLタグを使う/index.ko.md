---
title: "Hugo Markdown에서 원시 HTML 허용하기"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "YAML·TOML·JSON 설정 예시와 보안상 주의점, 이 옵션을 활성화하면 안 되는 경우를 함께 살펴봅니다."
---

Hugo의 Goldmark Markdown 렌더러는 기본적으로 원시 HTML을 렌더링하지 않습니다. 필요하다면 사이트 설정에서 `markup.goldmark.renderer.unsafe`를 `true`로 지정합니다. Hugo는 YAML, TOML, JSON 설정 파일을 지원합니다. 예를 들어 `hugo.yaml`에서는 다음과 같습니다.

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

`hugo.toml`에서는 다음과 같습니다.

```toml
[markup.goldmark.renderer]
  unsafe = true
```

`hugo.json`에서는 다음과 같이 설정합니다.

```json
{
  "markup": {
    "goldmark": {
      "renderer": {
        "unsafe": true
      }
    }
  }
}
```

기본값은 `false`입니다. `unsafe: true`는 Markdown의 원시 HTML을 출력에 포함시키며 Hugo의 콘텐츠 신뢰 경계를 약화합니다. 신뢰할 수 없는 작성자나 외부 입력의 Markdown을 처리하는 사이트에서는 활성화하지 마세요. 직접 관리하고 검토할 수 있는 콘텐츠에 한해 영향을 이해한 뒤 사용하세요. 복잡한 레이아웃에는 shortcode나 HTML 콘텐츠 파일이 더 적합할 수 있습니다.

참고: [마크업 설정](https://gohugo.io/configuration/markup/) · [Hugo 보안 모델](https://gohugo.io/about/security/)
