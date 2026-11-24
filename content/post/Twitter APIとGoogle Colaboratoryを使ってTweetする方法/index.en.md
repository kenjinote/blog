---
title: "Post with the X API and Google Colab [Python]"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Read credentials from Google Colab Secrets and publish one post with Tweepy and X API v2. Check current API access and pricing before running the example."
---

# Introduction

This is a minimal example that uses Tweepy in Google Colab to publish one post to your own account with X API v2. Access, pricing, and authentication requirements can change, so check the official documentation and Developer Console before running it.

## Important: credentials in the previous version

An earlier version of this article included API keys and access tokens in its text. Treat any credentials that were published as compromised. If those values were real and active, revoke the affected keys and tokens in the X Developer Console and issue new ones. Copies may remain in repository history, so removing them from the current page alone is not sufficient.

# Before you start

1. Create a Project and App in the [X Developer Console](https://developer.x.com/en/portal/dashboard), then create user credentials with permission to post. For OAuth 1.0a User Context, configure read and write permissions for the App before generating access tokens. With OAuth 2.0 PKCE, request the required scopes, including `tweet.write`.
2. Check the current plan, write-endpoint price, and usage limits in the Developer Console. Pricing and access can change; do not rely on old tutorials or amounts quoted in this article.
3. Create a notebook in [Google Colab](https://colab.research.google.com/). In the Secrets panel (key icon), add four secrets with the names below and allow this notebook to access them. Enter your own App values; do not paste them into notebook code or output.
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# Publish one post

Running this cell publishes the text in `text` from your X account. Check the account and wording before running it. X API charges may apply.

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

## About automation

This example publishes one post only when you run the cell manually. Before extending it to scheduled posting or automated replies, read [X Automation Rules](https://help.x.com/en/rules-and-policies/x-automation). Automated replies have additional requirements, including a clear indication of intent from the recipient. Colab is not a guaranteed always-on job runner, and its runtimes and usage limits are subject to change.

## References

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)
