---
title: Pwn and memory-safety concepts
description: Memory layout aur safe systems programming ke concepts ka gentle introduction.
tags:
  - pwn
  - systems
  - beginner
---

# Pwn

Pwn challenges aam tor par program behavior, memory layout aur bugs ke concepts sikhate hain. Yahan hum pehle defensive foundations padhte hain: bytes, buffers, bounds aur compiler protections.

## Safe beginner exercise

Apne local machine par ek chhota C program likho jo user-supplied byte array ko **bounds ke andar** print karta ho. Input length verify karo, phir sanitizer-enabled compiler build ki diagnostics padhna seekho. Kisi network service, real executable, ya doosre user ke process ko target na karo.

```sh
cc -Wall -Wextra -Wpedantic -fsanitize=address -g safe-bytes.c -o safe-bytes
```

## Aage parho

- [MITRE CWE: Memory Buffer Errors](https://cwe.mitre.org/data/definitions/119.html)
- [GCC instrumentation options](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html)
- [OpenSSF Secure Coding Guide](https://best.openssf.org/Secure-Coding-Guide-for-Python/)

Is intro mein exploit development shamil nahi; pehle safe coding aur authorized, isolated training labs par focus karo.
