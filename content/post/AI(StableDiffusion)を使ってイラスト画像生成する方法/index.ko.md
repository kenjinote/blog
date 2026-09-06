---



title: "'AI(StableDiffusion)를 사용하여 일러스트 이미지를 생성하는 방법'"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "일러스트", "이미지 생성", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---




# Stable diffusion이란
Stable diffusion은 독일 뮌헨 대학교의 연구팀이 개발한, 입력된 텍스트 정보로부터 이미지를 생성하는 AI입니다.
다양한 이미지를 학습시킴으로써 실사부터 일러스트까지 다양한 이미지를 생성할 수 있습니다.

이번에는 Stable diffusion의 학습된 데이터를 사용하여 일러스트 이미지를 생성하는 방법을 소개합니다.

# 준비물

- Google 계정

이 전부입니다.

# 생성 절차

1. https://colab.research.google.com 을 엽니다.
2. 왼쪽 상단의 `파일`에서 `새 노트 만들기`를 선택합니다.
3. `수정`에서 `노트 설정`을 선택합니다.
4. `하드웨어 가속기`를 `GPU`로 변경합니다.
![img_2.png](img_2.png)
5. 아래의 코드를 붙여넣고 실행합니다.
```
!pip install diffusers==0.8.0 transformers
```
6. 아래의 코드를 붙여넣고 실행합니다.
```
from diffusers import StableDiffusionPipeline
```
7. 아래의 코드를 붙여넣고 실행합니다.
```
pipe = StableDiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5")
pipe.to("cuda")
```
8. 아래의 코드를 붙여넣고 실행합니다.
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

여기서 사용한 `Prompt`는 [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)의 `Prompt`를 참고했습니다.

## 생성 결과 (일부)
![img_1.png](img_1.png)

![img_3.png](img_3.png)

![img_4.png](img_4.png)

## 참고

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [인공지능(AI)을 사용한 이미지 생성 프로그램을 15분 만에 만들어 보았다【실황 프로그래밍】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
