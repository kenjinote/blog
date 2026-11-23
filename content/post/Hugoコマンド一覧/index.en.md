---
title: 'Hugo CLI Installation and List of Frequently Used Basic Commands'
slug: "HugoCommand一覧"
date: 2024-05-31T01:36:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["hugo", "command"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'We introduce the CLI installation method for the fast static site generator Hugo, and a list of basic commands frequently used in blog operation. We explain the operations Hugo beginners should remember, such as launching a new site, creating articles, starting a local server, and building.'
---

# What is Hugo?

Hugo is a static site generator. It can convert Markdown files into HTML and create websites. Hugo is written in the [Go](https://kenji.blog/en/p/programming-languages-history-paradigm-evolution/) language and runs very fast.

This blog is also created with Hugo.

# Installing the Hugo CLI

To install the Hugo CLI, run the following command.

* Example for macOS. For other operating systems, please refer to the official documentation.

```bash
brew install hugo
```

You can install it using Homebrew.

# Hugo Command List

Hugo provides various commands. Below is a summary of commonly used commands.

## Create a new site

```bash
hugo new project <site-name>
```

Creates a new site using the name you provide.

## Create a new post

```bash
hugo new content posts/<post-name>.md
```

Creates a new content file at the specified path.

## Start the server

```bash
hugo server
```

Command to start a local server. You can access it at `http://localhost:1313`.

## Build the site

```bash
hugo
```

Command to build the site. HTML files will be generated in the `public` directory.

## Deploy the site

```bash
hugo deploy
```

This command deploys to supported cloud storage providers. Configure a target in the `deployment` section of the site configuration and authenticate with the provider's CLI. It is not a general-purpose command for web hosts such as GitHub Pages. Hugo v0.159.2 and later require the Deploy edition.

## List all posts

```bash
hugo list all
```

Lists all content, including drafts, future-dated items, and expired content.

## Check configuration

```bash
hugo config
```

Displays both default settings and the settings configured for the site.

## Display help

```bash
hugo help
```

Command to display help information.

## Display version

```bash
hugo version
```

Displays the Hugo version and environment information.


That concludes the Hugo command list. There are many other commands available, so please refer to the official documentation for more details.

# References
- [Create a project](https://gohugo.io/commands/hugo_new_project/)
- [Create content](https://gohugo.io/commands/hugo_new_content/)
- [Deploy](https://gohugo.io/commands/hugo_deploy/)
- [List all content](https://gohugo.io/commands/hugo_list_all/)
- [Install on macOS](https://gohugo.io/installation/macos/)
