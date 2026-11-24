---
title: "Windows 11で起動時にDPI設定が変わる場合の確認事項"

slug: "マルチモニタで毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["マルチモニタ", "DPI", "コントロールパネル"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Windows 11でマルチモニタの拡大縮小設定が変わる場合に、高速スタートアップを一時的に無効化して確認する手順です。原因と断定せず、戻し方と注意点も説明します。"
---
高速スタートアップは、シャットダウン時にカーネルやデバイスドライバーの状態を休止状態ファイルに保存して、次回の起動を速める機能です。これを無効にすると通常の起動が遅くなることがあります。Microsoftの資料は、この機能がマルチモニタのDPIリセットを引き起こすとは確認していません。以下は原因を切り分けるための一時的な確認方法です。

## 設定を一時的に変更する

1. コントロールパネルを開き、[電源オプション]を選択します。
2. [電源ボタンの動作を選択する]を開きます。
3. [現在利用可能ではない設定を変更します]をクリックします（管理者権限が必要な場合があります）。
4. [高速スタートアップを有効にする（推奨）]のチェックを外し、[変更の保存]をクリックします。
5. PCを[シャットダウン]してから電源を入れ直し、設定が保持されるか確認します。テストでは[再起動]ではなく、シャットダウン後の起動を使います。

改善しない場合は同じ画面で高速スタートアップを再度有効に戻します。表示名はWindowsの言語や更新状況によって異なることがあります。

## Microsoftの参考資料

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)
