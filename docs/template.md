---
title: Writeup template
description: Reproducible, ethical aur learner-friendly CTF notes likhne ka template.
tags:
  - writing
  - beginner
---

# Writeup template

Is template ko copy karke `docs/writeups/<category>/<slug>.md` mein save karo. Sirf authorized practice ke notes publish karo; private data, credentials, ya live-target exploitation details mat dalo.

```yaml
---
title: Short, descriptive title
description: Ek jumle mein core learning point.
tags:
  - beginner
  - web
---
```

## Quick overview

Challenge ya exercise ka naam, category, apna role, aur kis qisam ka fictional lab tha? Live target ya private account ka URL/identifier publish na karo.

## Learning goals

- Kaunsa concept samajhna hai?
- Exercise ke end tak kya khud explain kar paoge?

## Scope and safety

Authorization/scope kya tha? Batao ke kaam local fixture, official sandbox, ya explicitly authorized challenge tak limited tha. Agar scope clear nahi tha, stop karo.

## Setup

Required tools aur versions likho. Commands ko reproducible rakho. Secrets, tokens, personal files aur environment-specific data redact karo.

```sh
# Apne approved local practice folder se shuru karo
pwd
```

## Investigation notes

Har qadam par observation aur us se nikla inference alag likho. Useful commands/code blocks add karo, magar unexplained output dump na karo.

1. Pehla observation aur evidence
2. Iska kya matlab ho sakta hai
3. Agla safe verification step

## Solution reasoning

Clue se answer tak reasoning ko qadam-ba-qadam samjhao. Alternative explanations aur uncertainty ka zikr karo. Reproduction ke liye bas zaroori details rakho.

## Result

Sirf is project ka fictional `CTFURDU{...}` demo marker ya non-sensitive lesson result. Platform flags, credentials, tokens, ya private challenge answers publish na karo.

## What I learned

- Kaunsa concept pehle mushkil tha?
- Kaunsi evidence ne conclusion support kiya?
- Is method ki limitation kya hai?

## References

Official docs / training material ke links, access date agar relevant ho, aur jis hissa se idea liya us ka clear attribution. Kisi answer key ya third-party writeup ko copy na karo.
