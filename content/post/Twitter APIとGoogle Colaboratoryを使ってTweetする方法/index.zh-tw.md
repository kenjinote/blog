---
title: "如何使用 Twitter API 和 Google Colaboratory 發布推文"
slug: "how-to-tweet-using-twitter-api-and-google-colaboratory-zh-tw"
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["程式設計"]
---

# 所需項目

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Google 帳號

有關如何取得 Twitter API，請參閱參考網站。

# 使用 API 發布推文的步驟

1. 進入 [https://colab.research.google.com/](https://colab.research.google.com/)
2. 選擇「檔案」→「新增筆記本」
3. 貼上並執行以下程式碼（請使用您自己取得的實際值）
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. 貼上並執行以下程式碼
```
import tweepy
```
4. 貼上並執行以下程式碼（API v1.1）
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→ 將發布一則內容為 `hello` 的推文

5. 貼上並執行以下程式碼（API v2.0）
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→ 將發布一則內容為 `hello v2` 的推文

以上

# 參考
- [【截至2021年4月】附帶使用範例與截圖的 Twitter API 使用申請徹底解說](https://bloomtectec.com/twitter-api-application-procedure/)
- [【無需繁瑣設定！】Google Colaboratory 是 Twitter API 測試環境的推薦選擇【附帶原始碼分享】](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [【Tweepy】Twitter API v2：推文、回覆、附帶投票的推文、附帶媒體的推文（v1.1）[Python]](https://3pysci.com/tweepy-28/)
