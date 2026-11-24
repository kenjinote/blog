---
title: "Qiskit 양자 프로그래밍 입문"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "큐비트, 측정, 얽힘의 기초를 살펴보고 현재 Qiskit과 AerSimulator로 벨 상태를 시뮬레이션합니다."
lastmod: 2026-11-24
---
# 양자 프로그래밍 기초

양자 컴퓨터는 양자역학을 따르는 상태를 조작해 계산합니다. 모든 문제를 더 빠르게 푸는 것은 아니며, 알려진 속도 향상은 특정 문제와 가정에 한정됩니다. 실제 성능은 알고리즘, 하드웨어, 잡음, 오류 정정에 좌우됩니다.

## 큐비트와 측정

한 큐비트의 순수 상태는 $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$로 쓰며 $|\alpha|^2+|\beta|^2=1$입니다. 계산 기저에서 측정하면 0과 1이 각각 $|\alpha|^2$, $|\beta|^2$의 확률로 나옵니다. n큐비트 상태 벡터에는 $2^n$개의 진폭이 있지만, 그렇다고 $2^n$개의 답을 한 번에 읽거나 임의의 계산을 지수적으로 빠르게 할 수 있는 것은 아닙니다.

## 게이트와 얽힘

양자 게이트는 양자 상태에 작용하는 유니터리 변환입니다. X는 0과 1을 바꾸고, H는 기저 상태를 중첩으로 바꾸며, CNOT은 제어 비트가 1일 때 표적 비트를 뒤집습니다. 첫 번째 큐비트에 H를 적용한 다음 CNOT을 적용하면 벨 상태 $(|00\rangle+|11\rangle)/\sqrt{2}$가 됩니다. 측정 결과는 상관관계를 보이지만 얽힘으로 빛보다 빠르게 정보를 보낼 수는 없습니다.

## Qiskit 설치 및 벨 회로 작성

Qiskit SDK로 회로를 만들고 변환합니다. Qiskit 1.0부터 Aer 시뮬레이터는 별도 패키지인 `qiskit-aer`로 배포됩니다. 아래 예제는 로컬 이상 시뮬레이션이며 실제 하드웨어의 잡음이나 성능을 재현하지 않습니다.

```bash
python -m pip install qiskit qiskit-aer
```

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

simulator = AerSimulator()
result = simulator.run(circuit, shots=1000).result()
print(result.get_counts(circuit))
```

이상적인 시뮬레이션에서는 `00`과 `11`만 나오며, 측정 횟수가 늘수록 각 결과의 횟수는 대략 절반에 가까워집니다. 유한한 표본에서는 차이가 생길 수 있습니다. 실제 하드웨어 잡음은 `01`이나 `10`도 만들 수 있습니다. 비트 문자열 순서는 고전 레지스터 규약을 확인하세요.

## 알고리즘 속도 향상에 관해

Deutsch–Jozsa 알고리즘의 한 번 오라클 호출 결과는 함수가 상수 또는 균형 함수라는 약속과 이상적인 오라클을 가정한 쿼리 복잡도 결과입니다. Grover 검색은 구조 없는 N개 후보에서 표시된 항목을 이상적인 오라클 $O(\sqrt{N})$회 호출로 찾습니다. 모든 데이터베이스 작업이 그 비율만큼 빨라진다는 뜻은 아닙니다.

## 참고 자료

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
