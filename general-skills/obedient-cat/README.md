# Obedient Cat

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

[Notes](#Notes)

## Details

- **Points:** 5

- **Source:** picoCTF

- **Author:** SYREAL

## Description

This file has a flag in plain sight (aka "in-the-clear").

### Hint 1

Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.

### Hint 2

To get the file accessible in your shell, enter the following in the Terminal prompt:
`$ wget https://mercury.picoctf.net/static/704f877da185904ec3992e7255a15c6c/flag`

### Hint 3

`$ man cat`

## Solution

1. Download the file by entering in your terminal window:
   `$ wget https://mercury.picoctf.net/static/704f877da185904ec3992e7255a15c6c/flag`

2. Read the content of the file with:
   `cat flag`

## Resources

- [wget command](https://www.man7.org/linux/man-pages/man1/wget.1.html)

- [cat command](https://man7.org/linux/man-pages/man1/cat.1.html)

## Notes

- Often times, the title of the challenge is the only hint you need.
- Remember to make reading the manual of the commands you use a habit. `man [cmd]` is your friend!
