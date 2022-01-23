# 2Warm

## Bases

[Solution](#Solution)

[Resources](#Resources)

## Details

- **Points:** 100

- **Source:** picoCTF

- **Author:** SANJAY C/DANNY T

## Description

What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

### Hint 1

Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution

- The goal of this challenge is to learn about Base encodings. I invite you to read the resources I linked down below if you're not familiar with them yet.

- Let's take a closer look at it this string ! The base used in this challenge to encode the string is `Base64` which is the most common base. We can decrypt it to a Raw Text Format using online tools such as [CyberChef](https://gchq.github.io/CyberChef/).

- Once you convert the character, just wrap it between a `picoCTF{_}` to respect the flag notation convention.

## Resources

- [Binary-to-text encoding](https://code.tutsplus.com/tutorials/base-what-a-practical-introduction-to-base-encoding--net-27590)
- [Base64 Encoding](https://en.wikipedia.org/wiki/Base64)
