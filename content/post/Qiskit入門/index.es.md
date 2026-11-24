---
title: "Introducción a la programación cuántica con Qiskit"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "Aprende los conceptos de qubits, medición y entrelazamiento, y simula un estado de Bell con Qiskit y AerSimulator actuales."
lastmod: 2026-11-24
---
# Fundamentos de la programación cuántica

Las computadoras cuánticas calculan manipulando estados que obedecen la mecánica cuántica. No aceleran todos los problemas: las ventajas conocidas se aplican a problemas y supuestos específicos. El rendimiento práctico depende del algoritmo, el hardware, el ruido y la corrección de errores.

## Qubits y medición

El estado puro de un qubit se expresa como $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, con $|\alpha|^2+|\beta|^2=1$. Al medir en la base computacional, se obtiene 0 o 1 con probabilidades $|\alpha|^2$ y $|\beta|^2$. El vector de estado de n qubits tiene $2^n$ amplitudes, pero eso no permite leer $2^n$ respuestas de una vez ni hace exponencialmente más rápido cualquier cálculo.

## Puertas y entrelazamiento

Las puertas cuánticas son transformaciones unitarias de los estados. X intercambia 0 y 1; H lleva un estado base a una superposición; CNOT invierte el objetivo cuando el control es 1. Aplicar H al primer qubit y después CNOT produce el estado de Bell $(|00\rangle+|11\rangle)/\sqrt{2}$. Sus mediciones están correlacionadas, pero el entrelazamiento no permite transmitir información más rápido que la luz.

## Instalar Qiskit y crear un circuito de Bell

El SDK de Qiskit sirve para crear y transformar circuitos. Desde Qiskit 1.0, Aer se distribuye por separado como `qiskit-aer`. El ejemplo usa un simulador local ideal; no reproduce el ruido ni el rendimiento del hardware real.

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

En una simulación ideal solo aparecen `00` y `11`, con recuentos que se aproximan a la mitad al aumentar los tiros. El muestreo finito puede variar. El ruido del hardware también puede producir `01` o `10`. Comprueba la convención del registro clásico al interpretar el orden de los bits.

## Sobre la velocidad de los algoritmos

El resultado de una consulta de Deutsch–Jozsa es de complejidad de consultas y presupone que la función promete ser constante o equilibrada, además de un oráculo ideal. Grover puede encontrar un elemento marcado entre N candidatos sin estructura en $O(\sqrt{N})$ consultas ideales al oráculo. Esto no significa que toda tarea con bases de datos se acelere en esa proporción.

## Referencias

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
