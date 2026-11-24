---
title: "P 대 NP 추측: 계산 복잡도 이론의 미해결 문제"
slug: "P≠NP 예상"
tags: ["P≠NP 예상", "수학", "미해결 문제"]
draft: false
categories: ["math-cryptography-quantum"]
description: "다항식 길이 증명서와 SAT 예시를 통해 P, NP와 P=NP 여부라는 미해결 문제를 설명합니다."
image: eyecatch.jpg
date: 2024-09-11T02:22:39+09:00
lastmod: 2026-11-24
---
# P와 NP란?

**P**는 입력 크기에 대한 다항 시간 안에 풀 수 있는 결정 문제의 집합입니다. **NP**는 답이 ‘예’인 각 입력에 대해 입력 크기의 다항식으로 길이가 제한되는 증명서(제안된 해)가 있고, 이를 다항 시간 안에 검증할 수 있는 결정 문제의 집합입니다. P의 해도 다항 시간에 검증할 수 있으므로 **P ⊆ NP**입니다.

## SAT 예시

SAT는 주어진 불리언 식을 참으로 만드는 변수 할당이 존재하는지 묻습니다. ‘예’인 입력에서는 그 할당이 증명서이며, 모든 절을 만족하는지 식의 크기에 대한 다항 시간에 확인할 수 있습니다. 3-SAT를 포함한 SAT는 NP-완전입니다. 따라서 SAT를 다항 시간에 푸는 알고리즘이 있다면 **P = NP**가 됩니다. NP-완전이란 NP의 모든 문제가 다항 시간 환원을 통해 해당 문제로 변환될 수 있다는 뜻입니다.

## 미해결 질문

**P = NP인지 P ≠ NP인지**는 아직 밝혀지지 않았습니다. 클레이 수학연구소는 P 대 NP를 미해결 문제로 분류합니다. P≠NP는 널리 연구되는 추측이지 증명된 정리는 아닙니다. 쉽게 말해, 제안된 해를 효율적으로 검증할 수 있는 모든 문제를 효율적으로 풀 수도 있는지를 묻는 문제입니다.

## 참고 자료

- [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)
- [Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)
