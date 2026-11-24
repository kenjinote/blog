---
title: "Qiskit 量子程式設計入門"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "認識量子位元、測量與糾纏，並使用目前版本的 Qiskit 和 AerSimulator 模擬貝爾態。"
lastmod: 2026-11-24
---
# 量子程式設計基礎

量子電腦透過操控遵循量子力學的狀態來計算。它不會讓所有問題都變快；已知的加速只適用於特定問題與前提。實際效能取決於演算法、硬體、雜訊與錯誤更正。

## 量子位元與測量

單一量子位元的純態可寫成 $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$，且 $|\alpha|^2+|\beta|^2=1$。在計算基底測量時，得到0或1的機率分別為 $|\alpha|^2$ 和 $|\beta|^2$。n個量子位元的狀態向量有 $2^n$ 個振幅，但這不代表能一次讀出 $2^n$ 個答案，也不代表任意計算都會獲得指數級加速。

## 量子閘與糾纏

量子閘是作用於量子狀態的么正變換。X閘交換0與1；H閘將基底狀態轉成疊加態；控制位為1時，CNOT閘會翻轉目標位。先對第一個量子位元施加H閘，再施加CNOT，可得到貝爾態 $(|00\rangle+|11\rangle)/\sqrt{2}$。其測量結果彼此相關，但糾纏不能用來超光速傳遞資訊。

## 安裝 Qiskit 並建立貝爾態電路

Qiskit SDK 用來建立與轉換量子電路。自 Qiskit 1.0 起，Aer 模擬器由獨立套件 `qiskit-aer` 提供。以下範例使用本機理想模擬器，不模擬真實硬體的雜訊或效能。

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

理想模擬只會得到 `00` 和 `11`；測量次數增加時，計數大致趨近各半。有限次取樣仍可能不均。真實硬體雜訊也可能產生 `01` 或 `10`。解讀位元字串順序時，請確認古典暫存器的慣例。

## 關於演算法加速

Deutsch–Jozsa 演算法的一次預言機呼叫，是在函數符合「常數或平衡」承諾並假設預言機理想時的查詢複雜度結果。Grover 搜尋在 N 個無結構候選項中尋找標記項，需要 $O(\sqrt{N})$ 次理想預言機呼叫。這不表示所有資料庫工作都會按此比例加速。

## 參考資料

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
