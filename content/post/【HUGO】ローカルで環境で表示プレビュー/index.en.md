---
title: '[HUGO] Display Preview in Local Environment'
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["Blog Operation"]
---
# Installing HUGO

## Download
[Download HUGO](https://github.com/gohugoio/hugo/releases)

From the site above, download and extract the Windows module that matches your environment.
In my case, I downloaded "hugo_0.102.3_Windows-64bit.zip".

## Extract
Extract the downloaded zip file and copy the hugo.exe inside it to a folder, for example, C:\bin.

## Register to Environment Variables
Register it to the environment variables so that you can run hugo.exe from anywhere.
This is the operation on Windows 11, but I think it can be registered with the following steps.

1. Press Win+Pause to open the About page
2. Click Advanced system settings
3. Click Environment Variables
4. Select Path and click Edit
5. Click New, enter "C:\bin" on a new line, and click OK to close the dialog

# Preview the Blog
In the command prompt, navigate to your HUGO blog folder and run the following command.

`hugo server -D`

The execution result is as follows. (The -D option is for displaying draft articles.)

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
Pages            | 39
Paginator pages  |  0
Non-page files   |  7
Static files     |  0
Processed images |  0
Aliases          | 13
Sitemaps         |  1
Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

The address will be output when executed (in the example above, `http://localhost:1313/`), so copy the address to your browser.
The preview will automatically update every time you save a file.
To end the preview, press Ctrl+C in the command prompt.
