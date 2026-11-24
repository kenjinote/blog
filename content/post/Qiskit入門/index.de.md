---
title: "Einführung in Quantenprogrammierung mit Qiskit"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "Lernen Sie Qubits, Messung und Verschränkung kennen und simulieren Sie einen Bell-Zustand mit aktuellem Qiskit und AerSimulator."
lastmod: 2026-11-24
---
# Grundlagen der Quantenprogrammierung

Quantencomputer berechnen durch Manipulation von Zuständen, die der Quantenmechanik folgen. Sie beschleunigen nicht jedes Problem; bekannte Vorteile gelten für bestimmte Probleme und Voraussetzungen. Die praktische Leistung hängt von Algorithmus, Hardware, Rauschen und Fehlerkorrektur ab.

## Qubits und Messung

Ein reiner Qubit-Zustand lautet $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, wobei $|\alpha|^2+|\beta|^2=1$ gilt. Eine Messung in der Rechenbasis liefert 0 oder 1 mit den Wahrscheinlichkeiten $|\alpha|^2$ und $|\beta|^2$. Der Zustandsvektor von n Qubits hat $2^n$ Amplituden. Das bedeutet jedoch weder, dass sich $2^n$ Antworten auf einmal auslesen lassen, noch dass jede Berechnung exponentiell schneller wird.

## Gatter und Verschränkung

Quantengatter sind unitäre Transformationen von Quantenzuständen. X vertauscht 0 und 1; H überführt einen Basiszustand in eine Superposition; CNOT invertiert das Ziel, wenn das Steuerbit 1 ist. H auf dem ersten Qubit und danach CNOT erzeugen den Bell-Zustand $(|00\rangle+|11\rangle)/\sqrt{2}$. Die Messergebnisse sind korreliert, doch Verschränkung kann keine Information schneller als Licht übertragen.

## Qiskit installieren und einen Bell-Schaltkreis erstellen

Das Qiskit-SDK erstellt und transformiert Schaltkreise. Seit Qiskit 1.0 wird Aer separat als `qiskit-aer` bereitgestellt. Das Beispiel nutzt einen idealen lokalen Simulator und bildet weder Hardware-Rauschen noch reale Hardware-Leistung ab.

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

In der idealen Simulation treten nur `00` und `11` auf; mit mehr Messungen nähern sich die Häufigkeiten jeweils der Hälfte. Bei endlicher Stichprobe kann es Abweichungen geben. Hardware-Rauschen kann auch `01` oder `10` erzeugen. Beachten Sie beim Lesen der Bitreihenfolge die Konvention des klassischen Registers.

## Zur Beschleunigung von Algorithmen

Das Ergebnis einer Abfrage beim Deutsch-Jozsa-Algorithmus gilt im Abfragekomplexitätsmodell: Die Funktion muss als konstant oder ausgeglichen versprochen sein, und das Orakel gilt als ideal. Grover findet ein markiertes Element unter N unstrukturierten Kandidaten mit $O(\sqrt{N})$ idealen Orakelaufrufen. Das bedeutet nicht, dass jede Datenbankaufgabe proportional schneller wird.

## Quellen

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
