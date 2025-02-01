---
title: 'Windows 11の右クリックメニューを従来版に戻す方法'
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "エクスプローラー"]
draft: true
image: "img.png"
---

# Windows 11の右クリックメニューを従来版に戻す方法

Windows 11の右クリックメニューを従来版に戻す方法を紹介します。

1. レジストリエディタを開きます。

`Winキー` + `Rキー`を押して、`regedit`と入力して`Enterキー`を押します。
![img_1.png](img_1.png)　

2. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`に移動します。このキーがない場合は作成します。


4. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`に移動します。このキーがない場合は作成します。
5. `InprocServer32`の`(規定)`に値が入っていないことを確認します。

![img_2.png](img_2.png)

6. コンピューターを再起動します。
7. 右クリックメニューが従来版に戻っていることを確認します。
