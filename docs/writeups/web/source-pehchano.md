---
title: "Source Pehchano: HTML Source Inspection"
description: "Beginner-friendly Roman Urdu/Hinglish guide to finding an intentionally exposed demo clue in HTML source using an original offline lab."
tags:
  - picoCTF
  - web-exploitation
  - html
  - source-inspection
category: Web
difficulty: Beginner
platform: picoCTF
---

# Source Pehchano: HTML Source Inspection

**CTF Urdu Hub by IFTIKHAR**

Yeh beginner walkthrough aik simple web-security habit samjhata hai: browser ko page dikhane se pehle server se HTML milta hai, aur jo HTML browser ko bheja jata hai woh visitor dekh sakta hai. Is liye HTML comments, hidden form fields, ya JavaScript mein secret rakhna secret ko protect nahin karta. picoCTF ka official [CTF Primer](https://primer.picoctf.org/) bhi batata hai ke browser mein "View Page Source" se HTML/JavaScript dekha ja sakta hai, aur page code mein secrets rakhna vulnerability hai. Is writeup mein picoCTF ko sirf **skill-area/platform context** ke taur par mention kiya gaya hai.

> **Zaroori wazahat:** Yeh platform ka exact solution nahin, original offline practice recreation hai. Is mein fictional page aur apna demo flag hai. Koi actual picoCTF ya TryHackMe flag, copied room question/answer, ya live competition content shamil nahin.

## Maqsad

Fictional local page mein HTML comment ke andar diya gaya demo flag dhoondhna hai. Yahan koi exploit ya remote target nahin: sirf apne computer par banaye gaye HTML file ka source inspect karna hai.

## Prerequisites

- Basic terminal use aur repository ka root folder kholna.
- Python 3.10 ya us se naya; is exercise mein sirf Python standard library use hoti hai.
- Browser optional hai. Terminal se HTML inspect karne ke liye browser zaroori nahin.

## Setup (repository root se)

Repo root woh directory hai jahan `labs/` folder maujood ho. Neeche ke tamam commands isi root se chalayein.

```bash
python3 --version
python3 labs/web-source.py
```

Generator yeh local file banayega: `labs/work/web-source/index.html`. Iska content fixed aur repeatable hai. Generator `pathlib` use karta hai, sirf us output folder mein file banata hai, aur network ya shell command nahin chalata.

Expected non-sensitive setup output ka format:

```text
Created /.../ctf-urdu-hub/labs/work/web-source/index.html
```

`/...` aapke apne absolute workspace path ki jagah hai.

## Walkthrough A: terminal se HTML source parhna

Pehle source ko line numbers ke saath dekhein:

```bash
nl -ba labs/work/web-source/index.html
```

Output mein page ka title aur visible text ke baad aik HTML comment hoga. Sirf demo clue wali line filter karne ke liye:

```bash
grep -n 'CTFURDU{' labs/work/web-source/index.html
```

Expected output:

```text
18:  <!-- Demo clue for this offline exercise: CTFURDU{source_is_public} -->
```

Line number file ke bilkul iss fixture version ke liye hai. Agar file edit ki ho to number badal sakta hai; clue text phir bhi search ho jayega.

Yahi is local exercise ka jawab hai:

```text
CTFURDU{source_is_public}
```

Flag ka format yahaan is fictional lab ka apna `CTFURDU{...}` format hai; yeh kisi platform ka flag nahin.

### Optional: Python se clue extract karna

Yeh bhi repo root se chalayein:

```bash
python3 - <<'PY'
from pathlib import Path
import re

html = Path("labs/work/web-source/index.html").read_text(encoding="utf-8")
match = re.search(r"CTFURDU\{[^}]+\}", html)
if match is None:
    raise SystemExit("Demo clue nahin mila: source aur path check karein")
print(match.group(0))
PY
```

Expected output:

```text
CTFURDU{source_is_public}
```

### Optional: apne browser mein kholna

Ek terminal mein repo root se local-only server start karein:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory labs/work/web-source
```

Apne browser mein `http://127.0.0.1:8000/` kholein. Page par fictional garden-club text dikhna chahiye. Ab browser ka **View Page Source** kholein (aksar `Ctrl+U`; menu ka naam browser ke mutabiq badal sakta hai). `CTFURDU{` search karein aur comment dekhein. Kaam khatam hone par server wale terminal mein `Ctrl+C` dabayein.

Server ko `127.0.0.1` par bind karna is liye hai ke yeh practice sirf isi computer par accessible rahe. Kisi doosre host ya public website ko target na karein.

## Samajhne wali baat

HTML tags browser ko structure batate hain; comment `<!-- ... -->` aam tor par page par render nahin hota, lekin original HTML source mein rehta hai. Exercise mein clue comment mein hai, is liye rendered page par nazar nahin aata magar source read karte hi mil jata hai. Official picoCTF [CTF Primer](https://primer.picoctf.org/) is bunyadi idea ko samjhata hai: page ka HTML/JavaScript browser mein dekha ja sakta hai aur secrets ko client-side code mein rakhna unsafe hai.

**Original source aur live DOM ka farq:** `View Page Source` aam tor par browser ko mila original HTML document dikhata hai. DevTools ka **Elements/Inspector** tab current, parsed DOM dikhata hai; JavaScript ne agar page badla ho to woh original response se mukhtalif ho sakta hai. Mozilla MDN ke [browser developer tools guide](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools) ke mutabiq Inspector runtime par loaded HTML/CSS dikhata aur temporarily edit bhi kar sakta hai. Is chhoti static practice mein dono views qareeban same honge, lekin real web pages mein zaroori nahin.

Yeh technique sirf authorized CTF exercise ya apne/local test page par istemal karein. Is walkthrough ka fixture **meri original fictional local recreation** hai: `labs/web-source.py` ise generate karta hai. Kisi asli picoCTF task ki prompt, page ya answer yahan reproduce nahin ki gayi.

## Aam ghaltiyan aur unka hal

- **Command `No such file or directory` kehti hai:** Pehle repository root par aayein; `pwd` aur `ls labs` se check karein. Phir `python3 labs/web-source.py` dobara chalayein.
- **`python` nahin milta:** `python3` use karein. Python 3.10+ installed hona chahiye; generator ke liye external packages nahin chahiye.
- **`grep` nahin milta:** Optional Python extraction command chala lein, ya `nl -ba ...` se file khol kar `CTFURDU{` manually dhoondein.
- **Browser mein page nahin khulta:** Dekhein server terminal abhi chal raha hai; exact URL `http://127.0.0.1:8000/` hai. `Ctrl+C` ke baad server band hota hai. Port busy ho to `8001` use karein aur URL bhi `:8001` karein.
- **Elements tab mein comment ya original markup alag lagta hai:** Elements runtime DOM hai; challenge ka sawal source ke bare mein ho to `View Page Source` ya local HTML file ko text editor/terminal se dekhein.
- **Flag line dhoondh nahin rahi:** Generator dobara chala kar fixture recreate karein, phir exact file path check karein. Python extraction mein file missing ho to pehle setup step chahiye.

## Defensive lesson

Browser ko bheja gaya HTML aur JavaScript public samjhein. Passwords, API keys, private tokens, ya aisi koi cheez jo user ko nahin milni chahiye client-side source/comment mein na rakhein. Sensitive access ko server-side rakhein, authorization server par enforce karein, aur secret exposure ho chuka ho to credential rotate/revoke karein. Comment mein chhupana ya CSS se text hide karna access control nahin hai.

## Safe scope

Is walkthrough mein commands sirf locally generated `labs/work/web-source/index.html` ko read karti hain. Optional HTTP server loopback (`127.0.0.1`) par rehta hai. Koi external URL fetch, scanning, login, uploaded artifact, tracking, ya real user data nahin. Is lab se bahar sirf aise systems inspect karein jinki testing ki aapko wazeh permission ho.
