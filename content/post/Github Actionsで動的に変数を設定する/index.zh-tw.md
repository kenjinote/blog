---
title: '在GitHub Actions中動態設定環境變數的方法【Windows環境】'
slug: "Github Actionsで動的に変数を設定する"
date: 2022-10-02T02:33:35+09:00
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["ツール・開発環境"]
description: '為您解說如何在GitHub Actions的workflow中動態設定環境變數。以Windows環境為例，介紹寫入「$env:GITHUB_ENV」的步驟，以及在後續步驟中參考變數並應用於建立Release的具體範例。'
---

若要在 Github Actions 中動態設定變數，可以透過附加寫入到 $env:GITHUB_ENV 來實現，如下所示。

【Windows 情況】
```
name: Rust

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

env:
  CARGO_TERM_COLOR: always

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Get Environment
      run: |
        echo 'VERSION=1.0.0' >> $GITHUB_ENV
        echo 'NAME=1.0.0' >> $GITHUB_ENV
    - name: Display Environment
      run: |
        echo $env:VERSION
        echo $env:NAME
    - name: Create Release
      id: create_release
      uses: actions/create-release@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        tag_name: ${{ env.VERSION }}
        release_name: ${{ env.VERSION }}
        draft: false
        prerelease: false
    - name: Upload Release Asset
      id: upload-release-asset 
      uses: actions/upload-release-asset@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        upload_url: ${{ steps.create_release.outputs.upload_url }} # This pulls from the CREATE RELEASE step above, referencing it's ID to get its outputs object, which include a `upload_url`. See this blog post for more info: https://jasonet.co/posts/new-features-of-github-actions/#passing-data-to-future-steps 
        asset_path: ./target/release/${{ env.NAME }}.exe
        asset_name: ${{ env.NAME }}.exe
        asset_content_type: application/octet-stream
```

【Linux 情況】
```
name: Rust

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

env:
  CARGO_TERM_COLOR: always

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Get Environment
      run: |
        echo 'VERSION=1.0.0' >> $GITHUB_ENV
        echo 'NAME=hello' >> $GITHUB_ENV
    - name: Display Environment
      run: |
        echo ${{ env.VERSION }}
        echo ${{ env.NAME }}
```
