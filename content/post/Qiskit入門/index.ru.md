---
title: "Введение в квантовое программирование с Qiskit"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "Изучите кубиты, измерение и запутанность, затем смоделируйте состояние Белла в актуальных Qiskit и AerSimulator."
lastmod: 2026-11-24
---
# Основы квантового программирования

Квантовые компьютеры выполняют вычисления, управляя состояниями, подчиняющимися квантовой механике. Они не ускоряют все задачи: известные преимущества относятся к определённым задачам и предположениям. Практическая производительность зависит от алгоритма, оборудования, шума и коррекции ошибок.

## Кубиты и измерение

Чистое состояние одного кубита записывается как $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, где $|\alpha|^2+|\beta|^2=1$. Измерение в вычислительном базисе даёт 0 или 1 с вероятностями $|\alpha|^2$ и $|\beta|^2$. Вектор состояния n кубитов содержит $2^n$ амплитуд, но это не позволяет сразу прочитать $2^n$ ответов и не ускоряет произвольные вычисления экспоненциально.

## Гейты и запутанность

Квантовые гейты — унитарные преобразования состояний. X меняет 0 и 1 местами; H переводит базисное состояние в суперпозицию; CNOT меняет целевой кубит, если управляющий равен 1. Применение H к первому кубиту, а затем CNOT создаёт состояние Белла $(|00\rangle+|11\rangle)/\sqrt{2}$. Результаты измерений коррелированы, но запутанность не позволяет передавать информацию быстрее света.

## Установка Qiskit и создание схемы Белла

SDK Qiskit используют для создания и преобразования схем. Начиная с Qiskit 1.0, Aer распространяется отдельно в пакете `qiskit-aer`. Пример использует идеальный локальный симулятор и не воспроизводит шум или производительность реального оборудования.

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

В идеальной симуляции появляются только `00` и `11`, а при увеличении числа измерений их частоты приближаются к половине. Конечная выборка может быть неравномерной. Шум оборудования может также приводить к `01` или `10`. При чтении порядка битов учитывайте соглашение классического регистра.

## Об ускорении алгоритмов

Результат одного вызова оракула в алгоритме Deutsch–Jozsa относится к сложности запросов и предполагает обещание, что функция постоянна или сбалансирована, а оракул идеален. Поиск Гровера находит помеченный элемент среди N неструктурированных вариантов за $O(\sqrt{N})$ идеальных вызовов оракула. Это не означает, что любая задача с базой данных ускоряется в такой пропорции.

## Источники

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
