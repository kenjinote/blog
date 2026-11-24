---
title: "La conjetura P ≠ NP: un problema abierto de complejidad"
slug: "Conjetura P≠NP"
tags: ["Conjetura P≠NP", "Matemáticas", "Problemas no resueltos"]
draft: false
categories: ["math-cryptography-quantum"]
description: "Introducción a P, NP, los certificados de longitud polinómica, SAT y la pregunta abierta de si P es igual a NP."
image: eyecatch.jpg
date: 2024-09-11T02:22:39+09:00
lastmod: 2026-11-24
---
# ¿Qué son P y NP?

**P** es la clase de problemas de decisión que pueden resolverse en tiempo polinómico respecto del tamaño de la entrada. **NP** es la clase de problemas de decisión para los que cada instancia con respuesta sí tiene un certificado (una solución propuesta) de longitud acotada por un polinomio del tamaño de la entrada, cuya validez puede comprobarse en tiempo polinómico. Todo problema de P también se puede verificar en tiempo polinómico, por lo que **P ⊆ NP**.

## SAT como ejemplo

SAT pregunta si una fórmula booleana dada tiene una asignación que la hace verdadera. Para una instancia afirmativa, la asignación es el certificado: comprobar que satisface cada cláusula requiere tiempo polinómico en el tamaño de la fórmula. SAT, incluido 3-SAT, es NP-completo. Por tanto, un algoritmo de tiempo polinómico para SAT implicaría **P = NP**. NP-completo significa que todo problema de NP se puede reducir a ese problema en tiempo polinómico.

## La pregunta abierta

Aún no se sabe si **P = NP** o **P ≠ NP**. El Clay Mathematics Institute clasifica P vs. NP como no resuelto. P≠NP es una conjetura ampliamente estudiada, no un teorema demostrado. En términos sencillos, se pregunta si todo problema cuya solución propuesta puede verificarse eficientemente también puede resolverse eficientemente.

## Referencias

- [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)
- [Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)
