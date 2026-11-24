---
title: "Instalar Hugo en Windows y previsualizar el sitio localmente"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Instala Hugo en Windows, configura PATH si hace falta y previsualiza un sitio local con borradores mediante los comandos actuales."
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Instalar Hugo en Windows y previsualizar un sitio localmente

> **Actualizado el 24 de noviembre de 2026.** El artículo anterior dependía de la salida de Hugo 0.102.3 y de pasos de Windows de 2022. Esta versión sigue la documentación oficial actual de instalación en Windows y de la CLI. Hugo, los cuadros de Windows y los paquetes pueden cambiar; consulta las guías oficiales enlazadas si la pantalla no coincide.

## Instalar Hugo

En Windows 10 o posterior, WinGet es una opción sencilla. Abre un terminal nuevo después de instalar y ejecuta el comando siguiente. Como alternativa, descarga del área oficial de versiones el archivo adecuado para tu versión de Windows y arquitectura de CPU, extráelo y coloca `hugo.exe` en una carpeta. Añade a PATH la carpeta que contiene el ejecutable, no el archivo en sí.

Para modificar PATH manualmente, busca en Inicio «Editar las variables de entorno de tu cuenta» y añade, por ejemplo, `C:/Hugo/bin` a la variable de usuario `Path`. Después abre un terminal nuevo.

## Instalar Hugo

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## Previsualizar localmente

Inicia el servidor desde la raíz del proyecto Hugo, donde está el archivo o directorio de configuración. `--buildDrafts` incluye los borradores en la vista previa. No uses una salida que incluya borradores para publicar en producción. Abre en el navegador la URL que muestra Hugo. La dirección predeterminada es `http://localhost:1313/`, pero comprueba la salida si el puerto está ocupado. Pulsa Ctrl+C en el terminal para detener el servidor.

## Referencias oficiales

- [Instalación en Windows](https://gohugo.io/installation/windows/)
- [Uso básico y borradores](https://gohugo.io/getting-started/usage/)
- [Comando hugo server](https://gohugo.io/commands/hugo_server/)
