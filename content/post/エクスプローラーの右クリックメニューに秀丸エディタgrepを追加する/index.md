---
title: 'Windowsで右クリックメニューに秀丸エディタのgrepを追加する方法'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "エクスプローラーの右クリックメニューに秀丸エディタgrepを追加する"
tags: ["秀丸エディタ", "エクスプローラー", "右クリックメニュー", "grep", "レジストリ"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Windows 10/11のエクスプローラーの右クリックメニューに、秀丸エディタのgrep機能を追加する便利な設定手順を紹介。レジストリ登録ファイルを使った簡単な方法をわかりやすく解説します。'
---
Window 10/11でエクスプローラーの右クリックメニューに秀丸エディタのgrepを追加する方法を紹介します。

**※以下の手順ではレジストリを変更するため、自己責任でお願いします。**

この登録ファイルは現在のユーザーのフォルダー用メニューだけを追加し、全ファイルへの「秀丸で開く」項目やシステム全体の登録は行いません。取り込む前にメモ帳で開き、秀丸エディタの実際のインストール先に合わせて実行ファイルのパスを確認・修正してください。対象キーが既にある場合は、レジストリエディターで選択し、［ファイル］→［エクスポート］でバックアップしてから進めます。Windows 11では旧形式の項目が［その他のオプションを表示］にある場合があります。Windows 10は2025年10月14日にサポート終了済みです。 付属の解除ファイルが削除するのはこのユーザー単位の項目だけで、以前の全ユーザー向け登録は解除しません。以前の登録ファイルを使った場合は、追加された旧キーをレジストリエディターで個別に確認してください。
## 手順

1. 下記のリンクを開き、任意のフォルダに保存する。

[秀丸レジストリ登録.reg](秀丸レジストリ登録.reg)

[秀丸レジストリ解除.reg](秀丸レジストリ解除.reg)

2. `秀丸レジストリ登録.reg`ファイルをダブルクリックしてレジストリに追加する。

## 参考

- [秀丸grepをフォルダの右クリックメニューから行う](https://aimek-developer.blogspot.com/2019/02/grep.html)

## 参考資料

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
