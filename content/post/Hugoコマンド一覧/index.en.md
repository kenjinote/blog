---
title: 'Hugo Command List'
slug: "Hugoコマンド一覧"
date: 2024-05-31T01:36:00+09:00
tags: ["hugo", "command"]
draft: false
image: "img.png"
categories: ["blog management"]
---

# What is Hugo?

Hugo is a static site generator. It can convert Markdown files into HTML and create websites. Hugo is written in the Go language and runs very fast.

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
hugo new site <site-name>
```

Command to create a new site. Specify the name of the site in `<site-name>`.

## Create a new post

```bash
hugo new <post-name>.md
```

Command to create a new post. Specify the name of the post in `<post-name>`.

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

Command to deploy the site. Deployment settings are configured in the `config.toml` file.

## List all posts

```bash
hugo list all
```

Command to display a list of all posts.

## Check configuration

```bash
hugo config
```

Command to check the configuration.

## Display help

```bash
hugo help
```

Command to display help information.

## Display version

```bash
hugo version
```

Command to display the version.

That concludes the Hugo command list. There are many other commands available, so please refer to the official documentation for more details.

# References
- [Hugo Official Documentation](https://gohugo.io/documentation/)
