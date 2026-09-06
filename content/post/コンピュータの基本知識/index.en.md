---
title: 'Basic Knowledge of Computers'
slug: "コンピュータの基本知識"
date: 2024-09-19T01:10:20+09:00
tags: ["Computer", "Basic Knowledge"]
draft: false
image: "img.png"
categories: ["IT/Technology"]
---

# Basic Knowledge of Computers

This page explains what a computer is.

## Definition of a Computer
A computer is a machine that has the following five units:

1. Input unit
2. Output unit
3. Storage unit
4. Control unit
5. Arithmetic logic unit

Roughly speaking, a computer is a machine that performs a specific `process` on a certain `input` and `outputs` the result.
It can `store`, `calculate`, and `output` the `input` data. `Control` has the role of controlling the aforementioned four units.

## What is needed to operate a computer
To operate a computer, programs (software) are needed in addition to the devices (hardware).

Programs instruct the computer on what kind of processing to perform. Programs are written in a format that the computer can understand.

An example of a program is as follows.
A program that calculates the sum from 1 to an input integer:
```
#include <iostream>
using namespace std;

int main() {
    // Secure necessary storage area
    int n, sum = 0;
    
    // Output
    cout << "Please enter an integer: ";
    
    // Input 
    cin >> n;
    
    // Calculation
    for (int i = 1; i <= n; i++) { // Calculation
        sum += i;
    }
    
    // Output
    cout << "The sum from 1 to " << n << " is " << sum << "." << endl;
    
    // Exit
    return 0;
}
```

The program is converted into machine code by a compiler, transforming it into a format that the computer can execute.
