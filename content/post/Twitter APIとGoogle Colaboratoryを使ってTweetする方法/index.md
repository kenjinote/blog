---
title: 'Twitter APIとGoogle Colaboratoryを使ってTweetする方法'
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
---

# 必要なもの

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Google アカウント

Twitter API の取得方法は参考のサイトを参照してください。

# APIを使ってツイートする手順

1. [https://colab.research.google.com/](https://colab.research.google.com/) にアクセス
2. 「ファイル」→「ノートブックを新規作成」を選択
3. 下記のコードを貼り付けて実行（実際の各値はご自身で取得したものを使ってください）
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. 下記のコードを貼り付けて実行
```
import tweepy
```
4. 下記のコードを貼り付けて実行(API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→`hello`というツイートが投稿される

5. 下記のコードを貼り付けて実行(API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→`hello v2`というツイートが投稿される

以上

# 参考
- [【2021年4月時点】Twitter APIの利用申請を使用用途の例文とスクリーンショット付きで徹底解説](https://bloomtectec.com/twitter-api-application-procedure/)
- [【面倒な設定不要！】Twitter APIのお試し環境ならGoogle Colaboratoryがオススメ【ソースコードも共有します】](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [【Tweepy】Twitter API v2：ツイート、返信（リプライ）、投票付きツイート、メディア付きツイート（v1.1）[Python]](https://3pysci.com/tweepy-28/)