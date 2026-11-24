---







title: '얕은 기록으로 Git 저장소를 복제하는 방법'
slug: "git리포지토리の最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "저장소", "명령어"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'git clone --depth 1이 가져오는 기록, 브랜치 선택, 나중에 기록을 더 가져오는 방법을 설명합니다.'
---

# 얕은 기록으로 Git 저장소 복제하기

`git clone --depth 1`은 선택한 브랜치의 최신 커밋부터 기록 깊이가 1인 얕은 복제본을 만듭니다. 기본적으로 원격 저장소의 기본 브랜치를 선택합니다. 전송되는 커밋 기록은 줄어들지만 현재 파일과 필요한 Git 객체는 내려받으므로, 큰 파일이 있는 저장소는 여전히 클 수 있습니다.

```sh
git clone --depth 1 <repository-url>
```

브랜치를 직접 선택하려면 이름을 지정합니다.

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

나중에 다음처럼 기록을 더 가져올 수 있습니다.

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

`<directory>`와 `<branch>`는 실제 이름으로 바꾸세요. `--depth`는 별도로 재정의하지 않는 한 `--single-branch`도 뜻합니다. `--unshallow`를 포함한 자세한 내용은 공식 [`git clone`](https://git-scm.com/docs/git-clone), [`git fetch`](https://git-scm.com/docs/git-fetch) 설명서를 참고하세요.
