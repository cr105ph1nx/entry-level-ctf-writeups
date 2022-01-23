# Mind Your Ps and Qs

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

## Details

- **Points:** 20

- **Source:** picoCTF

- **Author:** SARA

## Description

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this?

### Hint 1

Bits are expensive, I used only a little bit over 100 to save money.

## Solution

- As usual, you need to download the file provided by the challenge using `wget` like so:

```
$ wget https://mercury.picoctf.net/static/b9ddda080c56fb421bf30409bec3460d/values
```

PS: Right-click on the link and click on `copy link adress` to get the download URL.

- Read the content of the file with `$ cat values`

Output:

```
Decrypt my super sick RSA:
c: 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n: 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e: 65537
```

I invite you to read more about RSA cryptosystem from the articles I linked below.

- By convention, C is the ciphertext we want to decode. N is the result of multiplying two prime numbers p and q (`n = p * q`). E is the multiplicative inverse of a private exponent and Phi such as Phi equals `(p-1)*(q-1)`.

- In order to find the `p` and the `q`, you need to factorize the `n` using the tool `factordb`. Either import the library to your python script or use [an online tool](http://factordb.com/).

- Now that we have the `p` and `q`, the rest of our [decrypting script](dec.py) shouldn't be that hard to finish. I added a last line to convert the output to Raw text format.

- Since in this example the `n`, `e` and `c` are weak numbers as also suggested by the hint _(I used only a little bit over 100 bits)_, you can always solve the challenge by using RsaCtfTool by entering the following command in your shell:

```
python RsaCtfTool -n 1584586296183412107468474423529992275940096154074798537916936609523894209759157543 -e 65537 --uncipher 964354128913912393938480857590969826308054462950561875638492039363373779803642185
```

- You can also use the website https://www.dcode.fr/rsa-cipher to decode the ciphertext by feeding it your `c`, `n` and `e`. You will have to convert the series of HEX numbers to characters in order to obtain the flag.

## Resources

- [RSA cryptosystem](<https://en.wikipedia.org/wiki/RSA_(cryptosystem)>)
- [Understanding RSA cryptosystem](https://medium.com/crypto-0-nite/understanding-rsa-cryptosystem-5e82af321cff)
- [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
- [More on RSA attacks](https://www.ctfnote.com/crypto/rsa/attacks)
