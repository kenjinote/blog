---
title: "使用 X API 與 Google Colab 發布貼文【Python】"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "從 Google Colab Secrets 讀取憑證，並使用 Tweepy 與 X API v2 發布一則貼文。執行前請確認目前的 API 權限與費用。"
---

# 簡介

本文提供一個最小範例：在 Google Colab 中使用 Tweepy，透過 X API v2 向自己的帳號發布一則貼文。API 權限、費用與驗證要求可能變動，請在執行前查看官方文件與 Developer Console。

## 重要：舊版中的憑證

本文舊版曾在內文放入 API 金鑰與存取權杖。請將所有曾公開的憑證視為已外洩。如果這些值曾經有效，請在 X Developer Console 撤銷相關金鑰與權杖，並重新產生。儲存庫歷史或副本可能仍保留舊值，因此只從目前網頁刪除並不足以確保安全。

# 開始前準備

1. 在 [X Developer Console](https://developer.x.com/en/portal/dashboard) 建立 Project 與 App，並產生具備發文權限的使用者憑證。若使用 OAuth 1.0a User Context，請先為 App 設定讀寫權限，再產生存取權杖。若使用 OAuth 2.0 PKCE，請要求包含 `tweet.write` 的必要範圍。
2. 在 Developer Console 查看目前方案、寫入端點價格與使用上限。費用與開放條件可能變動，請勿依賴舊教學或本文中的舊價格。
3. 在 [Google Colab](https://colab.research.google.com/) 建立筆記本。在左側 Secrets（鑰匙圖示）新增以下四個 Secret，並允許此筆記本存取。填入自己的 App 憑證；不要貼在筆記本程式碼或輸出中。
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# 發布一則貼文

執行下方儲存格後，`text` 中的文字會由你的 X 帳號公開發布。執行前請確認帳號與文字。可能會產生 X API 費用。

```python
%pip install -q tweepy

from google.colab import userdata
import tweepy

client = tweepy.Client(
    consumer_key=userdata.get("X_API_KEY"),
    consumer_secret=userdata.get("X_API_KEY_SECRET"),
    access_token=userdata.get("X_ACCESS_TOKEN"),
    access_token_secret=userdata.get("X_ACCESS_TOKEN_SECRET"),
)

text = "Hello from the X API"
response = client.create_tweet(text=text)
print(response.data["id"])
```

## 自動化說明

本範例只有在手動執行儲存格時才會發布一則貼文。若要擴充為排程發布或自動回覆，請先閱讀 [X 自動化規則](https://help.x.com/en/rules-and-policies/x-automation)。自動回覆有額外要求，例如接收者必須明確表示希望收到回覆。Colab 並非保證持續執行的工作環境，執行階段與使用上限也可能變動。

## 參考資料

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)
