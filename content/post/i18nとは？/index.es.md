---
title: '¿Qué es i18n (Internacionalización)? Su significado en el desarrollo de software y elementos clave'
slug: "i18nとは？"
tags: ["Internacionalización", "i18n", "Terminología"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Explicamos de forma sencilla el significado y origen de "i18n (Internationalization: internacionalización)", a menudo escuchado en el desarrollo de software. Hemos recopilado los principales elementos a considerar al globalizar una app o sistema, como codificación de caracteres, formato de fecha y hora, información de moneda, etc.'
date: "2023-04-07T00:42:02+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---





# ¿Qué es i18n?

## Internacionalización y localización

La internacionalización consiste en diseñar y desarrollar un producto o software para facilitar su adaptación a distintos idiomas, regiones y culturas. La localización (l10n) lo adapta a una configuración regional concreta. La internacionalización (i18n) no es traducir: facilita la traducción y otros ajustes locales.

`i18n` es una abreviatura de `Internationalization`, que significa internacionalización. Debido a que `Internationalization` es larga, se abrevia como `i18n` indicando que hay 18 letras entre la primera `i` y la última `n`.

A menudo se utiliza en el contexto de la internacionalización de software.

Los principales elementos sujetos a la internacionalización son los siguientes:

- Texto e idioma (Unicode, codificación de caracteres, etiquetas de idioma, cobertura de fuentes y representación del texto)
- Dirección del texto (de izquierda a derecha, de derecha a izquierda, de arriba a abajo hacia la izquierda, etc.)
- Texto
- Fuentes
- Formato
  - Números (carácter de punto decimal, separador de miles, cantidad de dígitos a separar, etc.)
  - Fecha y hora (formato de año, mes y día, diferencias en el calendario utilizado como calendario islámico / calendario gregoriano / calendario hebreo / calendario japonés, etc.)
- Diferencia horaria en la información de fecha y hora
- Información de moneda

- Cadenas y mensajes (separa el texto visible del código, gestiona los plurales y el orden de palabras de cada idioma y evita concatenar fragmentos de frases)
- Datos regionales (nombres, direcciones, teléfonos, métodos de entrada, teclados, símbolos, colores, requisitos legales y expectativas culturales)

## Pruebas

Usa pseudolocalización para detectar textos que se expanden y cadenas sin traducir. Prueba diseño, entrada, ordenación y formatos de números/fechas en cada idioma y configuración regional. En idiomas RTL, comprueba toda la interfaz y el texto bidireccional.

## References

- [W3C: Localization vs. Internationalization](https://www.w3.org/International/questions/qa-i18n)
- [W3C Internationalization Glossary](https://www.w3.org/TR/i18n-glossary/)
- [Unicode CLDR: Common Locale Data & Rules](https://www.unicode.org/reports/tr35/)
