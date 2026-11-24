---
title: 'How to Introduce and Enable GitHub Copilot in IntelliJ IDEA'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA", "GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'Learn how to install the GitHub Copilot plugin in IntelliJ IDEA, sign in with GitHub, and use inline code suggestions. This guide covers access requirements and the current authentication flow, with links to official instructions.'
---
# Introduction

The GitHub Copilot plugin adds inline code suggestions and Copilot Chat to JetBrains IDEs. This guide covers the basic installation and sign-in flow in IntelliJ IDEA. Menu names and screens can vary by IDE and plugin version.

## Before you start

You need a GitHub account with access to Copilot and a compatible IntelliJ IDEA version. Copilot Free has usage limits; paid plans provide additional access. Plans and IDE compatibility can change, so check the current official documentation.

## Install the plugin

1. Open the Plugins settings. On Windows or Linux, select **File > Settings > Plugins**. On macOS, select **IntelliJ IDEA > Settings > Plugins**.
2. In Marketplace, search for **GitHub Copilot** and click **Install** on the plugin provided by GitHub.
3. Restart the IDE after installation.

## Sign in to GitHub

1. Open **Tools > GitHub Copilot > Login to GitHub**.
2. In the sign-in dialog, click **Copy and Open**. Your browser opens.
3. Sign in to GitHub in the browser, paste the device code shown by the IDE, and click **Continue**.
4. Review the requested permissions and select **Authorize GitHub Copilot Plugin**. Return to the IDE and click **OK** on the confirmation screen.

## Use code suggestions

Start typing in the editor. Copilot displays a suggestion in grayed text; press **Tab** to accept it. Review suggestions before using them because they are generated from context and may need changes. Open the GitHub Copilot Chat icon on the right side of the IDE to start a chat.

Menus and features may change. See the official documentation for current steps and compatibility information.

## References

- [Install and sign in to the GitHub Copilot plugin](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Get code suggestions in JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [GitHub Copilot plugin in JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
