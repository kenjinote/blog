---
title: "X API और Google Colab से पोस्ट कैसे करें [Python]"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Google Colab Secrets से क्रेडेंशियल पढ़ें और Tweepy व X API v2 से एक पोस्ट प्रकाशित करें। उदाहरण चलाने से पहले मौजूदा API पहुँच और शुल्क जाँचें।"
---

# परिचय

यह एक छोटा उदाहरण है जो Google Colab में Tweepy का उपयोग करके X API v2 से आपके अपने खाते पर एक पोस्ट प्रकाशित करता है। API पहुँच, शुल्क और प्रमाणीकरण की शर्तें बदल सकती हैं, इसलिए चलाने से पहले आधिकारिक दस्तावेज़ और Developer Console देखें।

## महत्वपूर्ण: पिछले संस्करण के क्रेडेंशियल

इस लेख के पिछले संस्करण में API keys और access tokens लिखे हुए थे। जो भी क्रेडेंशियल सार्वजनिक हुए हैं, उन्हें लीक हुआ मानें। यदि वे वास्तविक और सक्रिय थे, तो X Developer Console में संबंधित keys और tokens रद्द करके नए जारी करें। रिपॉज़िटरी इतिहास या प्रतियों में पुराने मान बचे हो सकते हैं, इसलिए केवल मौजूदा पेज से हटाना पर्याप्त नहीं है।

# शुरू करने से पहले

1. [X Developer Console](https://developer.x.com/en/portal/dashboard) में Project और App बनाएँ और पोस्ट करने की अनुमति वाले user credentials जारी करें। OAuth 1.0a User Context में access tokens बनाने से पहले App के लिए read और write permissions सेट करें। OAuth 2.0 PKCE में `tweet.write` सहित आवश्यक scopes माँगें।
2. Developer Console में मौजूदा plan, write endpoint का मूल्य और उपयोग सीमाएँ देखें। मूल्य और उपलब्धता बदल सकते हैं; पुराने tutorials या पुराने दामों पर भरोसा न करें।
3. [Google Colab](https://colab.research.google.com/) में notebook बनाएँ। बाएँ तरफ़ Secrets (चाबी आइकन) में नीचे दिए नामों से चार secrets जोड़ें और इस notebook को उन तक पहुँच दें। अपने App के मान दर्ज करें; उन्हें notebook code या output में न चिपकाएँ।
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# एक पोस्ट प्रकाशित करें

इस cell को चलाने पर `text` में दिया गया संदेश आपके X खाते से सार्वजनिक रूप से पोस्ट होगा। चलाने से पहले खाता और संदेश जाँच लें। X API शुल्क लग सकता है।

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

## स्वचालन के बारे में

यह उदाहरण केवल cell को हाथ से चलाने पर एक पोस्ट प्रकाशित करता है। इसे scheduled posting या automated replies तक बढ़ाने से पहले [X Automation Rules](https://help.x.com/en/rules-and-policies/x-automation) पढ़ें। Automated replies के लिए अतिरिक्त शर्तें हैं, जिनमें प्राप्तकर्ता की स्पष्ट इच्छा शामिल है। Colab हमेशा चालू रहने वाला job runner नहीं है; runtime और उपयोग सीमाएँ बदल सकती हैं।

## संदर्भ

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)
