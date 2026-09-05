---
title: '[For Beginners] Steps to Install libcurl (with OpenSSL support) in Visual Studio using vcpkg'
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
categories: ["Tools/Development Environment"]
---

## For using libcurl (with OpenSSL support) in Visual Studio, vcpkg is easy and recommended

When you want to handle HTTP communication in C++, `libcurl` is often used. However, adjusting builds and dependencies can be unexpectedly troublesome, right?

In such cases, the Microsoft-made C++ library management tool "**vcpkg**" is very useful.
This time, we will introduce the steps from introducing `libcurl` (with OpenSSL support) using `vcpkg` to making it smooth to use in Visual Studio.

---

### Installing vcpkg (Only for those who haven't installed it yet)

First, let's install `vcpkg`. Please run the following steps in PowerShell.

```powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
```

* If Git is not installed yet, please install it from the [Git official website](https://git-scm.com/).

---

### Installing libcurl (with OpenSSL support)

Next, we will use vcpkg to install `libcurl`. To specify the 64bit version with OpenSSL support, run the following command.

```powershell
vcpkg install curl[ssl] --triplet x64-windows
```

When this command is run, necessary dependencies (such as OpenSSL) are also set up automatically.

---

### Integration settings with Visual Studio

To easily use the library introduced by vcpkg from a Visual Studio project, configure the integration setting with the following command.

```powershell
vcpkg integrate install
```

By doing this setting, `#include <curl/curl.h>` can be automatically used in Visual Studio projects, eliminating the need to manually set up library paths and linker settings.

---

## Conclusion

With this, the preparation to introduce `libcurl` (with OpenSSL support) into Visual Studio is complete.

* With vcpkg, troublesome dependencies can be managed all at once.
* Easily introduce libcurl with `vcpkg install curl[ssl] --triplet x64-windows`
* Automatic integration with Visual Studio is possible with `vcpkg integrate install`

After this, just include the header in your project and start developing using the libcurl API.
Please utilize the convenient vcpkg and dramatically increase your development efficiency.
