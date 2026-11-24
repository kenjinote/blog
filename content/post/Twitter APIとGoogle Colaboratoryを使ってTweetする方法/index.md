---
title: "X APIとGoogle Colabで投稿する方法【Python】"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Google ColabのSecretsから認証情報を読み込み、TweepyでX API v2に1件投稿する方法を解説します。公開前にAPIの利用条件と料金を確認してください。"
---

# はじめに

この記事は、Google ColabからTweepyを使い、X API v2で自分のアカウントに1件投稿する最小例です。APIの利用可否・料金・認証条件は変更されるため、実行前に公式ドキュメントとDeveloper Consoleを確認してください。

## 重要：以前の認証情報について

以前の版にはAPIキーとアクセストークンが本文に記載されていました。公開された認証情報は漏えいしたものとして扱ってください。実際に有効な値だった場合は、X Developer Consoleで該当するキーとトークンを失効し、新しい値を発行してください。履歴やコピーが残っている可能性があるため、公開ページから削除しただけでは安全になりません。

# 準備

1. [X Developer Console](https://developer.x.com/en/portal/dashboard)でProjectとAppを用意し、投稿権限を含むユーザー認証情報を発行します。OAuth 1.0a User Contextを使う場合は、Appに読み書き権限を設定した後、アクセストークンを再発行してください。OAuth 2.0 PKCEを使う場合は、`tweet.write`など必要なスコープを含めます。
2. Developer Consoleで現在のプラン、書き込みエンドポイントの料金・利用上限を確認します。料金や提供条件は変わるため、古い解説や記事中の金額を前提にしないでください。
3. [Google Colab](https://colab.research.google.com/)で新しいノートブックを作成します。左側のSecrets（鍵アイコン）に次の名前で4つのSecretを追加し、このノートブックからのアクセスを許可します。値は自分のAppのものを設定し、ノートブックのコードや出力に貼り付けないでください。
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# 1件投稿する

次のセルを実行すると、`text`に指定した内容があなたのXアカウントから公開投稿されます。実行前に文面とアカウントを確認してください。API利用料が発生する場合があります。

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

## 自動投稿について

この例は、セルを手動実行したときに1件だけ投稿します。定期実行や自動返信へ拡張する前に、[Xの自動化ルール](https://help.x.com/en/rules-and-policies/x-automation)を確認してください。特に、自動返信には相手の明確な意思表示など追加条件があります。Colabは常時稼働のジョブ実行環境ではなく、ランタイムや利用制限も保証されません。

## 参考資料

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)
