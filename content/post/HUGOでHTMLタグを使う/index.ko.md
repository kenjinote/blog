---




title: "HUGO에서 HTML 태그 사용하기"
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["블로그 운영"]
---





HUGO의 기본 설정에서는 게시물 내에 HTML 태그를 사용할 수 없게 되어 있지만, config.toml에 아래와 같이 기재하면 사용할 수 있게 됩니다.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

참고: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
