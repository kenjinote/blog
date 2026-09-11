---







title: '실수로 실행한 git reset을 취소하는 방법｜커밋 복원 절차'
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "복원", "취소"]
draft: false
image: "img.webp"
categories: ["도구・개발 환경"]
description: 'Git에서 실수로 ''git reset''을 실행해버렸을 때, 리셋을 취소하고 원래의 커밋 상태로 복원하는 방법을 해설합니다. ''git reflog''를 사용하여 커밋 ID를 확인하고, 올바르게 상태를 되돌리는 절차를 알기 쉽게 소개합니다.'
---







# git reset을 취소하는 방법
git commit을 수행한 후, 실수로 git reset을 실행해버린 경우, git reset을 취소하는 방법(git commit 시의 상태를 복원하는 방법)을 소개합니다.

1. `git reflog`로 리셋 전의 커밋 ID를 확인
2. `git reset --hard HEAD@{숫자}`로 리셋 전의 상태로 되돌림

이상, git reset을 취소하는 방법이었습니다.
