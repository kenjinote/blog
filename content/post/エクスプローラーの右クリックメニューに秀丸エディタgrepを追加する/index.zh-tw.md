---
title: '在 Windows 右鍵選單中新增秀丸編輯器 grep 的方法'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "檔案總管の右鍵選單に秀丸編輯器grepを追加する"
tags: ["Hidemaru Editor", "檔案總管", "右鍵選單", "grep", "登錄檔"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '介紹在 Windows 10/11 檔案總管的右鍵選單中，新增秀丸編輯器 grep 功能的實用設定步驟。淺顯易懂地解說使用登錄檔登錄檔的簡單方法。'
---
以下將介紹如何在 Windows 10/11 的檔案總管右鍵選單中新增 Hidemaru Editor 的 grep 功能。

 **※以下步驟會修改登錄檔，請自行承擔風險。**

此檔案只會為目前使用者新增資料夾選單項目，不會為所有檔案新增「以秀丸開啟」，也不會修改整台電腦的設定。匯入前請用記事本開啟，核對並依秀丸實際安裝位置修改執行檔路徑。若目標機碼已存在，請先在登錄編輯程式選取並透過「檔案」>「匯出」備份。Windows 11 的舊式命令可能位於「顯示更多選項」。Windows 10 已於 2025 年 10 月 14 日終止支援。 隨附的解除檔只會刪除這些目前使用者項目，不會還原舊版的全電腦登錄。若曾匯入舊檔案，請在登錄編輯程式中另行檢查並移除其機碼。
## 步驟

1. 開啟下方連結，並儲存至任意資料夾。

[秀丸レジストリ登録.reg](秀丸レジストリ登録.reg)

[移除秀丸登錄項目](秀丸レジストリ解除.reg)

2. 點擊兩下 `秀丸レジストリ登録.reg` 檔案以將其新增至登錄檔。

## 參考

- [秀丸grepをフォルダの右クリックメニューから行う](https://aimek-developer.blogspot.com/2019/02/grep.html)

## 官方參考資料

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
