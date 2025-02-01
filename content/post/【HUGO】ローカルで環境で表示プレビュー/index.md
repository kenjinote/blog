---
title: '【HUGO】ローカルで環境で表示プレビュー'
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
---
# HUGOのインストール

## ダウンロード
[HUGOのダウンロード](https://github.com/gohugoio/hugo/releases)

上記のサイトから、環境に合わせたWindowsのモジュールをダウンロードして展開する。
私の場合は「hugo_0.102.3_Windows-64bit.zip」をダウンロードしました。

## 展開
ダウンロードしたzipファイルを展開して、その中にあるhugo.exeを例えばC:\bin等のフォルダを作ってそこにコピーします。

## 環境変数に登録
任意の場所からhugo.exeを実行するために環境変数に登録します。
Windows11での操作になりますが、下記のような手順で登録できると思います。

1. Win+Pauseボタンを押してバージョン情報を開く
2. システムの詳細設定をクリックする
3. 環境変数をクリックする
4. Pathを選択して編集をクリックする
5. 新規をクリックして、新しい行に「C:\bin」と入力してOKでダイアログを閉じる
 
# ブログをプレビューする
コマンドプロンプトでHUGOブログのフォルダに移動して、下記のコマンドを実行する。

`hugo server -D`

実行結果は下記。（-Dはドラフトの記事を表示するオプションです。）

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
Pages            | 39
Paginator pages  |  0
Non-page files   |  7
Static files     |  0
Processed images |  0
Aliases          | 13
Sitemaps         |  1
Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

アドレスは実行時に出力されるので（上記の例では`http://localhost:1313/`）、ブラウザにアドレスをコピーする。
プレビューはファイルが保存されるたびに自動更新される。
プレビュー終えるにはコマンドプロンプトでCtrl+Cを入力する。
