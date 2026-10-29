---
title: '¿Qué es la criba de Eratóstenes? Algoritmo e implementación para enumerar números primos hasta 1000'
slug: "Criba de Eratóstenesを使って1000以下のNúmero primoを列挙する方法"
tags: ["Criba de Eratóstenes", "Números primos", "Matemáticas", "Rust"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Enumera los 168 primos hasta 1000 con Rust. Explica el inicio en el cuadrado, los candidatos impares, los límites 0 y 1, la complejidad y la memoria."
date: 2023-04-09T12:54:24+09:00
lastmod: 2026-10-29
---

La criba de Eratóstenes enumera todos los primos hasta un límite superior `n`, incluido. Estos programas en Rust imprimen los 168 primos menores o iguales a 1000. El límite está incluido; 0 y 1 no son primos.

## Pasos de la criba y por qué se empieza en el cuadrado

1. Reserva `n + 1` elementos booleanos para usar los índices de 0 a `n`. La versión básica los inicializa a verdadero y marca 0 y 1 como falsos. Si el límite es menor que 2, devuelve un resultado vacío antes de acceder al índice 1.
2. Examina los candidatos `p` en orden creciente, empezando por 2. Si la marca sigue siendo verdadera, `p` es primo: marca como falsos sus múltiplos desde $p^2$, avanzando de `p` en `p`. No marques el propio `p`.
3. Basta con eliminar múltiplos para los candidatos que cumplen $p^2\le n$, porque todo compuesto tiene un factor primo menor o igual que su raíz cuadrada.
4. Al final, recorre de 2 a `n` e imprime todos los números que conservan la marca verdadera. El rango de salida no se limita a la raíz cuadrada.

Un múltiplo $kp$ menor que $p^2$, con $2\le k<p$, ya fue eliminado por un factor primo de `k` menor que `p`. Esto no significa que todos los números menores ya se hayan enumerado.

![Animación de la criba con los números de 2 a 120](Animation_Sieb_des_Eratosthenes.gif)

Imagen: SKopp, versión actualizada por Suricata, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). El archivo no se ha modificado. La ilustración abarca de 2 a 120; los programas siguientes usan un límite de 1000.

## Implementación básica en Rust

```rust
fn sieve(n: usize) -> Vec<usize> {
    if n < 2 {
        return Vec::new();
    }
    let len = n.checked_add(1).expect("n + 1 is too large");
    let mut is_prime = vec![true; len];
    is_prime[0] = false;
    is_prime[1] = false;

    let mut p = 2;
    while p <= n / p {
        if is_prime[p] {
            let mut multiple = p * p;
            loop {
                is_prime[multiple] = false;
                if n - multiple < p {
                    break;
                }
                multiple += p;
            }
        }
        p += 1;
    }

    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn main() {
    for prime in sieve(1000) {
        println!("{}", prime);
    }
}
```

Guarda como `sieve.rs` y compila con `rustc --edition=2021 sieve.rs -o sieve`. En Windows, usa `sieve.exe` como nombre del ejecutable. Al ejecutarlo se imprimen 168 líneas: la primera contiene 2 y la última, 997. Estos ejemplos se ejecutaron con Rust 1.90.0.

`sieve(0)` y `sieve(1)` devuelven un vector vacío; `sieve(2)` devuelve `[2]`. La condición `p <= n / p` hace que `p * p` se evalúe solo cuando el cuadrado está dentro del límite. Antes de sumar el siguiente múltiplo se comprueba la distancia restante. No se necesita una raíz cuadrada en coma flotante.

## Versión que elimina solo candidatos impares

Los pares mayores que 2 son compuestos. Podemos marcar 2 como verdadero e inicializar solo los impares como candidatos. Para un primo impar `p`, su cuadrado es impar; avanzar desde él en pasos de $2p$ visita únicamente múltiplos impares.

```rust
fn sieve_odd(n: usize) -> Vec<usize> {
    if n < 2 {
        return Vec::new();
    }
    let len = n.checked_add(1).expect("n + 1 is too large");
    let mut is_prime = vec![false; len];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }

    let mut p = 3;
    while p <= n / p {
        if is_prime[p] {
            let step = 2 * p;
            let mut multiple = p * p;
            loop {
                is_prime[multiple] = false;
                if n - multiple < step {
                    break;
                }
                multiple += step;
            }
        }
        p += 2;
    }

    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn main() {
    for prime in sieve_odd(1000) {
        println!("{}", prime);
    }
}
```

Guarda esta versión en otro archivo y compílala. Imprime los mismos 168 primos, devuelve un resultado vacío para 0 y 1, y `[2]` para 2. No combines los dos `main` en un mismo archivo.

Esta versión omite parte del trabajo con los pares. Sin embargo, inicializar a falso no garantiza mayor velocidad. El tiempo depende de la inicialización, las escrituras, el acceso a memoria, el compilador y la máquina. Aquí no se comparan tiempos medidos. El arreglo sigue teniendo `n + 1` elementos para que los índices correspondan directamente a los números.

## Complejidad y límites de uso

En el modelo RAM habitual, la criba necesita tiempo $O(n\log\log n)$ y espacio $O(n)$ para las marcas. Son estimaciones asintóticas de operaciones y almacenamiento, no tiempos medidos ni complejidad en bits para enteros de precisión arbitraria. El ejercicio de la criba del [material de análisis de Princeton](https://introcs.cs.princeton.edu/java/41analysis/) también indica este crecimiento.

En Rust, [`bool`](https://doc.rust-lang.org/reference/types/boolean.html) ocupa un byte y [`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees) almacena elementos contiguos. Este `Vec<bool>` no es un arreglo de bits empaquetados. Hay `n + 1` marcas lógicas; los metadatos del vector, la capacidad reservada y el `Vec<usize>` devuelto también requieren memoria.

Si no se puede representar `n + 1`, `checked_add` devuelve `None`, y el `expect` que sigue provoca un panic. En los demás casos sigue siendo necesario disponer de suficiente memoria; no se admiten límites arbitrariamente grandes. Para intervalos grandes, considera una criba segmentada. Enumerar primos en un rango tiene un propósito distinto de comprobar un solo entero grande.
