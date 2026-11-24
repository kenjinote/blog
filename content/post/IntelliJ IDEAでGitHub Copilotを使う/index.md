---
title: 'IntelliJ IDEAでGitHub Copilotを導入・有効化する方法'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'IntelliJ IDEAにGitHub Copilotプラグインをインストールし、GitHubアカウントで認証してコード補完を使う手順を紹介します。必要なCopilotアクセス、現在のサインイン方法、提案の受け入れ方を公式資料に基づいて説明します。'
---
# はじめに

GitHub CopilotプラグインをJetBrains IDEに追加すると、入力中のコード候補やCopilot Chatを利用できます。このページではIntelliJ IDEAでの基本的な導入とサインインを説明します。メニュー名や画面はIDE・プラグインのバージョンによって異なる場合があります。

## 始める前に

GitHub Copilotを利用できるGitHubアカウントと、Copilotに対応したIntelliJ IDEAが必要です。Copilot Freeには利用上限があり、有料プランではより多くの機能を利用できます。プランとIDEの対応状況は変更されるため、最新の公式資料を確認してください。

## プラグインをインストールする

1. IntelliJ IDEAのPlugins設定を開きます。Windows/Linuxでは **File > Settings > Plugins**、macOSでは **IntelliJ IDEA > Settings > Plugins** を選びます。
2. Marketplaceで「GitHub Copilot」を検索し、GitHubが提供するプラグインの **Install** をクリックします。
3. インストールが終わったらIDEを再起動します。

## GitHubにサインインする

1. IDEの **Tools > GitHub Copilot > Login to GitHub** を開きます。
2. サインイン画面で **Copy and Open** をクリックします。ブラウザーが開きます。
3. ブラウザーでGitHubにサインインし、IDEに表示されたデバイスコードを貼り付けて **Continue** をクリックします。
4. 権限を確認して **Authorize GitHub Copilot Plugin** を選びます。IDEに戻り、確認画面で **OK** をクリックします。

## コード提案を使う

エディターでコードを書き始めると、Copilotが候補を薄い文字で表示します。候補を採用するには **Tab** を押します。候補は文脈に基づく提案なので、採用前に内容を確認してください。画面右側のGitHub Copilot Chatアイコンからチャットも開けます。

画面や機能は更新されることがあります。詳しい手順と対応バージョンは公式資料を参照してください。

## 参考

- [GitHub Copilotプラグインのインストールとサインイン](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [JetBrains IDEでコード提案を使う](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [JetBrains MarketplaceのGitHub Copilotプラグイン](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
