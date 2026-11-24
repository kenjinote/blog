---







title: "reflog로 git reset 전 커밋 복구하기"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "복원", "취소"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "reflog에서 이전 HEAD를 찾고 브랜치로 보존한 뒤 --hard의 주의점을 확인합니다."
---








# reflog로 git reset 전 커밋 복구하기

reset 전 커밋의 참조가 로컬 reflog에 남아 있으면 복구할 수 있습니다. `git reflog --date=local`을 확인해 올바른 `HEAD@{n}` 항목을 고르세요. 아래의 `HEAD@{1}`은 예시입니다.

`git reset --hard`는 추적 중인 파일의 미커밋 변경을 버립니다. 필요한 작업을 먼저 백업하고 아직 없는 복구 브랜치 이름을 사용하세요. hard reset으로 이미 잃은 미커밋 편집은 reflog로 복구할 수 없습니다. 공유된 이력은 협업자와 조정하고 보통 `git revert`를 고려하세요.

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

`HEAD@{1}`을 선택한 reflog 항목으로, `rescue-before-reset`을 새 브랜치 이름으로 바꾸세요. 커밋을 확인하고 브랜치가 만들어진 것을 확인한 뒤 마지막 명령을 실행하세요.

## 참고 자료

[git reset 공식 설명서](https://git-scm.com/docs/git-reset)

[git reflog 공식 설명서](https://git-scm.com/docs/git-reflog)
