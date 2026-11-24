---
title: "X API와 Google Colab으로 게시물 올리기 [Python]"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Google Colab Secrets에서 인증 정보를 읽고 Tweepy와 X API v2로 게시물 하나를 올립니다. 실행 전에 현재 API 이용 조건과 요금을 확인하세요."
---

# 소개

이 글은 Google Colab에서 Tweepy를 사용해 X API v2로 본인 계정에 게시물 하나를 올리는 최소 예제입니다. API 이용 가능 여부, 요금, 인증 요건은 바뀔 수 있으므로 실행 전에 공식 문서와 Developer Console을 확인하세요.

## 중요: 이전 버전의 인증 정보

이전 버전의 본문에는 API 키와 액세스 토큰이 포함되어 있었습니다. 공개된 인증 정보는 유출된 것으로 간주하세요. 실제로 유효한 값이었다면 X Developer Console에서 해당 키와 토큰을 폐기하고 새로 발급하세요. 저장소 기록이나 복사본에 값이 남아 있을 수 있으므로 현재 페이지에서 지우는 것만으로는 충분하지 않습니다.

# 시작 전 준비

1. [X Developer Console](https://developer.x.com/en/portal/dashboard)에서 Project와 App을 만들고 게시 권한이 있는 사용자 인증 정보를 발급합니다. OAuth 1.0a User Context를 사용하는 경우 App에 읽기/쓰기 권한을 설정한 뒤 액세스 토큰을 발급하세요. OAuth 2.0 PKCE는 `tweet.write`를 포함한 필요한 scope를 요청합니다.
2. Developer Console에서 현재 요금제, 쓰기 endpoint의 가격 및 사용 한도를 확인하세요. 가격과 이용 조건은 바뀔 수 있으므로 오래된 글이나 이전 가격을 기준으로 삼지 마세요.
3. [Google Colab](https://colab.research.google.com/)에서 노트북을 만듭니다. 왼쪽 Secrets(열쇠 아이콘)에 아래 이름의 Secret 네 개를 추가하고 이 노트북의 접근을 허용하세요. 본인 App의 값을 입력하고 노트북 코드나 출력에 붙여 넣지 마세요.
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# 게시물 하나 올리기

아래 셀을 실행하면 본인의 X 계정에서 `text`의 내용이 공개 게시됩니다. 실행 전에 계정과 문구를 확인하세요. X API 이용료가 발생할 수 있습니다.

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

## 자동화에 관해

이 예제는 셀을 수동으로 실행할 때 게시물 하나만 올립니다. 예약 게시나 자동 답글로 확장하기 전에 [X 자동화 규칙](https://help.x.com/en/rules-and-policies/x-automation)을 읽으세요. 자동 답글에는 받는 사람이 명확한 의사를 표시해야 하는 등 추가 요건이 있습니다. Colab은 항상 실행되는 작업 환경이 아니며 런타임과 사용 한도도 보장되지 않습니다.

## 참고 자료

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)
