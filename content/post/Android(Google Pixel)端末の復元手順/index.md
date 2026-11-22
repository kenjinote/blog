---
title: "Google Pixel公式ツールでソフトウェアを更新・再インストールする手順"
slug: "Android(Google Pixel)端末の復元手順"
tags: ["Android", "Google Pixel", "復元", "トラブルシューティング"]
draft: false
image: "pixel_restore_eyecatch_1788588727945.webp"
categories: ["programming"]
description: "Google公式Pixel Update and Software Repairツールの使い方を解説。対象機種、更新と再インストールの違い、データ消去の注意点を確認します。"
date: "2025-02-28T01:20:41+09:00"
lastmod: "2026-11-23T19:00:00+09:00"
---

# Google Pixel公式ツールでソフトウェアを更新・再インストールする

> **データ消去に関する重要事項（2026年11月23日確認）:** Googleのツールには「Update」と「Reinstall」があります。Updateは初期化せずに最新ソフトウェアを適用できる場合があります。Reinstallは端末を初期化し、データを消去します。再インストール前にバックアップし、Googleアカウントの認証情報を確認してください。Googleの現行ヘルプではPixel 4a以降（Foldを含む）が対象です。利用前に最新の対応情報と画面上の案内を確認してください。

[Pixel Update and Software Repair](https://pixelrepair.withgoogle.com/)は、対応するPixel端末のソフトウェア更新・再インストールを行う公式ツールです。ブートループや起動不良でも必ず修復できる保証はありません。初期化の前に、再起動、Android更新、セーフモード、ストレージ確認など[Google公式のトラブルシューティング](https://support.google.com/pixelphone/answer/4582729)を試してください。

## 1. 対応端末とツールを確認する

[公式ツール](https://pixelrepair.withgoogle.com/)を開き、端末に表示される対応状況と操作を確認します。対応機種・地域・利用できる操作は変わることがあるため、現在の画面と[Google公式ヘルプ](https://support.google.com/pixelphone/answer/4596836)を優先してください。

## 2. 作業前に準備する

- 端末を操作できる場合は必要なデータをバックアップし、Googleアカウントと画面ロックの認証情報を確認します。
- パソコンとデータ転送対応のUSBケーブルを用意し、可能ならハブを避けて直接接続します。
- 初期化する場合、Googleの一般案内はバッテリーを70%以上に充電するよう推奨しています。ツールに別の指示があれば画面に従います。
- Windowsで端末が認識されない場合は、必要に応じて[Google USBドライバの公式手順](https://developer.android.com/studio/run/win-usb)を確認してください。

## 3. 接続して画面の案内に従う

1. パソコンで[Pixel Update and Software Repair](https://pixelrepair.withgoogle.com/)を開きます。
2. ツールの指示があれば端末の電源を切ります。現在の案内では、電源ボタンと音量大ボタンを長押しして電源を切ります。
3. 電源ボタンと音量小ボタンを同時に約3秒押してFastbootモードにします。機種や画面の案内が異なる場合は、画面の指示を優先してください。
4. USBでパソコンに接続し、「Connect device」から正しい端末を選択してブラウザ接続を許可します。
5. 「Update」または「Reinstall」を選びます。Updateはデータを残せる場合があります。Reinstallは工場出荷時の状態に戻してデータを消去するため、バックアップ後に限って選んでください。処理中はケーブルを抜かないでください。

接続できない、または起動が回復しない場合は、書き込みを繰り返さず、[Googleの公式サポート手順](https://support.google.com/pixelphone/answer/4596836)を確認してください。

## まとめ

操作前にツールの最新画面と公式ヘルプを確認してください。UpdateとReinstallはデータへの影響が異なり、Reinstallはデータを消去します。初期化前にバックアップとアカウント情報を確認してください。