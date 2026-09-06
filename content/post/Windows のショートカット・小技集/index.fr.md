---
title: "Raccourcis et astuces Windows"
slug: "Raccourcis et astuces Windows"
date: 2022-09-18T23:49:29+09:00
tags: ["Windows", "Astuces", "Raccourcis"]
draft: false
image: "img.png"
categories: ["PC et Gadgets"]
---
Voici une collection de petites astuces pour Windows que vous pouvez utiliser au quotidien. J'espère que ceux qui commencent à utiliser Windows la trouveront utile.
Elle est conçue pour Windows 11, mais je pense que la plupart des astuces fonctionnent également sur Windows 10.

## Fermer une fenêtre
- `Alt + F4` lorsque la fenêtre est active
- `Ctrl + W` lorsque la fenêtre est active. Ferme un onglet ou une fenêtre (uniquement pour les applications compatibles)
- Double-cliquez sur l'icône à gauche de la barre de titre de la fenêtre
- Cliquez sur le `×` dans la barre de titre de la fenêtre

## Afficher le bureau
- `Win + D`. Appuyez deux fois pour restaurer l'état précédent de la fenêtre. Pratique lorsque vous souhaitez afficher le bureau un instant.
- `Win + M`. Réduire toutes les applications. Appuyer deux fois ne restaure pas les fenêtres.

## Saisie vocale
- `Win + H`. Démarrer la saisie vocale. Pour arrêter la saisie vocale, appuyez sur `Esc` ou à nouveau sur `Win + H`.

## Afficher l'ancien menu contextuel dans l'Explorateur
- Appuyez sur `Shift + F10` ou sur la touche Application. La touche Application est située en bas à droite de votre clavier.

## Sélectionner une zone et faire une capture d'écran
- Vous pouvez sélectionner une zone et capturer l'écran avec `Win + Shift + S`.
- Vous pouvez capturer tout l'écran avec `Win + Print Screen` ou simplement `Print Screen`.
(Si vous ajoutez `Win`, l'image capturée sera enregistrée dans `C:\Users\Nom d'utilisateur\Pictures\Screenshots`.)
- Vous pouvez capturer la fenêtre actuelle avec `Alt + Print Screen`.

## Lancer des applications épinglées à la barre des tâches
- Vous pouvez lancer une application épinglée à la barre des tâches avec `Win + touche numérique`.  
  Par exemple, appuyer sur `Win + 1` lancera la première application en partant de la gauche dans la barre des tâches.
- Vous pouvez déplacer le focus vers les icônes de la barre des tâches avec `Win + T`, puis appuyer sur `Win + T` plusieurs fois ou utiliser `←` ou `→` pour vous déplacer et appuyer sur la touche `Enter` pour lancer l'application sélectionnée.

## Zoom avant / Zoom arrière
- `Win + +` lance la Loupe Windows. Vous pouvez ensuite utiliser `Win + + ou -` pour zoomer ou dézoomer l'écran.
- Vous pouvez utiliser `Ctrl + + ou -` pour zoomer/dézoomer dans des applications comme le Bloc-notes ou les navigateurs web (applications compatibles uniquement).

## Verrouiller Windows
- `Win + L`
- `Ctrl + Alt + Del` → `Space` ou `Enter`

## Éteindre Windows
- Si vous affichez le bureau avec `Win + M` ou `Win + D`, ou si la barre des tâches est active avec `Win + T` ou `Win + B`, appuyer sur `Alt + F4` affichera une boîte de dialogue comme ci-dessous. Assurez-vous que "Arrêter" est sélectionné et appuyez sur `Enter`.
  Vous pouvez aussi faire `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_20.png](img_20.png)
- Vous pouvez éteindre avec `Win + X` → `U` → `U`.
- Vous pouvez éteindre en tapant `shutdown /s /t 0` dans l'Invite de commandes ou dans "Exécuter" (`Win + R`). Ajouter `/f` forcera l'arrêt.

## Redémarrer Windows
- Si vous affichez le bureau avec `Win + M` ou `Win + D`, ou si la barre des tâches est active avec `Win + T` ou `Win + B`, appuyer sur `Alt + F4` affichera une boîte de dialogue comme ci-dessous. Appuyez sur `↓` une fois pour sélectionner "Redémarrer" et appuyez sur `Enter`.
  Vous pouvez aussi faire `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_21.png](img_21.png)
- Vous pouvez redémarrer avec `Win + X` → `U` → `R`.
- Vous pouvez redémarrer avec `shutdown /r /t 0`. Ajouter `/f` forcera le redémarrage.

## Mettre Windows en veille
- Si vous affichez le bureau avec `Win + M` ou `Win + D`, ou si la barre des tâches est active avec `Win + T` ou `Win + B`, appuyer sur `Alt + F4` affichera une boîte de dialogue comme ci-dessous. Appuyez sur `↑` une fois pour sélectionner "Veille" et appuyez sur `Enter`.
  Vous pouvez aussi faire `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_23.png](img_23.png)
