---
title: '[C++20] Exemple de code simple pour afficher l''heure actuelle au format ISO8601 (UTC)'
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Date et Heure", "ISO8601"]
draft: false
image: "img.webp"
categories: ["Programmation"]
description: 'Incontournable pour les ingénieurs qui souhaitent afficher l''heure actuelle au format standard mondial ISO8601 en C++ ! Cet article présente un exemple de code clair et élégant pour convertir le format de l''heure actuelle de manière intelligente et concise, en utilisant std::format de C++20 et la bibliothèque chrono.'
---

### Prérequis

- Norme ISO C++ 20 (/std:c++20)

### Code

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

Voici comment afficher l'heure actuelle au format ISO 8601 en C++.

### Références

- [std::format](https://eel.is/c++draft/time.format)
