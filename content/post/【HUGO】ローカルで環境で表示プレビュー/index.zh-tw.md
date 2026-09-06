---
title: "【HUGO】本機環境顯示預覽"
slug: "【HUGO】本機環境顯示預覽"
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["部落格營運"]
---
# 安裝 HUGO

## 下載
[下載 HUGO](https://github.com/gohugoio/hugo/releases)

從上述網站，下載並解壓縮符合您環境的 Windows 模組。
就我而言，我下載了「hugo_0.102.3_Windows-64bit.zip」。

## 解壓縮
解壓縮下載的 zip 檔案，將其中的 hugo.exe 複製到您建立的資料夾中，例如 C:\bin。

## 登錄到環境變數
將其登錄到環境變數中，以便從任何位置執行 hugo.exe。
以下是在 Windows 11 上的操作，但您應該可以透過類似的步驟進行登錄：

1. 按 Win+Pause 鍵開啟版本資訊
2. 點擊「進階系統設定」
3. 點擊「環境變數」
4. 選擇 Path，然後點擊「編輯」
5. 點擊「新增」，在新的一行輸入「C:\bin」，然後點擊「確定」關閉對話框
 
# 預覽部落格
在命令提示字元中，移動到 HUGO 部落格的資料夾，然後執行以下命令。

`hugo server -D`

執行結果如下。（-D 是顯示草稿文章的選項。）

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
  Pages            | 39
  Paginator pages  |  0
  Non-page files   |  7
  Static files     |  0
  Processed images |  0
  Aliases          | 13
  Sitemaps         |  1
  Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

由於地址在執行時會顯示（在上述範例中為 `http://localhost:1313/`），請將該地址複製到您的瀏覽器中。
每次儲存檔案時，預覽都會自動更新。
要結束預覽，請在命令提示字元中輸入 Ctrl+C。
