---
title: '使用 Twitter API 和 Google Colaboratory 发送推文的方法'
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["编程"]
---

# 所需条件

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Google 账号

关于如何获取 Twitter API，请参阅参考网站。

# 使用 API 发送推文的步骤

1. 访问 [https://colab.research.google.com/](https://colab.research.google.com/)
2. 选择“文件”→“新建笔记本”
3. 粘贴并运行以下代码（请使用您自己获取的实际值）
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. 粘贴并运行以下代码
```
import tweepy
```
4. 粘贴并运行以下代码(API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→将会发布一条内容为`hello`的推文

5. 粘贴并运行以下代码(API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→将会发布一条内容为`hello v2`的推文

以上

# 参考
- [【2021年4月】附带用途示例与截图详解Twitter API申请流程](https://bloomtectec.com/twitter-api-application-procedure/)
- [【免去繁琐设置！】想要体验Twitter API，强烈推荐Google Colaboratory【内附源码】](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [【Tweepy】Twitter API v2：发推、回复、带投票发推、带媒体发推（v1.1）[Python]](https://3pysci.com/tweepy-28/)
