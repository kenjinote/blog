---



title: "'git에서 태그 삭제하기'"
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.png"
categories: ["도구 및 개발 환경"]
---



# 로컬 태그 삭제하기

1. `git tag` 로 로컬에 존재하는 태그를 확인한다.
2. `git tag -d v0.1.0` 으로 태그를 삭제한다. (`v0.1.0` 부분에는 삭제하고 싶은 태그를 지정한다)

# 원격 태그 삭제하기

1. `git ls-remote --tags` 로 원격에 존재하는 태그를 확인한다.
2. `git push origin --delete v0.1.0` 으로 원격에 존재하는 태그를 삭제한다. (`v0.1.0` 부분에는 삭제하고 싶은 태그를 지정한다)

## 참고
[git에서 tag를 원격과 로컬에서 삭제하는 방법！](https://qumeru.com/magazine/528)
