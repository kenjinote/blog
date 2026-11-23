---
title: 'How to Dynamically Set Environment Variables in GitHub Actions [Windows Environment]'
slug: "Github Actionsで動的に変数を設定する"
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
date: "2022-10-02T02:33:35+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Set values for later GitHub Actions steps with GITHUB_ENV and create a release from a Windows PowerShell workflow."
---

# Set dynamic environment variables in GitHub Actions

In GitHub Actions, write a value to the `GITHUB_ENV` file to make it available to later steps in the same job. The step that writes the value cannot read the new value. This Windows PowerShell example creates a GitHub Release when manually dispatched. It assumes a previous build placed the executable in `dist`.

## Create a GitHub Release on a Windows runner

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

## Scope of GITHUB_ENV

With PowerShell 7 (`pwsh`), append `NAME=value` to `$env:GITHUB_ENV`. On Linux Bash, use `printf 'NAME=value\n' >> "$GITHUB_ENV"`. `GITHUB_ENV` does not pass values between jobs; use step and job outputs for that. See [workflow commands](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands) and [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs).

Official references: [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs), [gh release create](https://cli.github.com/manual/gh_release_create), [GitHub CLI authentication and GH_TOKEN](https://cli.github.com/manual/gh_auth_login), [checkout releases](https://github.com/actions/checkout/releases), and the [archived create-release action](https://github.com/actions/create-release).
