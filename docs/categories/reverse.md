---
title: Reverse engineering basics
description: Apne banaye hue chhote program ke behavior ko samajhne ka safe intro.
tags:
  - reverse
  - beginner
---

# Reverse

Reverse engineering mein compiled program ka behavior aur structure inspect karte hain. Begin apne banaye hue sample se karo; unknown software ko run karne se pehle usay isolate karo, aur proprietary code ke rights aur license ka ehtiram karo.

## Safe beginner exercise

Ek chhota local Python program likho jo ek fixed word ko reverse kare. Usay Python bytecode mein compile karke `dis` module se instructions print karo, phir source aur bytecode view ka farq likho. Sample mein network, files, ya credentials access na rakho.

```sh
python3 -m compileall sample.py
python3 -m dis sample.py
```

## Aage parho

- [Python `dis` module documentation](https://docs.python.org/3/library/dis.html)
- [Ghidra documentation](https://ghidra-sre.org/)
- [OWASP: Mobile Application Security Testing Guide](https://mas.owasp.org/MASTG/) — mobile testing sirf apne/authorized app par.
