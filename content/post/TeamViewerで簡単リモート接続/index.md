---
title: 'TeamViewerで簡単リモート接続'
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "コマンド", "リモート接続"]
draft: false
image: "img.png"
---

# TeamViewerで簡単リモート接続

TeamViewerを使うとリモートデスクトップ接続が簡単に行えます。

リモート先とリモート元でTeamViewerを起動し、
リモート元でリモート先のIDとパスワードを入力するとリモートが行えます。

コマンドラインでリモート接続する場合は以下のようにします。

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
`<ID>`にはリモート先のIDを、`<Password>`にはリモート先のパスワードを入力します。

上記のコマンドでショートカットファイルを作成しておくと、ID/PWの入力を省略できるため便利です。

参考サイト：[Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
