---
title: "Comment compiler OpenSSL sous Windows"
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "Compilation", "C++"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

# Qu'est-ce qu'OpenSSL ?

C'est une bibliothèque open-source qui fournit les traitements nécessaires pour effectuer des communications chiffrées.

Pour l'utiliser à partir d'un programme, puisque le code source en C est publié, vous devez le compiler pour créer une bibliothèque.

Ci-dessous, nous présentons la procédure de compilation.

# Préparation de l'environnement de compilation

- **Perl**

  Téléchargez `strawberry-perl-5.32.1.1-64bit.msi` à partir de [https://strawberryperl.com/](https://strawberryperl.com/). La dernière version devrait convenir.

- **NASM**

  Téléchargez `2.16.01/nasm-2.16.01-win64.zip` depuis `Download` sur [https://www.nasm.us/](https://www.nasm.us/). La dernière version non-RC devrait convenir.
  Après l'installation, vous devez ajouter le dossier où NASM est installé à la variable d'environnement PATH.

- **Visual Studio 2022** ou **Build Tools for Visual Studio 2022**

  Installez `Visual Studio 2022 Community` ou `Build Tools for Visual Studio 2022` à partir de [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# Procédure de compilation d'OpenSSL sous Windows

1. Téléchargez `openssl-3.1.0.tar.gz` sur [https://www.openssl.org/source/](https://www.openssl.org/source/) et extrayez-le. Si vous ne pouvez pas l'extraire, exécutez `tar -xzf openssl-3.1.0.tar.gz` dans l'invite de commande.
2. Lancez l'invite de commande **avec des privilèges d'administrateur**.
3. Ouvrez le dossier extrait.
4. Exécutez la commande suivante. *Modifiez la partie `Community` pour correspondre à votre version installée de Visual Studio.
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
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

C'est tout.

# Références
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
