---
title: "【Hugo入門】Windowsへのインストールとローカルプレビュー"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "WindowsにHugoを入れる方法、PATHの設定、ドラフトを含めたローカルプレビューの確認手順を公式ドキュメントに基づいて説明します。"
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 【Hugo入門】Windowsにインストールしてローカルでプレビューする

> **更新日：2026年11月24日。** 旧版はHugo 0.102.3の画面出力と2022年当時の手順に依存していました。現在の公式Windowsインストール案内とCLIに合わせて書き直しています。HugoやWindowsの画面、パッケージは更新されるため、迷ったらリンク先の公式資料を優先してください。

## Hugoをインストールする

Windows 10以降では、WinGetを使う方法が簡単です。新しいターミナルを開き、コマンドを実行します。WinGetを使わない場合は、公式リリースからWindowsとCPUアーキテクチャに合うアーカイブを選び、展開して `hugo.exe` を配置できます。PATHへ登録するのは実行ファイルそのものではなく、実行ファイルを置いたフォルダーです。

PATHを手動で設定するときは、スタートメニューで「環境変数を編集」と検索し、ユーザー環境変数の `Path` に、たとえば `C:/Hugo/bin` を追加します。設定後はターミナルを開き直します。

## Hugoをインストールする

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## ローカルでプレビューする

Hugoプロジェクトのルート（設定ファイルまたは設定ディレクトリがある場所）でサーバーを起動します。`--buildDrafts` はドラフトを含めて表示する指定です。ドラフトを含めた状態で公開ビルドしないよう注意してください。Hugoの出力に表示されたURLをブラウザーで開きます。既定では `http://localhost:1313/` ですが、ポートが使用中の場合などは出力を確認してください。終了時はターミナルで Ctrl+C を押します。

## 公式資料

- [Windowsへのインストール](https://gohugo.io/installation/windows/)
- [基本的な使い方とドラフト](https://gohugo.io/getting-started/usage/)
- [hugo serverコマンド](https://gohugo.io/commands/hugo_server/)
