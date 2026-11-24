---
title: "Windows 11で従来のコンテキストメニューを表示する"
slug: "Windows 11の右クリックメニューを従来版に戻す方法"
tags: ["Windows11", "エクスプローラー"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Windows 11で「その他のオプションを表示」から従来のコンテキストメニューを開く方法と、環境によって動作しないことがあるレジストリ変更を紹介します。"
date: "2024-03-30T13:13:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows 11で従来のコンテキストメニューを表示する

Windows 11では、項目を右クリックして「その他のオプションを表示」を選ぶと、従来のコンテキストメニューを開けます。選択した項目で`Shift`+`F10`を押す方法もあり、`Shift`を押しながら右クリックすると「その他のオプションを表示」を開けます。まずはこの方法を使ってください。

> **注意:** 以下のレジストリ変更は、従来メニューを既定表示にする非公式の回避策です。Microsoftの公式サポート手順ではなく、Windowsのバージョンによっては動作しない場合があります。レジストリを変更する前にバックアップしてください。

## レジストリによる非公式な回避策

1. レジストリエディタを開きます。

`Winキー` + `Rキー`を押して、`regedit`と入力して`Enterキー`を押します。
![img_1.png](img_1.webp)　

2. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`に移動します。このキーがない場合は作成します。

3. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`に移動します。このキーがない場合は作成します。
4. `InprocServer32`の`(規定)`に値が入っていないことを確認します。

![img_2.png](img_2.webp)

5. コンピューターを再起動します。
6. 右クリックメニューが従来版に戻っていることを確認します。

この変更を元に戻す場合は、自分で作成した`{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`キーを削除し、エクスプローラーを再起動します。既存の設定を変更する前に、必ずバックアップしてください。

## 参考資料

- [Microsoft Support: エクスプローラーのコンテキストメニュー](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft Support: Windowsのキーボードショートカット](https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows)
