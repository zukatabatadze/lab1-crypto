# Lab 1 - Cryptography Fundamentals and Pentesting Basics

## 1. Caesar Cipher
Given ciphertext: `Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu.`  
I used a simple Python script that tries all 26 possible shifts.  
The decrypted message was: **The Quick Brown Fox Jumps Over The Lazy Dog.**

Caesar cipher is not secure because it has only 25 possible keys, and anyone can decrypt it using brute force or frequency analysis.  
Still, some old or simple systems may use similar encryption just to hide data, not to protect it.

---

## 2. XOR Encryption / Decryption
Ciphertext: `mznxpz`  
Using the same script, I found that shift 5 gives the word **rescue**.  
When rearranged (anagram), it becomes **secure**, which is the passphrase.

Then I used that passphrase to decrypt this Base64 ciphertext:  
`Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ=`

After decoding from Base64 and XOR decrypting with the key `secure`,  
the final plaintext was: **This is the XOR challenge!**

---

### Author
**Zurab Tabatadze**
