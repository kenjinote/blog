---
title: '【初心者向け】vcpkgでlibcurl（OpenSSL対応）をVisual Studioに導入する手順'
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
---

## 【初心者向け】vcpkgでlibcurl（OpenSSL対応）をVisual Studioに導入する手順

Visual Studio 環境で `libcurl` を使いたいけど、ビルドや依存関係の管理が面倒…
そんなときに便利なのが、Microsoft製のC++ライブラリ管理ツール **vcpkg** です。

今回は、`vcpkg` を使って `libcurl`（OpenSSL対応）を導入し、Visual Studio プロジェクトからすぐに使える状態にするまでの流れをご紹介します。

---

### 1. vcpkgをインストール（まだ導入していない場合）

まずは `vcpkg` 自体を入手してセットアップします。以下のコマンドをPowerShellで実行してください。

```powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
```

※Gitがインストールされていない場合は、先に[Git公式サイト](https://git-scm.com/)から導入してください。

---

### 2. libcurl（OpenSSL対応）をインストール

`vcpkg` を使って、OpenSSLサポート付きの `libcurl` をインストールします。ここでは64bit版を指定しています。

```powershell
vcpkg install curl[ssl] --triplet x64-windows
```

このコマンドで、必要な依存関係（OpenSSLなど）もまとめて自動的に解決してくれます。

---

### 3. Visual Studio への統合

vcpkgでインストールしたライブラリをVisual Studioのプロジェクトから自動的に認識させるには、以下のコマンドで統合設定を行います。

```powershell
vcpkg integrate install
```

この設定を行うことで、以降は **すべてのVisual Studioプロジェクトで** `#include <curl/curl.h>` が使えるようになります。ライブラリのパス設定やリンカの設定は不要です。

---

## まとめ

以上で、Visual Studio 環境に `libcurl`（OpenSSL対応）を導入する準備は完了です。

* ライブラリ管理には `vcpkg` が便利
* `vcpkg install curl[ssl] --triplet x64-windows` で一発インストール
* `vcpkg integrate install` でプロジェクト設定も自動化

以降は、ヘッダをインクルードし、通常通り `libcurl` のAPIを使って開発を進められます。
