---
title: "Introduction à la programmation quantique avec Qiskit"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "Découvrez les qubits, la mesure et l’intrication, puis simulez un état de Bell avec les versions actuelles de Qiskit et AerSimulator."
lastmod: 2026-11-24
---
# Bases de la programmation quantique

Les ordinateurs quantiques calculent en manipulant des états régis par la mécanique quantique. Ils n’accélèrent pas tous les problèmes : les accélérations connues concernent des problèmes et des hypothèses spécifiques. Les performances pratiques dépendent de l’algorithme, du matériel, du bruit et de la correction d’erreurs.

## Qubits et mesure

L’état pur d’un qubit s’écrit $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, avec $|\alpha|^2+|\beta|^2=1$. Une mesure dans la base computationnelle renvoie 0 ou 1 avec les probabilités $|\alpha|^2$ et $|\beta|^2$. Le vecteur d’état de n qubits comporte $2^n$ amplitudes, mais cela ne permet pas de lire $2^n$ réponses à la fois et ne rend pas tout calcul exponentiellement plus rapide.

## Portes et intrication

Les portes quantiques sont des transformations unitaires des états. X échange 0 et 1 ; H transforme un état de base en superposition ; CNOT inverse la cible lorsque le contrôle vaut 1. Appliquer H au premier qubit puis CNOT produit l’état de Bell $(|00\rangle+|11\rangle)/\sqrt{2}$. Les mesures sont corrélées, mais l’intrication ne permet pas de transmettre de l’information plus vite que la lumière.

## Installer Qiskit et créer un circuit de Bell

Le SDK Qiskit sert à créer et transformer des circuits. Depuis Qiskit 1.0, Aer est distribué séparément dans `qiskit-aer`. L’exemple utilise un simulateur local idéal ; il ne reproduit ni le bruit ni les performances d’un matériel réel.

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

Une simulation idéale ne produit que `00` et `11`, avec des comptes qui tendent vers la moitié chacun lorsque le nombre de tirs augmente. Un échantillon fini peut être déséquilibré. Le bruit matériel peut aussi produire `01` ou `10`. Vérifiez la convention du registre classique pour interpréter l’ordre des bits.

## À propos de l’accélération des algorithmes

Le résultat d’une requête de Deutsch–Jozsa relève de la complexité des requêtes et suppose que la fonction promise est constante ou équilibrée, ainsi qu’un oracle idéal. Grover trouve un élément marqué parmi N candidats non structurés en $O(\sqrt{N})$ appels idéaux à l’oracle. Cela ne signifie pas que toute tâche sur une base de données s’accélère dans cette proportion.

## Références

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
