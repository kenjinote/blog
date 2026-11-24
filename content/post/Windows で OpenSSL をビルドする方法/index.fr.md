---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: 'Procédure pour compiler et installer OpenSSL dans un environnement Windows et configuration de l''environnement'
slug: "Windows で OpenSSL をBuildする方法"
tags: ["Windows", "OpenSSL", "Compilation", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Comment compiler OpenSSL depuis les sources sous Windows, avec OpenSSL 3.5.9 comme exemple et les étapes pour préparer les outils et compiler en x64."
---

# Qu'est-ce qu'OpenSSL ?

Pour utiliser OpenSSL dans une application, il faut les en-têtes et bibliothèques de développement. Vous pouvez obtenir une distribution binaire ou compiler les sources selon vos besoins ; cette page décrit la compilation depuis les sources.

Below, we will introduce the build procedure.
# Préparation de l'environnement de compilation

- **Perl**

  Téléchargez `strawberry-perl-5.42.3.1-64bit.msi` à partir de [https://strawberryperl.com/](https://strawberryperl.com/). La dernière version devrait convenir.

- **NASM**

  Téléchargez `3.02/nasm-3.02-win64.zip` depuis `Download` sur [https://www.nasm.us/](https://www.nasm.us/). La dernière version non-RC devrait convenir.
  Après l'installation, vous devez ajouter le dossier où NASM est installé à la variable d'environnement PATH.

- **Visual Studio 2022** ou **Build Tools for Visual Studio 2022**

  Installez `Visual Studio 2022 Community` ou `Build Tools for Visual Studio 2022` à partir de [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# Procédure de compilation d'OpenSSL sous Windows

1. Téléchargez `openssl-3.5.9.tar.gz` sur [https://openssl-library.org/source/](https://openssl-library.org/source/) et extrayez-le. Si vous ne pouvez pas l'extraire, exécutez `tar -xzf openssl-3.5.9.tar.gz` dans l'invite de commande.

Au 2026-11-25, OpenSSL 3.5.9 appartient à la série LTS 3.5, prise en charge jusqu’au 2030-04-08. Vérifiez la dernière version corrective prise en charge sur la page officielle avant la compilation.

2. Utilisez l’invite de développement x64 de Visual Studio. Ouvrez-la comme administrateur uniquement si vous installez dans Program Files.
3. Ouvrez le dossier extrait.
4. Exécutez la commande suivante. *Modifiez la partie `Community` pour correspondre à votre version installée de Visual Studio.
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
5. Exécutez la commande suivante :
```
perl Configure VC-WIN64A
```
6. Exécutez la commande suivante (prend beaucoup de temps) :
```
nmake
```
7. Exécutez la commande suivante (prend beaucoup de temps) :
```
nmake test
```
8. Exécutez la commande suivante :
```
nmake install
```

En cas de succès, OpenSSL sera installé dans `C:\Program Files\OpenSSL`.
L’installation dans cet emplacement par défaut nécessite des droits administrateur. Pour éviter l’élévation, indiquez un prefix accessible en écriture lors de la configuration.

C'est tout.

# Références

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)