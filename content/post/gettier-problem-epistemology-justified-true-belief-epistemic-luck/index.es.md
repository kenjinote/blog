---
title: "¿Se puede creer por buenas razones y acertar por casualidad sin 'saber'?：El problema de Gettier y la definición del conocimiento"
slug: "gettier-problem-epistemology-justified-true-belief-epistemic-luck"
date: 2026-10-14T01:00:00+09:00
image: "eyecatch.jpg"
math: true
draft: false
tags: ["Filosofía", "Epistemología", "Problema de Gettier", "Creencia verdadera justificada", "Suerte epistémica", "Filosofía contemporánea", "Epistemología de la IA"]
categories: ["Filosofía"]
description: "¿Cómo es posible que una creencia esté racionalmente justificada y sea objetivamente verdadera sin constituir auténtico conocimiento? En 1963, un artículo de tres páginas de Edmund Gettier demolió la definición platónica del conocimiento (teoría JTB). Del seguimiento de la verdad de Nozick a las alucinaciones de la IA actual."
---

## Introducción: El artículo de tres páginas que derribó una catedral milenaria

En la vida cotidiana empleamos el verbo «saber» con absoluta ligereza y certeza:
- «Sé que está lloviendo» (porque veo el agua caer en la calle);
- «Sé que la Tierra gira alrededor del Sol» (gracias a la evidencia astronómica acumulada);
- «Sé que $2 + 3 = 5$» (en virtud de las leyes de la aritmética elemental).

Sin embargo, desde el rigor filosófico: <strong>¿qué significa exactamente que un sujeto 'sepa' una proposición? ¿Cuáles son las condiciones necesarias y suficientes del conocimiento?</strong>

Desde los diálogos platónicos *Teeteto* y *Menón*, la filosofía occidental abrazó la definición tripartita de la <strong>Creencia Verdadera Justificada (JTB, por sus siglas en inglés: Justified True Belief)</strong>:
Un sujeto $S$ sabe que $P$ si y solo si:
1. <strong>Creencia</strong>: $S$ cree firmemente que $P$ ($B_S(P)$);
2. <strong>Verdad</strong>: $P$ es objetivamente verdadera ($P = \text{Verdadero}$);
3. <strong>Justificación</strong>: $S$ posee razones racionales y pruebas suficientes para creer que $P$ ($J_S(P)$).

```mermaid
flowchart TD
    subgraph JTB ["Definición clásica del conocimiento (JTB)"]
        direction LR
        J["Justificación (J)<br/>Evidencia racional suficiente"] --- T["Verdad (T)<br/>Realidad objetiva comprobable"]
        T --- B["Creencia (B)<br/>Convicción mental del sujeto"]
    end
    JTB ==>|Intersección de las tres| K["Conocimiento (K)<br/>S sabe que P"]
end
```

Durante más de dos mil años, esta definición pareció incontrovertible: adivinar por azar carece de justificación; creer una falsedad carece de verdad.

Pero en <strong>junio de 1963</strong>, un artículo de <strong>apenas tres páginas</strong> publicado por el filósofo estadounidense <strong>Edmund L. Gettier (1927–2021)</strong> en la revista *Analysis* destruyó este dogma: *«Is Justified True Belief Knowledge?»*. Gettier construyó contraejemplos matemáticamente irrefutables donde las tres condiciones se cumplen a la perfección, pero donde nadie en su sano juicio aceptaría que existe auténtico conocimiento.

---

## 1. Los contraejemplos originales de Gettier

### Caso 1: Smith, Jones y las diez monedas
Smith y Jones aspiran al mismo puesto laboral. El presidente de la compañía asegura a Smith que Jones obtendrá el trabajo. Además, Smith vio a Jones contar diez monedas en su bolsillo. Smith infiere lógicamente:
> *(e) El hombre que obtendrá el trabajo tiene diez monedas en el bolsillo.*

Inesperadamente, la junta directiva contrata a <strong>Smith</strong>. Y sin que Smith lo supiera, él mismo llevaba <strong>exactamente diez monedas</strong> en su pantalón.
La proposición *(e)* es verdadera, creída y plenamente justificada. ¿Pero lo sabía Smith? <strong>¡No!</strong> Fue un acierto por pura coincidencia cósmica.

---

## 2. La raíz patológica: La suerte epistémica (Epistemic Luck)

Los casos de Gettier se caracterizan por una estructura de doble azar:
1. <strong>Mala suerte inicial</strong>: la premisa de la que parte la justificación es falsa (Jones no es contratado);
2. <strong>Buena suerte compensatoria</strong>: un hecho imprevisto e independiente rescata la proposición y la hace verdadera (Smith tiene diez monedas).
El azar cancela la conexión genuina entre el esfuerzo intelectual del sujeto y la realidad ontológica del mundo.

---

## 3. En busca de la cuarta condición

- <strong>Sin premisas falsas (No False Lemmas)</strong>: Prohíbe basarse en premisas erróneas. Fracasa ante el dilema del <strong>reloj parado</strong> (mirar por casualidad a las 8:20 un reloj averiado hace 24 horas).
- <strong>Teoría causal de Goldman</strong>: Exige un vínculo causal directo. Fue refutada por el experimento mental del <strong>país de las granjas falsas (Fake Barn Country)</strong> de Ginet y Goldman.
- <strong>Rastreo de la verdad de Nozick (Truth-Tracking)</strong>: Demanda que la creencia sea sensible a mundos posibles contrafácticos: «si $P$ no fuera verdad, $S$ no creería que $P$».

---

## 4. Epistemología de las virtudes y el dilema de la IA

- <strong>El modelo AAA de Ernest Sosa</strong>: El conocimiento equivale a un disparo certero en tiro con arco: certero (Accurate), diestro (Adroit) y oportuno (Apt), donde el éxito se atribuye a la competencia y virtud del agente, no a una ráfaga de viento favorable.
- <strong>Modelos masivos de lenguaje (LLM)</strong>: Las inteligencias artificiales actuales generan respuestas médicamente correctas a partir de alucinaciones intermedias, comportándose como gigantescas máquinas de Gettier sin anclaje semántico en la realidad.

## Conclusión

El problema de Gettier evidencia la fragilidad de la razón humana: creer con justificación y acertar no basta para conocer. El auténtico conocimiento exige desterrar la suerte y forjar un vínculo irrompible con la verdad.
