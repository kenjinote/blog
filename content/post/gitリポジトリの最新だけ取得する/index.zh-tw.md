---
title: '如何以淺層歷史複製 Git 儲存庫'
slug: "git儲存庫の最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "儲存庫", "指令"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '了解 git clone --depth 1 取得的內容、分支選擇方式，以及之後如何取得更多歷史。'
---

# 以淺層歷史複製 Git 儲存庫

`git clone --depth 1` 會從所選分支的最新提交開始，建立歷史深度為 1 的淺層複製。預設選取遠端儲存庫的預設分支。這會減少傳輸的提交歷史，但目前檔案及必要的 Git 物件仍會下載，因此含有大型檔案的儲存庫仍可能很大。

```sh
git clone --depth 1 <repository-url>
```

若要指定分支，請寫出分支名稱：

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

之後可以繼續取得更多歷史，例如：

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

請將 `<directory>` 和 `<branch>` 換成實際名稱。使用 `--depth` 時，除非另行覆寫，Git 也會啟用 `--single-branch`。關於 `--unshallow` 等選項，請參閱 [`git clone`](https://git-scm.com/docs/git-clone) 與 [`git fetch`](https://git-scm.com/docs/git-fetch) 官方手冊。
