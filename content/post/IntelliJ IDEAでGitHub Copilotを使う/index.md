---
title: 'IntelliJ IDEAでGitHub Copilotを使う'
date: 2022-09-10T09:44:55+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.png"
---
# はじめに
GitHub Copilotは、GitHubが開発したAIベースのコード補完ツールです。
開発環境IntelliJ IDEAにGitHub Copilotのプラグインを入れるとIntelliJ IDEAでもGitHub Copilotを使うことができます。
有効化するにはGithubのアカウントが必要となります。

# インストール方法
1. IntelliJ IDEAのメニューのFileからSettingsを選択
2. Pluginsを選択して、検索で「GitHub Copilot」を検索
![img.png](images/img_0.png)
3. インストールボタンからインストール
![img_1.png](images/img_1.png)
4. Restart IDEボタンを押してIntelliJ IDEAを再起動
![img_2.png](images/img_2.png)
![img_3.png](images/img_3.png)
IntelliJ IDEAを再起動するとインストールは完了です。

# 有効化
1. 右下のアイコンをクリック
2. Login to Githubをクリック
![img_4.png](images/img_4.png)
3. Copy and Openボタンをクリック
![img_6.png](images/img_6.png)
4. ブラウザが立ち上がるので、Githubにログインしていない場合はログインしたのち、Ctrl+Vでコードを貼り付けてContinueボタンをクリック
![img_7.png](images/img_7.png)
5. Authorize GitHub Copilot Pluginボタンをクリック
![img_8.png](images/img_8.png)
![img_9.png](images/img_9.png)
上記の画面が表示されれば有効化完了です。

# 使ってみる
![img_10.png](images/img_10.png)
IntelliJ IDEAのエディタで文字を数文字入力すると、GitHub Copilotがコードの続きを提案してくれるようになります。
それではAIによる強力な補完機能を楽しんでください！
