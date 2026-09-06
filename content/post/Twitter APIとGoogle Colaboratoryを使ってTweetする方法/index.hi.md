---
title: "Twitter API और Google Colaboratory का उपयोग करके ट्वीट कैसे करें"
slug: "how-to-tweet-using-twitter-api-and-google-colaboratory-hi"
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["प्रोग्रामिंग"]
---

# क्या चाहिए

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Google अकाउंट

Twitter API कैसे प्राप्त करें, इसके लिए संदर्भ साइट देखें।

# API का उपयोग करके ट्वीट करने के चरण

1. [https://colab.research.google.com/](https://colab.research.google.com/) पर जाएं
2. "फ़ाइल" -> "नई नोटबुक" चुनें
3. नीचे दिया गया कोड पेस्ट करें और चलाएं (कृपया अपने द्वारा प्राप्त वास्तविक मानों का उपयोग करें)
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. नीचे दिया गया कोड पेस्ट करें और चलाएं
```
import tweepy
```
4. नीचे दिया गया कोड पेस्ट करें और चलाएं (API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→ `hello` कहने वाला एक ट्वीट पोस्ट किया जाएगा

5. नीचे दिया गया कोड पेस्ट करें और चलाएं (API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→ `hello v2` कहने वाला एक ट्वीट पोस्ट किया जाएगा

बस इतना ही

# संदर्भ
- [【अप्रैल 2021 तक】उपयोग उदाहरणों और स्क्रीनशॉट के साथ Twitter API उपयोग एप्लिकेशन की विस्तृत व्याख्या](https://bloomtectec.com/twitter-api-application-procedure/)
- [【जटिल सेटिंग्स की कोई आवश्यकता नहीं!】Twitter API परीक्षण वातावरण के लिए Google Colaboratory की अनुशंसा की जाती है 【स्रोत कोड भी साझा किया गया है】](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [【Tweepy】Twitter API v2: ट्वीट, रिप्लाई, पोल वाले ट्वीट, मीडिया वाले ट्वीट (v1.1) [Python]](https://3pysci.com/tweepy-28/)
