---
title: 'Cómo crear un atajo para insertar la fecha actual en IntelliJ IDEA'
slug: "IntelliJ IDEAでFechaを貼り付けるComandoを追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'Crea una plantilla dinámica de IntelliJ IDEA que inserta una fecha y hora ISO 8601 con el desfase horario local. La guía sigue la documentación actual de JetBrains para configurar la expresión y la tecla de expansión.'
---

# Introducción

Si escribes fechas y horas con frecuencia, una plantilla dinámica de IntelliJ IDEA puede insertarlas mediante una abreviatura breve. En este ejemplo se crea una marca de tiempo ISO 8601 con la hora y el desfase horario local del equipo.

## Crear la plantilla dinámica

1. Abre **Settings > Editor > Live Templates**. En Windows o Linux, accede desde **File > Settings**; en macOS, desde **IntelliJ IDEA > Settings**.
2. Elige un grupo de plantillas (por ejemplo, **other**) y pulsa **+ > Live Template**.
3. Escribe `date` en **Abbreviation** y añade una breve **Description**.
4. En **Template text**, escribe `$date$`.
5. Pulsa **Edit Variables**. Para la variable `date`, introduce `date("yyyy-MM-dd'T'HH:mm:ssXXX")` en **Expression**. Activa **Skip if defined** para calcular el valor al expandir la plantilla.
6. Pulsa **Define** y selecciona los contextos donde quieras usarla (elige **Everywhere** si corresponde). Guarda la configuración.

## Usar la plantilla

En el editor, escribe `date` y pulsa la tecla de expansión predeterminada, **Tab**. IntelliJ IDEA insertará la fecha y hora actuales del sistema en un formato como `2026-11-24T09:30:00+09:00`. La hora y el desfase dependen de la zona horaria actual del equipo. Si cambiaste la tecla de expansión, compruébala en Live Templates.

El patrón `XXX` genera un desfase horario ISO 8601. Como la expresión no fija `+09:00`, cada lector obtiene la hora de su zona horaria local. Comprueba que la fecha generada corresponda a la hora de publicación que deseas.

## Referencias

- [Crear y editar plantillas dinámicas](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Variables de plantillas y función date](https://www.jetbrains.com/help/idea/template-variables.html)
- [Configurar la tecla de expansión](https://www.jetbrains.com/help/idea/settings-live-templates.html)
