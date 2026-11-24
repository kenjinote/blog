---
title: "Qiskit量子编程入门"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "了解量子比特、测量和纠缠的基础，并使用当前版本的Qiskit与AerSimulator模拟贝尔态。"
lastmod: 2026-11-24
---
# 量子编程基础

量子计算机通过操控遵循量子力学的状态来计算。它并不能让所有问题都更快；已知的加速只适用于特定问题和前提。实际性能取决于算法、硬件、噪声和纠错。

## 量子比特与测量

单个量子比特的纯态可写为 $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$，且 $|\alpha|^2+|\beta|^2=1$。在计算基下测量，得到0或1的概率分别为 $|\alpha|^2$ 和 $|\beta|^2$。n个量子比特的状态向量有 $2^n$ 个振幅，但这不代表能一次读出 $2^n$ 个答案，也不代表任意计算都会获得指数级加速。

## 量子门与纠缠

量子门是作用于量子态的酉变换。X门交换0和1；H门将基态变为叠加态；当控制位为1时，CNOT门翻转目标位。先对第一个量子比特施加H门，再施加CNOT，可得到贝尔态 $(|00\rangle+|11\rangle)/\sqrt{2}$。其测量结果具有相关性，但纠缠不能用于超光速传递信息。

## 安装Qiskit并构造贝尔态电路

Qiskit SDK用于创建和转换量子电路。自Qiskit 1.0起，Aer模拟器由单独的 `qiskit-aer` 软件包提供。以下示例使用本机理想模拟器，不模拟真实硬件的噪声或性能。

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

理想模拟只会得到 `00` 和 `11`，随着测量次数增加，计数大致趋于各占一半。有限次采样会有偏差。真实硬件的噪声也可能产生 `01` 或 `10`。解释比特串顺序时，请核对经典寄存器的约定。

## 关于算法加速

Deutsch–Jozsa算法的一次预言机调用结论，是在函数满足“常数或均衡”的承诺并假设预言机理想时，对查询复杂度的描述。Grover搜索在N个无结构候选项中寻找标记项，需要 $O(\sqrt{N})$ 次理想预言机调用。这不表示所有数据库任务都会按该比例加速。

## 参考资料

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
