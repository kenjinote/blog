---




title: 'Hugo에서 HTML 태그를 활성화하는 방법(config.toml 설정)'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["블로그 운영"]
description: '정적 사이트 생성기 Hugo의 Markdown 기사 내에서 HTML 태그를 직접 작성하여 사용할 수 있도록 하는 방법을 해설합니다. config.toml에 markup.goldmark.renderer의 unsafe 설정을 추가하기만 하면 완료됩니다.'
---





HUGO의 기본 설정에서는 게시물 내에 HTML 태그를 사용할 수 없게 되어 있지만, config.toml에 아래와 같이 기재하면 사용할 수 있게 됩니다.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

참고: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
