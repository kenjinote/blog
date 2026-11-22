---
title: "使用 Google 官方工具更新或重新安裝 Pixel 軟體"
slug: "Android(Google Pixel)端末の還原手順"
tags: ["Android", "Google Pixel", "還原", "疑難排解"]
draft: false
image: "pixel_restore_eyecatch_1788588727945.webp"
categories: ["programming"]
description: "介紹 Google Pixel Update and Software Repair 官方工具、支援裝置、Update 與 Reinstall 的差異，以及資料遺失風險。"
date: "2025-02-28T01:20:41+09:00"
lastmod: "2026-11-23T19:00:00+09:00"
---

# 使用 Google 官方工具更新或重新安裝 Pixel 軟體

> **資料遺失重要提醒（2026 年 11 月 23 日確認）：** Google 工具提供「Update（更新）」與「Reinstall（重新安裝）」。更新有時可在不恢復原廠設定的情況下安裝最新軟體；Reinstall 會重設手機並清除資料。操作前請先備份，並確認手機使用的 Google 帳戶憑證。Google 目前說明列出的支援範圍為 Pixel 4a 及後續機型，包括 Fold。請先查看最新支援情況與工具畫面提示。

[Pixel Update and Software Repair](https://pixelrepair.withgoogle.com/) 是 Google 為支援的 Pixel 裝置提供的軟體更新或重新安裝工具。它無法保證修復所有不斷重新啟動或無法開機的問題。重設手機前，請先嘗試 Google 的[官方故障排除方法](https://support.google.com/pixelphone/answer/4582729)，例如重新啟動、檢查 Android 更新、使用安全模式及檢查儲存空間。

## 1. 確認裝置支援

開啟[官方工具](https://pixelrepair.withgoogle.com/)，查看裝置可用的操作。支援範圍與選項可能因機型或地區而異，請遵循工具與 [Google 官方說明](https://support.google.com/pixelphone/answer/4596836)中的最新資訊。

## 2. 開始前準備

- 如果還能操作手機，請備份重要資料，並確認 Google 帳戶密碼與螢幕鎖定憑證。
- 準備支援資料傳輸的 USB 線和電腦，盡量直接連接電腦。
- 若要恢復原廠設定，Google 一般說明建議先將電量充至至少 70%。若工具有其他提示，請以工具為準。
- 若 Windows 無法辨識手機，可視需要查看 Google 官方的 [USB 驅動程式說明](https://developer.android.com/studio/run/win-usb)。

## 3. 連接裝置並依畫面操作

1. 在電腦上開啟 [Pixel Update and Software Repair](https://pixelrepair.withgoogle.com/)。
2. 若工具提示關機，請依指示操作。目前說明是同時長按電源鍵與音量增加鍵關機。
3. 同時按住電源鍵與音量降低鍵約 3 秒，進入 Fastboot 模式。若機型步驟不同，請遵循畫面提示。
4. 以 USB 連接手機，按下 **Connect device**，選擇正確裝置並確認名稱後允許瀏覽器連線。
5. 選擇 **Update** 或 **Reinstall**。更新有時可保留資料；Reinstall 會恢復原廠設定並清除資料，請只在備份後選擇。工具顯示處理中時不要拔除連接線。

若工具無法連線或手機仍無法啟動，請勿反覆安裝。請查看 Google 的[官方 Pixel 支援說明](https://support.google.com/pixelphone/answer/4596836)。

## 總結

操作前查看工具和 Google 說明的最新資訊。Update 與 Reinstall 對資料的影響不同；Reinstall 會清除資料。重設前請先備份並確認帳戶憑證。
