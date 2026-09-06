---
title: "Comment supprimer par lots les métadonnées (informations personnelles) d'Excel, Word, etc. avec PowerShell"
slug: "Comment supprimer les métadonnées (informations personnelles) d'Excel avec PowerShell"
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Métadonnées", "Informations personnelles"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["Programmation"]
---

# "Comment supprimer par lots les métadonnées (informations personnelles) d'Excel, Word, etc. avec PowerShell"

Les fichiers Office comme Excel enregistrent automatiquement des « métadonnées (informations personnelles) » telles que le créateur, la dernière personne à avoir modifié le fichier et le nom de l'entreprise. Il y a de nombreux cas où vous souhaitez supprimer ces informations, par exemple lors du partage d'un fichier à l'extérieur de l'entreprise.

Dans cet article, nous expliquerons en détail comment supprimer les métadonnées Excel à l'aide de PowerShell, en nous concentrant sur ** le traitement par lots dans un dossier ** et ** l'application à d'autres fichiers Office tels que Word et PowerPoint ** .

---

## 1. Supprimer les métadonnées d'un seul fichier Excel

Il s'agit du script le plus basique pour supprimer les informations personnelles d'un seul fichier Excel. Il appelle l'objet COM d'Excel, définit la propriété `RemovePersonalInformation` sur `$true` et l'enregistre en écrasant le fichier.

```powershell
# Démarrer l'application Excel de manière invisible
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# Ouvrir le fichier (*veuillez spécifier le chemin absolu)
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# Activer le paramètre pour supprimer les métadonnées (informations personnelles)
$wb.RemovePersonalInformation = $true

# Écraser et fermer
$wb.Save()
$wb.Close($false)

# Quitter Excel et libérer la mémoire
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> ** Attention : ** Assurez-vous de spécifier le ** chemin absolu (chemin complet) ** pour le chemin passé à `Workbooks.Open()`. Un chemin relatif peut entraîner une erreur.

---

## 2. Traiter par lots tous les fichiers Excel dans un dossier

Dans la pratique, vous voudrez souvent « supprimer d'un coup toutes les métadonnées de dizaines de fichiers Excel dans un dossier spécifique ». Cela peut être réalisé en utilisant un traitement en boucle combiné à `Get-ChildItem`.

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# Obtenir tous les fichiers .xlsx et .xls dans le dossier
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "Aucun fichier Excel trouvé."
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "Suppression des métadonnées de $($file.Name)..."
    
    # Ouvrir le fichier
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # Supprimer les métadonnées et enregistrer
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "Tout le traitement est terminé !"
```

---

## 3. Supprimer les métadonnées d'autres fichiers Office (Word / PowerPoint)

Les métadonnées peuvent être supprimées avec exactement la même logique non seulement dans Excel, mais aussi dans Word et PowerPoint. Seul le nom de l'objet COM à appeler est différent, et il est courant que la propriété `RemovePersonalInformation` soit fournie.

### Pour Word

```powershell
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

$doc = $word.Documents.Open("C:\Path\To\Your\File.docx")
$doc.RemovePersonalInformation = $true
$doc.Save()
$doc.Close()

$word.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
```

### Pour PowerPoint

Pour PowerPoint, le réglage de la propriété `RemovePersonalInformation` est similaire, mais le comportement du démarrage invisible est légèrement différent.

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# Ouvrir en spécifiant le mode caché (msoFalse) etc. avec les 2ème à 4ème arguments
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## Conclusion

En utilisant PowerShell et des objets COM, vous pouvez automatiser entièrement la suppression des métadonnées des fichiers Office. Il est très utile d'avoir sous la main un script de traitement par lots avant la livraison afin d'éviter la fuite involontaire d'informations confidentielles ou de noms personnels.
