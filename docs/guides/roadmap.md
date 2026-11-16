# Roadmap: do alag learning paths

Yeh roadmap skills aur practice evidence banane ka plan hai, job ya certification ki guarantee nahin. Har stage ko apni raftaar se karo; paid course lena zaroori nahin. Labs, CTFs aur systems par sirf unki published rules aur written authorization ke andar kaam karo. Kisi real organization ko test karne ki ijazat assume na karo.

**Evidence notebook:** har milestone ke liye date, objective, lab ka scope, apna process, sanitized screenshot/log ya notes, result ki limitation, aur agla sawal likho. Secrets, real personal data aur challenge flags/answers publish na karo. Har milestone ka output apne alfaaz mein samjha pao tabhi aage barho.

## Path A — SOC analyst foundation

SOC (Security Operations Center) path ka focus defensive monitoring, triage aur incident documentation hai. Beginner lab ke liye synthetic/sample data use karo; real logs mein personal data ho sakta hai.

1. **Terminal aur files:** directory navigation, `grep`, `find`, `file`, timestamps aur basic text handling seekho. Kali docs ka [introduction](https://www.kali.org/docs/introduction/) aur [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) ke authorized exercises se bunyaad banao. **Evidence:** 8–10 commands ka apna mini cheat-sheet aur practice notes.
2. **Python aur data hygiene:** Python mein text/CSV read karna, columns count karna aur safe output file banana practice karo; sample log ki original copy preserve karo. **Evidence:** sanitized sample par parsing ka chhota script/note, jisme missing ya ambiguous values ka zikr ho.
3. **Networking basics:** localhost par Python HTTP server chalao, HTTP request/response ke basic parts aur ports samjho. Nmap ke sirf localhost `-sT` example ko use karo. **Evidence:** ek simple service inventory note jisme address, port, observation aur test scope likha ho.
4. **Log triage:** synthetic web/auth logs mein timestamps normalize karo, repeated failures aur unusual sequence ko identify karo; ek indicator ko conclusion na banao. **Evidence:** 3 observations, alternative explanation aur confidence level ke saath.
5. **Packet basics:** supplied, sanitized PCAP ko Wireshark mein open karke protocol layers aur conversations ka overview padho. Live capture ya kisi aur ka traffic record karna is stage ka hissa nahin. **Evidence:** packet fields par short explanation; private payload ko reproduce na karo.
6. **Threat concepts:** [MITRE ATT&CK](https://attack.mitre.org/) ko behavior taxonomy ke taur par samjho—mapping hypothesis hoti hai, verdict nahin. [CISA cybersecurity resources](https://www.cisa.gov/resources-tools/resources) se defensive advisories/learning material padho. **Evidence:** 3 observed behaviors ko relevant concept se map karo, uncertainty note karo.
7. **Detection aur incident note:** toy logs par ek transparent detection rule/hunt question banao; false positives, data source aur time range likho. **Evidence:** alert summary, supporting facts, benign explanation, severity ki reasoning, aur escalation point.
8. **Portfolio review:** 2–3 self-contained sanitized case studies curate karo—lab setup, analysis, conclusion, limitation aur remediation. **Evidence:** aisa write-up jo naya reader repeat kar sake, lekin credentials, personal data, answer flags ya unapproved target detail na dikhaye.

Free/low-cost practice ke liye official [OverTheWire Bandit](https://overthewire.org/wargames/bandit/), [picoCTF practice](https://picoctf.org/) aur CISA ke public resources dekho. Platform ki current rules aur account requirements khud verify karo; yeh materials SOC job training ya hiring guarantee nahin.

## Path B — Authorized pentester foundation

Pentester path ka focus permission ke daire mein weakness ko reproduce, document aur responsibly report karna hai. “Pentest” ka matlab permission ke baghair scanning nahin. Har hands-on target intentionally vulnerable, local ya explicitly authorized hona chahiye.

1. **Ethics, scope, Linux:** rules of engagement, in-scope/out-of-scope, time window aur stop condition ko pehle samjho; terminal aur file permissions practice karo. **Evidence:** toy lab ke liye one-page scope note; real system par kaam nahin.
2. **Web aur HTTP fundamentals:** browser dev tools se apni localhost toy site ke request/response, methods, headers aur status codes dekho. **Evidence:** sanitized request lifecycle diagram aur glossary.
3. **Safe local networking:** Python server `127.0.0.1:8000` par run karke Nmap `-sT -p 8000 127.0.0.1` se sirf apna port check karo. **Evidence:** scan ka target, result aur limitation note karo; public address/range bilkul nahin.
4. **Web testing methodology:** [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) ko checklist/methodology ki tarah padho; pehle concepts, phir authorized training labs. [PortSwigger Web Security Academy](https://portswigger.net/web-security) free interactive web security lessons/labs provide karti hai. **Evidence:** ek lab concept ko apne alfaaz mein samjhao, flags/solutions nahin.
5. **Proxy aur request analysis:** desktop par Burp Community ko alag browser profile ke saath configure karo; sirf training lab ya apni localhost app ka traffic proxy karo. CA trust ko optional aur scoped rakho; system-wide install mat karo. **Evidence:** ek sanitized request/response explanation aur proxy cleanup checklist.
6. **Content discovery aur input handling:** apni toy web app aur khud banayi hui chhoti lab-only wordlist ke saath Gobuster ka localhost example samjho. Koi fixture preinstalled hone ka assumption nahin. **Evidence:** test fixture ka source, request limits aur expected false positives note karo.
7. **Finding ko verify aur report karo:** authorized training lab mein finding ka minimal safe reproduction, impact ka context, evidence aur remediation likho. Sirf proof ke liye data exfiltrate, destructive action ya persistence mat karo. **Evidence:** concise report with scope, observation, risk reasoning, fix aur verification plan.
8. **Portfolio aur review:** 2–3 public training-lab write-ups taiyar karo jo platform rules allow karte hon; actual flags/answers, hidden challenge solutions, secrets ya unauthorized target data publish na karo. **Evidence:** method-centered portfolio, limitations aur remediation recommendations ke saath.

Low-cost/free starting points: [PortSwigger Web Security Academy](https://portswigger.net/web-security), [picoCTF](https://picoctf.org/) aur [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/). Tool references ke liye [Nmap docs](https://nmap.org/book/man-port-scanning-techniques.html) aur [Kali docs](https://www.kali.org/docs/) dekho. Training access, features aur rules waqt ke saath badal sakte hain; current official pages ko follow karo.

## Dono paths ke liye ethical boundary

CTF platform ka naam dekh kar scope assume na karo: har event ke current rules padho. Written authorization ke baghair third-party website, IP, network, account ya device ko scan, enumerate, intercept ya test na karo. Agar accidental real data ya out-of-scope system mil jaye to foran ruk kar data ko preserve/share na karo, aur lab owner ke reporting channel ko follow karo. Skill evidence aapki practice dikhata hai; employment, certification, client work ya legal approval ka substitute nahin.
