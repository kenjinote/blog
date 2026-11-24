---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25
title: '用「hide」指令一秒啟動秀丸編輯器！Windows 實用設定方法'
slug: "指令「hide」で秀丸編輯器を立ち上げる方法"
tags: ["指令", "Hidemaru 編輯器", "登錄檔"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "說明如何在 Windows 10/11 註冊 App Paths 名稱，並從「執行」或使用 start hide 啟動秀丸編輯器。"
---

## 以下介紹如何使用「hide」指令啟動 Hidemaru 編輯器。

注意：此方法已在 `Windows 10/11` 上測試過。

1. 打開「登錄編輯程式」。
2. 導覽至 `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`。
3. 在 `App Paths` 下建立一個名為 `hide.exe` 的機碼。 **在此機碼名稱中， `.exe` 前面的部分即為指令名稱。**
4. 將 `hide.exe` 機碼的 `(預設值)` 設為 Hidemaru 編輯器執行檔的路徑。在我的環境中是 `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`。
5. Path 值為選用項目。只有應用程式需要額外 DLL 搜尋目錄時才設定；ShellExecuteEx 啟動時會將其加入處理程序 PATH。
6. 按下 Win + R 開啟「執行」，輸入 hide。在命令提示字元中使用 start hide；本文說明的方式不是直接輸入 hide。

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
如果您將上述內容儲存為 `.reg` 檔案並執行它，這些設定將被新增至登錄檔中。

此 .reg 範例只會為目前使用者註冊。請將路徑換成秀丸實際的執行檔路徑。若要為所有使用者註冊，請將 HKEY_CURRENT_USER 改為 HKEY_LOCAL_MACHINE，並以系統管理員權限匯入。


## 參考資料

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)
