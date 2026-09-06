---
title: "FizzBuzz"
slug: "FizzBuzz"
date: 2025-04-18T00:58:11+09:00
tags: ["FizzBuzz", "Python", "Algorithme"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

## Au fait, qu'est-ce que FizzBuzz ?

Bonjour !

Aujourd'hui, j'aimerais parler de « FizzBuzz ».

Que vous soyez de ceux qui se disent « Ah, je connais ça ! » ou de ceux qui disent « J'en ai entendu parler, mais je ne comprends pas vraiment », restez avec moi un instant. Cela ne prend que quelques minutes à lire, et peut-être vous direz-vous : « C'est logique ».

---

### Est-il vrai que « si vous ne pouvez pas écrire FizzBuzz, vous êtes un mauvais programmeur » ?

FizzBuzz, pour faire simple, c'est ça.

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

Oui, c'est le fameux « Problème FizzBuzz ».

Vous regardez les nombres de 1 à 100 dans l'ordre,  
si c'est un multiple de 3, vous affichez « Fizz », si c'est un multiple de 5, vous affichez « Buzz »,  
si c'est un multiple des deux, vous affichez « FizzBuzz » – c'est extrêmement simple.

Et pourtant, pour une raison quelconque, c'est souvent traité comme « le test minimum pour un programmeur ». Il apparaît lors des entretiens, et sur les réseaux sociaux, vous verrez des commentaires du genre « Quelqu'un qui ne peut même pas écrire FizzBuzz... ».

Mais, attendez une minute.

Pouvons-nous vraiment affirmer que « ne pas savoir écrire FizzBuzz = ne pas savoir programmer » ?

---

### Il ne s'agit pas de savoir si on peut le faire, mais si on a l'« état » pour le faire

Il est vrai que FizzBuzz exige une compréhension de la syntaxe et de la pensée logique de base. Il est donc logique qu'il soit utilisé pour « vérifier les bases ».

Mais, voilà.

Si l'environnement est différent, les résultats seront différents.

Par exemple,

- Quand vous êtes nerveux devant un recruteur que vous venez de rencontrer
- Quand on vous tend soudainement un tableau blanc et que vous n'avez pas d'éditeur sous la main
- Quand vous n'arrivez pas à vous souvenir immédiatement de « Au fait, c'est quoi le modulo ? »

...Cela n'arrive-t-il pas ? Nous sommes humains. Je pense que cela arrive.

Par conséquent, plutôt que de dire « pouvez-vous écrire FizzBuzz », je pense qu'il est en fait beaucoup plus important de se demander « pouvez-vous vous mettre dans un état où vous pouvez écrire FizzBuzz ».

---

### Le piège du conseil habituel « Il suffit de s'entraîner et tout ira bien »

Quand ce sujet est abordé, le conseil « Alors entraîne-toi tous les jours ! » a tendance à surgir.

Il est vrai qu'une pratique répétée vous permettra de l'écrire couramment, et c'est en soi une bonne chose. Mais si nous partons du principe que « si vous ne pouvez pas écrire FizzBuzz, vous êtes disqualifié », cela peut facilement se transformer en simple peur.

En d'autres termes, cela tend à créer une structure où vous ressentez que « j'ai fait une erreur = je suis inutile ».

Par exemple, le jour où vous vous réveillez tard, n'avez-vous pas tendance à penser « Je suis un paresseux... » ? Mais il se peut simplement que votre corps ait été fatigué à ce moment-là.

FizzBuzz, c'est la même chose.

---

### Cela dit, FizzBuzz reste une bonne question

Cela dit, FizzBuzz n'est pas une mauvaise chose.

Au contraire, je pense que c'est une question très bien conçue. Les règles sont simples et il est facile de la développer. Par exemple, si vous la modifiez de cette façon, votre réflexion s'approfondira.

```python
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)
```

C'est un exemple qui montre que « vous pouvez l'écrire même sans if-elif-else ». C'est plutôt astucieux, n'est-ce pas ?

En d'autres termes, FizzBuzz ne consiste pas seulement à savoir « si vous avez réussi à le faire », mais sert également de point d'entrée pour voir « comment vous l'écrivez » et « jusqu'à quel point vous comprenez ».

---

### En résumé

Je pense que nous ne devrions pas accorder trop d'importance au fait de savoir si vous pouvez ou non faire FizzBuzz.

Même si vous n'avez pas réussi à l'écrire, c'est peut-être simplement que « vous ne vous sentiez pas bien sur le moment », et souvent, vous y parviendrez si vous y réfléchissez attentivement plus tard.

Ne vous précipitez pas, avançons lentement.

Le code est écrit par des humains. En tant qu'humains, il nous arrive d'oublier des choses et d'être nerveux. En acceptant cela, je pense qu'il suffit de pouvoir avancer petit à petit.

Alors, écrivons du code de manière détendue aujourd'hui aussi.
