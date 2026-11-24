---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25



title: 'Procedimientos de compilación e instalación y configuración del entorno de OpenSSL en Windows'
slug: "Windows で OpenSSL をConstrucciónする方法"
tags: ["Windows", "OpenSSL", "Compilar", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Cómo compilar OpenSSL desde el código fuente en Windows, con OpenSSL 3.5.9 como ejemplo y los pasos para preparar herramientas y construir para x64."
---




# ¿Qué es OpenSSL?

Para usar OpenSSL en una aplicación necesitas encabezados y bibliotecas de desarrollo. Puedes obtener una distribución binaria o compilar el código fuente según tus necesidades; esta página cubre la compilación desde el código fuente.

Below, we will introduce the build procedure.
# Preparación del entorno de compilación

- **Perl**

  Descargue `strawberry-perl-5.42.3.1-64bit.msi` desde [https://strawberryperl.com/](https://strawberryperl.com/). Creo que está bien usar la última versión.

- **NASM**

  Descargue `3.02/nasm-3.02-win64.zip` desde la sección de `Download` en [https://www.nasm.us/](https://www.nasm.us/). Creo que está bien usar la última versión (que no sea rc).
  Después de la instalación, es necesario registrar la carpeta donde se instaló NASM en la variable de entorno PATH.

- **Visual Studio 2022 ** o ** Build Tools for Visual Studio 2022**

  Instale `Visual Studio 2022 Community` o `Build Tools for Visual Studio 2022` desde [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# Pasos para compilar OpenSSL en Windows

1. Descargue y extraiga `openssl-3.5.9.tar.gz` desde [https://openssl-library.org/source/](https://openssl-library.org/source/). Si no puede extraerlo, ejecute `tar -xzf openssl-3.5.9.tar.gz` en el símbolo del sistema.

A 2026-11-25, OpenSSL 3.5.9 pertenece a la serie LTS 3.5, que sigue teniendo soporte hasta 2030-04-08. Consulta la página oficial para elegir el último parche compatible cuando compiles.

2. Usa el símbolo de herramientas para desarrolladores x64 de Visual Studio. Ábrelo como administrador solo si vas a instalar en Program Files.
3. Abra la carpeta extraída.
4. Ejecute el siguiente comando. * Cambie la parte de `Community` según la versión de Visual Studio que haya instalado:
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
5. Ejecute el siguiente comando:
```
perl Configure VC-WIN64A
```
6. Ejecute el siguiente comando (toma bastante tiempo):
```
nmake
```
7. Ejecute el siguiente comando (toma bastante tiempo):
```
nmake test
```
8. Ejecute el siguiente comando:
```
nmake install
```

Si todo sale bien, OpenSSL se instalará en `C:\Program Files\OpenSSL`.
La instalación en esta ubicación predeterminada requiere permisos de administrador. Para evitar elevar permisos, indica un prefix con permisos de escritura al configurar.

Eso es todo.

# Referencias

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)