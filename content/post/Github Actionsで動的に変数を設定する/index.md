---
title: 'GitHub Actionsで動的に環境変数を設定する方法【Windows環境】'
slug: "Github Actionsで動的に変数を設定する"
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
date: "2022-10-02T02:33:35+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "GitHub ActionsのGITHUB_ENVで後続ステップへ値を渡す方法を、Windows PowerShellのGitHub Release例で説明します。"
---

# GitHub Actionsで動的に環境変数を設定する

GitHub Actionsでは、ステップから`GITHUB_ENV`環境ファイルへ値を書き込むと、同じジョブの後続ステップで参照できます。書き込んだステップ自身には反映されません。以下はWindows runner（PowerShell）から、手動実行でGitHub Releaseを作る例です。release用の実行ファイルは事前のbuildで`dist`に用意する想定です。

## Windows runnerでGitHub Releaseを作成する例

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

## GITHUB_ENVの適用範囲

PowerShell 7（`pwsh`）では`NAME=value`形式を`$env:GITHUB_ENV`へ追記します。LinuxのBashでは`printf 'NAME=value\n' >> "$GITHUB_ENV"`を使います。複数ジョブで値を渡す場合は`GITHUB_ENV`ではなくstep/job outputsを使います。詳しくは[ワークフローコマンド](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands)と[変数の受け渡し](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs)を参照してください。

Official references: [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs), [gh release create](https://cli.github.com/manual/gh_release_create), [GitHub CLI authentication and GH_TOKEN](https://cli.github.com/manual/gh_auth_login), [checkout releases](https://github.com/actions/checkout/releases), and the [archived create-release action](https://github.com/actions/create-release).
