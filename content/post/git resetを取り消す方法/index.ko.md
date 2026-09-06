---




title: "git reset을 취소하는 방법"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "복원", "취소"]
draft: false
image: "img.png"
categories: ["도구・개발 환경"]
---




# git reset을 취소하는 방법
git commit을 수행한 후, 실수로 git reset을 실행해버린 경우, git reset을 취소하는 방법(git commit 시의 상태를 복원하는 방법)을 소개합니다.

1. `git reflog`로 리셋 전의 커밋 ID를 확인
2. `git reset --hard HEAD@{숫자}`로 리셋 전의 상태로 되돌림

이상, git reset을 취소하는 방법이었습니다.
