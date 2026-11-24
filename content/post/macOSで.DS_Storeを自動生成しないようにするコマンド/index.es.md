---
title: "Controlar la lectura de .DS_Store en recursos SMB de macOS"
slug: "macOSで.DS_Storeを自動生成しないようにするComando"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Instrucciones de Apple para desactivar o reactivar la lectura de archivos .DS_Store en recursos SMB de macOS. No impide que se creen; hay que cerrar sesión y volver a iniciarla."
---
Apple documenta esta preferencia como una forma de agilizar la navegación SMB: indica a macOS que **no lea archivos `.DS_Store` en recursos compartidos SMB**. No impide que se creen archivos nuevos ni elimina los existentes. Puede cambiar la presentación y el orden en Finder.

### Desactivar la lectura en recursos SMB

Ejecuta este comando en Terminal:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

Cierra la sesión de macOS y vuelve a iniciarla para aplicar el cambio. Finder utilizará información básica en vez de los metadatos de `.DS_Store` al mostrar las carpetas.

### Volver a activar la lectura

Establece el valor en `FALSE` para recuperar el comportamiento predeterminado:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

Después, cierra e inicia sesión de nuevo. Apple presenta esta opción como un ajuste de navegación SMB y señala que la guía está dirigida a administradores de empresas y centros educativos. Consulta [Soporte de Apple](https://support.apple.com/en-us/102064).
