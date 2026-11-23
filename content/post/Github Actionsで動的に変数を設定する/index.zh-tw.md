---
title: '在GitHub Actions中動態設定環境變數的方法【Windows環境】'
slug: "Github Actionsで動的に変数を設定する"
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
date: "2022-10-02T02:33:35+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "說明如何用 GITHUB_ENV 將值傳給後續 GitHub Actions 步驟，並透過 Windows PowerShell 建立 Release。"
---

# 在 GitHub Actions 設定動態環境變數

在 GitHub Actions 中，將值寫入 `GITHUB_ENV` 檔案後，同一 job 的後續步驟即可讀取。寫入值的步驟本身無法讀取新值。以下 Windows PowerShell 範例透過手動觸發建立 GitHub Release，並假設先前的建置步驟已將執行檔放入 `dist`。

## 在 Windows runner 建立 GitHub Release

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

## GITHUB_ENV 的適用範圍

使用 PowerShell 7（`pwsh`）時，將 `NAME=value` 附加到 `$env:GITHUB_ENV`。Linux Bash 則使用 `printf 'NAME=value\n' >> "$GITHUB_ENV"`。`GITHUB_ENV` 不會在 job 之間傳值；跨 job 請使用步驟與 job 輸出。參閱[工作流程命令](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands)及[job 輸出](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs)。

Official references: [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs), [gh release create](https://cli.github.com/manual/gh_release_create), [GitHub CLI authentication and GH_TOKEN](https://cli.github.com/manual/gh_auth_login), [checkout releases](https://github.com/actions/checkout/releases), and the [archived create-release action](https://github.com/actions/create-release).
