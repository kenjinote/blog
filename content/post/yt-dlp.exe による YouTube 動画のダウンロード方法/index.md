---
title: "yt-dlp.exeの使い方：許可された動画の保存とMP3変換"
slug: "yt-dlp.exe による YouTube 動画のダウンロード方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "yt-dlp.exeの取得、更新、動画保存とMP3変換の基本を紹介します。コンテンツの権利とYouTubeの利用規約に従って利用してください。"
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# yt-dlp.exeの使い方：許可された動画の保存とMP3変換

yt-dlpは動画や音声を取得するオープンソースのコマンドラインツールです。以下はWindowsでの基本例です。

## 利用上の注意

自分が権利を持つコンテンツ、または権利者の許可があるコンテンツに限り、YouTubeの利用規約と適用される法律が許す範囲で使用してください。自分がアップロードした動画はYouTube Studioからダウンロードできます。

## インストールと更新

公式リリースページからWindows用の`yt-dlp.exe`をダウンロードし、任意のフォルダーに置きます。フォルダーを`PATH`に追加すると、どの場所からでも実行できます。実行ファイルは公式リリースから取得してください。

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## 基本的な使い方

コマンドプロンプトまたはPowerShellで動画URLを指定します。出力ファイルは現在のフォルダーに保存されます。

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

音声をMP3にする場合は`-x`と`--audio-format mp3`を使います。

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

実行ファイルのバージョンは`yt-dlp.exe --version`で確認できます。リリース版は`yt-dlp.exe -U`で更新できます。MP3への変換には`ffmpeg`と`ffprobe`が必要です。YouTubeの仕様変更で取得に失敗する場合は、最新版に更新し、公式READMEの依存関係を確認してください。

サムネイルやメタデータを埋め込みたい場合は`--embed-thumbnail`や`--embed-metadata`を追加できますが、形式に応じて追加ツールが必要です。

## うまくいかない場合

取得できないときは、実行ファイルを最新版に更新し、公式ドキュメントで必要な依存関係と対応状況を確認してください。制限を回避したり、権限のないコンテンツを取得したりしないでください。

## 参考資料

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)
