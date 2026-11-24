---
title: "Windows 11：啟動後顯示縮放變更時的檢查方式"

slug: "多螢幕で毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["多螢幕", "DPI", "控制台"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Windows 11 顯示縮放變更時，可暫時停用快速啟動進行排查；本文說明測試方式、如何復原，並指出原因未必在此。"
---
快速啟動會在關機時將核心工作階段和裝置驅動程式狀態儲存至休眠檔案，以加快下次啟動。停用後開機可能變慢。Microsoft 文件並未確認它會造成多螢幕縮放重置；以下步驟僅供暫時排查，並非已證實的修復方法。

## 暫時變更設定

1. 開啟控制台並選取「電源選項」。
2. 開啟「選擇電源按鈕的行為」。
3. 點選「變更目前無法使用的設定」（可能需要管理員權限）。
4. 取消勾選「開啟快速啟動（建議選項）」，再點選「儲存變更」。
5. 選擇「關機」後再按電源鍵開機，檢查縮放是否保留。測試時要先關機再開機；「重新啟動」不會使用快速啟動。

若沒有改善，請回到同一頁重新啟用快速啟動。選單名稱可能因 Windows 語言和更新而異。

## Microsoft 參考資料

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)
