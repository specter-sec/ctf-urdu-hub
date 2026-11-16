---
title: Beginner Linux
description: Paths, commands aur local files ko safely explore karna seekho.
tags:
  - linux
  - beginner
---

# Beginner Linux

Linux terminal se files aur folders par kaam karna CTF learning ka useful hissa hai. Paths ko quote karo, `pwd` se location confirm karo, aur destructive command chalane se pehle uska effect samjho.

## Safe beginner exercise

[File Dhoondo](../writeups/linux/file-dhoondo.md) ka offline directory tree generate karo. Sirf usi folder ke andar `find` se `clue.txt` dhoondo aur `cat` se parho. Fixture se bahar recurse na karo; [generator source](https://github.com/specter-sec/ctf-urdu-hub/blob/main/labs/linux-find.py) doosri jagah files nahin dhoondhta.

```sh
python3 labs/linux-find.py
find labs/work/linux-find -type f -name 'clue.txt' -print
```

## Aage parho

- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [`find(1)` Linux manual](https://man7.org/linux/man-pages/man1/find.1.html)
- [The Linux Command Line](https://linuxcommand.org/tlcl.php)

Commands ko samajh kar use karo; unknown shell scripts ko seedha execute mat karo.
