---
title: "La conjetura abc y la teoría IUT: una demostración reivindicada y un debate abierto"
date: "2026-09-14T13:00:00+09:00"
lastmod: 2026-11-23
slug: "abc-conjecture"
image: "eyecatch.jpg"
categories: ["mathematics", "science"]
tags: ["ABC Conjecture", "Number Theory", "IUT Theory", "Shinichi Mochizuki"]
draft: false
description: "Una introducción a la conjetura abc, la demostración que Shinichi Mochizuki afirma obtener con IUT, su publicación en PRIMS y el debate matemático aún no resuelto."
---

## Qué afirma la conjetura abc

Sean $a,b,c$ enteros positivos coprimos dos a dos que cumplen $a+b=c$. El **radical** de un entero positivo $n$ es el producto de sus divisores primos distintos:

$$\operatorname{rad}(n)=\prod_{p\mid n}p$$

Por ejemplo, $\operatorname{rad}(2^3\cdot3^2)=6$. El radical no tiene en cuenta los exponentes de los factores primos y, por eso, puede ser mucho menor que el entero.

La conjetura abc afirma que, para todo $\varepsilon>0$, existe una constante $K_\varepsilon$ tal que todo triple de este tipo satisface

$$c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}.$$

La constante puede depender de $\varepsilon$. Joseph Oesterlé y David Masser formularon la conjetura en 1985. Expresa una fuerte restricción entre la suma y la factorización en primos; no es la regla simple de que los factores primos pequeños de $a$ y $b$ obliguen a que $c$ tenga un factor primo grande.

## La demostración que Mochizuki atribuye a IUT

En 2012, Shinichi Mochizuki, de la Universidad de Kioto, publicó trabajos que presentaban la teoría de Teichmüller interuniversal (IUT) como un nuevo marco para problemas de geometría diofántica, incluida la conjetura abc. IUT es una teoría muy técnica sobre objetos aritméticos, como curvas elípticas sobre cuerpos numéricos, y combina ideas relacionadas con la teoría de Teichmüller, la teoría de Hodge-Arakelov y la geometría anabeliana. Conceptos como los teatros de Hodge y la red log-theta sirven para comparar datos aritméticos entre estructuras. Describirla simplemente como «separar la suma y la multiplicación en universos distintos» sería engañoso.

Mochizuki afirma que abc se deduce de IUT. Los cuatro artículos pasaron por un largo proceso de revisión y aparecieron en un número especial de 2021 de *Publications of the Research Institute for Mathematical Sciences* (PRIMS). Su publicación es un hecho importante, pero no establece por sí sola un consenso matemático ni pone fin al debate.

## Qué sigue en discusión

En un informe de 2018, Peter Scholze y Jakob Stix sostuvieron que hay una laguna en un paso clave —el que va del teorema 3.11 al corolario 3.12 de IUT III, utilizado en el camino hacia la desigualdad abc—. Mochizuki rechaza la crítica por considerarla basada en una lectura errónea de la teoría y expuso de nuevo su postura en un informe de octubre de 2025. Este apartado resume las posiciones declaradas por los autores; no verifica de manera independiente la demostración de IUT.

Por tanto, una explicación cuidadosa distingue tres hechos: los artículos de IUT se publicaron en PRIMS; Mochizuki afirma que prueban abc; y los matemáticos no han resuelto su desacuerdo sobre el argumento central. No es adecuado presentar la conjetura abc como un teorema ampliamente aceptado.

## Relación con el último teorema de Fermat

Si abc fuera cierta, implicaría el último teorema de Fermat: no existen soluciones enteras positivas de $x^n+y^n=z^n$ para $n\ge3$. Es una consecuencia condicional, no significa que el teorema de Fermat siga sin demostrarse: Andrew Wiles y otros ya lo probaron.

Supongamos que existiera una solución $x,y,z$ coprima dos a dos. Para todo entero positivo $k$, $(x^{nk},y^{nk},z^{nk})$ también sería un triple coprimo cuya suma cumple la ecuación. Su radical seguiría siendo el mismo, $\operatorname{rad}(x^{nk}y^{nk}z^{nk})=\operatorname{rad}(xyz)$, mientras que $z^{nk}$ crecería sin límite. Así se obtendrían infinitos triples que violarían la cota abc para cualquier $\varepsilon>0$ fijo, una contradicción.

## Fuentes

- [Formulación estándar de abc (Jordan S. Ellenberg)](https://arxiv.org/abs/math/9909098)
- [Número especial de PRIMS sobre IUT de 2021](https://ems.press/journals/prims/issues/1507)
- [Informe de Scholze y Stix (2018)](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [Informe de IUT de Mochizuki (octubre de 2025)](https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf)
- [Panorama general de IUT (Mochizuki, 2012)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf)

Esta es una introducción breve a la conjetura y a la controversia pública; no reconstruye ni evalúa la demostración de IUT.