- Vous pouvez mettre en veille prolongée en tapant `rundll32.exe powrprof.dll,SetSuspendState` dans `Win + R` ou l'Invite de commandes.

## Se déconnecter de Windows
- Si vous affichez le bureau avec `Win + M` ou `Win + D`, ou si la barre des tâches est active avec `Win + T` ou `Win + B`, appuyer sur `Alt + F4` affichera une boîte de dialogue comme ci-dessous. Appuyez sur `↑` deux fois pour sélectionner "Se déconnecter" et appuyez sur `Enter`.
  Vous pouvez aussi faire `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_22.png](img_22.png)
- `Win + X` → `U` → `I`
- `Ctrl + Alt + Del` → `Tab` deux fois ou `↓` deux fois → `Enter` ou `Space`
- Vous pouvez vous déconnecter avec `logoff`.

## Déplacer les fenêtres avec le clavier
- `Win + ←` : Déplacer vers la gauche
- `Win + →` : Déplacer vers la droite
- `Win + ↑` : Déplacer vers le haut / Agrandir
- `Win + ↓` : Déplacer vers le bas / Réduire
- `Win + Shift + ← ou →` : Déplacer entre les moniteurs
- `Win + Alt + ← ou → ou ↑ ou ↓` : Déplacer la fenêtre sans l'agrandir ou la réduire
- Lorsque non réduit, appuyez sur `Alt + Space`, puis `M`, puis utilisez les touches fléchées pour déplacer.  
* La fenêtre suivra le curseur de la souris, vous permettant de la récupérer même si elle est affichée hors de l'écran.

## Terminer un processus avec le Gestionnaire des tâches
![img_24.png](img_24.png)
1. Vous pouvez lancer le Gestionnaire des tâches avec `Ctrl + Shift + Esc`.
2. Vous pouvez changer d'onglet avec `Ctrl + Tab`.
3. Après avoir appuyé sur `Tab` dans l'onglet `Détails`, vous pouvez rechercher des processus par préfixe en utilisant la saisie alphanumérique du clavier.
4. Lorsque le nom du processus est sélectionné, appuyez sur la touche `Delete`, suivie de la touche `Enter` pour terminer le processus.

## Terminer un processus par son nom avec une commande
- Vous pouvez terminer un processus avec `taskkill /f /im nom_du_processus`.
Par exemple, vous pouvez terminer l'Explorateur avec `taskkill /f /im explorer.exe`

## Lancer plusieurs instances du même programme depuis la barre des tâches
- Maintenez la touche `Shift` et faites un clic gauche sur la barre des tâches pour lancer plusieurs instances du même programme. (Uniquement pour les applications qui supportent plusieurs instances)

## Lancer un programme avec des privilèges d'administrateur
- Lancer un programme en maintenant `Ctrl + Shift` le lancera avec des privilèges d'administrateur.

## Lancer l'Explorateur
- Vous pouvez lancer l'Explorateur avec `Win + E`.
- Affichez "Exécuter" avec `Win + R`, tapez `explorer` et appuyez sur `Enter`.
- Vous pouvez créer un nouveau dossier avec `Ctrl + Shift + N`.

## Ouvrir l'Invite de commandes à l'emplacement ouvert dans l'Explorateur
- Sur Windows 11, vous pouvez lancer l'Invite de commandes à partir de "Terminal" dans le menu du clic droit.
- Vous pouvez également lancer l'Invite de commandes en tapant `cmd` dans la barre d'adresse et en appuyant sur `Enter`.

## Afficher l'historique du presse-papiers
- Vous pouvez afficher l'historique du presse-papiers avec `Win + V`.
Vous pouvez sélectionner des textes ou images précédemment copiés pour les copier à nouveau.

## Exécuter
![img_28.png](img_28.png)
- Vous pouvez lancer "Exécuter" avec `Win + R`.

Voici quelques commandes que vous pouvez exécuter dans "Exécuter" ou dans l'Invite de commandes.

## Ouvrir Edge
![img_18.png](img_18.png)
- Tapez `msedge` et appuyez sur `Enter`

## Ouvrir Internet Explorer 11 (IE11)
![img_25.png](img_25.png)
- Tapez `powershell.exe -Command "(New-Object -ComObject InternetExplorer.Application).Visible = $true"` et appuyez sur `Enter`

## Ouvrir Terminal
![img_19.png](img_19.png)
- Tapez `wt` et appuyez sur `Enter`

## Ouvrir le Panneau de configuration
![img_15.png](img_15.png)
- Tapez `control` et appuyez sur `Enter`
- Vous pouvez également l'ouvrir avec `explorer.exe shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}`.

## Lancer le Bloc-notes
![img_4.png](img_4.png)
- Tapez `notepad` et appuyez sur `Enter`  

## Lancer la Calculatrice
![img_5.png](img_5.png)
- Tapez `calc` et appuyez sur `Enter`

## Lancer Paint
![img_6.png](img_6.png)
- Tapez `mspaint` et appuyez sur `Enter`  

## Lancer PowerShell
![img_7.png](img_7.png)
- Tapez `powershell` et appuyez sur `Enter`  

## Lancer Visual Studio Code
![img_8.png](img_8.png)
- Tapez `code` et appuyez sur `Enter`

## Lancer Excel
![img_9.png](img_9.png)
- Tapez `excel` et appuyez sur `Enter`  
* Uniquement si Excel est installé.

## Ouvrir Word
![img_10.png](img_10.png)
- Tapez `winword` et appuyez sur `Enter`  
* Uniquement si Word est installé.

## Ouvrir PowerPoint
![img_11.png](img_11.png)
- Tapez `powerpnt` et appuyez sur `Enter`  
  * Uniquement si PowerPoint est installé.

## Ouvrir la Configuration du système
![img_1.png](img_1.png)
- Tapez `msconfig` et appuyez sur `Enter`  

## Ouvrir les Propriétés système
![img_2.png](img_2.png)
- Tapez `sysdm.cpl` et appuyez sur `Enter`

## Ouvrir À propos de Windows
![img_27.png](img_27.png)
- Tapez `winver` et appuyez sur `Enter`

## Ouvrir le Clavier visuel
![img_14.png](img_14.png)
- Tapez `osk` et appuyez sur `Enter`

## Ouvrir WordPad
![img_12.png](img_12.png)
- Tapez `wordpad` ou `write` et appuyez sur `Enter`

## Ouvrir l'Éditeur du Registre
![img_13.png](img_13.png)
- Tapez `regedit` et appuyez sur `Enter`

## Ouvrir Programmes et fonctionnalités
- Tapez `explorer.exe shell:::{7b81be6a-ce2b-4676-a29e-eb907a5126c5}` et appuyez sur `Enter`

## Ouvrir les Propriétés de Clavier
- Tapez `explorer.exe shell:::{725BE8F7-668E-4C7B-8F90-46BDB0936430}` et appuyez sur `Enter`

## Ouvrir les Propriétés de Souris
![img_16.png](img_16.png)
- Tapez `explorer.exe shell:::{6C8EEC18-8D75-41B2-A177-8831D59D2D50}` et appuyez sur `Enter`

## Ouvrir Son
![img_3.png](img_3.png)
- Tapez `explorer.exe shell:::{F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D}` et appuyez sur `Enter`

## Ouvrir Comptes d'utilisateurs
- Tapez `explorer.exe shell:::{60632754-c523-4b62-b45c-4172da012619}` et appuyez sur `Enter`

## Copier le texte d'une boîte de message standard
![img_26.png](img_26.png)
- Vous pouvez copier le texte d'une boîte de message standard avec `Ctrl + C`.
Copier la boîte de message ci-dessus copiera ceci dans le presse-papiers :
```
[Window Title]
WordPad

