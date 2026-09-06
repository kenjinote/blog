---





title: "Conocimientos básicos de computación"
date: 2024-09-19T01:10:20+09:00
tags: ["Computadora", "Conocimientos básicos"]
draft: false
image: "img.png"
categories: ["IT y Tecnología"]
---






# Conocimientos básicos de computación

Esta página explica qué es una computadora.

## Definición de una computadora
Una computadora es una máquina que tiene los siguientes 5 componentes:

1. Dispositivo de entrada
2. Dispositivo de salida
3. Dispositivo de almacenamiento
4. Dispositivo de control
5. Dispositivo de procesamiento aritmético

En términos generales, una computadora es una máquina que recibe una `entrada`, realiza un `procesamiento` específico y produce una `salida` con el resultado.
Puede `almacenar`, `calcular` y dar como `salida` los datos que se han dado de `entrada`. El `control` tiene la función de gestionar los otros cuatro componentes mencionados.

## Qué se necesita para hacer funcionar una computadora
Para operar una computadora, además de los dispositivos (hardware), se necesitan programas (software).

A través de los programas, se le indica a la computadora qué procesamiento debe realizar. Los programas se escriben en un formato que la computadora puede entender.

Un ejemplo de programa es el siguiente.
Programa para calcular la suma desde 1 hasta un número entero introducido:
```
#include <iostream>
using namespace std;

int main() {
    // Reservar el espacio de memoria necesario
    int n, sum = 0;
    
    // Salida
    cout << "Ingrese un número entero: ";
    
    // Entrada 
    cin >> n;
    
    // Operación aritmética
    for (int i = 1; i <= n; i++) { // Operación aritmética
        sum += i;
    }
    
    // Salida
    cout << "La suma desde 1 hasta " << n << " es " << sum << "." << endl;
    
    // Fin
    return 0;
}
```

El programa es convertido a lenguaje de máquina por un compilador, transformándolo a un formato que la computadora puede ejecutar.
