---
title: 'How to Tweet Using Twitter API and Google Colaboratory'
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["Programming"]
---

# Requirements

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Google Account

For instructions on how to obtain the Twitter API, please refer to the reference sites.

# Steps to Tweet using API

1. Access [https://colab.research.google.com/](https://colab.research.google.com/)
2. Select "File" -> "New notebook"
3. Paste and run the following code (use your own obtained values)
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. Paste and run the following code
```
import tweepy
```
4. Paste and run the following code (API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→ A tweet saying `hello` will be posted

5. Paste and run the following code (API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→ A tweet saying `hello v2` will be posted

That's all

# References
- [[As of April 2021] Thorough Explanation of Twitter API Application Process with Example Use Cases and Screenshots](https://bloomtectec.com/twitter-api-application-procedure/)
- [[No Troublesome Setup Needed!] Google Colaboratory is Recommended for Trying Out Twitter API [Source Code is also Shared]](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [[Tweepy] Twitter API v2: Tweet, Reply, Poll, Media (v1.1) [Python]](https://3pysci.com/tweepy-28/)
