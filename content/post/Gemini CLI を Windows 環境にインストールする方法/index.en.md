---
title: 'How to Install Gemini CLI on Windows Environment'
date: 2025-07-13T23:49:56+09:00
tags: ["Gemini", "CLI", "Windows", "install", "development"]
draft: false
image: "img.png"
categories: ["PC & Gadgets"]
---

# [For Beginners] How to Install Gemini CLI on Windows

"Gemini CLI" allows you to use Google's generative AI "Gemini" from the command line.
In this article, we will explain the steps to install Gemini CLI in a Windows environment as easily as possible.

---

## 1. Preparation: Install Node.js and npm

First, since Gemini CLI runs on an environment called "Node.js", you need to have the following installed:

* **Node.js**
* **npm (Package management tool included with Node.js)**
* **npx (Command execution tool included with npm)**

Please download the Windows version of Node.js from the official website below (the LTS version is recommended):

👉 [Node.js Official Website](https://nodejs.org/)

Once the installation is complete, let's verify if it was installed correctly with the following commands.

```powershell
node -v
npm -v
```

---

## 2. Launch PowerShell

To use Gemini CLI on Windows, it is common to operate it using PowerShell.
Type "PowerShell" in the Start menu to launch it.

---

## 3. Install Gemini CLI

Copy and paste the following command into PowerShell and execute it:

```bash
npx @google/gemini-cli
```

This command temporarily executes the Gemini CLI package published by Google.
You may be prompted for initial setup or login if necessary.

* Note: It may take a few minutes the first time. If you encounter an error, please double-check your Node.js or network environment.

---

## 4. Installation Complete! What to do next

Now, Gemini CLI has been installed on Windows.
From now on, you will be able to perform various operations using Gemini from the command line, such as text generation and code completion.

If you want to check the official documentation or help, you can also utilize commands like the following.

```bash
npx @google/gemini-cli --help
```

---

## Conclusion

Let's review the steps to introduce Gemini CLI to Windows.

1. Install Node.js and npm
2. Launch PowerShell
3. Execute `npx @google/gemini-cli`

Now you're all set!
If you want to use generative AI locally, please give it a try using these steps as a reference.
