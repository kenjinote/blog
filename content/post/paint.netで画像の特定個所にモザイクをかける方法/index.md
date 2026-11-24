---
title: 'paint.netで画像の特定箇所にモザイクをかける方法を簡単解説'
slug: "paint.netで画像の特定個所にモザイクをかける方法"
tags: ["paint.net", "モザイク", "画像編集", "プライバシー"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
description: "paint.netの選択範囲にPixelate効果を適用する手順を説明します。セルサイズと拡大縮小方式を調整できます。モザイクは安全な情報墨消しを保証しないため、機密情報を隠す方法も案内します。"
date: "2023-04-11T16:33:10+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


paint.netで画像の特定箇所にモザイクをかける方法を紹介します。

ネット上に画像をアップロードする際に、画像の特定箇所にモザイクをかけたい場合があると思いますが、
paint.netを使うとすぐに画像を加工することができます。

## 手順

#### 1. モザイク処理を行いたい画像をpaint.netで開く
#### 2. 選択ツールを使って、モザイクしたい部分を選択する（複数選択可能）

![img_2.png](img_2.webp)

#### 3. メニュー＞エフェクト＞歪み＞モザイクを選択

![img_1.png](img_1.webp)

- セルサイズは拡大されるピクセルの大きさを決めます。値を大きくすると四角いブロックが大きくなりますが、情報を安全に隠せる保証にはなりません。
- [Scale Down]は`Multisample Bilinear`、[Scale Up]は`Nearest Neighbor`を選ぶと、四角いピクセルの見た目になります。

`OK`でダイアログを閉じます。

#### 4. 画像がモザイク加工されるので、画像を保存します。

![img.png](img.webp)

## プライバシー上の注意

個人情報などを確実に隠す必要がある場合、モザイクやぼかしだけに頼らないでください。不透明な単色で完全に覆い、レイヤーや編集履歴を含まないPNG/JPEGとして書き出したファイルを確認します。編集可能な元ファイルは別途安全に保管してください。

以上。

## 参考資料

- [paint.net: Pixelate effect](https://paint.net/doc/latest/EffectsDistortMenu.html)
- [paint.net: Roadmap and change log](https://paint.net/roadmap.html)
- [UK Information Commissioner’s Office: Securely disclosing documents](https://ico.org.uk/media2/pbwchh24/disclosing-documents-to-the-public-securely-all-1-0-0.pdf)
