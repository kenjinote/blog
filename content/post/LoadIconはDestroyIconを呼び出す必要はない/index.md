---
title: 'LoadIcon関数で取得したアイコンはDestroyIconが不要な理由'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["アイコン", "LoadIcon", "DestroyIcon", "Windowsプログラミング"]
draft: false
categories: ["programming"]
description: 'Windows APIのアイコンハンドルは、共有リソースか呼び出し側所有かでDestroyIconの要否が変わります。LoadIcon、LoadImage、CopyIconの解放条件と、Microsoft公式資料で仕様の説明が食い違うAPIを整理します。'
image: eyecatch.jpg
---

# アイコンハンドルの所有権

`DestroyIcon`を呼び出すかどうかは、アイコンが共有リソースか、呼び出し側が解放責任を持つリソースかで決まります。共有アイコンを破棄すると、同じリソースを使う別の処理に影響します。

## DestroyIconを呼ばないケース

- `LoadIcon`が返すアイコンは共有リソースです。`DestroyIcon`で破棄してはいけません。`LoadIcon`は現在のサイズの標準メトリックに合うアイコンを読み込み、サイズを指定したい場合は`LoadImage`が推奨されています。
- `LoadImage`に`LR_SHARED`を指定すると、ハンドルは共有されます。`DestroyIcon`を呼ばないでください。`LR_SHARED`は、ファイルから読み込む画像や標準外サイズの画像には使えません。
- `CopyImage`に`LR_COPYRETURNORG`を指定し、元の`hImage`が共有アイコンの場合、元のハンドルが返ることがあります。その場合も破棄してはいけません。

## DestroyIconを呼ぶケース

呼び出し側が所有するアイコンは、使用を終えたら`DestroyIcon`で解放します。Microsoftは次の例を挙げています。

- `CreateIconFromResourceEx`（`LR_SHARED`なし）
- `CreateIconIndirect`
- `CopyIcon`（複製アイコンのハンドルを返します）
- `LoadImage`でアイコンを読み込み、`LR_SHARED`を指定しない場合

## CreateIconFromResourceの注意点

Microsoftの一般的な`DestroyIcon`資料は`CreateIconFromResource`を共有アイコンの取得元として記載していますが、各関数の個別資料は`DestroyIcon`を呼ぶよう説明しています。`CreateIconFromResource`と`CreateIconFromResourceEx`の資料内にも、`LR_SHARED`の説明と解放指示の食い違いがあります。これらのAPIでは一般論だけで判断せず、対象関数の最新資料を確認してください。この矛盾は`LoadIcon`の共有ハンドルの説明とは分けて考えます。

`DestroyIcon`に渡すアイコンは使用中であってはなりません。共有ハンドルかどうか、またモジュールの有効期間も確認してください。

## 参考資料

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
