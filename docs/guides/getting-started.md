# Getting started: CTF Urdu Hub

Yeh guide aap ko safe, chhote aur repeatable practice setup se shuru karwati hai. CTF ka maqsad concepts seekhna aur authorized challenge solve karna hai—kisi real website, Wi-Fi, server ya doosre shakhs ke device ko test karna nahin. Har tool ko sirf apne local lab ya aise target par chalao jiske liye wazeh ijazat ho.

## Pehle setup chunno

### Kali Linux: desktop/laptop ke liye

Kali Linux ek Linux distribution hai jisme security tools aur training ke liye packages milte hain. Agar aap naye ho, Kali ko VirtualBox/VMware jaisi virtual machine mein chalana asaan aur host system se alag rakhna hota hai. Official installation aur image guidance ke liye [Kali Linux documentation](https://www.kali.org/docs/installation/) aur [Kali introduction](https://www.kali.org/docs/introduction/) dekho. Random ISO ya unofficial download mirror se install na karo.

Terminal khol kar pehle package index update karo; phir zaroorat ke mutabiq tools install karo:

```bash
sudo apt update
sudo apt install python3 curl git nmap grep findutils file binutils
```

`sudo apt upgrade` tabhi chalao jab system update ka waqt aur stable network ho. Install ke baad version check kar sakte ho:

```bash
python3 --version
nmap --version
```

### Android: Termux, bina root

Termux Android par terminal aur Linux-style package environment deta hai; basic shell aur bohat se packages bina root ke chalte hain. Iska matlab yeh **nahin** ke phone Kali ban jata hai ya Kali ke har tool/feature ko support karta hai. Android ki limits, CPU/battery management, app permissions aur package availability desktop se mukhtalif hain.

Termux sirf official [F-Droid listing](https://f-droid.org/packages/com.termux/) ya [Termux GitHub releases](https://github.com/termux/termux-app/releases) se lo. Project ke [official installation notes](https://github.com/termux/termux-app#installation) par source aur update rules parho. F-Droid aur GitHub builds ki signing alag ho sakti hai: in sources ko mix karke update na karo; source badalne se pehle official instructions dekho. Random APK sites, forwarded APKs aur unofficial social-media links se bacho.

Termux ke andar package list refresh aur zaroori beginner tools install karo:

```bash
pkg update
pkg upgrade
pkg install python curl git nmap grep findutils file binutils
```

Phone par files apne Termux home directory mein rakho; Android shared storage ko dene wali optional permission samajh kar hi enable karo. Android root karna is guide ke workflow ke liye zaroori nahin. Root ki zaroorat batane wali random command ko copy-paste na karo.

**Platform farq:** Nmap ka `-sT` TCP connect scan unprivileged use ke liye munasib option hai. Raw-packet features ke liye extra privilege ho sakti hai. `gobuster` aur Wireshark desktop par optional hain; unhein Termux mein install karne ki yahan hidayat nahin. Burp Suite Java-based desktop tool hai; Android par is guide ka supported setup nahin. CyberChef browser mein chal sakta hai.

## Project aur Python ka pehla qadam

Repository clone karne ke liye sirf authorized public project URL use karo. Neeche `URL` ko project ka official clone URL milne par replace karna hai:

```bash
git clone URL ctf-urdu-hub
cd ctf-urdu-hub
```

Agar aap ke paas project pehle se hai, us directory mein jao. Python ka version dekh kar files aur folders samjho:

```bash
python3 --version
pwd
ls
```

Termux mein Python command `python` hoti hai; Kali par zaroorat par `python3` use karo. Is project ke beginner lab paths hain: `labs/web-source.py`, `labs/crypto-rot13.py`, `labs/forensics-strings.py`, `labs/linux-find.py`, aur `labs/osint-metadata.py`. Har checkout mein tamam labs available hon yeh zaroori nahin—file maujood ho aur uski instructions parh kar hi chalao. Generic workflow:

```bash
python labs/<name>.py
# Misal: jab yeh file checkout mein maujood ho
python labs/web-source.py
# Kali par, agar `python` command na ho:
python3 labs/web-source.py
```

Apne device par `labs/work/` ko output aur scratch work ke liye use karo. Pehle directory banao:

```bash
mkdir -p labs/work
```

Agar kisi lab ki instructions output file ka naam dein, usi lab ke mutabiq output `labs/work/` mein save karo. Files ko overwrite karne se pehle check karo; apni original evidence/input ko alag rakho. Git mein sirf woh changes commit karo jo aap ne khud banaye hain.

## Safe, local-only practice loop

1. **Scope likho:** target sirf aapki apni local VM, localhost service ya purpose-built challenge ho. Challenge ka scope unclear ho to test rok kar poochho.
2. **Input samjho:** prompt, files, request aur expected output ko pehle read karo. Original sample ki copy `labs/work/` mein rakho.
3. **Ek chhota experiment:** ek waqt mein ek command ya ek hypothesis test karo. Public network, school/work network, random IP range aur third-party service ko scan/probe na karo.
4. **Evidence note karo:** date/time, exact local command, input, output, kya samjha aur agla sawal likho. Passwords, tokens aur personal data notes mein na rakho.
5. **Clean up:** temporary files hataane se pehle dobara check karo; lab service ko `Ctrl+C` se band karo.

Agar apne computer par local HTTP page chahiye, pehle target files ke baghair sirf localhost server kaise bind hota hai yeh samjho. Yeh server current directory ki files serve karega, is liye us directory mein private files na rakho:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Server chalte waqt browser mein `http://127.0.0.1:8000/` khol sakte ho. Doosre terminal se bhi sirf `127.0.0.1` ko address karo. Server ko rokne ke liye pehle terminal mein `Ctrl+C` dabao. Yeh command public interface par server publish nahin karti kyun ke binding loopback address par hai.

## Beginner routine

- Terminal mein `pwd`, `ls`, `cd`, `cat`, `grep` aur `find` ki practice karo.
- Python script chalane se pehle usay text editor mein parho; unknown script ko seedha execute na karo.
- Har practice ke baad ek chhota note likho: maqsad, evidence, nateeja aur ek naya sawal.
- Galat output ko bhi learning evidence samjho. Challenge ke flags/answers publish karne ke bajaye apna reasoning aur method likho.
- Safety aur permission boundaries ke liye [ethics guide](../ethics.md) dekho, aur lab write-up ka format chahiye to [template](../template.md) use karo.

## Agla qadam

Apni pehli lab tab shuru karo jab uski file aur instructions maujood hon. Phir [tools handbook](tools.md) se ek tool chuno; aage ka skill path [roadmap](roadmap.md) mein hai.
