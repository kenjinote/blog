---


title: "Cómo enumerar los números primos hasta 1000 usando la criba de Eratóstenes"
date: 2023-04-09T12:54:24+09:00
tags: ["Criba de Eratóstenes", "Números primos", "Matemáticas", "Rust"]
draft: false
math: true
image: "img.png"
categories: ["Matemáticas・Criptografía・Cuántica"]
---



## ¿Qué es la criba de Eratóstenes?

La criba de Eratóstenes es un algoritmo para enumerar los números primos menores o iguales a un cierto número.
El algoritmo es simple y se puede implementar con los siguientes pasos:

1. Crear un arreglo de valores booleanos de tamaño N e inicializar todos los elementos a true.
2. Establecer el 0º y 1º elemento del arreglo a false (porque 0 y 1 no son primos).
3. Si el 2º elemento del arreglo es true, mostrar 2 como número primo.
4. Establecer a false todos los elementos del arreglo que sean múltiplos de 2 mayores o iguales a $2^2$*.
5. Si el 3º elemento del arreglo es true, mostrar 3 como número primo.
6. Establecer a false todos los elementos del arreglo que sean múltiplos de 3 mayores o iguales a $3^2$.
7. Repetir el mismo proceso para el 4º, 5º, ..., N-ésimo elemento.

*Se dirigen los elementos a partir del cuadrado para convertirlos a false porque los números más pequeños que el cuadrado ya han sido procesados (su enumeración se ha completado).

![](Animation_Sieb_des_Eratosthenes.gif)


## Implementación en Rust

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![true; n+1];
    is_prime[0] = false;
    is_prime[1] = false;
    for i in 2..=n {
        if is_prime[i] {
            println!("{}", i);
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i;
            }
        }
    }
}
```

## Una versión un poco más rápida

Realizaremos una implementación ligeramente más rápida considerando los siguientes puntos:

- Inicializar el arreglo a false en lugar de true (esto es más rápido).
- Omitir el proceso de establecer en false los elementos múltiplos de 2, ya que no son primos.
- No es necesario iterar hasta n; si enumeramos los primos hasta la raíz cuadrada de n, podremos enumerar todos los primos menores o iguales a n.

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![false; n+1];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }
    for i in 3..=((n as f64).sqrt() as usize) {
        if is_prime[i] {
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i * 2;
            }
        }
    }
    for i in (2..=n).filter(|&x| is_prime[x]) {
        println!("{}", i);
    }
}
```

## Referencia
- [Criba de Eratóstenes](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)
