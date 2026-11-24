---
title: "使用 reflog 復原 git reset 前的提交"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "復原", "取消"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "透過 reflog 找到先前的 HEAD，先用分支保存，再了解 --hard 的風險。"
---

# 使用 reflog 復原 git reset 前的提交

若本機 reflog 仍保留 reset 前提交的參照，有時可以復原。檢查 `git reflog --date=local` 並選擇正確的 `HEAD@{n}`；下方的 `HEAD@{1}` 僅為範例。

`git reset --hard` 會捨棄受追蹤檔案中的未提交變更。請先備份要保留的工作，並使用尚不存在的救援分支名稱。reflog 無法復原 hard reset 已捨棄的未提交編輯。若歷史已共享，請先與協作者協調，通常可考慮 `git revert`。

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

請將 `HEAD@{1}` 換成選定的 reflog 編號，並將 `rescue-before-reset` 換成新的分支名稱。先檢查提交並確認分支已建立，再執行最後一個命令。

## 參考資料

[git reset 官方手冊](https://git-scm.com/docs/git-reset)

[git reflog 官方手冊](https://git-scm.com/docs/git-reflog)
