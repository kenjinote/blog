---
title: 'How to Install Gemini CLI on Windows | Thorough Explanation from Node.js'
slug: "Gemini CLI を Windows 環境にInstallする方法"
tags: ["Gemini", "CLI", "Windows", "install", "development"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Install Gemini CLI on Windows with Node.js and npm, including global and one-off use, authentication, PATH checks, and safe tool approvals."
---

# Install and use Gemini CLI on Windows

Gemini CLI is an open-source command-line tool for using Gemini from a terminal. These steps follow the current official guidance; check the [installation guide](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx) for changes.

## 1. Prepare Node.js and npm

Gemini CLI requires Node.js 20.0.0 or later. The official documentation recommends Windows 11 24H2 or later, supports PowerShell, and requires internet access. Download the Windows LTS installer from the [Node.js website](https://nodejs.org/en/download/).

```powershell
node --version
npm --version
```

## 2. Install Gemini CLI with npm

For ongoing use, install the package globally:

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

If `gemini` is not found, run `npm config get prefix`, ensure that folder is on Windows `PATH`, open a new PowerShell window, and check with `Get-Command gemini`. See [npm’s documentation](https://docs.npmjs.com/cli/v11/configuring-npm/folders/).

## 3. First launch and authentication

Start `gemini` in PowerShell and follow the first-run authentication prompts. Documented options include a Google account, a Gemini API key, and Vertex AI. Availability, pricing, quotas, and terms depend on the account and service; see the [authentication guide](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx). Treat API keys as secrets; never put them in prompts or public repositories.

```powershell
gemini
```

Use `gemini --help` for the command list; enter `/quit` to leave the interactive session.

## 4. Run once without a global install

For a one-off run, use `npx`; this does not permanently install the command, so run it again next time. Gemini CLI can read and edit files in the working folder and run shell commands. Use a project you trust and review each confirmation prompt before approving changes or commands. See [tools and security](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md).

```powershell
npx @google/gemini-cli
```

## 5. Summary

1. Prepare Node.js 20 or later.
2. For ongoing use, install globally with npm.
3. Start `gemini` and authenticate.
4. For a one-off run, use `npx`. Check the official guides for current requirements and terms.
