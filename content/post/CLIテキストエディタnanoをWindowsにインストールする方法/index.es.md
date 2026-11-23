---







title: 'Cómo usar el editor de texto nano en Windows: WSL y MSYS2'
slug: "CLIEditor de textonanoをWindowsにInstalaciónする方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "editor de texto"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'Métodos actuales para usar GNU nano en Windows: instálelo en WSL para disponer de Linux o en MSYS2 para usar herramientas de desarrollo de Windows. Incluye los atajos básicos.'
---


Hay varias formas de usar GNU nano en Windows. Los archivos `nano.exe` independientes de sitios antiguos pueden tener un origen y un mantenimiento difíciles de verificar; por eso esta guía usa dos vías mantenidas.

## Opción 1: Usar nano en WSL

Elija WSL si también necesita herramientas de línea de comandos de Linux. En Windows 11 o Windows 10 versión 2004 (compilación 19041) o posterior, abra PowerShell como administrador y ejecute:

```powershell
wsl --install
```

Después de reiniciar, abra Ubuntu e instale nano en la terminal de Linux:

```bash
sudo apt update
sudo apt install nano
nano --version
```

Abra un archivo con `nano nombre`. La unidad C: de Windows está disponible en `/mnt/c/` dentro de WSL; por ejemplo: `nano /mnt/c/Users/Nombre/notes.txt`. Consulte la [guía de instalación de WSL de Microsoft](https://learn.microsoft.com/es-es/windows/wsl/install) para conocer la configuración y el acceso a archivos.

## Opción 2: Usar nano desde MSYS2

Si no necesita una distribución Linux completa y quiere herramientas de desarrollo con comandos de estilo Unix, elija [MSYS2](https://www.msys2.org/). Siga la [guía oficial del instalador](https://www.msys2.org/docs/installer/) y abra la terminal “MSYS2 MSYS”. El instalador gráfico requiere Windows de 64 bits 10 versión 1809 o posterior, o Windows Server 2019; los requisitos de cada paquete pueden variar (consulte las [versiones de Windows compatibles](https://www.msys2.org/docs/windows_support/)). Actualice primero la base de datos y los paquetes instalados. Si la actualización pide reiniciar la terminal, vuelva a abrirla y termine la actualización antes de instalar nano.

```bash
pacman -Suy
pacman -S nano
nano --version
```

El nombre del paquete y el comando aparecen en la [página del paquete nano de MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64). Ejecute nano dentro de una terminal MSYS2. Usarlo desde el Símbolo del sistema o PowerShell normales requiere configurar PATH y el entorno de ejecución; no se recomienda añadir `/usr/bin` de MSYS2 a PATH de Windows sin más.

## Atajos básicos

Inicie el editor con un comando como `nano notes.txt`. La leyenda de atajos aparece en la parte inferior: `^` significa Ctrl y `M-` significa Meta (normalmente Alt). Pulse `Ctrl+O` para escribir el archivo, confirme el nombre mostrado con Enter y pulse `Ctrl+X` para salir. Las versiones actuales también guardan el búfer con `Ctrl+S`. Consulte la [chuleta oficial de GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html).

nano admite internacionalización y UTF-8, pero la escritura y visualización del japonés también dependen del terminal, las fuentes, la configuración regional y el método de entrada. Si aparecen caracteres ilegibles o no puede escribir japonés en WSL o MSYS2, compruebe la configuración UTF-8 y del método de entrada del terminal.

## Referencias

- [GNU nano](https://www.nano-editor.org/)
- [Chuleta de GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn: instalar WSL](https://learn.microsoft.com/es-es/windows/wsl/install)
- [Guía del instalador de MSYS2](https://www.msys2.org/docs/installer/)
- [Versiones de Windows compatibles](https://www.msys2.org/docs/windows_support/)
- [Paquete nano de MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64)
