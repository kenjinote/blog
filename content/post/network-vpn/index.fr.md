---
title: "Ligne dédiée virtuelle : Comment fonctionne un VPN - Un tunnel sécurisé sur Internet"
description: "Le VPN (Virtual Private Network), indispensable au télétravail. Nous expliquons comment le cryptage et l'encapsulation créent un « tunnel dédié privé et sécurisé » sur Internet, où n'importe qui peut normalement jeter un œil."
slug: "network-vpn"
date: "2026-09-23T10:00:00+09:00"
image: "eyecatch.jpg"
categories:
    - "technology"
    - "computer-science"
tags:
    - "network"
    - "vpn"
    - "security"
    - "remote"
    - "à distance"
---

## 1. Le Wi-Fi d'un café est une place publique où « tout le monde peut tout entendre »

L'Internet que nous utilisons habituellement est un immense réseau public où les ordinateurs du monde entier sont connectés.
Surtout lorsque vous utilisez un réseau public comme le Wi-Fi gratuit d'un café ou d'un aéroport, les données que vous envoyez et recevez (mots de passe, historique de navigation, informations confidentielles de l'entreprise, etc.) sont constamment exposées au risque d'être « interceptées (mises sur écoute) » par un tiers malveillant connecté au même Wi-Fi.

Pour faire une comparaison, Internet est une « **immense place publique où les gens parlent à haute voix** ».
Le « **VPN (Virtual Private Network : réseau privé virtuel)** » est un mécanisme permettant d'avoir une conversation secrète avec quelqu'un au loin (comme le serveur de votre entreprise) sur cette place où tout le monde peut entendre votre voix, de sorte que personne d'autre ne puisse absolument l'entendre.

## 2. Les 3 magies qui rendent le VPN possible

Le VPN construit littéralement un « réseau virtuel (Virtual) dédié à vous-même (Private) dans le lieu public qu'est Internet (Network) ». Pour y parvenir, les trois technologies suivantes sont principalement utilisées.

### ① Le tunneling (sécurisation du chemin)
Il crée virtuellement un « **tunnel dédié** » invisible de l'extérieur au sein de la place publique qu'est Internet.
Il crée un tuyau logique entre votre ordinateur et le serveur VPN de votre entreprise, empêchant les données de s'égarer dans d'autres réseaux ou les personnes non autorisées d'entrer dans ce tuyau sans permission.

### ② L'encapsulation (dissimulation des données)
Les données passant par le tunnel sont en outre enveloppées dans une « capsule (une autre boîte) » avant d'être envoyées.
Normalement, les adresses de l'« expéditeur » et du « destinataire » (adresses IP) sont écrites sur les données. Avec l'encapsulation, les données d'origine sont entièrement enveloppées dans un autre paquet, et la destination devient le « serveur VPN ». Grâce à cela, même si le paquet est intercepté en cours de route, il est possible de cacher « avec qui vous communiquez en fin de compte ».

### ③ Le cryptage (protection du contenu)
Même si elles sont encapsulées et passent par le tunnel, cela ne sert à rien si quelqu'un perce un trou dans le tunnel et regarde à l'intérieur. C'est pourquoi les données elles-mêmes sont « **cryptées** ».
Les VPN utilisent de puissants algorithmes de cryptage (comme l'AES). Ainsi, même si les données sont interceptées, si vous n'avez pas la clé pour décrypter le code, cela ne ressemblera qu'à une « chaîne de caractères dénuée de sens ».

```mermaid
graph LR
    User["Votre ordinateur"] -->|"Tunnel crypté"| VPN_Server["Serveur VPN de l'entreprise"]
    VPN_Server -->|"Communication normale"| Internal_Network["Réseau interne"]
    Hacker["Tiers malveillant"] -.->|"Incompréhensible même si intercepté"| User
```

## 3. Les 2 principaux types de VPN

Il existe deux principaux types de VPN, selon leur objectif.

1. **VPN Internet (VPN d'accès à distance)**
   C'est ce que nous utilisons lorsque nous nous connectons au réseau de l'entreprise depuis la maison pour le télétravail. En utilisant un logiciel VPN installé sur votre ordinateur, un tunnel est créé jusqu'au routeur VPN de l'entreprise.
2. **VPN de site à site (VPN inter-sites)**
   Il s'agit d'une méthode pour connecter de manière sécurisée les réseaux de bureaux éloignés, tels que le « siège de Tokyo » et la « succursale d'Osaka », via Internet. Cela permet de réduire considérablement les coûts par rapport à l'installation d'une ligne dédiée.

## 4. L'évolution des protocoles (règles de communication)

Il existe également plusieurs types de règles (protocoles) pour créer des tunnels VPN.

- **IPsec** : Un protocole très robuste qui effectue le cryptage au niveau de la couche Internet (niveau IP). Souvent utilisé dans les VPN de site à site.
- **OpenVPN** : Le protocole dominant aujourd'hui, développé en open source, avec une sécurité et une flexibilité extrêmement élevées.
- **WireGuard** : Le protocole le plus récent qui attire l'attention ces dernières années. Il se caractérise par un code source très court et simple, et il est à la fois rapide et sécurisé.

## 5. Résumé

Le VPN est la « clé de voûte indispensable de la sécurité » dans notre société moderne où le télétravail s'est démocratisé.
Cependant, le VPN n'est pas omnipotent. Les cyberattaques visant les « vulnérabilités des équipements VPN (bugs logiciels) » augmentent également rapidement. Il est important de ne pas avoir une confiance aveugle dans le « tunnel sécurisé » qu'est le VPN, de toujours maintenir les logiciels à jour, et de mettre en œuvre une défense multicouche, comme la combinaison de l'authentification à deux facteurs (MFA) avec les mots de passe.
