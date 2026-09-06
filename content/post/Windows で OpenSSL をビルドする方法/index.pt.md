---
title: "Como compilar o OpenSSL no Windows"
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.png"
categories: ["Programação"]
---

# O que é o OpenSSL?

É uma biblioteca de código aberto que fornece o processamento necessário para realizar comunicação criptografada.

Para usá-lo a partir de um programa, como o código-fonte em C é publicado, você precisa compilá-lo para criar uma biblioteca.

Abaixo, apresentamos o procedimento de compilação.

# Preparação do ambiente de compilação

- **Perl**

  Baixe o `strawberry-perl-5.32.1.1-64bit.msi` de [https://strawberryperl.com/](https://strawberryperl.com/). A versão mais recente deve servir.

- **NASM**

  Baixe o `2.16.01/nasm-2.16.01-win64.zip` em `Download` no site [https://www.nasm.us/](https://www.nasm.us/). A versão não-RC mais recente deve servir.
  Após a instalação, você precisa registrar a pasta onde o NASM está instalado na variável de ambiente PATH.

- **Visual Studio 2022** ou **Build Tools for Visual Studio 2022**

  Instale o `Visual Studio 2022 Community` ou o `Build Tools for Visual Studio 2022` a partir de [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# Procedimento de compilação do OpenSSL no Windows

1. Baixe o `openssl-3.1.0.tar.gz` de [https://www.openssl.org/source/](https://www.openssl.org/source/) e extraia-o. Se não conseguir extrair, execute `tar -xzf openssl-3.1.0.tar.gz` no prompt de comando.
2. Inicie o prompt de comando **com privilégios de administrador**.
3. Abra a pasta extraída.
4. Execute o seguinte comando. *Altere a parte `Community` para corresponder à versão instalada do Visual Studio.
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
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

Isso é tudo.

# Referências
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
