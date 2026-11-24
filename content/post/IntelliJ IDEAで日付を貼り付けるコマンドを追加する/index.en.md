---
title: 'How to Create a Shortcut to Insert the Current Date in IntelliJ IDEA'
slug: "IntelliJ IDEAでDateを貼り付けるCommandを追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'Create an IntelliJ IDEA live template that inserts an ISO 8601 timestamp with your local time-zone offset. This guide follows current JetBrains documentation for the settings path, date expression, and template expansion key.'
---

# Introduction

If you repeatedly enter timestamps while writing, an IntelliJ IDEA live template can insert one from a short abbreviation. This example creates an ISO 8601 timestamp with the computer's local time and UTC offset.

## Create the live template

1. Open **Settings > Editor > Live Templates**. On Windows or Linux, open it from **File > Settings**; on macOS, use **IntelliJ IDEA > Settings**.
2. Select a template group (for example, **other**) and click **+ > Live Template**.
3. Set **Abbreviation** to `date` and enter a short **Description**.
4. Set **Template text** to `$date$`.
5. Click **Edit Variables**. For the `date` variable, set **Expression** to `date("yyyy-MM-dd'T'HH:mm:ssXXX")`. Enable **Skip if defined** so the value is calculated automatically when the template expands.
6. Click **Define** and select the contexts where you want the template available (use **Everywhere** if appropriate). Save the settings.

## Use the template

In the editor, type `date` and press the default expansion key, **Tab**. IntelliJ IDEA inserts the current system date and time in a form such as `2026-11-24T09:30:00+09:00`. The time and offset follow your computer's current time zone. If you changed the expansion key, check it in Live Templates settings.

The `XXX` pattern produces an ISO 8601 time-zone offset. Because the expression does not hard-code `+09:00`, it uses the local time zone on readers' computers. Check that the generated timestamp matches the publication time you intend.

## References

- [Create and edit live templates](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live template variables and the date function](https://www.jetbrains.com/help/idea/template-variables.html)
- [Configure the live-template expansion key](https://www.jetbrains.com/help/idea/settings-live-templates.html)
