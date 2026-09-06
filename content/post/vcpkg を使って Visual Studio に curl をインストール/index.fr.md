---
title: "【Pour les débutants】Guide d'installation de libcurl (avec support OpenSSL) dans Visual Studio à l'aide de vcpkg"
slug: "vcpkg を使って Visual Studio に curl をインストール"
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
categories: ["Outils et environnement de développement"]
---

## Si vous souhaitez utiliser libcurl (avec support OpenSSL) dans Visual Studio, l'installation de vcpkg est facile et recommandée

Lorsqu'on souhaite gérer des communications HTTP en C++, libcurl est souvent utilisé. Mais la compilation et la gestion des dépendances sont étonnamment fastidieuses, n'est-ce pas ?

Dans de tels moments, l'outil de gestion de bibliothèques C++ de Microsoft, ** "vcpkg" ** , s'avère très utile.
Cette fois-ci, nous allons vous présenter les étapes depuis l'installation de libcurl (compatible OpenSSL) en utilisant cpkg, jusqu'à ce qu'il puisse être utilisé sans problème dans Visual Studio.

---

### Installation de vcpkg (uniquement pour ceux qui ne l'ont pas encore installé)

Tout d'abord, installons cpkg. Veuillez exécuter les étapes suivantes dans PowerShell.

`powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.ootstrap-vcpkg.bat
`

※Si Git n'est pas encore installé, veuillez l'installer depuis le [Site officiel de Git](https://git-scm.com/).

---

### Installation de libcurl (compatible OpenSSL)

Ensuite, nous allons utiliser vcpkg pour installer libcurl. Pour spécifier la version 64 bits prenant en charge OpenSSL, exécutez la commande suivante.

`powershell
vcpkg install curl[ssl] --triplet x64-windows
`

L'exécution de cette commande configurera automatiquement les dépendances nécessaires (telles que OpenSSL).

---

### Paramètres d'intégration avec Visual Studio

Afin de pouvoir utiliser facilement les bibliothèques installées avec vcpkg à partir d'un projet Visual Studio, définissez les paramètres d'intégration avec la commande suivante.

`powershell
vcpkg integrate install
`

Une fois ceci configuré, #include <curl/curl.h> sera automatiquement disponible dans les projets Visual Studio, et vous n'aurez plus besoin de configurer manuellement les chemins des bibliothèques ou les paramètres de l'éditeur de liens.

---

## Conclusion

Ainsi, la préparation pour introduire libcurl (compatible OpenSSL) dans Visual Studio est terminée.

* Avec vcpkg, vous pouvez gérer toutes les dépendances complexes en une seule fois
* Introduisez facilement libcurl avec cpkg install curl[ssl] --triplet x64-windows
* L'intégration automatique avec Visual Studio est possible avec cpkg integrate install

Ensuite, il ne vous reste plus qu'à inclure l'en-tête dans votre projet et à utiliser l'API libcurl pour commencer le développement.
Tirez parti de cet outil pratique qu'est vcpkg et améliorez considérablement votre efficacité de développement.
