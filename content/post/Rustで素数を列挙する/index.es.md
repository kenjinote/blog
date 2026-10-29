---
title: 'Ejemplo de código y creación de un programa en Rust para enumerar números primos'
slug: "RustでNúmero primoを列挙する"
tags: ["Rust","números primos","algoritmos"]
draft: false
image: "images/img.webp"
categories: ["programming"]
description: "Enumera primos en Rust con división por primos conocidos. Límites pequeños, corte en la raíz cuadrada, iteración del vector e incrementos dentro del rango."
date: 2022-09-09T07:08:49+09:00
lastmod: 2026-10-29
---

Este ejemplo de Rust guarda los primos encontrados y los usa para la división por tentativa. `primes_up_to(max)` devuelve la lista de primos hasta el límite, incluido. Hay 168 primos menores o iguales a 1000; 0 y 1 no son primos. No es una implementación de la criba.

## Código

```rust
fn primes_up_to(max: usize) -> Vec<usize> {
    if max < 2 {
        return Vec::new();
    }
    let mut primes = vec![2];
    let mut n = 3;
    while n <= max {
        let mut is_prime = true;
        for &p in &primes {
            if p > n / p {
                break;
            }
            if n % p == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            primes.push(n);
        }
        if max - n < 2 {
            break;
        }
        n += 2;
    }
    primes
}

fn main() {
    for p in primes_up_to(1000) {
        println!("{}", p);
    }
}
```

## Ejecución y límites pequeños

Guarda como `primes.rs` y compila con `rustc --edition=2021 primes.rs -o primes`. En Windows, usa `primes.exe` como nombre del ejecutable. Imprime 168 líneas, desde 2 en la primera hasta 997 en la última. Estos ejemplos se ejecutaron con Rust 1.90.0.

`primes_up_to(0)` y `primes_up_to(1)` devuelven un vector vacío; `primes_up_to(2)` devuelve `[2]`, `primes_up_to(3)` devuelve `[2, 3]`, y `primes_up_to(10)` devuelve `[2, 3, 5, 7]`. El tipo del parámetro, `usize`, excluye los límites negativos. Este programa no analiza la entrada estándar.

## Funcionamiento de la prueba y del bucle

1. Devuelve un resultado vacío si el límite es menor que 2. En otro caso guarda 2 y comprueba solo candidatos impares desde 3 hasta el límite. Se comprueba el límite antes de procesar cada candidato, por lo que el límite 2 no añade 3.
2. Un candidato compuesto `n` tiene un factor primo menor o igual que su raíz cuadrada. Esos primos ya están en la lista gracias a los candidatos anteriores. Si una división no deja resto, se rechaza el candidato. Si no se ha encontrado un divisor al llegar a `p > n / p`, no hace falta seguir dividiendo. La división entera positiva expresa la condición de la raíz cuadrada sin calcular `p * p` ni una raíz en coma flotante.
3. `for &p in &primes` toma prestada la lista, recibe referencias sucesivas y copia cada valor `usize` en `p`. Solo se añade un primo nuevo cuando termina este bucle. El `for p in primes_up_to(1000)` final toma los valores del vector devuelto y los imprime. La [documentación de Vec de Rust](https://doc.rust-lang.org/std/vec/struct.Vec.html) distingue la iteración prestada de la que consume el vector del que se tiene la propiedad.
4. Dentro de `n <= max`, `max - n` no puede ser negativo. Si la distancia restante es menor que 2, se sale antes de sumar; en otro caso se ejecuta `n += 2`. Así se evita un incremento que supere el límite.

## Alcance

El programa original con límite fijo 1000 también imprime correctamente 168 primos. Sin embargo, cambiar únicamente el límite a 0, 1 o 2 imprime valores 2 o 3 fuera del rango, porque no se comprueba el límite antes del procesamiento. La función reutilizable de aquí trata esas fronteras.

La lista guarda un `usize` por primo descubierto. Los metadatos del vector y la capacidad reservada también necesitan memoria. Una cota superior aproximada de divisiones es `O(max sqrt(max))`, contando cada división como una operación; no es tiempo medido ni complejidad en bits. Los límites mayores requieren más tiempo y almacenamiento, sin garantía de enumerar rápidamente primos hasta límites arbitrariamente grandes. Para intervalos grandes, consulta el [artículo de la criba de Eratóstenes](https://kenji.blog/es/p/criba-de-erat%C3%B3stenes%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A61000%E4%BB%A5%E4%B8%8B%E3%81%AEn%C3%BAmero-primo%E3%82%92%E5%88%97%E6%8C%99%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/). No es un generador de primos criptográficos.
