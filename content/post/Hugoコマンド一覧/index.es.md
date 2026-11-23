---
title: 'Instalación de la CLI de Hugo y lista de comandos básicos más usados'
slug: "HugoComando一覧"
date: 2024-05-31T01:36:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["hugo", "comandos"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Presentamos cómo instalar la CLI de Hugo, un rápido generador de sitios estáticos, y una lista de comandos básicos que usarás frecuentemente al gestionar tu blog. Explicamos las operaciones que los principiantes en Hugo deben memorizar: crear un sitio nuevo, escribir artículos, iniciar el servidor local, hacer la build, etc.'
---

# ¿Qué es Hugo?

Hugo es un generador de sitios estáticos. Puedes crear sitios web convirtiendo archivos Markdown a HTML. Hugo está escrito en el lenguaje [Go](https://kenji.blog/es/p/programming-languages-history-paradigm-evolution/) y funciona a gran velocidad.

Este blog también fue creado con Hugo.

# Instalación del CLI de Hugo

Para instalar el CLI de Hugo, ejecuta el siguiente comando:

※ Ejemplo para macOS. Para otros sistemas operativos, consulta la documentación oficial.

```bash
brew install hugo
```

Se puede instalar usando Homebrew.

# Lista de comandos de Hugo

Hugo ofrece varios comandos. A continuación, se resumen los comandos más utilizados.

## Crear un nuevo sitio

```bash
hugo new project <site-name>
```

Crea un sitio nuevo con el nombre que indiques.

## Crear un nuevo artículo

```bash
hugo new content posts/<post-name>.md
```

Crea un archivo de contenido en la ruta especificada.

## Iniciar el servidor

```bash
hugo server
```

Comando para iniciar un servidor local. Se puede acceder en `http://localhost:1313`.

## Construir (Build)

```bash
hugo
```

Comando para construir el sitio. Los archivos HTML se generan en el directorio `public`.

## Desplegar (Deploy)

```bash
hugo deploy
```

Este comando despliega el sitio en proveedores compatibles de almacenamiento en la nube. Configura el destino en la sección `deployment` y autentícate con la CLI del proveedor. No es un comando genérico para cualquier alojamiento web, como GitHub Pages. Hugo v0.159.2 y posteriores requieren la edición Deploy.

## Mostrar la lista de artículos

```bash
hugo list all
```

Muestra todo el contenido, incluidos borradores, contenido con fecha futura y contenido vencido.

## Confirmar la configuración

```bash
hugo config
```

Muestra tanto los valores predeterminados como la configuración definida para el sitio.

## Mostrar la ayuda

```bash
hugo help
```

Comando para mostrar la ayuda.

## Mostrar la versión

```bash
hugo version
```

Muestra la versión de Hugo y la información del entorno.


Esta ha sido la lista de comandos de Hugo. Hay muchos otros comandos disponibles, así que consulta la documentación oficial.

# Referencia
- [Crear un proyecto](https://gohugo.io/commands/hugo_new_project/)
- [Crear contenido](https://gohugo.io/commands/hugo_new_content/)
- [Desplegar](https://gohugo.io/commands/hugo_deploy/)
- [Listar todo el contenido](https://gohugo.io/commands/hugo_list_all/)
- [Instalar en macOS](https://gohugo.io/installation/macos/)
