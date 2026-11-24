---
title: 'Git에서 로컬 및 원격의 태그를 삭제하는 방법'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["git"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Git에서 불필요해진 태그(tag)를 삭제하는 방법을 간단하게 해설합니다. ''git tag -d''를 통한 로컬 환경에서의 태그 삭제부터, ''git push origin --delete''를 사용한 원격 리포지토리 상의 태그 삭제까지 망라합니다.'
---
# 로컬 태그 삭제하기

1. `git tag` 로 로컬에 존재하는 태그를 확인한다.
2. `git tag -d v0.1.0` 으로 태그를 삭제한다. (`v0.1.0` 부분에는 삭제하고 싶은 태그를 지정한다)

# 원격 태그 삭제하기

1. `git ls-remote --tags --refs origin` 로 원격에 존재하는 태그를 확인한다.
2. `git push origin --delete v0.1.0` 으로 원격에 존재하는 태그를 삭제한다. (`v0.1.0` 부분에는 삭제하고 싶은 태그를 지정한다)

원격 태그를 삭제해도 공동 작업자의 로컬 복사본은 자동으로 삭제되지 않습니다. 원격 사용자에게 영향을 주므로 실행 전에 대상을 확인하세요.

## 참고 자료
[git-tag](https://git-scm.com/docs/git-tag), [git-ls-remote](https://git-scm.com/docs/git-ls-remote), [git-push](https://git-scm.com/docs/git-push)
