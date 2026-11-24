---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: 'Procedimentos para compilar e instalar OpenSSL no ambiente Windows e configuração do ambiente'
slug: "Windows で OpenSSL をBuildする方法"
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Como compilar OpenSSL a partir do código-fonte no Windows, usando o OpenSSL 3.5.9 como exemplo e apresentando as ferramentas e etapas para x64."
---

# O que é o OpenSSL?

Para usar OpenSSL em um aplicativo, você precisa dos cabeçalhos e bibliotecas de desenvolvimento. É possível obter uma distribuição binária ou compilar o código-fonte conforme a necessidade; esta página cobre a compilação do código-fonte.

Below, we will introduce the build procedure.
# Preparação do ambiente de compilação

- **Perl**

  Baixe o `strawberry-perl-5.42.3.1-64bit.msi` de [https://strawberryperl.com/](https://strawberryperl.com/). A versão mais recente deve servir.

- **NASM**

  Baixe o `3.02/nasm-3.02-win64.zip` em `Download` no site [https://www.nasm.us/](https://www.nasm.us/). A versão não-RC mais recente deve servir.
  Após a instalação, você precisa registrar a pasta onde o NASM está instalado na variável de ambiente PATH.

- **Visual Studio 2022** ou **Build Tools for Visual Studio 2022**

  Instale o `Visual Studio 2022 Community` ou o `Build Tools for Visual Studio 2022` a partir de [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# Procedimento de compilação do OpenSSL no Windows

1. Baixe o `openssl-3.5.9.tar.gz` de [https://openssl-library.org/source/](https://openssl-library.org/source/) e extraia-o. Se não conseguir extrair, execute `tar -xzf openssl-3.5.9.tar.gz` no prompt de comando.

Em 2026-11-25, OpenSSL 3.5.9 pertence à série LTS 3.5, com suporte até 2030-04-08. Confira na página oficial de downloads o patch compatível mais recente antes de compilar.

2. Use o Prompt de Comando de Desenvolvedor x64 do Visual Studio. Abra como administrador somente se for instalar em Program Files.
3. Abra a pasta extraída.
4. Execute o seguinte comando. *Altere a parte `Community` para corresponder à versão instalada do Visual Studio.
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
5. Execute o seguinte comando:
```
perl Configure VC-WIN64A
```
6. Execute o seguinte comando (leva bastante tempo):
```
nmake
```
7. Execute o seguinte comando (leva bastante tempo):
```
nmake test
```
8. Execute o seguinte comando:
```
nmake install
```

Se for bem-sucedido, o OpenSSL será instalado em `C:\Program Files\OpenSSL`.
Instalar neste destino padrão exige privilégios de administrador. Para evitar a elevação, informe um prefix gravável durante a configuração.

Isso é tudo.

# Referências

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)