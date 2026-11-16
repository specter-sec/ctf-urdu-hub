---
title: Digital forensics basics
description: Local files ko carefully inspect karke evidence aur assumptions alag rakho.
tags:
  - forensics
  - beginner
---

# Forensics

Digital forensics mein file type, bytes, metadata aur context se clues samjhe jate hain. Ek artifact akela aksar origin ya authenticity prove nahi karta; apni observations aur conclusions alag rakho.

## Safe beginner exercise

[Image Ke Andar](../writeups/forensics/image-ke-andar.md) ka fictional image fixture banao, `file` aur `strings` jaise read-only tools se inspect karo, aur result ko generator ke synthetic marker se compare karo. Fixture ke bahar files search na karo; [lab source](https://github.com/specter-sec/ctf-urdu-hub/blob/main/labs/forensics-strings.py) local output banata hai.

## Aage parho

- [NIST SP 800-86: Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final)
- [The Sleuth Kit documentation](https://www.sleuthkit.org/sleuthkit/docs.php)
- [ExifTool documentation](https://exiftool.org/)

Evidence preserve karo, timestamps aur provenance ko context ke saath samjho, aur privacy ka khayal rakho.
