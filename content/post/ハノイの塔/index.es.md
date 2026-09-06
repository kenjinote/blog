---





title: "La Torre de Hanói"
date: 2025-04-17T22:23:14+09:00
tags: ["La Torre de Hanói", "Algoritmo", "Python"]
draft: false
image: "img.png"
categories: ["Programación"]
---






# La Torre de Hanói

¡Hola!

Hoy me gustaría explicar sobre "La Torre de Hanói" junto con un programa de ejemplo en Python.

---

## ¿Qué es La Torre de Hanói?

La Torre de Hanói es un rompecabezas que usa 3 varillas y varios discos. Los discos tienen diferentes tamaños y, al principio, están apilados en una sola varilla en orden de tamaño de mayor a menor. Las reglas son las siguientes:

1. Solo se puede mover un disco a la vez.
2. No se puede colocar un disco más grande sobre uno más pequeño.

Este rompecabezas se considera un material didáctico excelente para aprender el pensamiento recursivo. La recursividad es un método para resolver un problema dividiéndolo en problemas más pequeños del mismo tipo. En la Torre de Hanói, para mover n discos, se repite la operación de mover n-1 discos.

---

## Resolvamos la Torre de Hanói en Python

A continuación, se muestra un código de ejemplo en Python para resolver la Torre de Hanói.

```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# Ejemplo: Mover 3 discos de A a C
hanoi(3, 'A', 'C', 'B')
```

En este código, la función `hanoi` se llama recursivamente y se muestran los pasos para mover los discos. Por ejemplo, para 3 discos, se obtiene la siguiente salida:

```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

De esta manera, al usar un enfoque recursivo, se pueden resolver problemas complejos de forma sencilla.

---

## ¿Cuánto tiempo se tarda en mover 64 discos?

El número de movimientos en la Torre de Hanói requiere al menos 2^n - 1 veces. Es decir, para mover 64 discos, se necesitan 2^64 - 1 veces, aproximadamente 1.84×10^19 movimientos. Incluso si pudieras mover uno por segundo, tomaría unos 584,900 millones de años. Esto es aproximadamente 42 veces la edad del universo (unos 13,700 millones de años).

Así, a medida que aumenta el número de discos, el número de movimientos necesarios aumenta exponencialmente. Por lo tanto, no es realista mover 64 discos en la práctica.

---

## Resumen

La Torre de Hanói es el rompecabezas perfecto para aprender el pensamiento recursivo. Usando Python, puedes implementar fácilmente su solución. Sin embargo, debes tener cuidado porque a medida que aumenta el número de discos, el número de movimientos necesarios aumenta drásticamente.

Al comprender el enfoque recursivo y escribir el código tú mismo, puedes mejorar tus habilidades de programación. ¡Por favor, intenta el desafío de la Torre de Hanói!

---
