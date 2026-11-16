---
title: "Linux Fundamentals Part 1: Local File Dhoondhna aur Parhna"
description: "Beginner walkthrough: safe offline practice tree mein find se file dhoondho aur cat se parho."
tags:
  - linux
  - beginner
  - shell
  - tryhackme
category: "Beginner Linux"
difficulty: "Beginner"
platform: "TryHackMe"
---

# Linux Fundamentals Part 1: Local File Dhoondhna aur Parhna

**CTF Urdu Hub by IFTIKHAR**

## Zaroori wazahat

Yeh TryHackMe ka exact solution nahin hai. Yeh CTF Urdu Hub ki taraf se banayi hui **original offline practice recreation** hai: is mein apne computer par banne wali fictional files aur demo marker hain. Is writeup mein TryHackMe room ke sawal, jawab, flags, ya live room machine ka data shamil nahin. TryHackMe apne Linux Fundamentals Part 1 ko Linux ke essential commands seekhne ka interactive room batata hai; yahan sirf us beginner context se milti-julti bunyadi shell technique par practice hai ([official room page](https://tryhackme.com/room/linuxfundamentalspart1)).

## Maqsad

Hum repository ke andar ek chhota sa local practice folder banayenge. Phir `pwd`, `ls`, `find`, aur `cat` se:

1. confirm karenge ke terminal kis directory mein hai;
2. practice files ka overview lenge;
3. naam maloom hone ke bawajood andar rakhi hui `clue.txt` dhoondhenge;
4. milne wale path ko `cat` se parhenge.

`find` ki `-name` test file ke basename ko pattern se match karti hai. Pattern ko quotes mein rakhna shell ki wildcard expansion se bachata hai. GNU find manual isi `-name` behavior aur quoted pattern ki wajah batata hai ([GNU find manual](https://man7.org/linux/man-pages/man1/find.1.html)). `cat` file ka content standard output par likhta hai, aur `ls` directory contents list karta hai ([GNU Coreutils manual: cat and ls](https://www.gnu.org/software/coreutils/manual/coreutils.html)).

## Prerequisites

- Linux, Kali, Termux, ya doosra Unix-jaisa terminal.
- Python 3.10 ya naya; generator mein sirf Python standard library istemal hoti hai.
- `specter-sec/ctf-urdu-hub` repository ka local clone, aur commands chalane ke liye us repository ki root directory.
- `find`, `cat`, `ls`, aur `pwd` commands. Is tutorial ke liye root/sudo access, internet, actual challenge account, ya paid content ki zaroorat nahin.

Python ka `pathlib.Path.mkdir(parents=True, exist_ok=True)` missing parent directories bana sakta hai; generator isi standard-library approach ko use karta hai ([official Python pathlib docs](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir)).

## Setup: repository root se

Pehle repository root mein aayen. Agar aap ne repo kisi aur jagah clone kiya hai to us location par `cd` karein. Neeche ke tamam commands root se chalne ke liye likhe gaye hain.

```bash
cd /path/to/ctf-urdu-hub
pwd
```

`pwd` current working directory print karega. Aap ke computer par is ka absolute path alag hoga. Ab fixture generator chalayein:

```bash
python3 labs/linux-find.py
```

Expected output:

```text
Created offline practice files in labs/work/linux-find
```

Generator deterministic hai: har run par wahi chhote text files aur wahi fictional marker likhta hai. Yeh network use nahin karta, shell commands execute nahin karta, aur apna output sirf `labs/work/linux-find/` ke andar banata hai. Dobara chalane par sirf isi fixed output folder ko recreate karta hai. Python mein `Path.mkdir` ke parent-folder behavior ki tafseel official docs mein hai ([Python pathlib](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir)).

## Walkthrough

### 1. Folder ke andar kya hai, dekho

```bash
ls -1 labs/work/linux-find
```

Expected output:

```text
README.txt
field-notes
```

Abhi top-level listing mein `clue.txt` seedha nazar nahin aati. Humein poora local practice folder recursively dekhna hai. `ls` directory contents dikhata hai; by default yeh listing recursive nahin hoti ([GNU Coreutils manual: ls](https://www.gnu.org/software/coreutils/manual/coreutils.html#ls-invocation)).

### 2. Naam se file dhoondho

```bash
find labs/work/linux-find -type f -name 'clue.txt'
```

Expected output:

```text
labs/work/linux-find/field-notes/archive/clue.txt
```

Is command ko hisson mein samjhein:

- `find` search shuru karta hai.
- `labs/work/linux-find` search ka starting point hai; hum sirf apne generated practice folder tak mehdood hain.
- `-type f` ka matlab sirf regular files match karna hai, directories nahin.
- `-name 'clue.txt'` basename ko exact pattern se match karta hai.

`find` result ka path relative hai kyun ke starting path relative di gayi thi. `-name` ke pattern mein slash nahin diya jata; yeh file ke naam ka hissa match karta hai, poora path nahin ([GNU find manual: `-name`](https://man7.org/linux/man-pages/man1/find.1.html)). Quotes yahan simple filename ke liye lazmi nahin, lekin pattern mein `*` ya `?` aa sakta ho to quotes shell ko wildcard pehle expand karne se rokte hain.

### 3. Mili hui file parho

Jo path `find` ne print kiya tha, usay `cat` ko dein:

```bash
cat labs/work/linux-find/field-notes/archive/clue.txt
```

Expected output:

```text
Demo marker: CTFURDU{find_then_read_local_file}
This marker is fictional and belongs only to this local exercise.
```

`CTFURDU{find_then_read_local_file}` sirf is fixture generator ka invented demo marker hai. Yeh **na TryHackMe flag hai, na picoCTF flag, na kisi platform ka answer**. `cat` file ka text terminal par print karta hai ([GNU Coreutils manual: cat](https://www.gnu.org/software/coreutils/manual/coreutils.html#cat-invocation)).

### 4. Apni understanding check karo

Ek aur file khol kar dekho:

```bash
cat labs/work/linux-find/README.txt
```

Expected output:

```text
Offline practice tree for CTF Urdu Hub.
Search below this folder for clue.txt.
```

Ab apne alfaaz mein jawab do: `ls` ke bajaye `find` kyun use kiya, aur `cat` ko poora path kyun diya? Jawab: top-level `ls` andar ke nested folders ko recursively nahin dikhata; `find` ne matching file ka nested path bataya, aur `cat` ko wohi path dene se sahi file parhi gayi.

## Common errors aur un ka hal

| Error ya masla | Mumkin wajah | Hal |
| --- | --- | --- |
| `python3: can't open file 'labs/linux-find.py'` | Aap repo root par nahin, ya file path ghalat hai. | `pwd` chala kar root confirm karein; phir `ls labs` dekhein. |
| `find: ... No such file or directory` | Generator abhi nahin chala, ya path spelling mein typo hai. | Root se `python3 labs/linux-find.py` chala kar phir `ls labs/work/linux-find` karein. |
| `find` koi result nahin deta | Naam exact match nahin, ya quotes/path misspelled hain. | `find labs/work/linux-find -type f` se saari generated files list karein; `clue.txt` ki spelling aur case check karein. |
| `cat: ... No such file or directory` | `cat` ko `find` se mila exact path nahin diya gaya. | Search dobara chalayein aur output ko bilkul waisa hi copy karein. |
| `Permission denied` | Folder permissions ya environment policy access rok rahi hai. | Sirf apni local repo copy aur is lab output ko check karein; sudo se random system paths explore na karein. |

Linux file names case-sensitive hote hain: `clue.txt` aur `Clue.txt` mukhtalif naam hain. Agar `find` ke baad koi line na aaye, to iska matlab matching file us search scope mein nahin mili; har jagah search karna zaroori ya safe nahin.

## Defensive lesson

Defensive kaam mein bhi yahi bunyadi flow kaam aata hai: pehle apni working directory confirm karo, search ko relevant aur authorized directory tak mehdood rakho, aur file parhne se pehle us ka path verify karo. `find` ko `/`, doosre users ke home folders, ya kisi unknown mounted drive par chalane ke bajaye apne test folder tak restrict karo. Unknown files ko run ya source mat karo; is exercise mein hum sirf plain text read kar rahe hain. `cat` file ko terminal mein dikhata hai, usay execute nahin karta.

## Safe scope aur cleanup

Yeh exercise local aur offline hai. Is mein koi live service, real person, real metadata, tracking, network request, external machine, ya kisi platform ki answer submission nahin. Generator apne fixed `labs/work/linux-find/` fixture folder ke siwa files nahin likhta. Agar generated files hataani hon to repository root se **sirf is lab ka folder** remove karein:

```bash
rm -r labs/work/linux-find
```

Command chalane se pehle path ko dobara check karein; doosri directories ya personal files ko delete na karein. Baad mein generator dobara chala kar lab ko recreate kiya ja sakta hai.

## Sources aur attribution

- TryHackMe, *Linux Fundamentals (Pt1)*: https://tryhackme.com/room/linuxfundamentalspart1 — platform aur room ka public introductory context. Is writeup mein room ke answers reproduce nahin kiye gaye.
- GNU find manual: https://man7.org/linux/man-pages/man1/find.1.html — `find`, `-type`, `-name`, aur shell wildcard quoting ki source-backed technique.
- GNU Coreutils manual: https://www.gnu.org/software/coreutils/manual/coreutils.html — `ls` aur `cat` ka behavior.
- Python documentation, `pathlib`: https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir — local fixture folders banane ke standard-library behavior ki documentation.
- Bash Reference Manual: https://www.gnu.org/software/bash/manual/bash.html — shell built-ins aur `cd`/working-directory context.

Commands ka local folder, file tree, text, demo marker, aur walkthrough examples CTF Urdu Hub ki original fictional offline practice recreation hain; woh kisi platform ki official challenge content nahin hain.
