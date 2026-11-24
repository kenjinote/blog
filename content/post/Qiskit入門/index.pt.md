---
title: "Introdução à programação quântica com Qiskit"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "Conheça qubits, medição e emaranhamento e simule um estado de Bell com as versões atuais do Qiskit e AerSimulator."
lastmod: 2026-11-24
---
# Fundamentos da programação quântica

Computadores quânticos calculam manipulando estados regidos pela mecânica quântica. Eles não aceleram todos os problemas: as vantagens conhecidas valem para problemas e hipóteses específicos. O desempenho prático depende do algoritmo, do hardware, do ruído e da correção de erros.

## Qubits e medição

O estado puro de um qubit é $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, com $|\alpha|^2+|\beta|^2=1$. Uma medição na base computacional retorna 0 ou 1 com probabilidades $|\alpha|^2$ e $|\beta|^2$. O vetor de estado de n qubits tem $2^n$ amplitudes, mas isso não permite ler $2^n$ respostas de uma só vez nem torna qualquer cálculo exponencialmente mais rápido.

## Portas e emaranhamento

Portas quânticas são transformações unitárias dos estados. X troca 0 e 1; H transforma um estado da base em superposição; CNOT inverte o alvo quando o controle é 1. Aplicar H ao primeiro qubit e depois CNOT produz o estado de Bell $(|00\rangle+|11\rangle)/\sqrt{2}$. As medições são correlacionadas, mas o emaranhamento não transmite informação mais rápido que a luz.

## Instalar Qiskit e criar um circuito de Bell

O SDK Qiskit cria e transforma circuitos. Desde o Qiskit 1.0, Aer é distribuído separadamente pelo pacote `qiskit-aer`. O exemplo usa um simulador local ideal e não reproduz o ruído nem o desempenho de hardware real.

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

Na simulação ideal, só aparecem `00` e `11`; com mais medições, as contagens tendem a ficar próximas da metade para cada resultado. Uma amostra finita pode variar. O ruído do hardware também pode produzir `01` ou `10`. Confira a convenção do registrador clássico para interpretar a ordem dos bits.

## Sobre aceleração de algoritmos

O resultado de uma consulta do algoritmo Deutsch–Jozsa é uma afirmação de complexidade de consultas e pressupõe a promessa de que a função é constante ou balanceada e um oráculo ideal. Grover encontra um item marcado entre N candidatos não estruturados com $O(\sqrt{N})$ consultas ideais ao oráculo. Isso não significa que toda tarefa de banco de dados terá aceleração nessa proporção.

## Referências

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
