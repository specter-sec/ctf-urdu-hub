---
title: CTF Urdu Hub
description: CTF seekho, clues samjho, aur apni notes Roman Urdu mein likho.
tags:
  - home
  - beginner
---

<div class="home-hero">
  <p class="eyebrow">FIELD NOTES / 06 — LEARN BY INVESTIGATING</p>
  <h1>Har clue ki <span>ek kahani</span> hoti hai.</h1>
  <p class="hero-copy">CTF Urdu Hub par cybersecurity ke bunyadi ideas ko Roman Urdu/Hinglish mein samjho. Chhote, offline aur fictional exercises se sawal poochna, evidence dekhna, aur apni reasoning likhna seekho.</p>
  <p class="hero-actions"><a class="action action-primary" href="guides/getting-started/">Pehla qadam <span aria-hidden="true">↗</span></a> <a class="action action-secondary" href="categories/web/">Topics explore karo</a></p>
</div>

<div class="terminal-panel" role="group" aria-label="Fictional offline practice terminal example">
  <div class="terminal-top"><span class="terminal-lights" aria-hidden="true">● ● ●</span><span>practice-session / local-only</span><span>SAFE MODE</span></div>
  <pre><code>$ python3 labs/web-source.py
Created fictional page: labs/work/web-source/index.html
$ grep -n 'Demo clue' labs/work/web-source/index.html
&lt;!-- Demo clue: CTFURDU{source_is_public} --&gt;
$ echo 'Scope first. Evidence second. Explain always.'</code></pre>
  <p class="terminal-caption">Yeh sirf local, banawati demo hai — live target ya real challenge nahi.</p>
</div>

## Apna learning route chuno

<div class="topic-strip">
  <a href="categories/web/"><span class="topic-index">01</span><strong>Web</strong><span>Source, requests, safe labs</span></a>
  <a href="categories/crypto/"><span class="topic-index">02</span><strong>Crypto</strong><span>Encoding se concepts tak</span></a>
  <a href="categories/forensics/"><span class="topic-index">03</span><strong>Forensics</strong><span>Files aur digital evidence</span></a>
  <a href="categories/pwn/"><span class="topic-index">04</span><strong>Pwn</strong><span>Memory safety ki bunyaad</span></a>
  <a href="categories/reverse/"><span class="topic-index">05</span><strong>Reverse</strong><span>Program ko samajhna</span></a>
  <a href="categories/osint/"><span class="topic-index">06</span><strong>OSINT</strong><span>Public info, ethical tareeqe se</span></a>
  <a href="categories/beginner-linux/"><span class="topic-index">07</span><strong>Beginner Linux</strong><span>Terminal aur file hunting</span></a>
</div>

## Pehle yeh samjho

Yeh site **seekhne aur authorized practice** ke liye hai. Har exercise isolated local files par chalti hai; kisi real system, account, network ya insaan ko target karne ki zaroorat nahi. Demo markers `CTFURDU{...}` ke format mein fictional hain aur kisi platform ka challenge flag nahi.

> **Mantra:** scope confirm karo → local evidence jama karo → reasoning likho → sirf authorized lab mein practice karo.

Shuru karne ke liye [Getting Started](guides/getting-started.md), apna [pehla writeup](template.md), ya [Ethics & Safe Practice](ethics.md) kholo. Search bar mein topic dhoondo; [tags index](tags.md) se tags browse karo.
