---
title: "ABC 추측과 IUT: 증명 주장과 계속되는 논쟁"
date: "2026-09-14T13:00:00+09:00"
lastmod: 2026-11-23
slug: "abc-conjecture"
image: "eyecatch.jpg"
categories: ["mathematics", "science"]
tags: ["ABC Conjecture", "Number Theory", "IUT Theory", "Shinichi Mochizuki"]
draft: false
description: "ABC 추측의 내용, IUT를 통한 모치즈키 신이치 교수의 증명 주장, PRIMS 게재와 해결되지 않은 수학계 논쟁을 소개합니다."
---

## ABC 추측의 내용

$a+b=c$를 만족하는 서로소인 양의 정수 $a,b,c$를 생각해 봅시다. 양의 정수 $n$의 **근기(radical)**는 $n$을 나누는 서로 다른 소수의 곱입니다.

$$\operatorname{rad}(n)=\prod_{p\mid n}p$$

예를 들어 $\operatorname{rad}(2^3\cdot3^2)=6$입니다. 근기는 소인수의 지수를 무시하므로 정수 자체보다 훨씬 작을 수 있습니다.

ABC 추측은 모든 $\varepsilon>0$에 대해 상수 $K_\varepsilon$가 존재하여, 이런 모든 삼중항이

$$c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}$$

를 만족한다는 주장입니다. 이 상수는 $\varepsilon$에 따라 달라질 수 있습니다. 조제프 오스테를레와 데이비드 마서는 1985년에 이 추측을 정식화했습니다. 이는 덧셈과 소인수분해 사이의 강한 제약을 나타내며, $a,b$에 작은 소인수가 있으면 $c$에 반드시 큰 소인수가 생긴다는 단순한 규칙은 아닙니다.

## IUT를 통한 모치즈키의 증명 주장

2012년 교토대의 모치즈키 신이치는 ABC 추측을 포함한 디오판토스 기하학 문제를 위한 새로운 틀로 우주 간 테이흐뮐러 이론(IUT) 논문을 공개했습니다. IUT는 수체 위의 타원곡선 같은 산술적 대상을 다루는 매우 전문적인 이론으로, 테이흐뮐러 이론·호지–아라켈로프 이론·아나벨 기하학과 관련된 개념을 결합합니다. 호지 극장과 로그-세타 격자 등의 개념을 통해 구조 간 산술 정보를 비교합니다. 이를 단순히 “덧셈과 곱셈을 서로 다른 우주에 둔다”고 설명하면 이론을 오해하게 됩니다.

모치즈키는 IUT에서 ABC 추측이 따라온다고 주장합니다. 네 편의 논문은 오랜 심사 과정을 거쳐 2021년 *Publications of the Research Institute for Mathematical Sciences* (PRIMS) 특집호에 실렸습니다. 게재는 중요한 사실이지만, 그 자체로 수학계의 합의나 논쟁의 종결을 뜻하지는 않습니다.

## 계속되는 쟁점

피터 숄체와 야코프 스틱스는 2018년 보고서에서 ABC 부등식으로 이어지는 IUT III의 정리 3.11에서 따름정리 3.12로 넘어가는 핵심 단계에 논리적 공백이 있다고 주장했습니다. 모치즈키는 이 비판이 이론을 오해한 데서 비롯됐다며 반박했고, 2025년 10월 보고서에서 자신의 입장을 다시 설명했습니다. 여기서는 각 저자가 밝힌 주장을 요약했을 뿐, IUT의 증명을 독립적으로 검증한 것은 아닙니다.

따라서 신중한 설명은 세 사실을 구분해야 합니다. IUT 논문은 PRIMS에 게재되었고, 모치즈키는 이 논문들이 ABC를 증명한다고 주장하며, 핵심 논증에 대한 수학자들의 견해 차이는 해결되지 않았습니다. ABC 추측을 널리 확립된 정리라고 소개하는 것은 부정확합니다.

## 페르마의 마지막 정리와의 관계

ABC 추측이 참이라면 페르마의 마지막 정리도 따라옵니다. 즉 $n\ge3$일 때 $x^n+y^n=z^n$의 양의 정수해는 없습니다. 이는 조건부 귀결이며, 페르마 정리가 아직 증명되지 않았다는 뜻은 아닙니다. 앤드루 와일스 등이 이미 증명했습니다.

서로소인 해 $x,y,z$가 있다고 가정해 봅시다. 임의의 양의 정수 $k$에 대해 $(x^{nk},y^{nk},z^{nk})$도 서로소인 합의 삼중항입니다. 이 삼중항의 근기 $\operatorname{rad}(x^{nk}y^{nk}z^{nk})=\operatorname{rad}(xyz)$는 변하지 않지만, $z^{nk}$는 한없이 커집니다. 그러면 고정된 $\varepsilon>0$에 대한 ABC의 상계를 위반하는 삼중항이 무한히 생기므로 모순입니다.

## 참고 자료

- [ABC의 표준 정식화 (Jordan S. Ellenberg)](https://arxiv.org/abs/math/9909098)
- [2021년 PRIMS IUT 특집호](https://ems.press/journals/prims/issues/1507)
- [숄체–스틱스 보고서 (2018)](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [모치즈키의 IUT 보고서 (2025년 10월)](https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf)
- [IUT 개관 (모치즈키, 2012)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf)

이 글은 추측과 공개된 논쟁을 간략히 소개하며, IUT 증명을 재구성하거나 판정하지 않습니다.
