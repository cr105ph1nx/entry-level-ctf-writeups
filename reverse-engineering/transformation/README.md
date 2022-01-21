# Transformation

## Table of Matters

[Solution](#Solution-1)

[Resources](#Resources)

[Notes](#Notes)

## Details

- **Points:** 20

- **Source:** picoCTF

- **Author:** MADSTACKS

## Description

I wonder what this really is... enc `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`.

### Hint 1

You may find some decoders online.

## Solution 1

- Fetch the file required for the challenge with the `wget` command like so:

```
$ wget https://mercury.picoctf.net/static/77a2b202236aa741e988581e78d277a6/enc
```

- Find out what is the file type with the command `file [file]`. The output tells us that it's a ` Unicode text, UTF-8 text, with no line terminators`.

- Reading the content of the file with the command `cat enc` outputs the following string: `灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽`. including mostly traditional chinese characters, one korean character `ㄶ` and one egyptian hieroglyph `㌴`, which I find quite peculiar...

So how does the `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])` come into place?

- Let's understand how the given decoding algorithm works first:

  - Given a string `flag`, every letter of the flag is shifted left by 8 bits.
  - Then it adds the next letter of the string `flag` to the shifted value.
  - Each letter is represented as 8 bits (1 byte) and they are all joined together in pairs of two.

- This algorithm is similar to `UTF-16BE` Encoding. Using an online tool like [CyberChef](https://gchq.github.io/CyberChef/) you can try the conversion from `UTF-16BE` to Raw Format, or you can use [this python script](./dec.py).

We got the flag !

## Solution 2

Another way to get the flag 'quickly' would be to use [CyberChef's](https://gchq.github.io/CyberChef) `magic` setting on our encrypted string. Magic is designed to automatically detect how your data is encoded and which operations can be used to decode it. A number of methods are used to achieve this.

## Resources

- [CyberChef's Magic](https://gitce.net/mirrors/CyberChef/wiki/Automatic-detection-of-encoded-data-using-CyberChef-Magic)
- [Unicode Transformation Format](https://en.wikipedia.org/wiki/Unicode#UTF)
