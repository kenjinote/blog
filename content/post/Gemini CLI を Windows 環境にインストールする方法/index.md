---
title: 'Gemini CLI を Windows 環境にインストールする方法'
date: 2025-07-13T23:49:56+09:00
tags: ["Gemini", "CLI", "Windows", "インストール", "開発"]
draft: true
image: "img.png"
---

# 【初心者向け】WindowsにGemini CLIをインストールする方法

Googleの生成AI「Gemini」をコマンドラインから使えるようにする「Gemini CLI」。
この記事では、Windows環境にGemini CLIをインストールする手順を、できるだけわかりやすく解説します。

---

## 1. 事前準備：Node.jsとnpmをインストール

まず、Gemini CLIは「Node.js」という環境上で動作するため、以下のものをインストールしておく必要があります。

* **Node.js**
* **npm（Node.jsに付属するパッケージ管理ツール）**
* **npx（npmに含まれるコマンド実行ツール）**

以下の公式サイトから、Windows版のNode.jsをダウンロードしてください（LTS版がおすすめです）：

👉 [Node.js公式サイト](https://nodejs.org/)

インストールが完了したら、次のコマンドで正しくインストールされたか確認しましょう。

```powershell
node -v
npm -v
```

---

## 2. PowerShellを起動する

WindowsでGemini CLIを使うには、PowerShellを使って操作するのが一般的です。
スタートメニューから「PowerShell」と入力して起動してください。

---

## 3. Gemini CLIをインストールする

以下のコマンドをPowerShellにコピー＆ペーストして実行します：

```bash
npx @google/gemini-cli
```

このコマンドは、Googleが公開しているGemini CLIパッケージを一時的に実行するためのものです。
必要に応じて初期設定やログインが求められることもあります。

※ 初回は数分かかることがあります。エラーが出た場合は、Node.jsやネットワーク環境を再確認してみてください。

---

## 4. インストール完了！次にやること

これで、Windows上にGemini CLIがインストールされました。
今後は、コマンドラインからGeminiを使って、テキスト生成やコード補完など、さまざまな操作が可能になります。

公式ドキュメントやヘルプを確認したい場合は、以下のようなコマンドも活用できます。

```bash
npx @google/gemini-cli --help
```

---

## まとめ

WindowsにGemini CLIを導入する手順をおさらいします。

1. Node.jsとnpmをインストール
2. PowerShellを起動
3. `npx @google/gemini-cli` を実行

これで準備完了です！
生成AIをローカルから使いたい方は、ぜひこの手順を参考にチャレンジしてみてください。
