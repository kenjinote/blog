---
title: '【初心者向け】vcpkgでlibcurl（OpenSSL対応）をVisual Studioに導入する手順'
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
---

## Visual Studioでlibcurl（OpenSSL対応）を使うなら、vcpkg導入が簡単でおすすめ

C++でHTTP通信を扱いたいときによく使われるのが `libcurl`。でも、ビルドや依存関係の調整って意外と面倒ですよね。

そんなときに役立つのが、Microsoft製のC++ライブラリ管理ツール「**vcpkg**」です。
今回は、`vcpkg`を使って `libcurl`（OpenSSL対応）を導入し、Visual Studioでスムーズに使えるようにするまでの手順を紹介します。

---

### vcpkgのインストール（未導入の方のみ）

まずは `vcpkg` をインストールしましょう。以下の手順を PowerShell で実行してください。

```powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
```

※Gitがまだ入っていない場合は、[Gitの公式サイト](https://git-scm.com/)からインストールしてください。

---

### libcurl（OpenSSL対応）のインストール

続いて、vcpkgを使って `libcurl` をインストールします。OpenSSLに対応した64bit版を指定するには、以下のコマンドを実行します。

```powershell
vcpkg install curl[ssl] --triplet x64-windows
```

このコマンドを実行すると、必要な依存関係（OpenSSLなど）も自動的にセットアップされます。

---

### Visual Studioとの連携設定

vcpkgで導入したライブラリをVisual Studioのプロジェクトから簡単に使えるようにするには、次のコマンドで統合設定を行います。

```powershell
vcpkg integrate install
```

この設定をしておくと、Visual Studioのプロジェクトで自動的に `#include <curl/curl.h>` が使えるようになり、ライブラリのパスやリンカの設定を手動で行う必要がなくなります。

---

## おわりに

これで、Visual Studioに `libcurl`（OpenSSL対応）を導入する準備は完了です。

* vcpkgを使えば、面倒な依存関係も一括で管理できる
* `vcpkg install curl[ssl] --triplet x64-windows` でlibcurlを簡単に導入
* `vcpkg integrate install` でVisual Studioと自動連携が可能

あとは、プロジェクト内でヘッダをインクルードして、libcurlのAPIを使って開発を始めましょう。
便利なvcpkgを活用して、開発効率を一気に高めてみてください。
