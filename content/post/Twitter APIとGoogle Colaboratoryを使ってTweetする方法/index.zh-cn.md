---
title: "使用 X API 和 Google Colab 发布帖子【Python】"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "从 Google Colab Secrets 读取凭据，并使用 Tweepy 和 X API v2 发布一条帖子。运行前请确认当前 API 权限与费用。"
---

# 简介

本文介绍一个最小示例：在 Google Colab 中使用 Tweepy，通过 X API v2 向自己的账号发布一条帖子。API 的权限、费用和认证要求可能变化，请在运行前查看官方文档和 Developer Console。

## 重要：旧版中的凭据

本文旧版曾在正文中写入 API 密钥和访问令牌。请将所有已公开的凭据视为已经泄露。如果这些值曾经有效，请在 X Developer Console 中撤销相关密钥和令牌并重新生成。代码仓库历史或副本中可能仍保留旧值，仅从当前网页删除并不足以确保安全。

# 准备工作

1. 在 [X Developer Console](https://developer.x.com/en/portal/dashboard) 中创建 Project 和 App，并生成具有发帖权限的用户凭据。使用 OAuth 1.0a User Context 时，先为 App 配置读写权限，再生成访问令牌。使用 OAuth 2.0 PKCE 时，请申请包括 `tweet.write` 在内的必要权限范围。
2. 在 Developer Console 中查看当前套餐、写入端点费用和使用限额。价格和开放条件可能变化，请勿依赖旧教程或本文中的旧价格。
3. 在 [Google Colab](https://colab.research.google.com/) 创建笔记本。在左侧 Secrets（钥匙图标）中添加以下四个 Secret，并允许此笔记本访问。填入自己的 App 凭据，不要将其粘贴到笔记本代码或输出中。
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# 发布一条帖子

运行下面的代码单元会从你的 X 账号发布 `text` 中的内容。运行前请确认账号和文案。可能会产生 X API 费用。

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

## 关于自动化

此示例仅在你手动运行代码单元时发布一条帖子。扩展为定时发布或自动回复前，请阅读 [X 自动化规则](https://help.x.com/en/rules-and-policies/x-automation)。自动回复还有额外条件，例如接收者必须明确表达希望收到回复。Colab 并非保证持续运行的任务执行环境，运行时和使用限额也可能变化。

## 参考资料

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)