[Main Instruction]
Voulez-vous enregistrer les modifications apportées à Document ?

[Enregistrer (S)] [Ne pas enregistrer (N)] [Annuler]
```

## Stocker la sortie de l'Invite de commandes dans le presse-papiers
Ajouter ` | clip` (tube + clip) après une commande, tel que `echo "hello" | clip`, copie la sortie standard dans le presse-papiers.

## Sortir la hiérarchie des dossiers sous forme de texte
Vous pouvez sortir la hiérarchie des dossiers au format d'arbre avec la commande `tree` dans l'Invite de commandes.

Exemple de sortie
```
C:.
├─.idea
│  └─libraries
├─binaryeditorbz
├─blog
│  ├─archetypes
│  ├─content
│  ├─data
│  ├─layouts
│  ├─static
│  └─themes
│      └─PaperMod
│          ├─.git
│          │  ├─branches
│          │  ├─hooks
│          │  ├─info
│          │  ├─logs
│          │  │  └─refs
│          │  │      ├─heads
│          │  │      └─remotes
│          │  │          └─origin
│          │  ├─objects
│          │  │  ├─info
│          │  │  └─pack
│          │  └─refs
│          │      ├─heads
│          │      ├─remotes
│          │      │  └─origin
│          │      └─tags
│          ├─.github
│          │  ├─ISSUE_TEMPLATE
│          │  └─workflows
│          ├─assets
│          │  ├─css
│          │  │  ├─common
│          │  │  ├─core
│          │  │  ├─extended
│          │  │  ├─hljs
│          │  │  └─includes
│          │  └─js
│          ├─i18n
│          ├─images
│          └─layouts
│              ├─partials
│              │  └─templates
│              ├─shortcodes
│              └─_default
│                  └─_markup
(et ainsi de suite)
```

## Référence
- [Raccourcis clavier de Windows](https://support.microsoft.com/ja-jp/windows/windows-%E3%81%AE%E3%82%AD%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89-%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%82%AB%E3%83%83%E3%83%88-dcc61a57-8ff0-cffe-9796-cb9706c75eec)
