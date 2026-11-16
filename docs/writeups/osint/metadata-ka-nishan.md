---
title: "Metadata ka Nishan: Image Claims ko Samajhna"
description: "TryHackMe OhSINT se inspired, magar alag aur offline fictional practice: image metadata, source claims, aur verification ke bunyadi usool."
tags:
  - osint
  - metadata
  - beginner
category: OSINT
difficulty: Beginner
platform: TryHackMe
---

# Metadata ka Nishan: Image Claims ko Samajhna

**CTF Urdu Hub by IFTIKHAR**

Yeh beginner writeup image ke saath milne wali maloomat ko ehtiyat se parhne aur source claims ko verify karne ka tareeqa samjhata hai. Official [TryHackMe OhSINT room page](https://tryhackme.com/room/ohsint) public taur par ek image se mil sakne wali maloomat ka broad theme batata hai. Is guide mein us room ke task prompts ya answers shamil nahin hain. **Yeh platform ka exact solution nahin, original offline practice recreation hai.** Neeche diye gaye naam, dates, source claim aur demo marker sab fictional local fixture ka hissa hain.

## Is exercise ke baad

- Samajh aayega ke metadata ek lead ya claim ho sakta hai, apne aap mein sach ka saboot nahin.
- JSON mein rakhe synthetic metadata aur asal embedded image metadata ka farq samajh aayega.
- Local PNG ke aakhir mein rakha harmless ASCII marker Python se parh paoge.
- Kisi claim ko independently verify karne aur privacy-respecting scope mein rehne ki aadat banegi.

## Zaroori pehle se maloomat

- Terminal mein basic commands chalana.
- Python 3.10 ya us se naya version. Kali, Termux aur Linux par Python aam tor par `python3` command se chalta hai.
- GitHub repository ka local checkout. Is exercise ko repository root se chalana hai.
- Pillow, ExifTool aur internet access lazim nahin. Fixture generator sirf Python standard library use karta hai.

## Setup: repository root se

Agar repository pehle hi clone ki hui hai to us folder mein jao; warna public repository ka clone command yeh hai:

```bash
git clone https://github.com/specter-sec/ctf-urdu-hub.git
cd ctf-urdu-hub
```

Agar folder pehle maujood hai to dobara clone na karo; sirf us mein `cd` karo. Root verify karo aur Python version dekho:

```bash
pwd
python3 --version
```

`pwd` ke output ka aakhri hissa `ctf-urdu-hub` hona chahiye. Ab fixture banao:

```bash
python3 labs/osint-metadata.py
```

Generator keval `labs/work/osint-metadata/` ke andar do files likhta hai. Har run deterministic hai: wohi fictional text aur wohi image bytes banenge. Script koi network request ya shell command nahin chalati.

## Step 1: synthetic claims ko parho

Hum ek chhoti JSON file ko ek imaginary image ke saath diye gaye notes samajh kar dekhenge. Yeh JSON **synthetic local metadata** hai: image ke andar embedded EXIF ya PNG metadata nahin.

```bash
python3 -c 'import json; from pathlib import Path; p=Path("labs/work/osint-metadata/synthetic-metadata.json"); d=json.loads(p.read_text(encoding="utf-8")); print(d["notice"]); print("Claimed creator:", d["fictional_claims"]["creator"]); print("Claimed source:", d["fictional_claims"]["claimed_source"]); print(d["verification_note"])'
```

Expected output:

```text
FICTIONAL LOCAL PRACTICE DATA; NOT EXIF AND NOT A REAL PERSON
Claimed creator: Mina Example
Claimed source: https://example.invalid/gallery/demo-17
These are invented claims in JSON. They are not embedded image metadata. Verify claims independently before treating them as true.
```

`Mina Example`, `DemoCam 1`, date aur `example.invalid` source sab banawati hain. Koi real shakhs ya website investigate nahin karni. JSON humein sirf yeh batati hai ke fixture ke author ne kya claim likha; yeh claim ki sachchai prove nahin karti.

## Step 2: marker ko local PNG mein dhoondo

Generator ek valid 1x1 transparent PNG banata hai aur us ke PNG data ke baad ek readable ASCII demo marker append karta hai. Is liye marker file ke aakhir mein hai, image ke pixels mein nazar aane wala text nahin. Neeche command bytes ko local file se parhti aur expected marker print karti hai:

```bash
python3 -c 'from pathlib import Path; p=Path("labs/work/osint-metadata/demo-image.png"); data=p.read_bytes(); marker=b"CTFURDU{local_metadata_is_not_proof}"; print(marker.decode("ascii") if data.endswith(b"\n"+marker+b"\n") else "marker not found")'
```

Expected output:

```text
CTFURDU{local_metadata_is_not_proof}
```

Yeh **sirf is guide ke liye banaya gaya demo flag** hai. Yeh TryHackMe ka flag ya jawab nahin. Marker ko appended file bytes mein paana, usay EXIF nahin bana deta aur na hi PNG ko banane wale ke baare mein koi claim sabit karta hai.

## Step 3: metadata aur verification ko alag rakho

Agar ExifTool pehle se installed hai to is optional read-only command se local PNG inspect kar sakte ho:

```bash
exiftool -a -u -g1 labs/work/osint-metadata/demo-image.png
```

ExifTool apni official [command-line documentation](https://exiftool.org/exiftool_pod.html) mein file metadata ko readable output mein dikhane ke liye `exiftool [OPTIONS] FILE` syntax deta hai. Output tool version ke mutabiq farq ho sakta hai. Is fixture mein synthetic JSON ko PNG ke EXIF fields na samjho; appended marker bhi standard EXIF/PNG metadata nahin. ExifTool na ho to isay install karna zaroori nahin—upar ke standard-library commands mukammal exercise hain.

Asal OSINT ya photo review mein ek ehtiyati workflow yeh hai:

1. **File aur claim ko identify karo.** Dekho ke tumhare paas original file hai, transformed/recompressed copy hai, ya sirf kisi aur ka description. Yahan humare paas apni banayi hui fixture aur alag JSON hai.
2. **Metadata ko lead samjho.** Camera model, timestamp, author ya location field ho bhi to uski maujoodgi sachchai, identity, ya capture location ki guarantee nahin. Fields edit, strip, copy, ya galat context mein present ho sakte hain.
3. **Claim ko independent context se parakho.** Agar authorized, public material mein source ka claim ho to usi original publisher ki page/context, publish date aur image caption ko check karo; phir alag, reliable public evidence se consistency dekho. Ek copied profile ya repeated repost ko independent confirmation na gino.
4. **Uncertainty likho.** “File mein yeh field mila” aur “yeh baat verified hai” alag statements hain. Agar independent corroboration na mile to natija unverified hi rakho.

Yeh verification workflow general analytical guidance hai; synthetic fixture kisi real source ko verify nahin karti. Official TryHackMe page sirf room ka broad image-based OSINT theme context deta hai—yeh recreation us platform ke prompts, data ya answers use nahin karti.

## Common errors

- **`python3: command not found`:** Apne system ka Python 3 install/enable karo; Termux par Python package manager ke zariye install kiya ja sakta hai. `python --version` se Python 3.10+ confirm karna, magar commands mein `python3` use karna.
- **`can't open file 'labs/osint-metadata.py'`:** Tum repository root mein nahin ho. `cd` karke `pwd` se folder verify karo.
- **JSON file nahin milti:** Pehle `python3 labs/osint-metadata.py` chalao. Generator files ko root ke relative `labs/work/osint-metadata/` mein banata hai.
- **`exiftool: command not found`:** Yeh optional hai. Is lab ke liye install ya network access ki zaroorat nahin.
- **Marker nahin milta:** Fixture ko dobara generate karo, phir wahi exact command chalao. PNG ko image editor ya exporter se save karne par trailing bytes hat sakte hain; original generated file istemal karo.
- **JSON ko “EXIF” samajhna:** JSON is practice mein sirf alag synthetic notes hain. Generator usay image file mein embed nahin karta.

## Defensive lesson aur safe scope

Metadata privacy-sensitive ho sakta hai. Apni photos public karne se pehle socho ke location, timestamps, device details ya doosri embedded fields zaroori hain ya nahin; zarurat par trusted local tool se inspect/remove karo, phir exported copy dobara check karo. Kisi aur ke baare mein metadata ya public posts ko correlate karke unki pehchan, ghar, workplace, account, ya movement trace na karo. Is practice mein sirf apne banaye local fixtures par kaam karo; real logon ko target na karo, login-gated material na kholo, aur kisi live challenge ya competition ke answers dhoondhne/share karne ki koshish na karo.

## Source aur provenance note

- [TryHackMe: OhSINT public room page](https://tryhackme.com/room/ohsint) — broad room introduction. Is guide ne platform ke task answers use ya reproduce nahin kiye.
- [ExifTool: Application documentation](https://exiftool.org/exiftool_pod.html) — official usage syntax aur metadata-reading behavior.
- [Python: `base64` standard-library documentation](https://docs.python.org/3/library/base64.html) — Base64 se binary bytes decode karne ka reference; generator mein PNG fixture text ko bytes mein decode karne ke liye istemal hota hai.
- [Python: `pathlib` standard-library documentation](https://docs.python.org/3/library/pathlib.html) — `Path.mkdir(parents=True, exist_ok=True)` aur `Path.write_bytes()` / `Path.write_text()` ke references; generator ke confined local outputs ke liye.

TryHackMe aur ExifTool links external official references hain. Fictional claims, appended marker aur unka interpretation is repository ke liye original offline recreation hain.
