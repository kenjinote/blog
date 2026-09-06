---




title: "Cómo eliminar de forma masiva metadatos (información personal) de Excel, Word, etc. con PowerShell"
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Metadatos", "Información personal"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["Programación"]
---





# Cómo eliminar de forma masiva metadatos (información personal) de Excel, Word, etc. con PowerShell

Los archivos de Office como Excel guardan automáticamente "metadatos (información personal)" como el autor, la persona que lo modificó por última vez, el nombre de la empresa, etc. Hay muchos casos en los que se desea eliminar esta información, como al compartir archivos fuera de la empresa.

En este artículo, explicaremos en detalle cómo eliminar metadatos de Excel usando PowerShell, enfocándonos en el **procesamiento por lotes en una carpeta** y su **aplicación a otros archivos de Office como Word y PowerPoint**.

---

## 1. Eliminar los metadatos de un solo archivo de Excel

Este es el script más básico para eliminar la información personal de un solo archivo de Excel. Llama al objeto COM de Excel, establece la propiedad `RemovePersonalInformation` en `$true` y guarda los cambios sobrescribiendo el archivo.

```powershell
# Iniciar la aplicación Excel de forma oculta
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# Abrir el archivo (*Especificar ruta absoluta)
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# Habilitar la configuración para eliminar metadatos (información personal)
$wb.RemovePersonalInformation = $true

# Guardar sobrescribiendo y cerrar
$wb.Save()
$wb.Close($false)

# Cerrar Excel y liberar memoria
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> **Nota:** La ruta que se pasa a `Workbooks.Open()` debe ser siempre una **ruta absoluta (ruta completa)**. El uso de rutas relativas puede causar errores.

---

## 2. Procesar todos los archivos de Excel en una carpeta en masa

En la práctica, habrá muchos casos en los que se desee "eliminar los metadatos de docenas de archivos de Excel en una carpeta específica a la vez". Esto se puede lograr combinando `Get-ChildItem` con un bucle.

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# Obtener todos los archivos .xlsx y .xls en la carpeta
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "No se encontraron archivos de Excel."
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "Eliminando metadatos de $($file.Name)..."
    
    # Abrir el archivo
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # Eliminar metadatos y guardar sobrescribiendo
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "¡Todo el procesamiento ha finalizado!"
```

---

## 3. Eliminar metadatos de otros archivos de Office (Word / PowerPoint)

Los metadatos se pueden eliminar no solo en Excel, sino también en Word y PowerPoint utilizando exactamente la misma lógica. Lo único que cambia es el nombre del objeto COM que se llama; la propiedad `RemovePersonalInformation` es común en todos.

### Para Word

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

### Para PowerPoint

En el caso de PowerPoint, la configuración de la propiedad `RemovePersonalInformation` es la misma, pero el comportamiento del inicio oculto es un poco diferente.

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# Abrir especificando el modo oculto (msoFalse), etc. del segundo al cuarto argumento
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## Resumen

Aprovechando PowerShell y los objetos COM, puede automatizar completamente la eliminación de metadatos de archivos de Office. Para evitar la filtración accidental de información confidencial o nombres personales, es muy útil tener a mano un script de procesamiento por lotes para carpetas antes de entregar los archivos.
