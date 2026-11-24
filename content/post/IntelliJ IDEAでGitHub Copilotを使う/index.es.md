---
title: 'Cómo instalar y habilitar GitHub Copilot en IntelliJ IDEA'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'Aprende a instalar el complemento de GitHub Copilot en IntelliJ IDEA, iniciar sesión con GitHub y usar sugerencias de código en línea. Esta guía explica los requisitos de acceso y el flujo actual de autenticación, con enlaces a instrucciones oficiales.'
---

# Introducción

El complemento GitHub Copilot añade sugerencias de código en línea y Copilot Chat a los IDE de JetBrains. Esta guía explica la instalación básica y el inicio de sesión en IntelliJ IDEA. Los menús y las pantallas pueden variar según la versión del IDE y del complemento.

## Antes de empezar

Necesitas una cuenta de GitHub con acceso a Copilot y una versión compatible de IntelliJ IDEA. Copilot Free tiene límites de uso; los planes de pago ofrecen más acceso. Los planes y la compatibilidad pueden cambiar, así que consulta la documentación oficial actual.

## Instalar el complemento

1. Abre la configuración de Plugins. En Windows o Linux, elige **File > Settings > Plugins**. En macOS, elige **IntelliJ IDEA > Settings > Plugins**.
2. En Marketplace, busca **GitHub Copilot** y pulsa **Install** en el complemento de GitHub.
3. Reinicia el IDE después de instalarlo.

## Iniciar sesión en GitHub

1. Abre **Tools > GitHub Copilot > Login to GitHub**.
2. En el cuadro de inicio de sesión, pulsa **Copy and Open**. Se abrirá el navegador.
3. Inicia sesión en GitHub, pega el código de dispositivo mostrado por el IDE y pulsa **Continue**.
4. Revisa los permisos y selecciona **Authorize GitHub Copilot Plugin**. Vuelve al IDE y pulsa **OK** en la confirmación.

## Usar sugerencias de código

Empieza a escribir en el editor. Copilot mostrará una sugerencia en texto atenuado; pulsa **Tab** para aceptarla. Revisa las sugerencias antes de usarlas, ya que se generan según el contexto y pueden requerir cambios. Abre el icono de GitHub Copilot Chat a la derecha del IDE para iniciar una conversación.

Los menús y las funciones pueden cambiar. Consulta la documentación oficial para ver los pasos y la compatibilidad actuales.

## Referencias

- [Instalar el complemento e iniciar sesión](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Obtener sugerencias de código en JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [Complemento GitHub Copilot en JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
