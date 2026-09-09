---
title: 'Windows 11の右クリックメニューを従来版（旧仕様）に戻す方法【レジストリ設定】'
slug: "Windows 11の右クリックメニューを従来版に戻す方法"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "エクスプローラー"]
draft: false
image: "img.webp"
categories: ["PC・ガジェット"]
description: 'Windows 11の新しい右クリックメニュー（コンテキストメニュー）を、Windows 10の従来版に戻す方法を解説します。レジストリエディタを使った設定変更で、旧仕様のメニューを常に表示できるようにする簡単な手順を紹介します。'
---

# Windows 11の右クリックメニューを従来版に戻す方法

Windows 11の右クリックメニューを従来版に戻す方法を紹介します。

1. レジストリエディタを開きます。

`Winキー` + `Rキー`を押して、`regedit`と入力して`Enterキー`を押します。
![img_1.png](img_1.webp)　

2. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`に移動します。このキーがない場合は作成します。


4. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`に移動します。このキーがない場合は作成します。
5. `InprocServer32`の`(規定)`に値が入っていないことを確認します。

![img_2.png](img_2.webp)

6. コンピューターを再起動します。
7. 右クリックメニューが従来版に戻っていることを確認します。
