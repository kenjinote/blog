---
title: 'Cómo instalar Gemini CLI en Windows｜Explicación detallada desde Node.js'
slug: "Gemini CLI を Windows 環境にInstalaciónする方法"
tags: ["Gemini", "CLI", "Windows", "Instalación", "Desarrollo"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Instala Gemini CLI en Windows con Node.js y npm: instalación global o puntual, autenticación, comprobación de PATH y aprobaciones seguras."
---

# Instalar y usar Gemini CLI en Windows

Gemini CLI es una herramienta de código abierto para usar Gemini desde la terminal. Estos pasos siguen la guía oficial actual; consulta la [guía de instalación](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx) por si hay cambios.

## 1. Preparar Node.js y npm

Gemini CLI requiere Node.js 20.0.0 o posterior. La documentación oficial recomienda Windows 11 24H2 o posterior, admite PowerShell y requiere Internet. Descarga el instalador LTS para Windows desde el [sitio de Node.js](https://nodejs.org/en/download/).

```powershell
node --version
npm --version
```

## 2. Instalar Gemini CLI con npm

Para usarlo habitualmente, instala el paquete globalmente:

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

Si no se encuentra `gemini`, ejecuta `npm config get prefix`, añade esa carpeta a `PATH`, abre otra ventana de PowerShell y comprueba con `Get-Command gemini`. Consulta la [documentación de npm](https://docs.npmjs.com/cli/v11/configuring-npm/folders/).

## 3. Primer inicio y autenticación

Inicia `gemini` en PowerShell y sigue las indicaciones de autenticación inicial. Las opciones documentadas incluyen una cuenta de Google, una clave de Gemini API y Vertex AI. La disponibilidad, los precios, las cuotas y las condiciones dependen de la cuenta y del servicio; consulta la [guía de autenticación](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx). Protege las claves API: no las incluyas en prompts ni repositorios públicos.

```powershell
gemini
```

Usa `gemini --help` para ver los comandos y escribe `/quit` para salir de la sesión interactiva.

## 4. Ejecutar una vez sin instalación global

Para una ejecución puntual, usa `npx`; no instala el comando de forma permanente y tendrás que repetirlo en otra sesión. Gemini CLI puede leer y modificar archivos y ejecutar comandos de shell. Úsalo en proyectos de confianza y revisa las solicitudes antes de aprobar acciones. Consulta [herramientas y seguridad](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md).

```powershell
npx @google/gemini-cli
```

## 5. Resumen

1. Prepara Node.js 20 o posterior.
2. Para uso habitual, instala globalmente con npm.
3. Inicia `gemini` y autentícate.
4. Para una ejecución puntual, usa `npx`. Consulta las guías oficiales para conocer los requisitos y condiciones actuales.
