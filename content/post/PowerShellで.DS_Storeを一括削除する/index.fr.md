---
title: "Supprimer des fichiers .DS_Store en masse avec PowerShell en toute sécurité"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Choisissez un dossier racine explicite, examinez les fichiers masqués correspondants et prévisualisez la suppression avec WhatIf."
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Si des fichiers `.DS_Store` créés par macOS restent dans des dossiers Windows, PowerShell peut les supprimer. Pour limiter l’opération, indiquez le dossier cible, vérifiez les chemins complets correspondants et prévisualisez l’action avec `-WhatIf` avant toute suppression.

## Lister les correspondances et prévisualiser

Remplacez `$root` par le chemin absolu du dossier à nettoyer. `-LiteralPath` empêche d’interpréter les caractères du chemin racine comme des jokers ; `-Filter` sélectionne les éléments nommés `.DS_Store`. `-File` exclut les dossiers portant ce nom. `-Recurse` parcourt les sous-dossiers et `-Force` inclut les éléments masqués.

```powershell
$root = 'C:\path\to\target-folder'

$files = @(
    Get-ChildItem -LiteralPath $root -Filter '.DS_Store' -File -Recurse -Force -ErrorAction Stop
)

# Review the exact files that matched.
$files | Select-Object -ExpandProperty FullName

# Preview the deletion; this does not remove files.
$files | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force -WhatIf
}
```

## Supprimer après vérification seulement

La première sortie affiche les chemins complets des fichiers correspondants. Le `-WhatIf` suivant présente les suppressions prévues sans les effectuer. Après avoir confirmé que la liste et l’aperçu sont corrects, retirez `-WhatIf` de la même ligne `Remove-Item` et exécutez-la.

## Périmètre et autorisations

L’exemple cible les fichiers nommés `.DS_Store` sous la racine choisie. Une racine incorrecte peut inclure des fichiers dans tout son contenu. `-Force` ne contourne pas les autorisations d’accès. En cas de refus d’accès, vérifiez le chemin et vos droits.

## Références Microsoft

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)
