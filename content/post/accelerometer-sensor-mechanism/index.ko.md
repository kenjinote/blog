---
title: "가속도 센서의 원리: MEMS와 중력·기울기·움직임 측정"
description: "MEMS 가속도 센서의 proof mass 구조와 정전용량·압저항 검출 방식, 중력과 직선 가속도를 구분할 때의 한계를 설명합니다."
date: "2026-10-01T21:47:14+09:00"
lastmod: 2026-11-23
slug: "accelerometer-sensor-mechanism"
categories: ["technology", "hardware"]
tags: ["tech", "sensor", "mems", "hardware"]
image: "eyecatch.jpg"
draft: false
---

## 가속도 센서가 측정하는 것

가속도는 시간에 따른 속도의 변화율입니다. 뉴턴의 제2법칙 $F=ma$는 질량 $m$에 작용하는 알짜힘 $F$와 가속도 $a$의 관계를 나타냅니다. 가속도 센서는 내부의 작은 질량에 작용하는 **비력(specific force)**을 감지해 가속도에 대응하는 값을 출력합니다. 축 방향과 부호 규약은 부품마다 다릅니다.

비력은 중력 자체를 직접 측정한 값이 아닙니다. 책상 위에 놓인 스마트폰은 책상의 지지력을 받으므로 센서가 대략 $1g$를 나타냅니다(표준 중력가속도는 $9.80665\,\mathrm{m/s^2}$). 자유 낙하 중에는 지지력이 거의 사라져 이상적인 가속도 센서 출력이 $0g$에 가까워집니다.

## 중력으로 기울기 추정하기

기기가 정지했거나 충분히 천천히 움직일 때는 중력 벡터가 세 축에 투영되는 방식으로 기울기를 추정할 수 있습니다. 하지만 가속도 센서만으로는 중력 성분과 기기의 직선 운동에 따른 가속도를 구분할 수 없습니다. 움직임 중 가속과 진동은 기울기 추정을 흐릴 수 있습니다. 스마트폰은 방향을 추정할 때 가속도계와 자이로스코프 및 필터를 함께 사용할 수 있으며, 정확도는 움직임과 알고리즘에 따라 달라집니다.

## MEMS의 proof mass와 스프링

많은 MEMS 가속도 센서는 작은 **proof mass(관성 질량)**를 스프링 모양의 지지 구조에 매답니다. 칩이 가속되면 관성으로 인해 질량체가 프레임에 대해 이동하면서 지지부가 변형됩니다. 센서는 이 상대 변위를 전기 신호로 바꾸고, 내부 회로가 신호를 조정·처리합니다. 실제 부품에는 감쇠와 더 복잡한 구조가 있으므로 “스프링에 매단 질량”은 기본 모델입니다.

## 변위를 신호로 바꾸는 방법

### 정전용량 방식

정전용량 센서는 움직이는 구조와 고정 전극 사이의 정전용량 변화를 검출합니다. 이상적인 평행판 커패시터는 $C=\varepsilon A/d$이며, $\varepsilon$은 유전율, $A$는 겹치는 면적, $d$는 간격입니다. MEMS에는 빗살형 전극 등 다른 구조도 있으며 움직임에 따라 간격이나 겹침 면적이 달라질 수 있습니다. 전용 회로가 미세한 정전용량 변화를 신호로 바꾸며, 일부 제품은 디지털 값을 출력합니다.

### 압저항 방식

압저항 센서는 가속도로 보나 다른 구조물이 변형될 때 생기는 전기저항 변화를 검출합니다. 브리지 회로를 사용해 저항 변화를 전압으로 읽을 수 있습니다. 이 방식은 큰 충격을 측정하는 일부 시험용 센서에 사용됩니다. 적합한 방식은 측정 범위, 대역폭, 온도, 전력 등 요구 사항에 따라 다르며 항상 우월한 한 가지 방식은 없습니다.

## 활용 분야

가속도 센서는 화면 회전, 동작·걸음 수 추정, 게임과 VR의 움직임 감지, 드론 및 기타 장비의 자세 제어에 활용됩니다. 자동차 충돌 감지에도 쓰이지만 에어백 전개 여부는 센서 하나가 아니라 차량별로 검증된 제어 시스템이 판단합니다. 걸음 수나 수면 단계 기능도 가속도 데이터를 포함해 소프트웨어가 추정한 결과입니다.

### 참고 자료

- [STMicroelectronics: MEMS 센서의 원리](https://www.st.com/content/st_com/en/support/learning/essentials-and-insights/mems/how-does-a-mems-sensor-work.html)
- [Analog Devices: 가속도 센서로 기울기 측정](https://www.analog.com/en/resources/app-notes/an-1057.html)
- [Bosch Sensortec: 센서 퓨전](https://www.bosch-sensortec.com/en/software-tools/software/sensor-fusion-software-bsx)
- [Analog Devices: 가속도 센서의 정전용량 검출](https://www.analog.com/en/resources/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
- [Analog Devices: 가속도 센서와 자동차 충돌 감지](https://www.analog.com/en/resources/product-faqs/adxl213.html)

가속도 센서는 각 축을 따른 가속도 관련 데이터를 측정합니다. 기울기와 움직임 상태는 소프트웨어가 이 출력과 다른 센서 정보를 해석해 추정합니다.

[PCB Piezotronics: Piezoresistive shock accelerometers](https://www.pcb.com/sensors-for-test-measurement/accelerometers/piezoresistive-shock)
