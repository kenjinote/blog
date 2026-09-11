---
title: 'Cara Mengatur Variabel Lingkungan secara Dinamis di GitHub Actions [Lingkungan Windows]'
slug: "Github Actionsで動的に変数を設定する"
date: 2022-10-02T02:33:35+09:00
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["ツール・開発環境"]
description: 'Menjelaskan cara mengatur variabel lingkungan secara dinamis di dalam alur kerja GitHub Actions. Mengambil contoh lingkungan Windows, memperkenalkan langkah menulis ke ''$env:GITHUB_ENV'' dan contoh nyata mereferensikan variabel di langkah berikutnya untuk digunakan dalam pembuatan rilis.'
---

Untuk mengatur variabel secara dinamis di Github Actions, Anda dapat mencapainya dengan menulis tambahan ke $env:GITHUB_ENV seperti di bawah ini.

【Untuk Windows】
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

【Untuk Linux】
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
