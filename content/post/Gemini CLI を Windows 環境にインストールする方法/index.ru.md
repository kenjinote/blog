---
title: 'Как установить Gemini CLI в Windows | Подробное руководство начиная с Node.js'
slug: "Gemini CLI を Windows 環境にУстановкаする方法"
tags: ["Gemini", "CLI", "Windows", "Установка", "開発"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Установка Gemini CLI в Windows через Node.js и npm: глобальный и разовый запуск, авторизация, PATH и безопасное подтверждение действий."
---

# Установка и использование Gemini CLI в Windows

Gemini CLI — консольный инструмент с открытым исходным кодом для работы с Gemini в терминале. Шаги основаны на текущей официальной документации; проверяйте [руководство по установке](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx) на предмет обновлений.

## 1. Подготовка Node.js и npm

Для Gemini CLI требуется Node.js 20.0.0 или новее. Официальная документация рекомендует Windows 11 24H2 или новее, поддерживает PowerShell и требует подключения к интернету. Скачайте установщик LTS для Windows на [сайте Node.js](https://nodejs.org/en/download/).

```powershell
node --version
npm --version
```

## 2. Установка Gemini CLI через npm

Для постоянного использования установите пакет глобально:

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

Если `gemini` не найден, выполните `npm config get prefix`, добавьте эту папку в Windows `PATH`, откройте новое окно PowerShell и проверьте команду через `Get-Command gemini`. См. [документацию npm](https://docs.npmjs.com/cli/v11/configuring-npm/folders/).

## 3. Первый запуск и авторизация

Запустите `gemini` в PowerShell и следуйте подсказкам при первой авторизации. В документации указаны аккаунт Google, ключ Gemini API и Vertex AI. Доступность, цены, квоты и условия зависят от аккаунта и сервиса; см. [руководство по авторизации](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx). Не помещайте ключи API в запросы или публичные репозитории.

```powershell
gemini
```

Используйте `gemini --help` для просмотра команд; введите `/quit`, чтобы завершить сеанс.

## 4. Разовый запуск без глобальной установки

Для разового запуска используйте `npx`; команда не устанавливается навсегда, поэтому её нужно выполнить снова в следующем сеансе. Gemini CLI может читать и изменять файлы, а также выполнять команды оболочки. Используйте его в доверенных проектах и проверяйте запросы на подтверждение. См. [руководство по инструментам и безопасности](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md).

```powershell
npx @google/gemini-cli
```

## 5. Кратко

1. Подготовьте Node.js 20 или новее.
2. Для постоянного использования выполните глобальную установку через npm.
3. Запустите `gemini` и авторизуйтесь.
4. Для разового запуска используйте `npx`. Актуальные требования и условия проверяйте в официальной документации.
