# Lets Warm Up

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

[Notes](#Notes)

## Details

- **Points:** 50

- **Source:** picoCTF

- **Author:** SANJAY C/DANNY TUNITIS

## Description

If I told you a word started with `0x70` in hexadecimal, what would it start with in ASCII?

### Hint 1

Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution

- The goal of this challenge is to learn about the basics of Hexadecimal and ASCII character encoding standards. I invite you to read the resources I linked down below if you're not familiar with them yet.

- The solution to this challenge is fairly simple, you only need to either look through a HEX to ASCII character conversion table or use online tools to convert the character `0x70` to ASCII.

PS: You can ignore the `0x` at the start of the character since it's a prefix to indicate that the character is in hexadecimal rather than in some other base.

- Once you convert the character, just wrap it between a `picoCTF{_}` to respect the flag notation convention.

## Resources

- [ASCII](https://en.wikipedia.org/wiki/ASCII)
- [Hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal)
