---

title: "'Twitter API와 Google Colaboratory를 사용하여 트윗하는 방법'"
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---


# 필요한 것

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Google 계정

Twitter API 취득 방법은 참고 사이트를 참조해 주세요.

# API를 사용하여 트윗하는 순서

1. [https://colab.research.google.com/](https://colab.research.google.com/) 에 접속
2. 「파일」→「새 노트 만들기」를 선택
3. 아래의 코드를 붙여넣고 실행 (실제 각 값은 직접 취득한 것을 사용해 주세요)
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. 아래의 코드를 붙여넣고 실행
```
import tweepy
```
4. 아래의 코드를 붙여넣고 실행 (API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→`hello`라는 트윗이 게시됨

5. 아래의 코드를 붙여넣고 실행 (API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→`hello v2`라는 트윗이 게시됨

이상

# 참고
- [【2021년 4월 기준】 Twitter API 이용 신청을 사용 용도 예문과 스크린샷으로 철저하게 해설](https://bloomtectec.com/twitter-api-application-procedure/)
- [【번거로운 설정 불필요!】 Twitter API 테스트 환경이라면 Google Colaboratory를 추천 【소스 코드도 공유합니다】](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [【Tweepy】 Twitter API v2: 트윗, 답글(리플라이), 투표 포함 트윗, 미디어 포함 트윗 (v1.1) [Python]](https://3pysci.com/tweepy-28/)
