---
title: 'Windowsのライセンス認証状態を確認する方法！コマンド一発で簡単にチェック'
slug: "Windows のライセンスの状態を確認するコマンド"
date: "2025-04-14T00:41:45+09:00"
lastmod: "2026-11-25"
tags: ["Windows", "ライセンス", "コマンドプロンプト"]
draft: false
image: "img_1.webp"
categories: ["pc-gadgets"]
description: 'Windows標準のslmgrコマンドで、ライセンスチャネルや認証状態を確認する方法を解説します。/dli、/dlv、/xprの違いと、認証状態がライセンスの適法性を証明するものではない点も説明します。'
---

# 【Windows】ライセンスの状態を確認する方法（コマンド1つでOK）

Windowsのライセンスが正しく認証されているかどうか、気になったことはありませんか？

そんなときに便利なのが、 **コマンド一発でライセンス情報を確認できる方法** です。以下の手順を実行するだけで、現在のライセンス状態を簡単にチェックできます。

## ライセンス状態を確認するコマンド

Windowsに標準搭載されているスクリプトツールを使って、ライセンスの情報を表示できます。使用するコマンドはこちら：

```
slmgr /dli
```

このコマンドを実行すると、ライセンスの一部情報がウィンドウで表示されます。

## 実行方法

1. 「スタート」から「cmd」を検索してコマンドプロンプトを開きます。`/dli`、`/dlv`、`/xpr`の確認に管理者権限は不要です。

2. コマンドプロンプトに以下を入力してEnterキーを押します：

   ```
   slmgr /dli
   ```

3. 数秒待つと、以下のようなライセンス情報が表示されます。

   ![Windowsのライセンス状態を表示した画面](img.webp)

## 表示される主な情報

* 一部のプロダクトキー
* ライセンスチャネル（Retail、OEMなど）
* ライセンス状態（表示内容はエディションやチャネルで異なります）

## もっと詳細な情報を知りたいときは？

以下のようなコマンドもあります：

* `slmgr /dlv`：より詳細なライセンス情報を表示
* `slmgr /xpr`：ライセンス認証の有効期限を表示

`/xpr`はライセンス認証の有効期限を表示し、主にKMSクライアント向けです。RetailやMAKでは永続認証と表示されることがあります。なお、`slmgr`はライセンスが適法に取得されたかどうかを検証しません。Windows 11では「設定」>「システム」>「ライセンス認証」でも状態を確認できます。

## まとめ

Windowsのライセンス状態は、コマンドひとつで簡単に確認できます。

* **簡易確認** ：`slmgr /dli`
* **詳細確認** ：`slmgr /dlv`
* **有効期限の確認** ：`slmgr /xpr`

状態が想定と異なる場合は、Windowsの「ライセンス認証」設定や購入元、組織の管理者に確認してください。

## 参考

- [Slmgr.vbs options for obtaining volume activation information](https://learn.microsoft.com/en-us/windows-server/get-started/activation-slmgr-vbs-options)
- [Activate Windows](https://support.microsoft.com/en-us/windows/activation/activate-windows)
