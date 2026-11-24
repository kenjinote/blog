---
title: 'What is i18n (Internationalization)? Meaning and Target Items in Software Development'
slug: "i18nとは？"
tags: ["Internationalization", "i18n", "Terminology"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'We clearly explain the meaning and origin of ''i18n (Internationalization)'', which is often heard in software development. We have summarized the main items to consider when making apps or systems globally compatible, such as character codes, date/time notation, and currency information.'
date: "2023-04-07T00:42:02+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


# What is i18n?

## Internationalization and localization

Internationalization is designing and developing a product or software so it can be localized for people with different languages, regions, and cultures. Localization (l10n) adapts it to a particular locale. Internationalization (i18n) is not translation itself; it removes barriers to translation and other locale-specific changes.

`i18n` is an abbreviation for `Internationalization`. Since `Internationalization` is long, it is abbreviated as `i18n` because there are 18 letters between the first `i` and the last `n`.

It is often used in the context of internationalizing software.

The main target items in internationalization include the following:

- Text and language (Unicode, character encoding, language tags, font coverage, and text rendering)
- Text direction (left to right, right to left, top to bottom towards the left, etc.)
- Text / Wording
- Fonts
- Formatting
  - Numbers (decimal point characters, thousands separator characters, number of digits to group by, etc.)
  - Date and time (how to format year, month, and day; differences in calendars used such as Islamic/Gregorian/Hebrew/Japanese calendars, etc.)
- Time difference in date and time information
- Currency information

- Strings and messages (keep user-facing text out of code, handle locale-specific plural forms and word order, and avoid joining sentence fragments)
- Regional details (names, addresses, phone numbers, input methods, keyboards, symbols, colors, legal requirements, and cultural expectations)

## Testing

Use pseudolocalization to find text expansion and untranslated strings. Test layout, input, sorting, and number/date behavior for each target language and locale. For RTL languages, check the interface and mixed-direction text.

## References

- [W3C: Localization vs. Internationalization](https://www.w3.org/International/questions/qa-i18n)
- [W3C Internationalization Glossary](https://www.w3.org/TR/i18n-glossary/)
- [Unicode CLDR: Common Locale Data & Rules](https://www.unicode.org/reports/tr35/)
