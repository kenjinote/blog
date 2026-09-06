---








title: "Lista de comandos de Hugo"
slug: "Hugoコマンド一覧"
date: 2024-05-31T01:36:00+09:00
tags: ["hugo", "comandos"]
draft: false
image: "img.png"
categories: ["Operación del blog"]
---









# ¿Qué es Hugo?

Hugo es un generador de sitios estáticos. Puedes crear sitios web convirtiendo archivos Markdown a HTML. Hugo está escrito en el lenguaje Go y funciona a gran velocidad.

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
hugo new site <nombre del sitio>
```

Comando para crear un nuevo sitio. Especifica el nombre del sitio en `<nombre del sitio>`.

## Crear un nuevo artículo

```bash
hugo new <nombre del artículo>.md
```

Comando para crear un nuevo artículo. Especifica el nombre del artículo en `<nombre del artículo>`.

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

Comando para desplegar el sitio. La configuración del destino de despliegue se realiza en el archivo `config.toml`.

## Mostrar la lista de artículos

```bash
hugo list all
```

Comando para mostrar la lista de artículos.

## Confirmar la configuración

```bash
hugo config
```

Comando para confirmar la configuración.

## Mostrar la ayuda

```bash
hugo help
```

Comando para mostrar la ayuda.

## Mostrar la versión

```bash
hugo version
```

Comando para mostrar la versión.

Esta ha sido la lista de comandos de Hugo. Hay muchos otros comandos disponibles, así que consulta la documentación oficial.

# Referencia
- [Documentación oficial de Hugo](https://gohugo.io/documentation/)
