---
title: '【初學者適用】使用 TeamViewer 輕鬆進行遠端桌面連線的方法'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単遠端連線"
tags: ["TeamViewer", "指令", "遠端連線"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: '說明如何使用 TeamViewer 輕鬆進行遠端桌面連線。同時介紹從命令列指定 ID 和密碼，並透過捷徑自動化及簡化連線步驟的實用小技巧巧。'
---
## Windows 命令列連線

TeamViewer 官方 Windows 命令列文件指出，可透過命令提示字元、指令碼或捷徑啟動完整版 TeamViewer。

此範例會從安裝資料夾啟動 `TeamViewer.exe`。在 `<ID>` 填入連線對象的 ID，在 `<Password>` 填入密碼。如果 TeamViewer 安裝在其他位置，請替換執行檔路徑。

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

省略 `-p` 時，若可使用 Easy Access，TeamViewer 會採用該方式；否則會提示輸入密碼。

包含密碼的捷徑會以可讀形式儲存密碼。請勿分享，也不要放在他人可讀取的位置。若需要定期無人值守存取，可考慮將裝置指派至帳戶，並使用 Easy Access、允許清單及多重要素驗證，而非儲存密碼。

## 官方參考資料

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)
