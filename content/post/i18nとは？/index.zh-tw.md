---
title: 'i18n（國際化）是什麼？在軟體開發中的意義與對應項目'
slug: "i18nとは？"
tags: ["Internationalization", "i18n", "術語"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: '淺顯易懂地解說在軟體開發中常聽到的「i18n（Internationalization：國際化）」的意義與字源。為您整理在將應用程式或系統進行全球化應對時，應考慮的主要項目，如文字編碼、日期時間格式、貨幣資訊等。'
date: "2023-04-07T00:42:02+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


# 什麼是 i18n？

## 國際化與在地化

國際化是設計與開發產品或軟體，使其容易調整以服務不同語言、地區與文化的使用者。在地化（l10n）則是依特定地區設定調整產品。國際化（i18n）本身不是翻譯，而是讓翻譯及其他地區調整更容易。

`i18n` 是 `Internationalization` 的縮寫，意思是國際化。因為 `Internationalization` 太長了，
所以在第一個 `i` 和最後一個 `n` 之間有 18 個字母，因此縮寫為 `i18n`。

它經常被用在軟體國際化的語境中。

國際化的主要考慮項目包括以下內容：

- 文字與語言（Unicode、字元編碼、語言標籤、字型涵蓋範圍與文字呈現）
- 文字方向（從左到右、從右到左、從上到下向左等）
- 語言 / 文字
- 字型
- 格式
  - 數字（小數點字元、千位分隔符號、分組位數等）
  - 日期和時間（日期格式、使用的日曆差異，如伊斯蘭曆/公曆/猶太曆/日本曆等）
- 日期和時間資訊的時區差異
- 貨幣資訊

- 字串與訊息（將使用者看到的文字與程式碼分離，處理各語言複數形式與詞序，避免直接串接句子片段）
- 地區資訊（姓名、地址、電話號碼、輸入法、鍵盤、符號、顏色、法律要求與文化習慣）

## 測試要點

使用偽在地化找出文字變長與未翻譯字串，並針對目標語言和地區測試版面、輸入、排序及數字／日期格式。RTL 語言還要檢查介面與混合方向文字。

## References

- [W3C: Localization vs. Internationalization](https://www.w3.org/International/questions/qa-i18n)
- [W3C Internationalization Glossary](https://www.w3.org/TR/i18n-glossary/)
- [Unicode CLDR: Common Locale Data & Rules](https://www.unicode.org/reports/tr35/)
