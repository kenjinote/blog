---
date: 2022-09-11T22:59:52+09:00
lastmod: 2026-11-23
title: 'Hugo 內建 Shortcodes：媒體嵌入、版本差異與隱私設定'
slug: "HUGOで使える短コード"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '認識 Hugo 內建 Shortcodes、各版本差異，以及媒體嵌入的隱私設定方式。'
---

# Hugo 內建 Shortcodes：媒體嵌入、版本差異與隱私設定

Shortcodes 是在 Markdown 內容中呼叫範本功能的語法。Hugo 本身有內建 Shortcodes，佈景主題與模組也可能提供其他項目，專案還能自行定義。名稱和參數會隨 Hugo 版本改變，請查閱實際使用版本的官方文件。

## Hugo 內建 Shortcodes

Flickr 不是 Hugo 核心內建的 Shortcode。若專案中的 `flickr` 呼叫可用，代表它由佈景主題、模組或自訂範本（例如 `layouts/_shortcodes/flickr.html`）提供。不要只憑名稱就認定它是內建功能。

目前的官方清單包含`details`、`figure`、`highlight`、`instagram`、`param`、`qr`、`ref`、`relref`、`vimeo`、`x`和`youtube`等項目。完整清單與引數請參閱官方頁面。

## 媒體範例

### YouTube

使用影片網址`v`參數中的 ID。

`{{</* youtube 0RKpf3rK57I */>}}`

### X（Hugo 0.141.0 及更新版本）

填入貼文網址中的使用者名稱和貼文 ID。

`{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}`

### 舊版 Twitter（Hugo 0.139.0）

Hugo 0.139.0 使用以下具名引數。

`{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Instagram

Instagram 貼文網址的最後一段就是貼文 ID。

`{{</* instagram CxOWiQNP2MO */>}}`

### Vimeo

使用 Vimeo 影片網址結尾的數字 ID。

`{{</* vimeo 19899678 */>}}`

## 留意版本差異

本部落格的建置版本固定為 Hugo 0.139.0。在此版本中，X（原 Twitter）的內建名稱是 `twitter`，必須使用 `user` 和 `id` 命名參數。`x` Shortcode 從 Hugo 0.141.0 開始提供，之後的版本將 `twitter` 標示為已棄用。複製新版文件範例前，請先確認專案使用的 Hugo 版本。

## 隱私設定

YouTube、X、Instagram 和 Vimeo 嵌入可能會讓訪客的瀏覽器連線至這些服務。Hugo 的 `privacy` 設定可以停用嵌入，或在支援時啟用簡易模式。YouTube 的 `privacyEnhanced` 設定會限制資訊儲存，直到訪客播放影片為止。

YouTube 隱私強化模式:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

X 簡易模式:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

舊版 Twitter（Hugo 0.139.0）:

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

請查閱符合所用 Hugo 版本的官方文件，確認各項設定名稱。

Instagram 的簡易模式仍會直接從 Instagram 伺服器載入圖片。Vimeo 的簡易模式會取得縮圖，點擊後在新分頁開啟 Vimeo。這些模式並不會完全消除第三方請求。

發布嵌入內容前，請確認對服務提供者的連線請求、Cookie 行為，以及讀者所在地適用的隱私要求。

## 以文字顯示語法

若要在文章中直接顯示 Shortcode 語法，請如範例所示，在分隔符中加入 `/*` 和 `*/` 進行跳脫。

`{{</*/* youtube 0RKpf3rK57I */*/>}}`

## 官方文件

- [Shortcodes 概述](https://gohugo.io/content-management/shortcodes/)
- [內建 Shortcodes](https://gohugo.io/shortcodes/)
- [YouTube](https://gohugo.io/shortcodes/youtube/)
- [X](https://gohugo.io/shortcodes/x/)
- [Instagram](https://gohugo.io/shortcodes/instagram/)
- [Vimeo](https://gohugo.io/shortcodes/vimeo/)
- [隱私設定](https://gohugo.io/configuration/privacy/)
