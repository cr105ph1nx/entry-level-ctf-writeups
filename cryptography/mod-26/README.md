# Mod 26

## Table of Matters

[Solution](#Solution-1:-Python)

[Resources](#Resources)

[Notes](#Notes)

## Details

- **Points:** 10

- **Source:** picoCTF

- **Author:** PANDU

## Description

Cryptography can be easy, do you know what ROT13 is?
`cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}`

### Hint 1

This can be solved online if you don't want to do it by hand!

## Solution 1: Python

The Python 3 documentation has rot13 listed on its [codecs page](https://docs.python.org/3/library/codecs.html) and there is a ROT13 string-to-string codec:

- Run `python` on your terminal window to switch to a python shell.
- Run the following instructions in your new shell:

```
import codecs;
string = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
print(codecs.encode(string, "rot-13"))
```

## Solution 2: Shell Script

A perfect job for `tr`. Each character in the first set (`'A-Za-z'`) will be replaced with the corresponding character in the second set (`N-ZA-Mn-za-m`). E.g. A replaced with N, B replaced with O, etc.. And then the same for the lower case letters. All other characters will be passed through unchanged.

```
echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

## Resources

- [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

- [ROT13](https://en.wikipedia.org/wiki/ROT13)

- [echo](https://man7.org/linux/man-pages/man1/echo.1.html)

- [tr](https://man7.org/linux/man-pages/man1/tr.1p.html)

## Notes

- "Cipher" is the algorithm or process used to encrypt the data (i.e. AES, RSA, etc.). "Encryption" is the process of converting data using the aforementioned cipher.
- Remember to make reading the manual of the commands you use a habit. `man [cmd]` is your friend!
