---
title: 'iOSアプリ開発用に中古のMac mini(2018)を購入した理由とスペック'
date: 2023-04-02T18:05:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "mac mini(2018)を購入"
tags: ["Apple", "mac mini", "xcode"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: '自宅での快適なiOSアプリ開発環境を構築するため、メルカリで型落ちのMac mini(2018)を購入しました。購入の決め手となった理由や詳細なスペック、環境構築の第一歩についてご紹介します。'
---
# Mac mini(2018)を購入

メルカリで型落ち中古のMac mini(2018)を購入した。スペックは下記。

- CPU: 3.2GHz 6コアIntel Core i7
- メモリ: 32GB
- ストレージ: 1TB SSD

価格は ￥ 77,000

# 購入に至った理由

- 会社でほぼ同じスペックのMac miniを使用してスマホアプリの開発をしているが、自宅でも開発環境(特にXcodeの実行環境)を整えたいと思っていた。
- MacBook Proを持っているが、9年前に購入したものでかなり動作が遅いためほぼ使っていない。
- 個人的にiOSアプリの開発をしたいと思っていた。

# さっそく Xcode と IntelliJ IDEA をインストール

XcodeはバージョンがVersion 14.3 (14E222b)
![img_1.png](img_1.webp)

IntelliJ IDEAはバージョンが2023.1
![img_2.png](img_2.webp)

さあ！開発していくぞ！

## 現在の互換性に関する注意

この記事は2023年4月2日時点の購入・開発環境の記録で、現在の購入推奨ではありません。2026年11月24日時点で、Mac mini (2018) はmacOS Tahoe 26の対応機種一覧に含まれていません。また、Xcode 27はAppleシリコン搭載Macでのみ動作し、Intel搭載MacでXcodeを使う場合はXcode 26以前が必要です。中古購入や開発環境の構築前に、対象OSとXcodeの要件を確認してください。

## 参考資料

- [Mac mini (2018) 技術仕様](https://support.apple.com/111912)
- [macOS Tahoe compatibility](https://support.apple.com/122867)
- [Xcode system requirements](https://developer.apple.com/Xcode/system-requirements/)
- [Porting your macOS apps to Apple silicon](https://developer.apple.com/documentation/Apple-Silicon/porting-your-macOS-apps-to-Apple-silicon)
