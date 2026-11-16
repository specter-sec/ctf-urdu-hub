# Tools handbook: kaam samjho, scope chhota rakho

Yeh handbook beginner CTF practice ke liye hai. Neeche ke tamam network examples **sirf apne `localhost` (`127.0.0.1`) lab** ke liye hain. Internet par public hosts, broad ranges, school/work networks ya kisi aur ke systems par in commands ko na chalao. Localhost ko target banana bhi tabhi jab local service aap ne khud start ki ho ya lab ne wazeh ijazat di ho.

## Basic Linux terminal

Linux commands se files dhoondo, content samjho aur evidence ko organize karo. Pehle current directory aur files check karo:

```bash
pwd
ls -la
find labs -maxdepth 2 -type f -print
grep -n "pattern" labs/README.md
file labs/sample.bin
strings labs/sample.bin | head
```

In examples mein `labs/README.md` ya `labs/sample.bin` ko maujood file se badlo; yeh repository fixtures hone ka dawa nahin. `grep` text mein match dhoondta hai, `find` paths dhoondta hai, `file` aam tor par file type pehchanne mein madad karta hai, aur `strings` binary mein printable text dikhata hai. `strings` output ko proof na samjho—context ke saath verify karo.

Useful package names yeh hain:

| Kaam | Kali/Debian package | Termux package |
| --- | --- | --- |
| Python | `python3` | `python` |
| HTTP/Git utilities | `curl`, `git` | `curl`, `git` |
| Network mapping | `nmap` | `nmap` |
| Text search | `grep` | `grep` |
| File search | `findutils` | `findutils` |
| File type identification | `file` | `file` |
| Binary utilities, jaise `strings` | `binutils` | `binutils` |

Termux package availability/version device aur repo state se farq kar sakti hai; package missing ho to official Termux package guidance dekho. **`pkg wireshark` ya `pkg burp` chalane ki koshish na karo**—is guide ka supported Termux setup un tools ke liye nahin.

## Nmap: localhost par ek port

Nmap network service discovery tool hai. Is handbook mein iska ek hi narrow example hai: aapke apne device ka localhost port. Pehle ek terminal mein Python server ko loopback par start karo:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Doosre terminal se **sirf apne local device** par TCP connect scan karo:

```bash
nmap -sT -p 8000 127.0.0.1
```

Termux mein `python` use karna ho sakta hai. `-sT` TCP connect scan hai aur unprivileged user ke liye munasib hai; Nmap docs ke mutabiq raw-packet scan types ko Unix par aam tor par elevated privilege chahiye. Result local test port ke hawale se samjho; is example ko kisi doosre address/range par na badlo. Server ko rokne ke liye server terminal mein `Ctrl+C` dabao. [Nmap port-scanning documentation](https://nmap.org/book/man-port-scanning-techniques.html).

## Gobuster: apni toy web app aur apni wordlist

Gobuster web content discovery mein madad karta hai; real systems par is tarah ke requests intrusive ho sakte hain. **Koi built-in lab app ya `labs/wordlists/lab-only.txt` fixture yahan guarantee nahin hai.** Pehle apne computer par chhoti toy web app/route set banao, test data ke siwa kuch na rakho, aur sirf localhost bound server use karo. Phir khud banayi hui chhoti wordlist ke saath isi local target ko test karne ka pattern:

```bash
gobuster dir -u http://127.0.0.1:8000 -w labs/wordlists/lab-only.txt
```

Yeh tabhi chalao jab dono cheezen waqai aap ne banayi hon: localhost par chalti toy web app aur `labs/wordlists/lab-only.txt` file. Python ka basic static server directory listing dikha sakta hai, lekin Gobuster ke liye meaningful route fixture nahin banata. Agar app/wordlist nahin, command na chalao—pehle lab fixture tayyar karo. Gobuster ka official project [GitHub repository](https://github.com/OJ/gobuster) hai.

## Burp Suite: browser aur local proxy

Burp Suite Community desktop par web request/response samajhne ka proxy-based toolkit hai. Browser ko Burp ke local proxy listener se connect karne se browser requests proxy ke zariye ja sakti hain; aap request dekh kar local lab mein inspect/forward karte ho. Sirf aapki apni `127.0.0.1` toy app ko target banao aur browser proxy tabhi enable rakho jab lab kar rahe ho.

Burp Java-based desktop application hai; yeh guide Android Termux par installation/support nahin deta. Download aur setup ke liye [PortSwigger ka official Community Edition page](https://portswigger.net/burp/communitydownload) aur unki [Web Security Academy](https://portswigger.net/web-security) dekho. HTTPS lab samajhne ke liye Burp ka CA certificate browser trust store mein add karna *optional* hai. Agar zaroorat ho, sirf alag lab browser/profile mein scope karke karo, instructions khud parho, phir certificate/proxy setting hatao. CA certificate ko system-wide trust store mein install na karo. Real site traffic intercept na karo.

## CyberChef: data transformations

CyberChef browser-based data transformation tool hai. Isay base64/hex conversion, URL decode, text inspection aur chhoti transformations samajhne ke liye use karo—har output ko source context se verify karo. Official [CyberChef project](https://github.com/gchq/CyberChef) aur browser app [gchq.github.io/CyberChef](https://gchq.github.io/CyberChef/) par milta hai. Browser mein tool load ho jane ke baad local sample text par kaam karo; private keys, credentials, personal records ya confidential files kisi online page mein paste na karo. Rot13 ko encryption na samjho: yeh reversible text transform hai, secrecy protection nahin.

## Wireshark: pehle se maujood sanitized PCAP

Wireshark desktop GUI mein packet capture files padhne aur network protocols samajhne ke kaam aata hai. Is beginner path mein **live capture nahin**: sirf aisi existing, local, sanitized `.pcap`/`.pcapng` file kholo jo aapki ho ya lab ne di ho aur jisme private data na ho. File khol kar packet list dekho, ek packet select karo, aur protocol layers ko expand karke fields padho. `http` ya `dns` jaise display filters ko sirf sample file ke context mein try karo; packet capture ko internet par upload/share na karo.

Is guide mein Wireshark ke liye interface capture, privileged mode ya capture permissions set karne ka dawa nahin kiya gaya. Wireshark optional desktop tool hai; Termux install instruction nahin. Official [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/) aur [Wireshark learning page](https://www.wireshark.org/learn) dekho.

## Evidence aur safety checklist

- Command chalane se pehle target ko literal `127.0.0.1` ya explicitly authorized lab se match karo.
- Koi broad CIDR, public IP, host discovery sweep ya third-party URL is handbook ka hissa nahin.
- `labs/work/` mein notes/output rakho; source evidence ki copy ko alag rakho.
- Unexpected host, real credential, personal information, ya production data nazar aaye to ruk jao; capture ko share na karo.
- Nateeja write-up mein explain karo, lekin kisi platform ka flag/answer expose na karo.
