---








title: "FizzBuzz"
date: 2025-04-18T00:58:11+09:00
tags: ["FizzBuzz", "Python", "Algoritmos"]
draft: false
image: "img.png"
categories: ["Programación"]
---









## ¿Qué es FizzBuzz, al final de cuentas?

¡Hola!

Hoy me gustaría escribir sobre "FizzBuzz".

Tanto para los que dicen "¡Ah, ya lo conozco!" como para los que piensan "He escuchado de eso, pero no lo entiendo bien", acompáñenme un momento por favor. Se lee en unos pocos minutos, y quizás terminen diciendo "Ya veo".

---

### ¿Es verdad que "si no puedes escribir FizzBuzz, no sirves como programador"?

FizzBuzz, en resumen, es algo como esto.

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

Sí, este es el famoso "problema de FizzBuzz".

Se revisan los números del 1 al 100 en orden,  
si es múltiplo de 3, se muestra "Fizz", si es múltiplo de 5, "Buzz",  
y si es múltiplo de ambos, "FizzBuzz". Es algo extremadamente simple.

Sin embargo, por alguna razón, a menudo es tratado como "la prueba mínima para un programador". Aparece en entrevistas, y en las redes sociales de vez en cuando se ven actitudes arrogantes como "Alguien que ni siquiera puede escribir FizzBuzz...".

Pero, un momento.

¿Realmente se puede afirmar que "no poder escribir FizzBuzz = no poder programar"?

---

### No se trata de si puedes hacerlo, sino de si estás en el "estado" para hacerlo

Es cierto que FizzBuzz requiere comprender la sintaxis y el pensamiento lógico básico. Por lo tanto, es comprensible que se use para "comprobar los fundamentos".

Pero, piénsenlo.

Si el entorno es diferente, el resultado también lo será.

Por ejemplo,

- Cuando estás nervioso frente a un entrevistador que ves por primera vez
- Cuando de repente te dan una pizarra y no tienes un editor a la mano
- Cuando te preguntas "¿Qué era modulo otra vez?" y no te acuerdas al instante

...¿No les ha pasado eso? Somos humanos. Creo que sí pasa.

Por eso, creo que más que "si puedes escribir FizzBuzz", lo que en realidad es importante es "si puedes llevarte a un estado donde puedas escribir FizzBuzz".

---

### La trampa del típico consejo "solo entrénate y estarás bien"

Cuando se habla de esto, suele surgir el consejo "¡Por eso debes practicar todos los días!".

Es cierto que la práctica repetitiva te permite escribir con fluidez, y eso en sí mismo es bueno. Pero si nos basamos en la premisa de que "si no puedes escribir FizzBuzz, estás descalificado", a veces simplemente se convierte en miedo.

Es decir, se tiende a crear una estructura donde sientes que "cometer un error = no sirvo".

Por ejemplo, el día que te quedas dormido por la mañana tiendes a pensar "soy un perezoso...". Pero puede ser simplemente que tu cuerpo estaba cansado.

Con FizzBuzz pasa lo mismo.

---

### A pesar de todo, FizzBuzz también es un buen problema

A pesar de todo, no es que FizzBuzz sea malo.

Al contrario, creo que es un problema muy bien hecho. Las reglas son simples y es fácil de expandir. Por ejemplo, si lo cambias de esta manera, el pensamiento se profundiza más.

```python
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)
```

Este es un ejemplo de que "puedes escribirlo sin usar if-elif-else". Es un poco más elegante, ¿verdad?

En otras palabras, FizzBuzz no solo sirve para ver "si pudiste hacerlo", sino que también es una puerta de entrada para ver "cómo lo escribes" y "hasta qué punto lo entiendes".

---

### En conclusión

Creo que no hay que darle un significado demasiado exagerado a si puedes hacer FizzBuzz o no.

Incluso si no pudiste escribirlo, puede que simplemente "hoy estabas en un mal momento", y a menudo puedes hacerlo si lo piensas detenidamente después.

Sin apresurarnos, avancemos lentamente.

El código es escrito por humanos. Por ser humanos, a veces olvidamos y a veces nos ponemos nerviosos. Creo que es suficiente si podemos avanzar poco a poco mientras aceptamos eso.

Entonces, escribamos código de manera relajada hoy también.
