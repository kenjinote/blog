---
title: '在GitHub Actions中动态设置环境变量的方法【Windows环境】'
slug: "Github Actionsで動的に変数を設定する"
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
date: "2022-10-02T02:33:35+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "介绍如何用 GITHUB_ENV 向后续 GitHub Actions 步骤传值，并通过 Windows PowerShell 创建 Release。"
---

# 在 GitHub Actions 中设置动态环境变量

在 GitHub Actions 中，将值写入 `GITHUB_ENV` 文件后，同一 job 的后续步骤便可读取。写入值的步骤本身无法读取新值。以下 Windows PowerShell 示例通过手动触发来创建 GitHub Release，并假设之前的构建步骤已将可执行文件放入 `dist`。

## 在 Windows runner 上创建 GitHub Release

```yaml
name: Create Release
on:
  workflow_dispatch:
    inputs:
      version:
        description: Release tag, for example v1.2.3
        required: true
        type: string
permissions:
  contents: write
jobs:
  release:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v7
      - name: Set release variables
        shell: pwsh
        env:
          RELEASE_VERSION_INPUT: ${{ inputs.version }}
        run: |
          if ($env:RELEASE_VERSION_INPUT -notmatch '^v[0-9]+(\.[0-9]+){2}$') { throw 'Enter a tag such as v1.2.3' }
          "RELEASE_VERSION=$env:RELEASE_VERSION_INPUT" >> $env:GITHUB_ENV
          "ASSET_NAME=sample-tool" >> $env:GITHUB_ENV
      - name: Check the built asset
        shell: pwsh
        run: |
          if (-not (Test-Path ".\dist\$env:ASSET_NAME.exe")) { throw 'Build the executable in dist before creating the release' }
      - name: Create release and upload asset
        shell: pwsh
        env:
          GH_TOKEN: ${{ github.token }}
        run: gh release create "$env:RELEASE_VERSION" ".\dist\$env:ASSET_NAME.exe" --target "$env:GITHUB_SHA" --title "$env:RELEASE_VERSION" --generate-notes
```

## GITHUB_ENV 的作用范围

使用 PowerShell 7（`pwsh`）时，将 `NAME=value` 追加到 `$env:GITHUB_ENV`。Linux Bash 使用 `printf 'NAME=value\n' >> "$GITHUB_ENV"`。`GITHUB_ENV` 不会在 job 之间传值；跨 job 请使用步骤和 job 输出。参阅[工作流命令](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands)和[job 输出](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs)。

Official references: [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs), [gh release create](https://cli.github.com/manual/gh_release_create), [GitHub CLI authentication and GH_TOKEN](https://cli.github.com/manual/gh_auth_login), [checkout releases](https://github.com/actions/checkout/releases), and the [archived create-release action](https://github.com/actions/create-release).
