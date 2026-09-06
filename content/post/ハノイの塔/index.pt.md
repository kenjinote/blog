---
title: "Torre de Hanói"
slug: "torre-de-hanoi"
date: 2025-04-17T22:23:14+09:00
tags: ["Torre de Hanói", "Algoritmo", "Python"]
draft: false
image: "img.png"
categories: ["Programação"]
---

# Torre de Hanói

Olá!

Hoje, gostaria de explicar sobre a "Torre de Hanói", usando um programa de exemplo em Python.

---

## O que é a Torre de Hanói?

A Torre de Hanói é um quebra-cabeça que usa 3 hastes e vários discos. Os discos têm tamanhos diferentes e, no início, estão empilhados em uma haste em ordem decrescente de tamanho. As regras são as seguintes:

1. Apenas um disco pode ser movido por vez.
2. Não é possível colocar um disco maior em cima de um disco menor.

Este quebra-cabeça é considerado um excelente material de ensino para aprender o pensamento recursivo. A recursividade é um método de resolver um problema dividindo-o em problemas menores do mesmo tipo. Na Torre de Hanói, para mover n discos, repete-se a operação de mover n-1 discos.

---

## Vamos resolver a Torre de Hanói com Python

Abaixo está um código de exemplo para resolver a Torre de Hanói em Python.

```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# Exemplo: Mover 3 discos de A para C
hanoi(3, 'A', 'C', 'B')
```

Neste código, a função `hanoi` é chamada recursivamente e os passos para mover os discos são exibidos. Por exemplo, no caso de 3 discos, a seguinte saída é obtida:

```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

Desta forma, ao usar uma abordagem recursiva, problemas complexos podem ser resolvidos de forma simples.

---

## Quanto tempo leva para mover 64 discos?

O número de movimentos na Torre de Hanói requer no mínimo 2^n - 1 vezes. Ou seja, para mover 64 discos, são necessários 2^64 - 1 movimentos, o que dá aproximadamente 1,84×10^19 movimentos. Mesmo que você pudesse mover um por segundo, levaria cerca de 584 bilhões de anos. Isso é cerca de 42 vezes a idade do universo (aproximadamente 13,7 bilhões de anos).

Desta forma, conforme o número de discos aumenta, o número necessário de movimentos aumenta exponencialmente. Portanto, mover 64 discos na prática não é realista.

---

## Resumo

A Torre de Hanói é um quebra-cabeça perfeito para aprender o pensamento recursivo. Com Python, você pode facilmente implementar a sua solução. No entanto, é preciso ter cuidado, pois à medida que o número de discos aumenta, o número de movimentos necessários aumenta drasticamente.

Ao entender a abordagem recursiva e tentar escrever código de fato, você pode melhorar suas habilidades de programação. Por favor, experimente enfrentar o desafio da Torre de Hanói.

--- 
