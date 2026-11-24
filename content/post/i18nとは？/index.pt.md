---
title: 'O que é i18n (Internacionalização)? Significado e Considerações no Desenvolvimento de Software'
slug: "i18nとは？"
tags: ["Internationalization", "i18n", "Terminologia"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Explicamos de forma simples o significado e a origem de ''i18n (Internacionalização)'', muito comum no desenvolvimento de softwares. Listamos as principais áreas a considerar ao expandir um app ou sistema globalmente, como codificação de caracteres, formato de datas/horas e de moedas.'
date: "2023-04-07T00:42:02+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


# O que é i18n?

## Internacionalização e localização

Internacionalização é projetar e desenvolver um produto ou software para facilitar sua adaptação a diferentes idiomas, regiões e culturas. Localização (l10n) adapta o produto a uma localidade específica. Internacionalização (i18n) não é a tradução em si; facilita traduções e outras adaptações locais.

`i18n` é a abreviação de `Internationalization`, que significa internacionalização. Como `Internationalization` é longo,
é abreviado como `i18n` porque há 18 letras entre o primeiro `i` e o último `n`.

É frequentemente usado no contexto da internacionalização de software.

Os principais itens a serem considerados na internacionalização incluem o seguinte:

- Texto e idioma (Unicode, codificação de caracteres, etiquetas de idioma, cobertura de fontes e renderização)
- Direção do texto (da esquerda para a direita, da direita para a esquerda, de cima para baixo em direção à esquerda, etc.)
- Idioma / Texto
- Fontes
- Formatos
  - Números (caractere de ponto decimal, caractere de separador de milhares, número de dígitos a agrupar, etc.)
  - Data e hora (formato da data, diferenças nos calendários usados, como Islâmico / Gregoriano / Judaico / Japonês, etc.)
- Diferenças de fuso horário em informações de data e hora
- Informações sobre moeda

- Mensagens (separe os textos visíveis do código, trate plurais e ordem das palavras de cada idioma e evite concatenar fragmentos de frases)
- Dados regionais (nomes, endereços, telefones, métodos de entrada, teclados, símbolos, cores, requisitos legais e expectativas culturais)

## Testes

Use pseudolocalização para encontrar textos que se expandem e itens não traduzidos. Teste layout, entrada, ordenação e formatos de números/datas em cada idioma e localidade. Em idiomas RTL, verifique a interface e textos bidirecionais.

## References

- [W3C: Localization vs. Internationalization](https://www.w3.org/International/questions/qa-i18n)
- [W3C Internationalization Glossary](https://www.w3.org/TR/i18n-glossary/)
- [Unicode CLDR: Common Locale Data & Rules](https://www.unicode.org/reports/tr35/)
