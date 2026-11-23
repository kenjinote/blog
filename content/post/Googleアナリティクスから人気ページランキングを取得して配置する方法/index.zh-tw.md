---
title: '使用 Ranklet4 在 Hugo 中顯示 GA4 熱門網頁排名'
date: 2023-04-10T20:26:57+09:00
lastmod: 2026-11-23




slug: "Google Analyticsから人気ページランキングを取得して配置する方法"
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '使用支援 GA4、接替已停用 Ranklet 小工具的 Ranklet4，在 Hugo 中加入熱門網頁排名。本文說明遷移、權限、範本及使用第三方服務時的注意事項。'
---

# 使用 Ranklet4 在 Hugo 中顯示 GA4 熱門網頁排名

舊版說明使用 Google Analytics 檢視畫面與舊 Ranklet 小工具。舊 Ranklet 服務已於 2023 年結束。請將舊標籤換成 GA4 專用獨立服務 Ranklet4 所產生的新標籤。請參閱[官方遷移說明](https://docs.ranklet4.com/changes.html)。

Ranklet4 會彙整 GA4 報表資料，並以 JavaScript 小工具提供排名，也支援 Hugo 等靜態網站。選單與方案可能變動，請以[官方教學](https://docs.ranklet4.com/tutorial.html)為準。

## 開始前

* 網站需要有記錄瀏覽資料的 GA4 資源。
* 用來登入的 Google 帳戶，在該資源中至少需要**檢視者**權限，不必使用管理員帳戶。
* Ranklet4 將取得 Google Analytics 資料存取權。其條款授予廣泛授權，可使用、複製、散布、創作衍生作品、展示及執行分析資料；條款也允許使用與公開無法識別個人的統計資訊。連結前請閱讀[服務條款](https://docs.ranklet4.com/agreement.html)與[隱私權政策](https://ranklet4.com/docs/privacy)，並確認你有權分享這些資料。

## 建立並發布排名

1. 使用可檢視目標 GA4 資源的帳戶登入 [Ranklet4](https://ranklet4.com/)。授權前先確認要求的權限。
2. 建立排名並選取 GA4 資源、統計期間與顯示筆數。可用標題或網址篩選，例如排除首頁。
3. 視需要設定標題文字取代，並在預覽中檢查結果。
4. 從設計庫選擇範本，或自訂 HTML/CSS。新範本使用 Handlebars；欄位名稱與語法請參閱[範本指南](https://docs.ranklet4.com/template.html)。
5. 儲存並發布後，複製管理畫面產生的排名標籤。不要沿用舊 Ranklet 的標籤或 ID。

以下是最基本的 HTML 範本。支援的欄位與迴圈語法請參閱官方指南。

```handlebars
<ol class="popular-pages">
  {{#each rankings}}
  <li><a href="{{url}}">{{title}}</a></li>
  {{/each}}
</ol>
```

## 加入 Hugo

1. 建立 `layouts/partials/ranklet4.html`，並貼上 Ranklet4 產生的完整排名標籤。
2. 在想顯示排名的版型中加入以下 Hugo 呼叫，例如 `layouts/_default/single.html` 或側欄 partial：

```go-html-template
{{- partial "ranklet4.html" . }}
```

3. 在本機預覽頁面，發布後確認小工具透過 HTTPS 載入。它依賴第三方 JavaScript，請考量載入速度、隱私權告知與網站安全政策。

## 更新與遷移注意事項

排名依據 GA4 報表與 Ranklet4 的更新時程重新整理，因此新造訪不一定會立即改變排名。更新頻率、方案功能、服務積分與廣告政策可能變動，請查看[目前方案](https://docs.ranklet4.com/plan.html)。Ranklet4 爬蟲會讀取公開網頁資訊，詳情請見[常見問題](https://docs.ranklet4.com/faq.html)。

## 官方參考資料

* [Ranklet4 官方教學](https://docs.ranklet4.com/tutorial.html)
* [與舊版 Ranklet 的差異](https://docs.ranklet4.com/changes.html)
* [Ranklet4 範本指南](https://docs.ranklet4.com/template.html)
* [Ranklet4 常見問題](https://docs.ranklet4.com/faq.html)
* [Ranklet4 服務條款](https://docs.ranklet4.com/agreement.html)
* [Ranklet4 隱私權政策](https://ranklet4.com/docs/privacy)
