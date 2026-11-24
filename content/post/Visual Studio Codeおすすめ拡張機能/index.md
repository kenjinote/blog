---
title: "Visual Studio Codeのおすすめ拡張機能：用途別ガイド"
date: "2024-05-29T17:20:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Codeおすすめ拡張機能"
tags: ["Visual Studio Code", "VSCode", "拡張機能", "エクステンション"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Remote開発、GitHub、Web、クラウド、データ、組み込み、言語別に、VS Codeの拡張機能を用途と公式Marketplaceへのリンク付きで紹介します。"
---

# VS Code拡張機能を用途別に選ぶ

拡張機能は、作業に必要なものだけを選ぶのが基本です。ここでは代表的な拡張を用途別にまとめました。Marketplaceの名称・機能は更新されます。2024年版にあった古い名称、重複する機能、誤解を招く説明を整理し、各項目をMarketplaceのページにリンクしています。

Gitの基本操作やJavaScript/TypeScriptのデバッグなど、VS Codeに標準搭載されている機能もあります。まず標準機能を試し、足りない機能だけ追加してください。

## リモート開発とコンテナー

- [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- [Container Tools](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-containers)

## GitHubとGit

- [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)

## Web開発

- [Microsoft Edge Tools for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-edgedevtools.vscode-edge-devtools)
- [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
- [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)

## クラウド

- [AWS Toolkit](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode)
- [Google Cloud Code](https://marketplace.visualstudio.com/items?itemName=GoogleCloudTools.cloudcode)
- [GitHub Copilot for Azure](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azure-github-copilot)

## データベースと組み込み開発

- [SQLTools](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)
- [PlatformIO IDE](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide)
- [Arduino Community Edition](https://marketplace.visualstudio.com/items?itemName=vscode-arduino.vscode-arduino-community)
- [Cortex-Debug](https://marketplace.visualstudio.com/items?itemName=marus25.cortex-debug)

## 言語とビルド

- [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

## 編集・共同作業ツール

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Hex Editor](https://marketplace.visualstudio.com/items?itemName=ms-vscode.hexeditor)
- [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
- [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
- [Japanese Language Pack](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)
- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)

Arduino Community EditionはMicrosoftの公式製品ではなく、旧Arduino拡張のコミュニティ保守フォークです。

SQLToolsは複数のデータベースに接続できるコミュニティ拡張です。接続先に応じたドライバーを別途選び、発行元とアクセス権を確認してください。

GitHub Copilot for AzureはCopilot向けのAzureスキルを追加します。汎用のAzure管理拡張とは異なります。

## インストール前に確認すること

VS Code拡張機能はVS Codeと同じ権限で動作し、ファイルの読み書き、ネットワーク接続、外部プロセスの起動が可能です。インストール前に発行元、拡張パックが追加する依存拡張、更新履歴、サポート情報、プライバシー条件を確認してください。AI機能を使う拡張では、コードやプロンプトが外部サービスへ送られる場合があります。機密情報を扱う場合は、各サービスのデータ利用条件と組織の方針を確認してください。

## まとめ

拡張機能の数を増やすこと自体が効率化につながるわけではありません。目的、信頼できる発行元、必要な権限、保守状況を確認し、使うものだけを導入しましょう。

- [VS Code extension runtime security](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security)
- [VS Code extension Marketplace](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)
