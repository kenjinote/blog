---
title: "An Introduction to Quantum Programming with Qiskit"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "Learn the basics of qubits, measurement, and entanglement, then simulate a Bell state with current Qiskit and AerSimulator."
lastmod: 2026-11-24
---
# Quantum-programming basics

Quantum computers process states governed by quantum mechanics. They do not solve every problem faster: speedups are known for particular problems under particular assumptions. Practical performance depends on the algorithm, hardware, noise, and error correction.

## Qubits and measurement

A pure state of one qubit is $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, with $|\alpha|^2+|\beta|^2=1$. Measurement in the computational basis returns 0 or 1 with probabilities $|\alpha|^2$ and $|\beta|^2$. An n-qubit state vector has $2^n$ amplitudes, but that does not let us read out $2^n$ answers at once or make arbitrary computations exponentially faster.

## Gates and entanglement

Quantum gates are unitary transformations on quantum states. X swaps 0 and 1; H creates a superposition from a basis state; CNOT flips its target when its control is 1. Applying H to the first qubit and then CNOT produces the Bell state $(|00\rangle+|11\rangle)/\sqrt{2}$. Its measurement outcomes are correlated, but entanglement cannot transmit information faster than light.

## Install Qiskit and build a Bell circuit

The Qiskit SDK creates and transforms circuits. Since Qiskit 1.0, Aer is a separate package, `qiskit-aer`. This example uses an ideal local simulator; it does not model hardware noise or hardware performance.

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

In an ideal simulation, only `00` and `11` occur, with counts approaching an even split as the number of shots increases. Finite sampling can be uneven. Hardware noise can also produce `01` or `10`. Check the classical-register convention when interpreting bit-string order.

## About algorithmic speedups

The one-query Deutsch–Jozsa result is a query-complexity statement under the promise that the function is constant or balanced and assuming an ideal oracle. Grover search can find a marked item among N unstructured candidates with $O(\sqrt{N})$ ideal oracle calls. This does not mean every database task becomes faster by that factor.

## References

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
