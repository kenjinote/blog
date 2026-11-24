---
title: "Qiskitで学ぶ量子プログラミング入門"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "量子ビット、測定、もつれの基本を説明し、現在のQiskitとAerSimulatorでベル状態をシミュレーションします。"
lastmod: 2026-11-24
---
# 量子プログラミングの基本

量子コンピュータは量子力学に従う状態を操作して計算します。量子計算があらゆる問題を速く解くわけではなく、特定の問題や条件で古典計算に対する高速化が知られています。実用上の性能は、アルゴリズム、ハードウェア、ノイズ、誤り訂正などに左右されます。

## 量子ビットと測定

1量子ビットの純粋状態は $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$ と表せ、$|\alpha|^2+|\beta|^2=1$ です。計算基底で測定すると、0と1がそれぞれ $|\alpha|^2$、$|\beta|^2$ の確率で得られます。n量子ビットの状態ベクトルには $2^n$ 個の振幅がありますが、これは2^n個の答えを一度に読み出せることや、一般の計算が指数的に速くなることを意味しません。

## ゲートともつれ

量子ゲートは量子状態に作用するユニタリ変換です。Xゲートは0と1を交換し、Hゲートは基底状態を重ね合わせへ移し、CNOTは制御ビットが1のとき標的ビットを反転します。Hを第1量子ビットに適用し、続けてCNOTを適用すると、$(|00\rangle+|11\rangle)/\sqrt{2}$ というベル状態が得られます。測定結果には相関がありますが、もつれを使って光速より速く情報を送ることはできません。

## Qiskitのインストールとベル状態

Qiskit SDKは量子回路の作成・変換に使います。Qiskit 1.0以降、Aerシミュレータは別パッケージの `qiskit-aer` です。以下はローカルの理想シミュレーションで、実機のノイズや性能を再現するものではありません。

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

理想シミュレータでは、測定結果は `00` と `11` だけになり、その回数はショット数を増やすとおおむね半分ずつに近づきます。有限回の測定では偏りが生じます。実機ではノイズにより `01` や `10` も出ることがあります。ビット列の表示順序は古典レジスタの規約を確認してください。

## アルゴリズムの速度について

Deutsch–Jozsaの1回のオラクル呼出しという結果は、関数が定数か均衡かという約束と理想的なオラクルを仮定したクエリ計算量の話です。Grover探索は、N個から印の付いた項目を探す非構造化探索で、理想的なオラクル呼出しを $O(\sqrt{N})$ 回にできます。これは一般のデータベース処理全体が同じ倍率で速くなるという意味ではありません。

## 参考資料

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
