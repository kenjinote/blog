---
title: "Die P-NP-Frage: ein offenes Problem der Komplexitätstheorie"
slug: "P≠NP-Vermutung"
tags: ["P≠NP-Vermutung", "Mathematik", "Ungelöste Probleme"]
draft: false
categories: ["math-cryptography-quantum"]
description: "Einführung in P, NP, polynomial lange Zertifikate, SAT und die offene Frage, ob P gleich NP ist."
image: eyecatch.jpg
date: 2024-09-11T02:22:39+09:00
lastmod: 2026-11-24
---
# Was sind P und NP?

**P** ist die Klasse der Entscheidungsprobleme, die in Polynomialzeit bezüglich der Eingabelänge lösbar sind. **NP** ist die Klasse der Entscheidungsprobleme, bei denen jede Ja-Instanz ein Zertifikat (einen Lösungsvorschlag) besitzt, dessen Länge durch ein Polynom der Eingabelänge beschränkt ist und das in Polynomialzeit überprüft werden kann. Eine Lösung für ein Problem in P lässt sich ebenfalls in Polynomialzeit prüfen; daher gilt **P ⊆ NP**.

## SAT als Beispiel

SAT fragt, ob es eine Variablenbelegung gibt, die eine gegebene boolesche Formel erfüllt. Bei einer Ja-Instanz ist diese Belegung das Zertifikat; die Prüfung aller Klauseln benötigt polynomielle Zeit in der Formellänge. SAT, einschließlich 3-SAT, ist NP-vollständig. Ein Polynomialzeitalgorithmus für SAT würde daher **P = NP** implizieren. NP-vollständig bedeutet, dass sich jedes Problem aus NP in Polynomialzeit auf dieses Problem reduzieren lässt.

## Die offene Frage

Ob **P = NP** oder **P ≠ NP** gilt, ist weiterhin offen. Das Clay Mathematics Institute führt P vs. NP als ungelöst. P≠NP ist eine viel untersuchte Vermutung, kein bewiesener Satz. Vereinfacht lautet die Frage: Kann jedes Problem, dessen Lösungsvorschlag effizient überprüfbar ist, auch effizient gelöst werden?

## Quellen

- [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)
- [Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)
