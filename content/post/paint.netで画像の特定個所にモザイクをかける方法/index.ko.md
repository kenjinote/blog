---
title: 'paint.net에서 이미지의 특정 부분에 모자이크를 적용하는 방법 간단 설명'
slug: "paint.netで이미지の特定個所にモザイクをかける方法"
tags: ["paint.net", "픽셀화", "이미지 편집", "개인정보 보호"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
description: "paint.net 선택 영역에 Pixelate 효과를 적용하고 Cell Size와 크기 조정 방식을 설정하는 방법입니다. 픽셀화는 안전한 정보 삭제를 보장하지 않으므로 더 안전한 가림 방법도 안내합니다."
date: "2023-04-11T16:33:10+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---






paint.net에서 이미지의 특정 부분에 모자이크 처리하는 방법을 소개합니다.

인터넷에 이미지를 업로드할 때, 이미지의 특정 부분에 모자이크를 처리하고 싶은 경우가 있을 텐데요,
paint.net을 사용하면 이미지를 금방 가공할 수 있습니다.

## 순서

#### 1. 모자이크 처리를 할 이미지를 paint.net에서 열기
#### 2. 선택 도구를 사용하여 모자이크할 부분을 선택하기 (다중 선택 가능)

![img_2.png](img_2.webp)

#### 3. 메뉴 ＞ 효과 ＞ 왜곡 ＞ 모자이크 선택

![img_1.png](img_1.webp)

- Cell Size는 확대되는 픽셀의 크기를 조절합니다. 값이 클수록 네모 블록도 커지지만, 정보가 안전하게 가려진다는 보장은 없습니다.
- 네모난 픽셀 블록을 원하면 [Scale Down]은 `Multisample Bilinear`, [Scale Up]은 `Nearest Neighbor`로 설정하세요.

`OK`로 대화 상자를 닫습니다.

#### 4. 이미지에 모자이크 처리가 되므로, 이미지를 저장합니다.

![img.png](img.webp)

## 개인정보 보호 주의

개인 정보처럼 확실히 숨겨야 하는 정보에는 픽셀화나 흐림 효과만 사용하지 마세요. 불투명한 단색으로 완전히 덮고, 레이어나 편집 이력이 없는 PNG 또는 JPEG로 내보낸 뒤 결과 파일을 확인하세요. 편집 가능한 원본은 별도로 안전하게 보관하세요.

이상.

## 참고 자료

- [paint.net: Pixelate effect](https://paint.net/doc/latest/EffectsDistortMenu.html)
- [paint.net: Roadmap and change log](https://paint.net/roadmap.html)
- [UK Information Commissioner’s Office: Securely disclosing documents](https://ico.org.uk/media2/pbwchh24/disclosing-documents-to-the-public-securely-all-1-0-0.pdf)
