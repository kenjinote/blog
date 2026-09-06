---



title: "Cómo compilar OpenSSL en Windows"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "Compilar", "C++"]
draft: false
image: "img.png"
categories: ["Programación"]
---




# ¿Qué es OpenSSL?

Es una biblioteca de código abierto que proporciona el procesamiento necesario para realizar comunicaciones cifradas.

Para utilizarlo desde un programa, dado que el código fuente en lenguaje C es público, es necesario compilarlo para crear la biblioteca.

A continuación se presentan los pasos para su compilación.

# Preparación del entorno de compilación

- **Perl**

  Descargue `strawberry-perl-5.32.1.1-64bit.msi` desde [https://strawberryperl.com/](https://strawberryperl.com/). Creo que está bien usar la última versión.

- **NASM**

  Descargue `2.16.01/nasm-2.16.01-win64.zip` desde la sección de `Download` en [https://www.nasm.us/](https://www.nasm.us/). Creo que está bien usar la última versión (que no sea rc).
  Después de la instalación, es necesario registrar la carpeta donde se instaló NASM en la variable de entorno PATH.

- **Visual Studio 2022** o **Build Tools for Visual Studio 2022**

  Instale `Visual Studio 2022 Community` o `Build Tools for Visual Studio 2022` desde [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# Pasos para compilar OpenSSL en Windows

1. Descargue y extraiga `openssl-3.1.0.tar.gz` desde [https://www.openssl.org/source/](https://www.openssl.org/source/). Si no puede extraerlo, ejecute `tar -xzf openssl-3.1.0.tar.gz` en el símbolo del sistema.
2. Inicie el símbolo del sistema **con privilegios de administrador**.
3. Abra la carpeta extraída.
4. Ejecute el siguiente comando. * Cambie la parte de `Community` según la versión de Visual Studio que haya instalado:
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
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

Eso es todo.

# Referencias
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
