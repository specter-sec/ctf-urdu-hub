---
title: "ROT13 Ka Raaz: Mod 26 Beginner Crypto"
description: "Roman Urdu/Hinglish beginner walkthrough of ROT13, modulo 26, and a safe fictional offline practice fixture."
tags:
  - crypto
  - rot13
  - beginner
category: Crypto
difficulty: Beginner
platform: picoCTF
---

# ROT13 Ka Raaz: Mod 26 Beginner Crypto

Is writeup mein hum `ROT13` ko samjhenge aur aik chhoti, local practice file decode karenge. Yahan platform ka naam sirf topic context hai: **yeh platform ka exact solution nahin, original offline practice recreation hai.** Is mein official picoCTF challenge ka prompt, data, flag, ya answer shamil nahin. Practice plaintext aur output neeche diye gaye generator ne is repository ke liye banaye hain.

> Brand: **CTF Urdu Hub by IFTIKHAR**

## Maqsad

Aakhir tak aap samajh sakenge ke ROT13 mein har English letter ko 13 positions aagay shift karne ka kya matlab hai, alphabet ke end par `mod 26` kaise wrap-around karta hai, aur local text file ko Python standard library se kaise decode karte hain.

## Zaroori pehle se maloomat

- Terminal mein repository root tak aana aur commands chalana.
- Basic Python command-line usage.
- English alphabet ke letters aur text files ka basic idea.
- Python 3.10 ya naya; extra package ki zaroorat nahin.

## Source-backed technique aur practice ki had

picoCTF Primer Caesar cipher ko letters ki substitution ke taur par samjhata hai, alphabet ke end par wrap-around dikhata hai, aur `% 26` ko 26-letter alphabet mein position wapas ghumane ke liye use karta hai ([picoCTF Primer: Substitution ciphers](https://primer.picoctf.org/)). ROT13 usi Caesar shift ka khaas case hai jahan shift 13 hota hai. Python ki official `codecs` documentation `rot_13`/`rot13` ko text-to-text transform aur Caesar-cipher transformation ke taur par list karti hai ([Python `codecs` documentation](https://docs.python.org/3/library/codecs.html#text-transforms)).

Is writeup ka fixture aur us ka demo flag hamara fictional local exercise hai. Yeh picoCTF ka asli challenge input ya flag nahin, aur na hi kisi live competition ka content hai. Aapko kisi platform par submit karne ke liye flag nahin diya ja raha.

## Setup: repository root se

Pehle repository ke root directory mein hon. Agar aap pehle se root par hain, agla command seedha chalayein:

```bash
cd /workspace/ctf-urdu-hub
```

Generator Python standard library use karta hai. Yeh deterministic hai, network access nahin karta, shell commands execute nahin karta, aur apni ek ASCII text fixture sirf `labs/work/crypto-rot13/` ke andar banata hai.

```bash
python3 labs/crypto-rot13.py
```

Expected output:

```text
Created local practice fixture: labs/work/crypto-rot13/ciphertext.txt
Ciphertext: PGSHEQH{zbqhyb_jencf_yrggref}
```

Yeh ciphertext file dekhne ke liye:

```bash
cat labs/work/crypto-rot13/ciphertext.txt
```

Expected output:

```text
PGSHEQH{zbqhyb_jencf_yrggref}
```

## Decode karein

Ab Python `codecs` ke built-in `rot_13` transform se file parhiye. Yeh poora command repository root se chalayein:

```bash
python3 -c 'from pathlib import Path; import codecs; p = Path("labs/work/crypto-rot13/ciphertext.txt"); print(codecs.decode(p.read_text(encoding="ascii").strip(), "rot_13"))'
```

Expected output:

```text
CTFURDU{modulo_wraps_letters}
```

Yeh sirf hamare synthetic, fictional demo ka output hai. Yeh kisi official picoCTF ya TryHackMe flag ki representation nahin.

## Is kaam ko samjhein

Alphabet ki positions ko zero se count karein: `a` position 0 aur `z` position 25 par hai. Letter ko number mein badal kar 13 jama karne ke baad `% 26` remainder deta hai. Is se agar position alphabet ke aakhir se aagay nikle to woh shuru se continue hoti hai. Misal ke taur par, `z` ko 13 aagay le jane par position `(25 + 13) % 26 = 12`, yani `m`, milti hai.

Is practice file mein uppercase aur lowercase letters apni case ke saath rotate hote hain. Curly braces, underscore aur doosre non-letter characters waise hi rehte hain. ROT13 13-step shift hone ki wajah se khud apna inverse bhi hai: wahi transform dobara lagao to asal letters wapas milte hain. Generator isi tarah fictional plaintext ko transform karke fixture banata hai; decode command file ke text par wohi transform lagata hai.

`codecs.decode(..., "rot_13")` yahan string-to-string kaam karta hai. Python docs ke mutabiq `rot_13` ek text transform hai, aam byte encoding nahin; isi liye hum `str.encode("rot_13")` ke bajaye `codecs.decode` istemal karte hain.

## Common errors

- **`No such file or directory`**: check karein ke aap repository root par hain aur pehle `python3 labs/crypto-rot13.py` chala chuke hain.
- **`python3: command not found`**: Python 3 install/available hona chahiye. Kali, Termux ya Linux par apne OS ke approved package manager se Python 3 hasil karein; is lab ko kisi extra Python package ki zaroorat nahin.
- **`LookupError: unknown encoding: rot_13`**: apne interpreter ka version dekhein (`python3 --version`) aur Python 3.10+ use karein.
- **Output mein extra newline ya spaces**: supplied command `.strip()` karta hai. Agar aap apna input badlein to non-letter whitespace bhi output mein reh sakta hai.
- **Decode ke baad samajh mein aane wala matn nahin milta**: input ko exact fixture se compare karein. ROT13 sirf tab munasib hai jab hint/format is qisam ke Caesar shift ki taraf ishara kare; har unreadable string ROT13 nahin hoti.

## Defensive lesson aur safe scope

ROT13 encryption ya secrecy provide nahin karta. Har shakhs publicly known transform ko foran reverse kar sakta hai, is liye passwords, tokens, personal data, ya confidential information ko ROT13 mein rakhna unsafe hai. Isay sirf harmless obfuscation ya learning puzzle samjhein, cryptographic protection nahin.

Is exercise ko sirf apni local copy ke generated fixture par chalayein. Koi external host, account, real person, live CTF, ya real-world secret target nahin hai. Generator ko dobara chalana safe hai; woh fixture ko deterministic content se overwrite karega aur repository mein kahin aur output nahin banayega.

## Optional: generator code khud dekhein

```bash
cat labs/crypto-rot13.py
```

Us mein `pathlib.Path` output folder banata hai aur fixture file likhta hai. Har letter ko alphabet ke andar rotate karne ke liye modulo 26 lagta hai; non-letters ko jaisa hai waisa rehne diya gaya hai. Koi downloaded asset ya third-party library istemal nahin hoti.
