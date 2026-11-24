---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25
title: '秀丸エディタを「hide」コマンド一発で起動！Windowsの便利な設定方法'
slug: "コマンド「hide」で秀丸エディタを立ち上げる方法"
tags: ["コマンド", "秀丸エディタ", "レジストリ"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "Windows 10/11で、レジストリのApp Pathsに登録した名前を「ファイル名を指定して実行」または start hide から使い、秀丸エディタを起動します。"
---

## コマンド「hide」で秀丸エディタを立ち上げる方法を紹介します。

注釈: この方法は`Windows 10/11`で動作確認しています。

1. レジストリエディタを開きます。
2. `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`に移動します。
3. `App Paths`に`hide.exe`というキーを作成します。※このキー名の`.exe`の前がコマンド名になります。
4. `hide.exe`キーの`(既定)`に秀丸エディタの実行ファイルパスを設定します。私の環境では`"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`でした。
5. Path値は任意です。DLL検索用の追加ディレクトリが必要な場合だけ設定します。ShellExecuteExで起動したプロセスのPATHに追加されます。
6. Winキー + Rで開く「ファイル名を指定して実行」に hide と入力します。コマンドプロンプトでは start hide を使います。コマンドプロンプトに hide だけを入力する方法ではありません。

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
上記の内容を`.reg`ファイルに保存して実行すると、レジストリに設定が追加されます。

この.reg例は現在のユーザーだけに登録します。実際の秀丸エディタ実行ファイルのパスに置き換えてください。全ユーザー向けの場合は HKEY_CURRENT_USER を HKEY_LOCAL_MACHINE に変更し、管理者権限で取り込みます。


## 参考資料

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)
