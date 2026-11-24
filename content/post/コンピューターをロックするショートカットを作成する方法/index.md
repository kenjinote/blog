---
title: 'WindowsPCを1秒でロック！便利なショートカットの作成方法と使い方'
slug: "コンピューターをロックするショートカットを作成する方法"
tags: ["Windows", "コンピューターをロック", "ショートカット"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Windowsパソコンをワンクリックでロックできるショートカットの作成方法を画像付きで分かりやすく解説します。離席時のセキュリティ対策として便利な、Win+Lキーを使った一瞬でロックする方法も紹介。'
date: "2024-04-01T01:37:49+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

コンピューターをロックさせるショートカットを作成する方法を紹介します。

作成したショートカットをデスクトップなどにおいてダブルクリックするとコンピューターをロックできるので便利です。

## 作成方法

#### 1. デスクトップで右クリックして、`新規作成`＞`ショートカット`を選択

![img_2.png](img_2.webp)
#### 2. ショートカットの作成画面が表示されるので`rundll32.exe user32.dll,LockWorkStation`を入力して`次へ`をクリック

![img_1.png](img_1.webp)

#### 3. ショートカットの名前`コンピューターをロック`を入力して`完了`をクリック

![img_3.png](img_3.webp)

#### 4. 作成されたショートカットのアイコンを変更する

作成されたショートカットを右クリックして`プロパティ`を選択

![img_4.png](img_4.webp)

`アイコンの変更`をクリック

![img_6.png](img_6.webp)

黄色の四角のアイコンを選択して`OK`をクリック、再度`OK`をクリックしてプロパティを閉じる

![img_5.png](img_5.webp)

以上。

![img_7.png](img_7.webp)

作成されたショートカットをダブルクリックするとコンピューターをロックされます。

`Winキー` + `Lキー`を押しても、同じくコンピューターをロックできます。

※注意：コンピューターをロックの確認ダイアログは表示されません。

Windowsをロックすると、作業中のアプリは開いたままで、再開時にはサインインが必要です。掲載した画面は日本語版Windowsの例で、表示名や画面配置はWindowsのバージョンと言語によって異なる場合があります。

## 参考資料

- [Microsoft Support：Windowsでユーザーアカウントにアクセスする（ロック）](https://support.microsoft.com/en-us/accounts-billing/security/user-account-access-in-windows)
- [Microsoft Learn：LockWorkStation関数](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-lockworkstation)
- [Microsoft Learn：コンピューターの状態を変更する（PowerShell）](https://learn.microsoft.com/en-us/powershell/scripting/samples/changing-computer-state)
- [Microsoft Learn：rundll32コマンド](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rundll32)
