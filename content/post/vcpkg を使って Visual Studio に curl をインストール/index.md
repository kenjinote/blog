---
title: 'vcpkg を使って Visual Studio に curl をインストールする方法'
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
---

1. vcpkgのインストール（未導入の場合）
   ```
   git clone https://github.com/microsoft/vcpkg
   cd vcpkg
   .\bootstrap-vcpkg.bat
   ```
   
2. libcurlをインストール（OpenSSL対応）
   ```
   vcpkg install curl[ssl] --triplet x64-windows
   ``` 
   
3. Visual Studio に統合
   ```
   vcpkg integrate install
   ```
   
これで Visual Studio のすべてのプロジェクトで #include <curl/curl.h> が使えるようになります。