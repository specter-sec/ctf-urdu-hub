---
title: Cryptography and encoding
description: Encoding, classical ciphers, aur security ke darmiyan farq samjho.
tags:
  - crypto
  - beginner
---

# Crypto

Crypto mein representations, ciphers aur security properties aate hain. Har unreadable string encryption nahi hoti: pehle pehchano ke data sirf encoded hai ya kisi key se protected.

## Safe beginner exercise

[ROT13 Ka Raaz](../writeups/crypto/rot13-ka-raaz.md) ke liye local text fixture banao. Har ASCII letter ko 13 positions rotate karke reverse karo, punctuation ko jaisa hai waisa rakho, aur samjhao ke ROT13 confidentiality provide nahi karta. [Lab generator source](https://github.com/specter-sec/ctf-urdu-hub/blob/main/labs/crypto-rot13.py) offline hai.

## Aage parho

- [CryptoHack: Introduction](https://cryptohack.org/challenges/introduction/)
- [CyberChef](https://gchq.github.io/CyberChef/) — tool ko apne supplied practice data par use karo.
- [MDN: Base64 glossary](https://developer.mozilla.org/en-US/docs/Glossary/Base64) — encoding ka example, cryptography nahi.

Asal cryptographic systems design ya deploy karne se pehle trusted, maintained library aur expert-reviewed guidance use karo; toy ciphers ko security ke liye use na karo.
