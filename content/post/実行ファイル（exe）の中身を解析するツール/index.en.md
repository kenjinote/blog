---
title: "Tools to Analyze the Contents of Executable Files (exe)"
slug: "tools-to-analyze-executable-files"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "executable files", "analysis"]
draft: false
image: "img_1.png"
categories: ["PC and Gadgets"]
---

# What is an Executable File (exe)

A file that can be executed on Windows. Basically, it is written in a format called PE format.
It contains machine code to execute, as well as resources such as icons and images.

Since there are several tools to analyze executable files, I will introduce them here.

## 7-Zip

![img.png](img.png)

EXE files are sometimes compressed because their size tends to be large otherwise. In this case, by using the file compression and decompression software 7-Zip, you can extract the executable file and examine its contents. WinRAR is another tool that can extract them similarly.

## Resource Hacker
![img_2.png](img_2.png)

It allows you to extract resources (icons, bitmaps, dialog boxes, strings, etc.) inside an EXE file. Additionally, since it functions as a binary editor, you can edit and rewrite the contents of an EXE file.

## PE Explorer
![img_3.png](img_3.png)

It can analyze PE files (EXE, DLL, OCX, SYS, drivers) for Windows. PE Explorer provides various analysis features, such as displaying the file structure, file headers, directory entries, and exported functions and symbols.

## Dependency Walker
![img_4.png](img_4.png)

You can investigate the DLL files that an EXE file depends on and verify whether they are loaded correctly. You can also trace the function calls of DLL files.

## Ghidra

![img_5.png](img_5.png)

This is a powerful reverse engineering tool developed by the NSA (National Security Agency) and released for free as open source. It is highly popular because it not only disassembles EXE files (converts them to assembly language) but also has decompilation capabilities to convert them into a form close to C language.

## IDA Free / IDA Pro

![img_6.png](img_6.png)

These are high-performance disassemblers and decompilers that have become a global industry standard in malware analysis and reverse engineering. The Pro version is very expensive, but you can use the functionally restricted version "IDA Free" for free for personal or non-commercial purposes.

## x64dbg (x32dbg)

![img_7.png](img_7.png)

An open source debugger for Windows. It specializes in "dynamic analysis," which involves analyzing the internal state and memory step-by-step while running the executable file. It is commonly used for solving crackmes (challenge programs for analysis) and investigating malware behavior.

## ILSpy / dotPeek

![img_8.png](img_8.png)

If the target EXE file is created in a .NET language such as C#, using these tools allows you to decompile (reverse compile) it into almost the exact same state as the original source code, completely exposing its contents.

These tools are useful for examining the contents of EXE files, but caution is required. Modifying files or using them for unauthorized purposes can cause copyright and security issues, so please ensure you fully understand this before using them.
